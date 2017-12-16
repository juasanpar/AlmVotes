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


class ApiCa(models.Model):
    name = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'api_ca'


class ApiCensus(models.Model):
    title = models.CharField(max_length=200)
    postalcode = models.IntegerField()
    ca_id = models.ForeignKey(ApiCa)

    class Meta:
        managed = False
        db_table = 'api_census'


class ApiCookie(models.Model):
    number_id = models.AutoField(primary_key=True)
    user_account_id = models.ForeignKey('ApiUserAccount')

    class Meta:
        managed = False
        db_table = 'api_cookie'


class ApiOptionPerVote(models.Model):
    question_option_id = models.ForeignKey('ApiQuestionOption')
    vote_id = models.ForeignKey('ApiVote')

    class Meta:
        managed = False
        db_table = 'api_option_per_vote'


class ApiPoll(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    startdate = models.DateField(db_column='startDate')  # Field name made lowercase.
    enddate = models.DateField(db_column='endDate')  # Field name made lowercase.
    census_id = models.ForeignKey(ApiCensus)

    class Meta:
        managed = False
        db_table = 'api_poll'


class ApiQuestion(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    optional = models.IntegerField()
    multiple = models.IntegerField()
    poll_id = models.ForeignKey(ApiPoll)

    class Meta:
        managed = False
        db_table = 'api_question'


class ApiQuestionOption(models.Model):
    description = models.CharField(max_length=200)
    question_id = models.ForeignKey(ApiQuestion)

    class Meta:
        managed = False
        db_table = 'api_question_option'


class ApiRole(models.Model):
    name = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'api_role'


class ApiUser(models.Model):
    name = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)
    genre = models.CharField(max_length=200)
    edad = models.IntegerField()
    dni = models.CharField(max_length=200)
    ca_id = models.ForeignKey(ApiCa)
    user_account_id = models.ForeignKey('ApiUserAccount')

    class Meta:
        managed = False
        db_table = 'api_user'


class ApiUserAccount(models.Model):
    username = models.CharField(unique=True, max_length=200)
    password = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    role_id = models.ForeignKey(ApiRole)

    class Meta:
        managed = False
        db_table = 'api_user_account'


class ApiUserAccountPerCensus(models.Model):
    census_id = models.ForeignKey(ApiCensus)
    user_account_id = models.ForeignKey(ApiUserAccount)

    class Meta:
        managed = False
        db_table = 'api_user_account_per_census'


class ApiVote(models.Model):
    token = models.CharField(max_length=200)
    vote_date = models.DateTimeField()
    vote_type_id = models.ForeignKey('ApiVoteType')

    class Meta:
        managed = False
        db_table = 'api_vote'


class ApiVoteType(models.Model):
    name = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'api_vote_type'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup)
    permission = models.ForeignKey('AuthPermission')

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group_id', 'permission_id'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    content_type = models.ForeignKey('DjangoContentType')
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type_id', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254, blank=True, null=True)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser)
    group = models.ForeignKey(AuthGroup)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user_id', 'group_id'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser)
    permission = models.ForeignKey(AuthPermission)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user_id', 'permission_id'),)


class Ca(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'ca'


class Census(models.Model):
    title = models.CharField(max_length=100)
    postalcode = models.IntegerField(db_column='postalCode', blank=True, null=True)  # Field name made lowercase.
    ca = models.ForeignKey(Ca)

    class Meta:
        managed = False
        db_table = 'census'


class Cookie(models.Model):
    number_id = models.CharField(primary_key=True, max_length=40)
    user_account = models.ForeignKey('UserAccount')

    class Meta:
        managed = False
        db_table = 'cookie'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', blank=True, null=True)
    user = models.ForeignKey(AuthUser)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


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


class UserAccount(models.Model):
    username = models.CharField(unique=True, max_length=50)
    password = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    role = models.ForeignKey(Role)

    class Meta:
        managed = False
        db_table = 'user_account'


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


class VoteType(models.Model):
    name = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'vote_type'
