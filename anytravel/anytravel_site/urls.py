from django.conf.urls import patterns, include, url
from django.contrib.auth   import *
from anytravel_site import views

urlpatterns = patterns('',
    url( r'^$', views.index, name='index' )
    #url( r'^login/$', 'django.contrib.auth.views.login', name='login' )
)