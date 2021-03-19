from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('profile/', views.profile, name='profile'),
    path('profile/edit', views.edit, name='edit'),
    path('accounts/signup/', views.signup, name='signup'),
    path('events/<int:event_id>/', views.events_detail, name='detail'),
    path('events/<int:event_id>/assoc_event/<int:user_id>/', views.assoc_event, name="assoc_event"),
    path('events/<int:event_id>/unassoc_event/<int:user_id>/', views.unassoc_event, name="unassoc_event"),
    path('search/', views.get_category, name="get_category")
]