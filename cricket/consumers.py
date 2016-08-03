import re
import json, random
import logging
from channels import Group
from channels.sessions import channel_session
from channels.auth import http_session_user, channel_session_user, channel_session_user_from_http
from Room.models import Gameroom, Message
from cards_db.models import Tests
from Room.serializers import Message_Serializer
from cards_db.serializers import Tests_Serializer
from django.http import JsonResponse


log = logging.getLogger(__name__)

@channel_session
@channel_session_user_from_http
def ws_connect(message):
    
    try:
        game, prefix, label = message['path'].decode('ascii').strip('/').split('/')
	
	if prefix != 'tests' and prefix != 'oneday':
           log.debug('invalid ws path=%s', message['path'])
           return
	room = Gameroom.objects.get(label=label)
    except ValueError:
        log.debug('invalid ws path=%s', message['path'])
        return
    except Room.DoesNotExist:
        log.debug('ws room does not exist label=%s', label)
        return

    log.debug('chat connect room=%s client=%s:%s', room.label, message['client'][0], message['client'][1])
    
    Group(prefix+'-'+label, channel_layer=message.channel_layer).add(message.reply_channel)

    message.channel_session['room'] = room.label

    game = Message.objects.get(Gameroom = room)	
    
    if not game.player_one:
	if game.user_two is not None and game.type_of_game == 'tests':
	    player_one = Tests.objects.get(id = random.randint(1182,1605))
	    player_two = None
	    while not player_two:
	        player_temp = Tests.objects.get(id = random.randint(1182,1605))
		if player_temp.id !=player_one.id:
                   player_two = player_temp
	    player_one_s = Tests_Serializer(player_one)
	    player_two_s = Tests_Serializer(player_two)
    	    game.player_one = player_one.name
	    game.player_two = player_two.name
	    game.save()
    else:
	if game.type_of_game == 'tests':
	    player_one = Tests.objects.get(name = game.player_one)
	    player_two = Tests.objects.get(name = game.player_two)
	    player_one_s = Tests_Serializer(player_one)
	    player_two_s = Tests_Serializer(player_two)
    	    
    serializer = Message_Serializer(game)
    if game.user_two is not None:
	Group(prefix+'-'+label, channel_layer=message.channel_layer).send({'text':json.dumps({"message":serializer.data, "player_one":player_one_s.data,"player_two":player_two_s.data})})
	


@channel_session
def ws_receive(message):
    try:
        label = message.channel_session['room']
        room = Room.objects.get(label=label)
    except KeyError:
        log.debug('no room in channel_session')
        return
    except Room.DoesNotExist:
        log.debug('recieved message, but room does not exist label=%s', label)
        return
    # Parse out a chat message from the content text, bailing if it doesn't
    # conform to the expected message format.
    try:
        data = json.loads(message['text'])
    except ValueError:
        log.debug("ws message isn't json text=%s", text)
        return
        
    if data:
        log.debug('game message room=%s handle=%s field_selected=%s', 
            room.label, data['handle'], data['id'])
        m = room.messages.all()[0]
	m.handle = data['handle']
	m.compare(data['id']);
        serializer = Message_Serializer(m)
        Group(prefix+'-'+label, channel_layer=message.channel_layer).send({'text': json.dumps({"message":serializer.data})})

  
@channel_session
def ws_disconnect(message):
    pass
'''
    try:
        label = message.channel_session['room']
        room = Room.objects.get(label=label)
        Group('chat-'+label, channel_layer=message.channel_layer).discard(message.reply_channel)
    except (KeyError, Room.DoesNotExist):
   pass
'''
