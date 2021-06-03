from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('login', views.loginPage, name="loginPage"),
    path('logout', views.logoutuser, name="logout"),
    path('registration', views.registration, name="registration"),
    path('customer', views.customer, name="customer"),
    path('payment/<int:id>', views.payment, name="paymentPage"),
    path('details', views.details, name="details"),
    path('service', views.service, name="service"),
]
