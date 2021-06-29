from django.urls import path

from . import views

app_name = 'kit'
urlpatterns = [
    path('kit', views.kitHome, name='kitHome'),
    path('kit/logout', views.kitLogout, name='kitLogout'),
    path('kit/borrowing', views.kitBorrowing, name='kitBorrowing'),
    path('kit/care', views.kitCare, name='kitCare'),
    path('kit/logout/takeBoard/<int:ID>', views.takeBoard, name='takeBoard'),
    path('kit/logout/returnBoard/<int:ID>', views.returnBoard, name='returnBoard'),
    path('kit/logout/takeSuit/<int:ID>', views.takeSuit, name='takeSuit'),
    path('kit/logout/returnSuit/<int:ID>', views.returnSuit, name='returnSuit'),
    path('kit/logout/takeMisc/<int:ID>', views.takeMisc, name='takeMisc'),
    path('kit/logout/returnMisc/<int:ID>', views.returnMisc, name='returnMisc'),
]
