
from django.urls import include, path
from . import views
from django.apps import apps
from django.conf.urls import include, url
from django.contrib import admin
app_name = 'accounts'

urlpatterns = [
    path('signup', views.signup,name= 'signup'),
    path('profile', views.profile,name= 'profile'),
    path('profile/edite', views.profile_edite,name= 'profile_edite'),



]
