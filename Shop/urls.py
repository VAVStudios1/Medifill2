from django.urls import path
from Shop import views
from . import *


urlpatterns = [
  
    path("", views.Shop , name="Shop"),
    path("dashboards", views.dashboards , name="dashboards"),
    path("dashboards/insert", views.insert , name="insert"),
    # path("registration", views.registration , name="registration"),
    
    
   
  
]