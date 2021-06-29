from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

app_name = 'events'
urlpatterns = [
    path('events/', views.eventsPage, name='events'),
    path('events/<int:eventID>/', views.eventDetail, name='eventDetail'),
    path('events/<int:eventID>/signup', views.signup, name='signup'),
    path('events/signupConfirm', views.signupConfirmation, name='confirmation'),
    path('events/<int:eventID>/admin', views.eventAdmin, name='eventAdmin'),
]
