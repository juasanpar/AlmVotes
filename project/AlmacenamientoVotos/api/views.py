from django.shortcuts import render, get_object_or_404
from models import *
<<<<<<< HEAD
from exceptions import PollDateException, NoQuestionOptionException, NoUserException
from django.http import HttpResponse, HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist
import time
import datetime
=======
from django.http import HttpResponse, HttpResponseRedirect
import time
>>>>>>> a80d56c35c68e07dd74b8a6480718ba8460ca631

# Create your views here.
def insertVoteWeb(request, id_poll, id_user, id_questionOption):
    
<<<<<<< HEAD
    checkDate(id_poll)
    checkUser(id_user)
    checkQuestionOp(id_questionOption)
    
    questionOptions= id_questionOption.split("&");
    voto = Vote.objects.create(token = id_user, vote_type = VoteType.objects.filter(id = 1).get(), vote_date = time.strftime("%Y-%m-%d"))
    poll = Poll.objects.get(id = id_poll)
    poll.votos_actuales += 1
    poll.save()
=======
    questionOptions= id_questionOption.split("&");
>>>>>>> a80d56c35c68e07dd74b8a6480718ba8460ca631
    
    for option in questionOptions:
        res = option.split("-")
        decision = res[0]
<<<<<<< HEAD
        priority = res[1]

        questionOp = QuestionOption.objects.filter(id = decision).get()
        op = OptionPerVote.objects.create(vote = voto, question_option = questionOp)
                    
=======
        print decision
        priority = res[1]
        voto = Vote.objects.create(token = id_user, vote_type = VoteType.objects.filter(id = 1).get())
        questionOp = QuestionOption.objects.filter(id = decision).get()
        op = OptionPerVote.objects.create(vote = voto, question_option = questionOp)

        
        print op.id
        
>>>>>>> a80d56c35c68e07dd74b8a6480718ba8460ca631
    html = "<html><body>Voto de web insertado con exito</body></html>"
    return HttpResponse(html)

def insertVoteSlack(request, id_poll, id_user, id_questionOption):
    
<<<<<<< HEAD
    checkDate(id_poll)
    checkUser(id_user)
    checkQuestionOp(id_questionOption)
    
    questionOptions= id_questionOption.split("&");
    voto = Vote.objects.create(token = id_user, vote_type = VoteType.objects.filter(id = 2).get(), vote_date = time.strftime("%Y-%m-%d"))
    poll = Poll.objects.get(id = id_poll)
    poll.votos_actuales += 1
    poll.save()
=======
    questionOptions= id_questionOption.split("&");
>>>>>>> a80d56c35c68e07dd74b8a6480718ba8460ca631
    
    for option in questionOptions:
        res = option.split("-")
        decision = res[0]
        priority = res[1]
<<<<<<< HEAD

        questionOp = QuestionOption.objects.filter(id = decision).get()
        op = OptionPerVote.objects.create(vote = voto, question_option = questionOp)
                    
    html = "<html><body>Voto de slack insertado con exito</body></html>"
=======
        voto = Vote.objects.create(token = id_user, vote_type = VoteType.objects.filter(id = 2).get())
        questionOp = QuestionOption.objects.filter(id = decision).get()
        op = OptionPerVote.objects.create(vote = voto, question_option = questionOp)
          
    html = "<html><body>Voto slack insertado con exito</body></html>"
>>>>>>> a80d56c35c68e07dd74b8a6480718ba8460ca631
    return HttpResponse(html)

def insertVoteTelegram(request, id_poll, id_user, id_questionOption):
    
<<<<<<< HEAD
    checkDate(id_poll)
    checkUser(id_user)
    checkQuestionOp(id_questionOption)
    
    questionOptions= id_questionOption.split("&");
    voto = Vote.objects.create(token = id_user, vote_type = VoteType.objects.filter(id = 3).get(), vote_date = time.strftime("%Y-%m-%d"))
    poll = Poll.objects.get(id = id_poll)
    poll.votos_actuales += 1
    poll.save()
=======
    questionOptions= id_questionOption.split("&");
>>>>>>> a80d56c35c68e07dd74b8a6480718ba8460ca631
    
    for option in questionOptions:
        res = option.split("-")
        decision = res[0]
        priority = res[1]
<<<<<<< HEAD

        questionOp = QuestionOption.objects.filter(id = decision).get()
        op = OptionPerVote.objects.create(vote = voto, question_option = questionOp)
                    
    html = "<html><body>Voto de telegram insertado con exito</body></html>"
    return HttpResponse(html)

def checkDate(id_poll):
=======
        voto = Vote.objects.create(token = id_user, vote_type = VoteType.objects.filter(id = 3).get())
        questionOp = QuestionOption.objects.filter(id = decision).get()
        OptionPerVote.objects.create(vote = voto, question_option = questionOp)
        
    html = "<html><body>Voto telegram insertado con exito</body></html>"
    return HttpResponse(html)

def checkDate(id_poll, Vote):
>>>>>>> a80d56c35c68e07dd74b8a6480718ba8460ca631
    
    poll = Poll.objects.filter(id=id_poll).get()
    checkdate = False
    
    startdate = poll.startdate
    enddate = poll.enddate
    
    datevote = time.strftime("%d/%m/%Y")
<<<<<<< HEAD
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
=======
    
    
    if datevote > startdate and datevote < enddate:
        checkdate = True 
        
    return checkdate
        
        
           
   
>>>>>>> a80d56c35c68e07dd74b8a6480718ba8460ca631
