#encoding: utf-8

from models import *
from exceptions import PollDateException, NoQuestionOptionException, NoUserException, MoreThanOneVoteException
from django.core.exceptions import ObjectDoesNotExist
import time
import datetime
import rsa

keys = {}

def insertVoteWeb(id_poll, id_user, id_questionOption):
    
    checkDate(id_poll)
    checkUser(id_user)
    checkQuestionOp(id_questionOption)
    checkQuestionOpInPoll(id_poll, id_questionOption)
    checkOnlyOneVotePerUser(id_poll, id_user)
    
    questionOptions= id_questionOption.split("&");
    
    username = UserAccount.objects.get(id = id_user).username

    voto = Vote.objects.create(token = username, vote_type = VoteType.objects.filter(id = 1).get(), vote_date = time.strftime("%Y-%m-%d"))
    
    (pub_key, priv_key) = rsa.newkeys(256)
    crypto = rsa.encrypt(str(username), pub_key)
    keys[voto] = [crypto, priv_key]

    voto.token = crypto.decode('utf8', 'ignore')
    voto.save()
        
    poll = Poll.objects.get(id = id_poll)
    poll.votos_actuales += 1
    poll.save()
    
    for decision in questionOptions:
        
        questionOp = QuestionOption.objects.get(id = decision)
        OptionPerVote.objects.create(vote = voto, question_option = questionOp)
                        
    return voto

def insertVoteSlack(id_poll, id_user, id_questionOption):
    
    checkDate(id_poll)
    checkUser(id_user)
    checkQuestionOp(id_questionOption)
    checkQuestionOpInPoll(id_poll, id_questionOption)
    checkOnlyOneVotePerUser(id_poll, id_user)
    
    questionOptions= id_questionOption.split("&");
    
    username = UserAccount.objects.get(id = id_user).username

    voto = Vote.objects.create(token = username, vote_type = VoteType.objects.filter(id = 2).get(), vote_date = time.strftime("%Y-%m-%d"))
    
    (pub_key, priv_key) = rsa.newkeys(256)
    crypto = rsa.encrypt(str(username), pub_key)
    keys[voto] = [crypto, priv_key]

    voto.token = crypto.decode('utf8', 'ignore')
    voto.save()
        
    poll = Poll.objects.get(id = id_poll)
    poll.votos_actuales += 1
    poll.save()
    
    for decision in questionOptions:
        
        questionOp = QuestionOption.objects.get(id = decision)
        OptionPerVote.objects.create(vote = voto, question_option = questionOp)
                        
    return voto

def insertVoteTelegram(id_poll, id_user, id_questionOption):
    
    checkDate(id_poll)
    checkUser(id_user)
    checkQuestionOp(id_questionOption)
    checkQuestionOpInPoll(id_poll, id_questionOption)
    checkOnlyOneVotePerUser(id_poll, id_user)
    
    questionOptions= id_questionOption.split("&");
    
    username = UserAccount.objects.get(id = id_user).username

    voto = Vote.objects.create(token = username, vote_type = VoteType.objects.filter(id = 3).get(), vote_date = time.strftime("%Y-%m-%d"))
    
    (pub_key, priv_key) = rsa.newkeys(256)
    crypto = rsa.encrypt(str(username), pub_key)
    keys[voto] = [crypto, priv_key]

    voto.token = crypto.decode('utf8', 'ignore')
    voto.save()
        
    poll = Poll.objects.get(id = id_poll)
    poll.votos_actuales += 1
    poll.save()
    
    for decision in questionOptions:
        
        questionOp = QuestionOption.objects.get(id = decision)
        OptionPerVote.objects.create(vote = voto, question_option = questionOp)
                        
    return voto

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
    
def checkOnlyOneVotePerUser (id_poll, id_user):
    username = UserAccount.objects.get(id = id_user).username
    pollT = Poll.objects.get(id = id_poll)
    questions = Question.objects.filter(poll = pollT)
    
    for questionT in questions:
        questionOptions = QuestionOption.objects.filter(question = questionT)
        
        for questionOptionT in questionOptions:
            optionPerVotes = OptionPerVote.objects.filter(question_option = questionOptionT)

            for optionPerVote in optionPerVotes:
                token = rsa.decrypt(keys[optionPerVote.vote][0], keys[optionPerVote.vote][1])

                if token == username:
                    raise MoreThanOneVoteException("El usuario ya ha participado en esta votacion")
                
def checkQuestionOpInPoll(id_poll, id_questionOption):
    questionOptions = id_questionOption.split("&");

    for option in questionOptions:
        qo = QuestionOption.objects.filter(id = option).get().question
        
        if qo.poll_id != id_poll:
            raise NoQuestionOptionException("las opciones elegidas no se encuentran en la votacion")
            
    