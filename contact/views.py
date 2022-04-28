from django.core.mail import send_mail
from django.shortcuts import render
from django.conf import settings
from requests.api import request
from .models import Info

# Create your views here.


def send_messag(request):
     myinfo = Info.objects.first()
     if request.method== 'POST':
          subject=request.POST['subject']
          email=request.POST['email']
          masseg= request.POST['message']
          
          send_mail(
               subject,
               masseg,
               settings.EMAIL_HOST_USER,
               [email],
          )

     return render(request , 'contact/contact.html', {'myinfo':myinfo})
