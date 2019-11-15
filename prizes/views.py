from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from .models import Profile
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.

# Create your views here.
# @login_required(login_url='/accounts/login/')
def welcome(request):
    return render(request, 'base.html')

@login_required(login_url='/accounts/login/')
def new_profile(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewsProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.username = current_user
            profile.user_id=current_user.id
            profile.save()
        return redirect('profile')
    else:
        form = NewsProfileForm()
    return render(request, 'profile.html', {"form":form})

def profile(request):
    current_user = request.user
    profile = Profile.objects.get(username=current_user)
    posts=Image.objects.filter(profile_id=current_user.id)
    return render(request, 'update_profile.html',{"profile":profile})
