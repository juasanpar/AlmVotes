from django.shortcuts import render, get_object_or_404
from models import *
from django.http import HttpResponse, HttpResponseRedirect
import time

# Create your views here.
def insertVoteWeb(request, id_poll, id_user, id_questionOption):
    
    questionOptions= id_questionOption.split("&");
    
    for option in questionOptions:
        res = option.split("-")
        decision = res[0]
        print decision
        priority = res[1]
        voto = Vote.objects.create(token = id_user, vote_type = VoteType.objects.filter(id = 1).get())
        questionOp = QuestionOption.objects.filter(id = decision).get()
        op = OptionPerVote.objects.create(vote = voto, question_option = questionOp)

        
        print op.id
        
    html = "<html><body>Voto de web insertado con exito</body></html>"
    return HttpResponse(html)

def insertVoteSlack(request, id_poll, id_user, id_questionOption):
    
    questionOptions= id_questionOption.split("&");
    
    for option in questionOptions:
        res = option.split("-")
        decision = res[0]
        priority = res[1]
        voto = Vote.objects.create(token = id_user, vote_type = VoteType.objects.filter(id = 2).get())
        questionOp = QuestionOption.objects.filter(id = decision).get()
        op = OptionPerVote.objects.create(vote = voto, question_option = questionOp)
          
    html = "<html><body>Voto slack insertado con exito</body></html>"
    return HttpResponse(html)

def insertVoteTelegram(request, id_poll, id_user, id_questionOption):
    
    questionOptions= id_questionOption.split("&");
    
    for option in questionOptions:
        res = option.split("-")
        decision = res[0]
        priority = res[1]
        voto = Vote.objects.create(token = id_user, vote_type = VoteType.objects.filter(id = 3).get())
        questionOp = QuestionOption.objects.filter(id = decision).get()
        OptionPerVote.objects.create(vote = voto, question_option = questionOp)
        
    html = "<html><body>Voto telegram insertado con exito</body></html>"
    return HttpResponse(html)

def checkDate(id_poll, Vote):
    
    poll = Poll.objects.filter(id=id_poll).get()
    checkdate = False
    
    startdate = poll.startdate
    enddate = poll.enddate
    
    datevote = time.strftime("%d/%m/%Y")
    
    
    if datevote > startdate and datevote < enddate:
        checkdate = True 
        
    return checkdate
        
        
           
   
