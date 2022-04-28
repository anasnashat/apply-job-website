
from django.urls import include, path
from . import views
from django.apps import apps
from django.conf.urls import include, url
from django.contrib import admin
app_name = 'job'

urlpatterns = [
    path('', views.send_messag,name= 'contact'),


]