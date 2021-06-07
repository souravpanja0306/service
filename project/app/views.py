from typing import Deque
from django.db.models.aggregates import Aggregate, Sum
from django.shortcuts import redirect, render
from .models import customerDetails, paymentOnEmi, serviceModel, techName, partsName
from .forms import customerDetailsForm, paymentOnEmiForm, techNameForm, serviceModelForm, partsNameForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Sum

# This is the Home page & DashBoard Page...................


@login_required(login_url="/login")
def home(request):
    tamt = customerDetails.objects.all().aggregate(
        sum=Sum('totalAmount'))['sum']
    tamt2 = customerDetails.objects.all().aggregate(
        sum2=Sum('advanceAmount'))['sum2']
    tamt3 = (tamt - tamt2)
    return render(request, "home.html", {"tamt": tamt, "tamt2": tamt2, "tamt3": tamt3})

# This The Login Page...........


def loginPage(request):
    if request.user.is_authenticated:
        return redirect("/customer")
    else:
        if request.method == "POST":
            username = request.POST.get("username")
            password = request.POST.get("password")
            userName = authenticate(
                request, username=username, password=password)
            if userName is not None:
                login(request, userName)
                messages.warning(request, "Successfully Loging")
                return redirect("/")
            else:
                messages.warning(request, "Username or Password is incurrect")
        return render(request, "login.html")


# For Registration of New Account................................
def registration(request):
    if request.user.is_authenticated:
        return redirect("/")
    else:
        regForm = UserCreationForm()
        if request.method == "POST":
            regForm = UserCreationForm(request.POST)
            if regForm.is_valid():
                regForm.save()
                user = regForm.cleaned_data.get("username")
                messages.success(
                    request, user + "  Account created successfully")
                return redirect("/login")
        context = {"regForm": regForm}
        return render(request, "registration.html", context)


# Create New Customer............................................
@login_required(login_url="/login")
def customer(request):
    fm = customerDetailsForm()
    if request.method == 'POST':
        fm = customerDetailsForm(request.POST)
        if fm.is_valid():
            fm.save()
            messages.info(request, "Successfully Submit")
            return redirect("/")

        else:
            messages.info(request, "Something Went Wrong")
    return render(request, "customer.html")


# Views Customer Detais, Payment Details and Etc..................
@login_required(login_url="/login")
def details(request):
    fmm = customerDetails.objects.all()
    return render(request, "details.html", {"fmm": fmm})

# For Payment Page................................................


@login_required(login_url="/login")
def payment(request, id):
    ps = paymentOnEmiForm()
    if request.method == "POST":
        ps = paymentOnEmiForm(request.POST)
        if ps.is_valid():
            ps.save()
            return redirect("/details")
    return render(request, "payment.html", {"id": id})


# Payment Data Page.................................................
@login_required(login_url="/login")
def pdata(request):
    pdd = paymentOnEmi.objects.all()
    return render(request, "pdata.html", {"pdd":pdd})


# For Logout.......................................................
@login_required(login_url="/login")
def logoutuser(request):
    logout(request)
    messages.warning(request, "Successfully Logout")
    return redirect("/login")



# For Service Requirement...........................
@login_required(login_url="/login")
def service(request):
    dtt = customerDetails.objects.all()
    return render(request, "service.html",{"dtt":dtt})


# For Technician Requirement...........................
@login_required(login_url="/login")
def technicianPage(request, id):
    tc = serviceModelForm()
    if request.method == "POST":
        tc = serviceModelForm(request.POST)
        if tc.is_valid():
            tc.save()
            return redirect("/service")
    return render(request, "technician.html", {"id":id, "tc":tc})