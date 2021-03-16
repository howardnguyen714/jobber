from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login

# Create your views here.

from django.http import HttpResponse
def home(request):
    return render(request, 'home.html')

def profile(request):
    return render(request, 'profile.html')