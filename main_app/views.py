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
  all_events = Event.objects.all()
  categories = []
  for event in all_events:
    if event.category not in categories:
      categories.append(event.category)
  context = {
    'events': Event.objects.all(),
    'categories': categories,
    'form': UserCreationForm
  }
  return render(request, 'home.html', context)

def get_category(request): 
  search_param = request.GET['search'].lower()
  category_param = request.GET['category']
  events = Event.objects.filter(title__contains=search_param, category__contains=category_param)
  return render(request, 'results.html', {'events': events})

@login_required
def profile(request):
  current_user = request.user.id
  users_events = Event.objects.filter(users__id=current_user)
  return render(request, 'profile.html', { 'users_events': users_events } )

@login_required
def edit(request):
  user = User.objects.get(username=request.user)
  user_form = UserForm(request.POST or None, instance=user)
  if request.POST and user_form.is_valid():
    user_form.save()
    return redirect('profile')
  else:
    return render(request, 'edit.html', { 'user_form': user_form })

def events_detail(request, event_id):
  event = Event.objects.get(id=event_id)
  current_user = request.user.id
  users_events = event.users.all().values_list('id')
  
  registered = True
  for user in users_events:
    if(user[0] == current_user):
      registered = False

  context = {
    'event': event,
    'registered': registered
  }
  return render(request, 'detail.html', context)

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