from django.contrib import admin
from django.urls import path
from Order import views
# from . import *


urlpatterns = [
    # path("add-to-cart/<id>/", views.add_to_cart , name="add_to_cart"),
    # path("remove-cart/<id>/", views.remove_cart , name="remove_cart"),
    path("", views.Order , name="Cart"),
    path("status", views.Status , name="Cart"),

    
   
  
]
