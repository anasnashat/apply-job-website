from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, render

from .forms import SignupForm,Userform,ProfileForm
from .models import Profile
from django.urls import reverse



# Create your views here.
def signup (request):
     if request.method=='POST':
          form = SignupForm(request.POST)
          if form.is_valid:
               form.save()
               username= form.cleaned_data['username']
               password=form.cleaned_data['password1']
               user= authenticate(username=username,password=password)
               login(request,user)
               return redirect('/account/profile')

     else:
          form = SignupForm()


     return render ( request , 'registration/signup.html',{'form':form})







def profile(request):
     profile=Profile.objects.get(user=request.user)
     return render (request, 'accounts/profile.html',{'profile':profile})



def profile_edite(request):
     profile=Profile.objects.get(user=request.user)
     if request.method=='POST':
          userform=Userform(request.POST,instance=request.user)
          profileform=ProfileForm(request.POST,request.FILES,instance=profile)
          if userform.is_valid and profileform.is_valid:
               userform.save()
               myform = profileform.save(commit=False)
               myform.user = request.user
               myform.save()
               return redirect(reverse('accounts:profile'))

     else:
          userform=Userform(instance=request.user)
          profileform=ProfileForm(instance=profile)


     return render (request, 'accounts/profile_edite.html',{'userform':userform,'profileform':profileform})
