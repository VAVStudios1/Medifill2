from django.contrib import admin
from django.urls import path
from Contact import views
from . import *


urlpatterns = [
    path("feedback", views.feedback , name="Home"),
    
    
   
  
]
