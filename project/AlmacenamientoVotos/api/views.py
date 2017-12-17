from django.shortcuts import render, get_object_or_404
from models import *
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.
def insertVoteWeb(request, id_poll, id_user, id_questionOption):
    
    questionOptions= id_questionOption.split("&");
    
    for option in questionOptions:
        res = option.split("-")
        decision = res[0]
        priority = res[1]
        voto = Vote.objects.create(token = id_user, vote_type = VoteType.objects.filter(id = 1).get())
        questionOp = QuestionOption.objects.filter(id = decision).get()
        op = OptionPerVote.objects.create(vote = voto, question_option = questionOp)
                
    html = "<html><body>Voto de web insertado con exito</body></html>"
    return HttpResponse(html)
