from django.db import models
import datetime

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=250, blank=False)
    surname = models.CharField(max_length=250, blank=False)
    email = models.EmailField(blank=True)
    genre = models.CharField(max_length=6, blank=False)
    autonomous_community = models.CharField(max_length=250, blank=False)
    age = models.IntegerField(blank=False)
    dni = models.CharField(unique = True, max_length=9, blank=False)

    def __unicode__(self):
        return self.name + self.surname + self.email


class Vote(models.Model):
    VOTE_TYPE_CHOICES=(
        ('WEB', 'Web'),
        ('SLACK', 'Slack'),
        ('TELEGRAM', 'Telegram'),
    )
    token = models.CharField(max_length=100000,blank=False)
    vote_date = models.DateTimeField(auto_now_add=True)
    vote_type = models.CharField(max_length=10,blank=False,choices=VOTE_TYPE_CHOICES,default='WEB')

    def __unicode__(self):
        return str(self.token) + ", " + str(self.vote_date) + ", " + str(self.vote_type)


class Poll(models.Model):
    id = models.IntegerField(blank=False, primary_key=True)
    title = models.CharField(max_length=250, blank=False)
    description = models.CharField(max_length=250, blank=False)
    startDate = models.DateTimeField()
    endDate = models.DateTimeField()

    def __unicode__(self):
        return str(self.id) + " " + str(self.title)


class Question(models.Model):
    question_id = models.IntegerField(blank=False, primary_key= True)
    title = models.CharField(max_length=250, blank=False)
    description = models.CharField(max_length=10000, blank=False)
    optional = models.BooleanField(default=False)
    poll_reference = models.ForeignKey(Poll, blank=False)

    def __unicode__(self):
        return str(self.question_id) + " " + str(self.text) + " " + str(self.questions)

class Answer(models.Model):
    answer_id = models.IntegerField(blank=False, primary_key= True)
    text = models.CharField(max_length=250, blank=False)
    question_reference = models.ForeignKey(Question, blank =False)