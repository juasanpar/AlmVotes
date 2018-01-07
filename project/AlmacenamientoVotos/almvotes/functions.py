#encoding: utf-8

from models import *
from exceptions import PollDateException, NoQuestionOptionException, NoUserException
from django.core.exceptions import ObjectDoesNotExist
import time
import datetime
from rsa import encrypt, key, common

priv_keys = {}

def insertVoteWeb(id_poll, id_user, id_questionOption):
    
    checkDate(id_poll)
    checkUser(id_user)
    checkQuestionOp(id_questionOption)
    
    questionOptions= id_questionOption.split("&");
    
    userAccount = User.objects.get(id = id_user).user_account
    username = userAccount.username
    
    voto = Vote.objects.create(token = username, vote_type = VoteType.objects.filter(id = 1).get(), vote_date = time.strftime("%Y-%m-%d"))
    poll = Poll.objects.get(id = id_poll)
    poll.votos_actuales += 1
    poll.save()
    
    for decision in questionOptions:
        
        questionOp = QuestionOption.objects.filter(id = decision).get()
        OptionPerVote.objects.create(vote = voto, question_option = questionOp)
                        
    return True

def insertVoteSlack(id_poll, id_user, id_questionOption):
    
    checkDate(id_poll)
    checkUser(id_user)
    checkQuestionOp(id_questionOption)
    
    questionOptions= id_questionOption.split("&");
    
    userAccount = User.objects.get(id = id_user).user_account
    username = userAccount.username    
    voto = Vote.objects.create(token = username, vote_type = VoteType.objects.filter(id = 2).get(), vote_date = time.strftime("%Y-%m-%d"))
    poll = Poll.objects.get(id = id_poll)
    poll.votos_actuales += 1
    poll.save()
    
    for decision in questionOptions:

        questionOp = QuestionOption.objects.filter(id = decision).get()
        OptionPerVote.objects.create(vote = voto, question_option = questionOp)
                        
    return "Voto insertado con exito"

def insertVoteTelegram(id_poll, id_user, id_questionOption):
    
    checkDate(id_poll)
    checkUser(id_user)
    checkQuestionOp(id_questionOption)
    
    questionOptions= id_questionOption.split("&");
    
    userAccount = User.objects.get(id = id_user).user_account
    username = userAccount.username    

    voto = Vote.objects.create(token = username, vote_type = VoteType.objects.filter(id = 3).get(), vote_date = time.strftime("%Y-%m-%d"))
    poll = Poll.objects.get(id = id_poll)
    poll.votos_actuales += 1
    poll.save()
    
    for decision in questionOptions:

        questionOp = QuestionOption.objects.filter(id = decision).get()
        OptionPerVote.objects.create(vote = voto, question_option = questionOp)
                    
    return "Voto insertado con exito"

def checkDate(id_poll):
    
    poll = Poll.objects.filter(id=id_poll).get()
    checkdate = False
    
    startdate = poll.startdate
    enddate = poll.enddate
    
    datevote = time.strftime("%d/%m/%Y")
    date = datetime.datetime.strptime(datevote, '%d/%m/%Y').date()

    if date > startdate and date < enddate:
        checkdate = True 
        
    if (checkdate == False):
        raise PollDateException ("El voto no es valido, la votacion no se encuentra activa en la fecha actual.")
        
def checkQuestionOp(id_questionOption):
    questionOptions= id_questionOption.split("&");
    
    for option in questionOptions:
        res = option.split("-")
        decision = res[0]
    
        try:
            QuestionOption.objects.filter(id = decision).get()
            
        except ObjectDoesNotExist:
            raise NoQuestionOptionException("La id de questionOption "+decision+" no existe")

def checkUser (id_user):
    try:
        User.objects.filter(id = id_user).get()
        
    except ObjectDoesNotExist:
        raise NoUserException("No existe un usuario con la id "+id_user)
    
    
    