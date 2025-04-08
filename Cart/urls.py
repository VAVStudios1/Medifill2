from django.contrib import admin
from django.urls import path
from Cart import views
from . import *


urlpatterns = [
    path("add-to-cart/<id>/", views.add_to_cart , name="add_to_cart"),
    path("remove-cart/<id>/", views.remove_cart , name="remove_cart"),
    path("", views.Cart , name="Cart")

    
   
  
]
