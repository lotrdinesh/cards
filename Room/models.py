from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from cards_db.models import Tests, OneDay

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
    
    def __str__(self):
    	return "[%s] %s: %s/%s" %(self.timestamp, self.type_of_game, self.user_one, self.user_two)
    

    def compare(self, field):
	if self.type_of_game == "tests":
	    player_one =Tests.objects.get(name=self.player_one)
	    player_two =Tests.objects.get(name=self.player_two)
	    
	    if field == "test_econ_rate" :
		if getattr(player_one, field) < getattr(player_two, field):
		    self.user_one_score += 1
		    self.player_one_turn = True
		elif getattr(player_one, field) > getattr(player_two, field):
	      	    self.user_two_score += 1
		    self.player_one_turn = False
		else:
		    self.user_one_score +=0.5
		    self.user_two_score +=0.5
	    elif field == "test_best_figs" :
		if getattr(player_one, 'test_bbm_wkts') > getattr(player_two, 'test_bbm_wkts'):
		    self.user_one_score += 1
		    self.player_one_turn = True 
		elif getattr(player_one, 'test_bbm_wkts') < getattr(player_two, 'test_bbm_wkts'):
	      	    self.user_two_score += 1
		    self.player_one_turn = False
		elif getattr(player_one, 'test_bbm_runs') < getattr(player_two, 'test_bbm_runs'):
		    self.user_one_score +=1
    		    self.player_one_turn = True
		elif getattr(player_one, 'test_bbm_runs') > getattr(player_two, 'test_bbm_runs'):
		    self.user_two_score +=1
		    self.player_one_turn = False
		else:
		    self.user_one_score +=0.5
		    self.user_two_score +=0.5
	    else:			
		if getattr(player_one, field) > getattr(player_two, field):
		    self.user_one_score += 1
    		    self.player_one_turn = True  
		elif getattr(player_one, field) < getattr(player_two, field):
	      	    self.user_two_score += 1
    		    self.player_one_turn = False
		else:
		    self.user_one_score +=0.5
		    self.user_two_score +=0.5
	    self.player_two_turn = not (self.player_one_turn) 
	    self.save()	
    
    def timeout(self):
	if self.player_one_turn == True:
		self.user_two_score += 1
		self.player_one_turn = False
	else:
	      	self.user_one_score += 1
		self.player_one_turn = True
	self.player_two_turn = not (self.player_one_turn) 
	self.save()	

