#encodign: utf-8
from django.db import models

class role (models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return '%s' % (self.name)

class user_account(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=200, unique = True)
    password = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    role_id = models.ForeignKey(role)

    def __str__(self):
        return '%s' % (self.username)
    
class cookie (models.Model):
    number_id = models.AutoField(primary_key=True)
    user_account_id = models.ForeignKey(user_account)

    def __str__(self):
        return '%s' % (self.number_id)
    
class ca (models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)

    def __str__(self):
        return '%s' % (self.name)
    
class user (models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)
    genre = models.CharField(max_length=200)
    edad = models.IntegerField()
    dni = models.CharField(max_length=200)
    ca_id = models.ForeignKey(ca)
    user_account_id = models.ForeignKey(user_account)

    def __str__(self):
        return '%s' % (self.name)

class census (models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    postalcode = models.IntegerField()
    ca_id = models.ForeignKey(ca)

    def __str__(self):
        return '%s' % (self.title)

class user_account_per_census(models.Model):
    id = models.AutoField(primary_key=True)
    census_id = models.ForeignKey(census)
    user_account_id = models.ForeignKey(user_account)
    
    def __str__(self):
        return '%s' % (self.id)
    
class poll (models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    startDate = models.DateField()
    endDate = models.DateField()
    census_id = models.ForeignKey(census)
    
    def __str__(self):
        return '%s' % (self.title)
    
class question(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    optional = models.BooleanField()
    multiple = models.BooleanField()
    poll_id = models.ForeignKey(poll)
    
    def __str__(self):
        return '%s' % (self.title)
    
class question_option(models.Model):
    id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=200)
    question_id = models.ForeignKey(question)

    def __str__(self):
        return '%s' % (self.description)
    
class vote_type(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return '%s' % (self.name)
    
class vote(models.Model):
    id = models.AutoField(primary_key=True)
    token = models.CharField(max_length=200)
    vote_type_id  = models.ForeignKey(vote_type)
    vote_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return '%s %s' % (self.id)
    
class option_per_vote(models.Model):
    id = models.AutoField(primary_key=True)
    vote_id = models.ForeignKey(vote)
    question_option_id = models.ForeignKey(question_option)
    
    def __str__(self):
        return '%s %s' % (self.id)
