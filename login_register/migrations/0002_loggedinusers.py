# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-24 15:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login_register', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='LoggedInUsers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.TextField()),
            ],
        ),
    ]
