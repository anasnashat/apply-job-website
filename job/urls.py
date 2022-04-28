
from django.urls import include, path
from . import views
from django.apps import apps
from django.conf.urls import include, url
from django.contrib import admin
app_name = 'job'

urlpatterns = [
    path('', views.job_liste,name= 'job_list'),
    path('add', views.add_job, name='add_job'),
    path('<str:slug>', views.job_detalis, name='job_detail'),

]
