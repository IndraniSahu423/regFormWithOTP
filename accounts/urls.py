# accounts/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.email_page, name='email_page'),
    path('verify/', views.verify_otp, name='verify_otp'),
    path('register/', views.register_details, name='register_details'),
    path('login/', views.login_view, name='login'),
]
