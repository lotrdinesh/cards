from .models import Gameroom, Message
from rest_framework import serializers


class Message_Serializer(serializers.ModelSerializer):
    
    class Meta:
	model = Message
	fields = ('id', 'Gameroom','handle', 'user_one', 'user_two', 'player_one', 'player_two', 'user_one_score', 'max_cards', 'type_of_game', 'player_one_turn','player_two_turn','timestamp')


