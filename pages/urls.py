from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from . import views


app_name = 'pages'
urlpatterns = [
    path('', views.homePage, name='home'),
    path('about/', views.aboutPage, name='about'),
    path('committee/', views.committeePage, name='committee'),
    path('join/', views.joinPage, name='join'),
    #Resources
    path('spots/', views.spotsPage, name='spots'),
    path('spots/<str:spot>/', views.spot_detail, name='spots_detail'),
    
]

if settings.DEBUG: # new
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)