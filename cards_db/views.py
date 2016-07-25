from django.shortcuts import render, get_object_or_404, redirect
from .models import Tests, OneDay
from .serializers import Tests_Serializer, OneDay_Serializer
from rest_framework import viewsets, response
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
import random
from rest_framework.renderers import JSONRenderer
from Room.models import Gameroom, Message


# Create your views here.

def index(request):
    return render(request, 'cards_db/index.html')

def cricket(request):
    return render(request, 'cards_db/cricket.html')    

@login_required
def tests(request):
    pass  
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
