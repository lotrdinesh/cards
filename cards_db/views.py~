from django.shortcuts import render, get_object_or_404, redirect
from .models import Tests, OneDay
from .serializers import Tests_Serializer, OneDay_Serializer
from rest_framework import viewsets, response
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
import random, haikunator
from rest_framework.renderers import JSONRenderer
from Room.models import Gameroom, Message
from django.db import transaction
import logging

# Create your views here.
log = logging.getLogger(__name__)

def index(request):
    return render(request, 'cards_db/index.html')

def cricket(request):
    return render(request, 'cards_db/cricket.html')    

@login_required
def tests_enter(request):
    try:
	if ('label' in request.COOKIES):
	    room = Gameroom.objects.get (label = request.COOKIES['label'])
	    
    	else:
	    record_counts = Message.objects.filter(user_two = None).count()
	    if (record_counts != 0):
	        record = Message.objects.filter(user_two = None)[0]
		record.user_two = request.user.username
		record.save()
		room = record.Gameroom
	    else:
		room=new_room()                
		message = Message.objects.create( Gameroom=room, handle ='start', user_one = request.user.username, max_cards = 5, type_of_game = 'tests', player_one_turn=True, player_two_turn=False)    
    except Gameroom.DoesNotExist:
	log.debug("Already playing an existing game in another room")	
     
    return redirect(tests, label=room.label)	  

'''
    if request.method == 'POST':
	if request.is_ajax():
	    player_two = get_object_or_404(Tests, id = random.randint(1182,1605))
	    serializer = Tests_Serializer(player_two)
	    return JsonResponse(serializer.data)
    	    
    if 'test_player_name' in request.COOKIES:
	player_name = request.COOKIES['test_player_name']
	player = get_object_or_404(Tests, name = player_name)
    else:
	player = get_object_or_404(Tests, id = random.randint(1182,1605))
	
    resp = render(request, 'cards_db/tests.html',{'player':player}) 
    resp.set_cookie('test_player_name', player.name)    
    return resp
 '''  
@login_required    
def tests(request, label):
    room, created = Gameroom.objects.get_or_create(label = label)
    messages = room.messages.all()[0]
    print room.label
    response = render(request, "cards_db/tests.html", {'room': room, 'messages':messages,})
    response.set_cookie('label', room.label)
    response.set_cookie('username', request.user.username)
    return response
  






@login_required
def oneday(request):
    if 'oneday_player_name' in request.COOKIES:
	player_name = request.COOKIES['oneday_player_name']
	player = get_object_or_404(OneDay, name = player_name)
    else:
	player = get_object_or_404(Tests, id = random.randint(1182,1605))

    resp = render(request, 'cards_db/one_day.html',{'player':player}) 
    resp.set_cookie('oneday_player_name', player.name)    
    return resp

class Tests_ViewSet(viewsets.ModelViewSet):
    queryset = Tests.objects.all()
    serializer_class = Tests_Serializer	 

class OneDay_ViewSet(viewsets.ModelViewSet):
    queryset = OneDay.objects.all()
    serializer_class = OneDay_Serializer



def new_room():
    new_room = None
    while not new_room:
    	with transaction.atomic():
       	    label = haikunator.Haikunator().haikunate()
            if Gameroom.objects.filter(label=label).exists():
                continue
            new_room = Gameroom.objects.create(label=label)
	
    new_room.name = 'Room-' + str(Gameroom.objects.get(label = label).id)
    return new_room
