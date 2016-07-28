from django.conf.urls import url, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'cricket/tests/view', views.Tests_ViewSet)
router.register(r'cricket/oneday/view', views.OneDay_ViewSet)

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^cricket/$', views.cricket, name = 'cricket'),
    url(r'^cricket/tests/$', views.tests_enter, name = 'tests'),
    url(r'^cricket/tests/(?P<label>[\w-]{,50})$', views.tests, name = 'tests_game'),
    url(r'^cricket/oneday/$', views.oneday, name='oneday'),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace = 'rest_framework'))
]
