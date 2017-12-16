#encoding:utf-8
from __future__ import unicode_literals

from django.db import models
from fernet_fields import EncryptedCharField

class Ca(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'ca'
        
    def __unicode__(self):
          return self.name

class Census(models.Model):
    title = models.CharField(max_length=100)
    postalcode = models.IntegerField(db_column='postalCode', blank=True, null=True)  # Field name made lowercase.
    ca = models.ForeignKey(Ca)

    class Meta:
        managed = False
        db_table = 'census'

    def __unicode__(self):
        return self.title

class Cookie(models.Model):
    number_id = models.CharField(primary_key=True, max_length=40)
    user_account = models.ForeignKey('UserAccount')

    class Meta:
        managed = False
        db_table = 'cookie'

class OptionPerVote(models.Model):
    vote = models.ForeignKey('Vote')
    question_option = models.ForeignKey('QuestionOption')

    class Meta:
        managed = False
        db_table = 'option_per_vote'


class Poll(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=150, blank=True, null=True)
    startdate = models.DateField(db_column='startDate')  # Field name made lowercase.
    enddate = models.DateField(db_column='endDate')  # Field name made lowercase.
    census = models.ForeignKey(Census)

    class Meta:
        managed = False
        db_table = 'poll'

    def __unicode__(self):
        return self.title
    
class Question(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=150, blank=True, null=True)
    optional = models.IntegerField()
    multiple = models.IntegerField()
    poll = models.ForeignKey(Poll)

    class Meta:
        managed = False
        db_table = 'question'


class QuestionOption(models.Model):
    description = models.CharField(max_length=150, blank=True, null=True)
    question = models.ForeignKey(Question)

    class Meta:
        managed = False
        db_table = 'question_option'


class Role(models.Model):
    name = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'role'

    def __unicode__(self):
        return self.name


class User(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=200)
    genre = models.CharField(max_length=1)
    edad = models.DateField()
    dni = models.CharField(max_length=9)
    ca = models.ForeignKey(Ca)
    user_account = models.ForeignKey('UserAccount')

    class Meta:
        managed = False
        db_table = 'user'

    def __unicode__(self):
          return self.name

class UserAccount(models.Model):
    username = models.CharField(unique=True, max_length=50)
    password = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    role = models.ForeignKey(Role)

    class Meta:
        managed = False
        db_table = 'user_account'
        
    def __unicode__(self):
        return self.username

class UserAccountPerCensus(models.Model):
    census = models.ForeignKey(Census)
    user_account = models.ForeignKey(UserAccount)

    class Meta:
        managed = False
        db_table = 'user_account_per_census'


class Vote(models.Model):
    token = models.CharField(max_length=150)
    vote_type = models.ForeignKey('VoteType')
    vote_date = models.DateField()

    class Meta:
        managed = False
        db_table = 'vote'
        
    def __unicode__(self):
        return self.token


class VoteType(models.Model):
    name = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'vote_type'

    def __unicode__(self):
        return self.name




