# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations

class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ca',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', fernet_fields.fields.EncryptedCharField(max_length=100)),
            ],
            options={
                'db_table': 'ca',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Census',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100)),
                ('postalcode', models.IntegerField(null=True, db_column='postalCode', blank=True)),
            ],
            options={
                'db_table': 'census',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Cookie',
            fields=[
                ('number_id', models.CharField(max_length=40, serialize=False, primary_key=True)),
            ],
            options={
                'db_table': 'cookie',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='OptionPerVote',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
                'db_table': 'option_per_vote',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Poll',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=150, null=True, blank=True)),
                ('startdate', models.DateField(db_column='startDate')),
                ('enddate', models.DateField(db_column='endDate')),
            ],
            options={
                'db_table': 'poll',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=150, null=True, blank=True)),
                ('optional', models.IntegerField()),
                ('multiple', models.IntegerField()),
            ],
            options={
                'db_table': 'question',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='QuestionOption',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description', models.CharField(max_length=150, null=True, blank=True)),
            ],
            options={
                'db_table': 'question_option',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'role',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('surname', models.CharField(max_length=200)),
                ('genre', models.CharField(max_length=1)),
                ('edad', models.DateField()),
                ('dni', models.CharField(max_length=9)),
            ],
            options={
                'db_table': 'user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='UserAccount',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('username', models.CharField(unique=True, max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'user_account',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='UserAccountPerCensus',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
                'db_table': 'user_account_per_census',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('token', models.CharField(max_length=150)),
                ('vote_date', models.DateField()),
            ],
            options={
                'db_table': 'vote',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='VoteType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'vote_type',
                'managed': False,
            },
        ),
    ]
