from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('login', views.loginPage, name="loginPage"),
    path('logout', views.logoutuser, name="logout"),
    path('registration', views.registration, name="registration"),

    # Custormer Registrations........................................
    path('customer', views.customer, name="customer"),

    path('technician/<int:id>', views.technicianPage, name="technicianPage"),

    path('customer/details', views.details, name="details"),
    path('details/<int:id>', views.iddetails, name="iddetails"),

    path('payment/<int:id>', views.payment, name="paymentPage"),
    path('moneyreceipts/', views.moneyreceipts, name="moneyreceipts"),
    path('payment_data', views.payment_data, name="payment_data"),

    path('customer/service', views.service, name="service"),

    path('amc/', views.amc, name="amc"),
    path('emi/', views.emi, name="emi"),

    # Under Profile Section........................................
    path('profile/', views.profile, name="profile"),

    path('profile/technician_reg/', views.techreg, name="technician_reg"),
    path('technician_reg/<int:id>/', views.tech_del, name="tech_del"),

    path('profile/parts_reg/', views.partsreg, name='partsreg'),
    path('parts_reg/<int:id>/', views.parts_del, name='parts_del'),



]
