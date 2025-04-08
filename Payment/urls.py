from django.urls import path
from Payment import views
from . import *


urlpatterns = [
  
    path("", views.payment , name="payment"),
    # path("payment", views.payment , name="payment"),
    # path("ordersuc", views.ordersuc , name="ordersuc"),
    # path("cancle", views.cancle , name="cancle"),
    # path("Reasion-cancle", views.Reasioncancle , name="Reasioncancle"),
    # path("dashboard", views.dashboard , name="dashboard"),
    # path("registration", views.registration , name="registration"),
    
    
   
  
]