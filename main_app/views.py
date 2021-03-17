from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from .forms import UserForm
from .models import Event, User
from random import randint

# Create your views here.

from django.http import HttpResponse
def home(request):
  events = Event.objects.all()
  rand_event_1 = events[randint(0, len(events)-1)]
  rand_event_2 = events[randint(0, len(events)-1)]
  rand_event_3 = events[randint(0, len(events)-1)]
  rand_event_4 = events[randint(0, len(events)-1)]
  while rand_event_2 == rand_event_1:
    rand_event_2 = events[randint(0, len(events)-1)]
  while rand_event_3 == rand_event_2 or rand_event_3 == rand_event_1:
    rand_event_3 = events[randint(0, len(events)-1)]
  while rand_event_4 == rand_event_3 or rand_event_4 == rand_event_2 or rand_event_4 == rand_event_1:
    rand_event_4 = events[randint(0, len(events)-1)]
  form = UserCreationForm()
  context = {
    'form': form,
    'event_1': rand_event_1,
    'event_2': rand_event_2,
    'event_3': rand_event_3,
    'event_4': rand_event_4
  }
  return render(request, 'home.html', context)

@login_required
def profile(request):
  return render(request, 'profile.html')

def edit(request):
  user = User.objects.get(username=request.user)
  print(user)
  # user=request.user
  user_form = UserForm(request.POST or None, instance=user)
  # print(user)
  if request.POST and user_form.is_valid():
    user_form.save()
    return redirect('profile')
  else:
    return render(request, 'edit.html', { 'user_form': user_form })

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('profile')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'home.html', context)