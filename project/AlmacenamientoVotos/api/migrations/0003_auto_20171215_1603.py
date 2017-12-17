# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20171210_1704'),
    ]

    operations = [
        migrations.CreateModel(
            name='ca',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='census',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('postalcode', models.IntegerField()),
                ('ca_id', models.ForeignKey(to='api.ca')),
            ],
        ),
        migrations.CreateModel(
            name='cookie',
            fields=[
                ('number_id', models.AutoField(serialize=False, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='option_per_vote',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='poll',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=200)),
                ('startDate', models.DateField()),
                ('endDate', models.DateField()),
                ('census_id', models.ForeignKey(to='api.census')),
            ],
        ),
        migrations.CreateModel(
            name='question',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=200)),
                ('optional', models.BooleanField()),
                ('multiple', models.BooleanField()),
                ('poll_id', models.ForeignKey(to='api.poll')),
            ],
        ),
        migrations.CreateModel(
            name='question_option',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('description', models.CharField(max_length=200)),
                ('question_id', models.ForeignKey(to='api.question')),
            ],
        ),
        migrations.CreateModel(
            name='role',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('surname', models.CharField(max_length=200)),
                ('genre', models.CharField(max_length=200)),
                ('edad', models.IntegerField()),
                ('dni', models.CharField(max_length=200)),
                ('ca_id', models.ForeignKey(to='api.ca')),
            ],
        ),
        migrations.CreateModel(
            name='user_account',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('username', models.CharField(unique=True, max_length=200)),
                ('password', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('role_id', models.ForeignKey(to='api.role')),
            ],
        ),
        migrations.CreateModel(
            name='user_account_per_census',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('census_id', models.ForeignKey(to='api.census')),
                ('user_account_id', models.ForeignKey(to='api.user_account')),
            ],
        ),
        migrations.CreateModel(
            name='vote',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('token', models.CharField(max_length=200)),
                ('vote_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='vote_type',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.DeleteModel(
            name='Voto',
        ),
        migrations.AddField(
            model_name='vote',
            name='vote_type_id',
            field=models.ForeignKey(to='api.vote_type'),
        ),
        migrations.AddField(
            model_name='user',
            name='user_account_id',
            field=models.ForeignKey(to='api.user_account'),
        ),
        migrations.AddField(
            model_name='option_per_vote',
            name='question_option_id',
            field=models.ForeignKey(to='api.question_option'),
        ),
        migrations.AddField(
            model_name='option_per_vote',
            name='vote_id',
            field=models.ForeignKey(to='api.vote'),
        ),
        migrations.AddField(
            model_name='cookie',
            name='user_account_id',
            field=models.ForeignKey(to='api.user_account'),
        ),
    ]
