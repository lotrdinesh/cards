from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.template.context_processors import csrf


def loggedin(request):
    user=request.user	
    return render_to_response('registration/loggedin.html', {'user': user})

