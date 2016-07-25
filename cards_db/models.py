# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models
import random


class OneDay(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    age = models.CharField(max_length=20, blank=True, null=True)
    team = models.CharField(max_length=15, blank=True, null=True)
    playing_role = models.CharField(max_length=20, blank=True, null=True)
    one_day_matches = models.IntegerField(blank=True, null=True)
    one_day_not_outs = models.IntegerField(blank=True, null=True)
    one_day_runs = models.IntegerField(blank=True, null=True)
    one_day_highest_score = models.IntegerField(blank=True, null=True)
    one_day_bat_average = models.FloatField(blank=True, null=True)
    one_day_bat_str_rate = models.FloatField(blank=True, null=True)
    one_day_hundreds = models.IntegerField(blank=True, null=True)
    one_day_fifties = models.IntegerField(blank=True, null=True)
    one_day_fours = models.IntegerField(blank=True, null=True)
    one_day_sixes = models.IntegerField(blank=True, null=True)
    one_day_balls = models.IntegerField(blank=True, null=True)
    one_day_runs_against = models.IntegerField(blank=True, null=True)
    one_day_wickets = models.IntegerField(blank=True, null=True)
    one_day_bbm_wkts = models.IntegerField(blank=True, null=True)
    one_day_bbm_runs = models.IntegerField(blank=True, null=True)
    one_day_bowl_average = models.FloatField(blank=True, null=True)
    one_day_econ_rate = models.FloatField(blank=True, null=True)
    one_day_bowl_str_rate = models.FloatField(blank=True, null=True)
    one_day_no_of_five_wickets = models.FloatField(blank=True, null=True)
    date = models.DateField()

    def __str__(self):
	return str(self.name)

    class Meta:
        db_table = 'one_day'


class Tests(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    age = models.CharField(max_length=20, blank=True, null=True)
    team = models.CharField(max_length=15, blank=True, null=True)
    playing_role = models.CharField(max_length=20, blank=True, null=True)
    test_matches = models.IntegerField(blank=True, null=True)
    test_not_outs = models.IntegerField(blank=True, null=True)
    test_runs = models.IntegerField(blank=True, null=True)
    test_highest_score = models.IntegerField(blank=True, null=True)
    test_bat_average = models.FloatField(blank=True, null=True)
    test_bat_str_rate = models.FloatField(blank=True, null=True)
    test_hundreds = models.IntegerField(blank=True, null=True)
    test_fifties = models.IntegerField(blank=True, null=True)
    test_fours = models.IntegerField(blank=True, null=True)
    test_sixes = models.IntegerField(blank=True, null=True)
    test_balls = models.IntegerField(blank=True, null=True)
    test_runs_against = models.IntegerField(blank=True, null=True)
    test_wickets = models.IntegerField(blank=True, null=True)
    test_bbi_wkts = models.IntegerField(blank=True, null=True)
    test_bbi_runs = models.IntegerField(blank=True, null=True)
    test_bbm_wkts = models.IntegerField(blank=True, null=True)
    test_bbm_runs = models.IntegerField(blank=True, null=True)
    test_bowl_average = models.FloatField(blank=True, null=True)
    test_econ_rate = models.FloatField(blank=True, null=True)
    test_bowl_str_rate = models.FloatField(blank=True, null=True)
    test_no_of_five_wickets = models.IntegerField(blank=True, null=True)
    date = models.DateField()

    def __str__(self):
	return self.name

    class Meta:
        db_table = 'tests'


