from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
# Create your models here.

class Gameroom(models.Model):
    name = models.TextField()
    label = models.SlugField(unique=True)

    def __str__(self):
        return self.label

    def new_room():
   	new_room = None
    	while not new_room:
            with transaction.atomic():
                label = haikunator.Haikunator().haikunate()
            	if Gameroom.objects.filter(label=label).exists():
                    continue
            new_room = Gameroom.objects.create(label=label)
	
   	new_room.name = 'Room' + Gameroom.objects.get(label = label).id
	return new_room

class Message(models.Model):
    Gameroom = models.ForeignKey(Gameroom, related_name='messages')
    handle = models.TextField()
    user_one = models.TextField()
    user_two = models.TextField(blank=True, null=True)
    player_one = models.TextField(blank=True, null=True)
    player_two = models.TextField(blank=True, null=True) 
    user_one_score = models.IntegerField(default = 0)
    user_two_score = models.IntegerField(default = 0)
    max_cards = models.IntegerField()
    type_of_game = models.TextField()
    player_one_turn = models.BooleanField()
    player_two_turn = models.BooleanField()
    timestamp = models.DateTimeField(default=timezone.now, db_index=True)
    '''
    def __str__(self):
    	return '[{timestamp}] {handle}: {message}'.format(**self.as_dict())
   
    def as_dict(self):
        return {'handle': self.handle, 'message': self.message, 'timestamp': self.formatted_timestamp}
    '''

