from django.urls import path
from Doctor import views
from . import *


urlpatterns = [
  
    path("", views.Doctors , name="Doctor"),
    path("registration", views.registration , name="registration"),
    path("appointment/", views.appointment , name="appointment"),
    path("dashboard", views.dashboard , name="dashboard"),
    path("profile/<str:doctor_name>/", views.dr_profile , name="dr_profile"),
    
    
   
  
]
