from django.shortcuts import render
from django.contrib.auth import logout, authenticate, login
from django.template.context_processors import csrf
from login_register.models import LoggedInUsers 

def logout_view(request):
    logout(request)
    return render(request, 'cards_db/index.html')
 
