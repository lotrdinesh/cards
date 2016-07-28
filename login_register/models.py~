from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.contrib.auth.signals import user_logged_in, user_logged_out


# Create your models here.

class LoggedInUsers(models.Model):
    username = models.TextField()

    def pop(name):
	LoggedInUsers.object.delete(username = User.objects.get(username = name).username)	



class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name = 'user')
    bio = models.TextField(default = '', blank =True)
    phone = models.CharField(max_length = 20, default = '', blank =True)
    city = models.CharField(max_length = 100, default = '', blank =True)
    country = models.CharField(max_length = 100, default = '', blank =True)
    
def create_profile(sender, **kwargs):
    user = kwargs["instance"]
    if kwargs["created"]:
	user_profile =UserProfile(user=user)
	user_profile.save()	

post_save.connect(create_profile, sender = User)


def logged_in(sender, user, request, **kwargs):
    loggedinuser = LoggedInUsers(username =user.username)
    loggedinuser.save()

user_logged_in.connect(logged_in)

def logged_out(sender, user, request, **kwargs):
    loggedoutuser = LoggedInUsers.objects.get(username =user.username)
    loggedoutuser.delete()
	
user_logged_out.connect(logged_out)


