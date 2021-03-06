from .models import Tests, OneDay
from rest_framework import serializers


class OneDay_Serializer(serializers.ModelSerializer):
    
    class Meta:
	model = OneDay
	fields = ('id', 'name','age', 'team', 'one_day_matches', 'one_day_not_outs', 'one_day_runs', 'one_day_highest_score', 'one_day_bat_average', 'one_day_bat_str_rate', 'one_day_hundreds','one_day_fifties','one_day_fours','one_day_sixes','one_day_balls', 'one_day_runs_against', 'one_day_wickets', 'one_day_bbm_wkts', 'one_day_bbm_runs', 'one_day_bowl_average', 'one_day_econ_rate', 'one_day_bowl_str_rate', 'one_day_no_of_five_wickets')


class Tests_Serializer(serializers.ModelSerializer):
    
    class Meta:
	model = Tests
	fields = ('id', 'name','age', 'team', 'test_matches', 'test_not_outs', 'test_runs', 'test_highest_score', 'test_bat_average', 'test_bat_str_rate', 'test_hundreds','test_fifties','test_fours','test_sixes','test_balls', 'test_runs_against', 'test_wickets', 'test_bbm_wkts', 'test_bbm_runs', 'test_bowl_average', 'test_econ_rate', 'test_bowl_str_rate', 'test_no_of_five_wickets')


