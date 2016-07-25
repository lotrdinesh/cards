from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^update/(?P<pk>\d+)/$', views.edit_user, name='update'),
]


