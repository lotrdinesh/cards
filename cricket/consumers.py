import re
import json, random
import logging
from channels import Group
from channels.sessions import channel_session
from Room.models import Gameroom, Message
from cards_db.models import Tests
from Room.serializers import Message_Serializer
from django.http import JsonResponse

log = logging.getLogger(__name__)

@channel_session
def ws_connect(message):
    try:
        game, prefix, label = message['path'].decode('ascii').strip('/').split('/')
        if prefix != 'tests' or prefix != 'oneday':
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
    
    if prefix == 'tests': 
    	Group('tests-'+label, channel_layer=message.channel_layer).add(message.reply_channel)
    if prefix == 'oneday': 
    	Group('oneday-'+label, channel_layer=message.channel_layer).add(message.reply_channel)
    message.channel_session['room'] = room.label

    game = Message.objects.filter(Gameroom = room)

    if game.user_two:
	if game.type_of_game == 'tests': 
	    player_one = Tests.object.get(id = random.randint(1182,1605))
	    player_two = None
	    while not player_two:
	    	player_temp = Tests.object.get(id = random.randint(1182,1605))
		if player_temp.id !=player_one.id:
                    player_two = player_temp
		    
            game.player_one = player_one.name
	    game.player_two = player_two.name
 	    serializer = Message_Serializer(game)
	    player_one_s = Tests_Serializer(player_one)
	    player_two_s = Tests_Serializer(player_two)
	    Group(prefix+'-'+label, channel_layer=message.channel_layer).send({'data': JsonResponse(serializer.data), 'player_one':player_one_s, 'player_two':player_two_s})




@channel_session
def ws_receive(message):
    pass
    # Look up the room from the channel session, bailing if it doesn't exist
    '''   
    try:
        label = message.channel_session['room']
        room = Room.objects.get(label=label)
    except KeyError:
        log.debug('no room in channel_session')
        return
    except Room.DoesNotExist:
        log.debug('recieved message, buy room does not exist label=%s', label)
        return

    # Parse out a chat message from the content text, bailing if it doesn't
    # conform to the expected message format.
    try:
        data = json.loads(message['text'])
    except ValueError:
        log.debug("ws message isn't json text=%s", text)
        return
    
    if set(data.keys()) != set(('handle', 'message')):
        log.debug("ws message unexpected format data=%s", data)
        return

    if data:
        log.debug('chat message room=%s handle=%s message=%s', 
            room.label, data['handle'], data['message'])
        m = room.messages.create(**data)

        # See above for the note about Group
        Group('chat-'+label, channel_layer=message.channel_layer).send({'text': json.dumps(m.as_dict())})
    '''
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
