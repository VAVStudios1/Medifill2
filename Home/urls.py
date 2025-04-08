from django.contrib import admin
from django.urls import path
from Home import views
from django.contrib.auth import views as auth_views
from . import *


urlpatterns = [
    path("", views.index , name="Home"),
    path("login/", views.login , name="login"),
    path("signup/", views.signup , name="signup"),
    path("logout/", views.logout_view , name="logout"),
    path("feedback/", views.feedback , name="feedback"),
    path("privacy/", views.privacy , name="privacy"),
    path("security/", views.security , name="security"),
    # path("contact/", views.contact , name="contact"),
    path("contact/", views.contact , name="contact"),
    path("return/", views.returnq , name="return"),
    path("aboutm/", views.aboutm , name="aboutm"),
    # path("chatbot/", views.chatbot , name="chatbot"),
    path('reset_password/' , auth_views.PasswordResetView.as_view(template_name = "Home/templates/reset_password.html") , name="reset_password"),
    path('reset_password_sent/' , auth_views.PasswordResetDoneView.as_view(template_name = "Home/templates/reset_password_sent.html"), name="password_reset_done"),
    path('reset/<uidb64>/<token>/' , auth_views.PasswordResetConfirmView.as_view(template_name = "Home/templates/password_reset_confirm.html"), name="password_reset_confirm"),
    path('reset_password_complete/' , auth_views.PasswordResetCompleteView.as_view(template_name = "Home/templates/password_reset_complete.html"), name="password_reset_complete"),
    
    path("Profile/", views.Profile , name="Profile"),
    path("Profile/myappointment", views.myappointment , name="myappointment"),
    # path("Profile/change", views.change , name="change"),
    path('Profile/change/' , auth_views.PasswordChangeView.as_view(template_name = "Home/templates/change_password.html") , name="change_password"),
    # path('Profile/change/' , auth_views.as_view(template_name = "Home/templates/change_password.html") , name="change_password"),
    path('Profile/change/done/', auth_views.PasswordChangeDoneView.as_view(template_name = "Home/templates/change_password_done.html"), name='password_change_done'),

   
  
]

    # path('reset_password/' , auth_views.PasswordResetView.as_view(template_name = "Home/templates/login.html") , name="reset_password"),