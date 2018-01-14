# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals

from django.db import models

class Ca(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100L)
    class Meta:
        db_table = 'ca'

class Census(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=100L)
    postalcode = models.IntegerField(null=True, db_column='postalCode', blank=True) # Field name made lowercase.
    estado = models.CharField(max_length=7L)
    ca = models.ForeignKey(Ca)
    class Meta:
        db_table = 'census'

class Cookie(models.Model):
    number_id = models.CharField(max_length=40L, primary_key=True)
    user_account = models.ForeignKey('UserAccount')
    class Meta:
        db_table = 'cookie'

class OptionPerVote(models.Model):
    id = models.IntegerField(primary_key=True)
    vote = models.ForeignKey('Vote')
    question_option = models.ForeignKey('QuestionOption')
    class Meta:
        db_table = 'option_per_vote'

class Poll(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=50L)
    description = models.CharField(max_length=150L, blank=True)
    startdate = models.DateField(db_column='startDate') # Field name made lowercase.
    enddate = models.DateField(db_column='endDate') # Field name made lowercase.
    census = models.ForeignKey(Census)
    participantes_admitidos = models.IntegerField()
    votos_actuales = models.IntegerField()
    class Meta:
        db_table = 'poll'

class Question(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=50L)
    description = models.CharField(max_length=150L, blank=True)
    optional = models.IntegerField()
    multiple = models.IntegerField()
    poll = models.ForeignKey(Poll)
    class Meta:
        db_table = 'question'

class QuestionOption(models.Model):
    id = models.IntegerField(primary_key=True)
    description = models.CharField(max_length=150L, blank=True)
    question = models.ForeignKey(Question)
    class Meta:
        db_table = 'question_option'

class Role(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=10L)
    class Meta:
        db_table = 'role'

class User(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100L)
    surname = models.CharField(max_length=200L)
    genre = models.CharField(max_length=1L)
    edad = models.DateField()
    dni = models.CharField(max_length=9L)
    ca = models.ForeignKey(Ca)
    user_account = models.ForeignKey('UserAccount')
    class Meta:
        db_table = 'user'

class UserAccount(models.Model):
    id = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=50L, unique=True)
    password = models.CharField(max_length=50L)
    email = models.CharField(max_length=100L)
    role = models.ForeignKey(Role)
    class Meta:
        db_table = 'user_account'

class UserAccountPerCensus(models.Model):
    id = models.IntegerField(primary_key=True)
    census = models.ForeignKey(Census)
    user_account = models.ForeignKey(UserAccount)
    class Meta:
        db_table = 'user_account_per_census'

class Vote(models.Model):
    id = models.IntegerField(primary_key=True)
    token = models.CharField(max_length=150L)
    vote_type = models.ForeignKey('VoteType')
    vote_date = models.DateField()
    class Meta:
        db_table = 'vote'

class VoteType(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=10L)
    class Meta:
        db_table = 'vote_type'