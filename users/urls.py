from django.urls import path, include
from django.contrib.auth import views as auth_views

from . import views

app_name = 'users'
urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('signup/confirmed', views.signupConfirmation, name='signupConfirmation'),

    path('login/', views.login_req, name='login_req'),
    path('logout/', views.logout_req, name='logout_req'),

    path('password_change/', views.password_change, name='password_change'),
    path('password_change/confirm', views.passwordChangeConfirmed, name='passwordChangeConfirmed'),
]
