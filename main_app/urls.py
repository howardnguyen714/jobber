from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('profile/', views.profile, name='profile'),
    path('profile/edit', views.edit, name='edit'),
    path('accounts/signup/', views.signup, name='signup'),
]