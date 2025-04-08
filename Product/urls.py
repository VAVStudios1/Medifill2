from django.contrib import admin
from django.urls import path
from Product import views
from . import *


urlpatterns = [
    path("view/<str:product_name>/", views.Product_view , name="product_view"),
    path("search", views.Product_search , name="search"),
    
    
   
  
]
