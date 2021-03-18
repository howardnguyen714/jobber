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
  context = {
    'events': Event.objects.all(),
    'form': UserCreationForm
  }
  return render(request, 'home.html', context)

@login_required
def profile(request):
  return render(request, 'profile.html')

def edit(request):
  user = User.objects.get(username=request.user)
  # print(user)
  # user=request.user
  user_form = UserForm(request.POST or None, instance=user)
  # print(user)
  if request.POST and user_form.is_valid():
    user_form.save()
    return redirect('profile')
  else:
    return render(request, 'edit.html', { 'user_form': user_form })

def events_detail(request, event_id):
  event = Event.objects.get(id=event_id)
  current_user = request.user.id
  # print(event.users.get(id=current_user).id)
  users_events = event.users.all().values_list('id')
  print(users_events)
  
  registered = True
  for user in users_events:
    print(user[0])
    print(current_user)
    if(user[0] == current_user):
      registered = False

  context = {
    'event': event,
    'registered': registered
  }
  return render(request, 'detail.html', context)

# def find_instance(users_events, current_user):
  

@login_required
def assoc_event(request, event_id, user_id):
  event = Event.objects.get(id=event_id)
  event.users.add(user_id)
  
  return redirect('detail', event_id=event_id)

@login_required
def unassoc_event(request, event_id, user_id):
  event = Event.objects.get(id=event_id)
  event.users.remove(user_id)
  
  return redirect('detail', event_id=event_id)

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