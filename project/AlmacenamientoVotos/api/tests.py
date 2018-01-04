#encoding:utf-8
from functions import insertVoteWeb
import unittest
import datetime
from models import Poll, User, Census
    
class TestInsertMethods(unittest.TestCase):

    def testInsertVote(self):
        print "Creando nueva votacion con fecha valida para el testeo"
        testCensus = Census.objects.get(id = 1)
        testPoll = Poll.objects.create(title = "Test Poll", description = "Votacion para testear", startdate = datetime.datetime.strptime("2010-2-12", '%Y-%m-%d').date(), enddate = datetime.datetime.strptime("2040-2-12", '%Y-%m-%d').date(), census = testCensus, participantes_admitidos = 0, votos_actuales = 0)        
        print "Tomando un usuario para el test"
        testUser = User.objects.get(id = 1)
        print "Creando valores 1-1&5-3&7-1 como questionOptions"
        testQuestionOptions = "1-1&5-3&7-1"
        print "Testeando insercion de voto en la votacion con id "+testPoll.title+", del usuario "+testUser.name+" con las opciones y prioridades "+testQuestionOptions
        testInsert = insertVoteWeb(testPoll.id, testUser.id, testQuestionOptions)
        self.assertTrue(testInsert, "Error en la insercion del voto")
        print "Insercion realizada correctamente"

if __name__ == '__main__':
    unittest.main()    
    
