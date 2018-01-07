#encoding:utf-8
from functions import insertVoteWeb, checkDate, checkQuestionOp
import unittest
import datetime
from exceptions import PollDateException, NoQuestionOptionException
from models import Poll, User, Census

class TestInsertMethods(unittest.TestCase):

    def testInsertVote(self):
        testCensus = Census.objects.get(id = 1)
        testPoll = Poll.objects.create(title = "Test Poll", description = "Votacion para testear insercion de voto", startdate = datetime.datetime.strptime("2010-2-12", '%Y-%m-%d').date(), enddate = datetime.datetime.strptime("2040-2-12", '%Y-%m-%d').date(), census = testCensus, participantes_admitidos = 0, votos_actuales = 0)        
        testUser = User.objects.get(id = 1)
        testQuestionOptions = "1&5&7"
        testInsert = insertVoteWeb(testPoll.id, testUser.id, testQuestionOptions)
        self.assertTrue(testInsert, "Error en la insercion del voto")
                
    def testCheckDate(self):
        testCensus = Census.objects.get(id = 1)
        testPoll = Poll.objects.create(title = "Test Poll", description = "Votacion para testear la fecha de la votacion", startdate = datetime.datetime.strptime("2010-2-12", '%Y-%m-%d').date(), enddate = datetime.datetime.strptime("2012-2-12", '%Y-%m-%d').date(), census = testCensus, participantes_admitidos = 1, votos_actuales = 0)        
        self.assertRaises(PollDateException, checkDate, testPoll.id)
        
    def testCheckQuestionOp(self):
        self.assertRaises(NoQuestionOptionException, checkQuestionOp,"114&512&71")
        
    def testIncreasePollVotes(self):
        testCensus = Census.objects.get(id = 1)
        testPoll = Poll.objects.create(title = "Test Poll", description = "Votacion para testear incremento de votos", startdate = datetime.datetime.strptime("2010-2-12", '%Y-%m-%d').date(), enddate = datetime.datetime.strptime("2040-2-12", '%Y-%m-%d').date(), census = testCensus, participantes_admitidos = 1, votos_actuales = 0)      
        
        testUser1 = User.objects.get(id = 1)
        testUser2 = User.objects.get(id = 2)
        
        testQuestionOptions = "1&5&7"
        insertVoteWeb(testPoll.id, testUser1.id, testQuestionOptions)
        votosPoll1 = Poll.objects.get(id = testPoll.id)
        self.assertEqual(votosPoll1.votos_actuales, 1)
        
        insertVoteWeb(testPoll.id, testUser2.id, testQuestionOptions)
        votosPoll2 = Poll.objects.get(id = testPoll.id)
        self.assertEqual(votosPoll2.votos_actuales, 2)
        
if __name__ == '__main__':
    unittest.main()    
    
