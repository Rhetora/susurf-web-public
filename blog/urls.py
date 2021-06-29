from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from . import views


app_name = 'blog'
urlpatterns = [
    path('blog/', views.blogList, name='blogList'),  
    path('blog/<int:blogID>/', views.blogDetail, name='blogDetail'),  
]