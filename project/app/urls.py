from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('login', views.loginPage, name="loginPage"),
    path('logout', views.logoutuser, name="logout"),
    path('registration', views.registration, name="registration"),

    path('customer', views.customer, name="customer"),
    path('payment/<int:id>', views.payment, name="paymentPage"),

    path('pdata', views.pdata, name="pdata"),
    path('details', views.details, name="details"),
    path('service', views.service, name="service"),
    path('technician/<int:id>', views.technicianPage, name="technicianPage"),

]
