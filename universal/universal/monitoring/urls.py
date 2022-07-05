from django.urls import path

from .views import *

urlpatterns = [    
    path('', index, name="home"),
    path('diagnostic/', diagnostic, name="diagnostic"),
    path('statistics/', statistics, name="statistics"),
    path('customization/', customization, name="customization"), 
    path('help/', help, name="help"), 
    path('reference/', reference, name="reference"), 
    path('contract/', contract, name="contract"), 
    path('profile/', profile, name="profile"),     
    path('login/', login, name="login"),    
    path('errors/', errors, name="errors"), 
    path('register/', register, name="register"),  
]

#path('monitoring/<int:pk>/',monitoring),