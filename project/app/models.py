from django.db import models
from django.db.models.base import Model
from django.db.models.deletion import CASCADE
from django.db.models.aggregates import Aggregate, Sum
from datetime import datetime, date, timedelta


class customerDetails(models.Model):
    custimerId = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100, null=True)
    phoneNo = models.CharField(max_length=100, unique=True)
    email = models.EmailField(null=True)

    service = models.IntegerField(null=True, blank=True)
    emi = models.CharField(max_length=10, null=True, blank=True)

    modelNameOne = models.CharField(max_length=100)
    quantityOne = models.CharField(max_length=2, null=True)
    modelNoOne = models.CharField(max_length=100)
    modelNameTwo = models.CharField(max_length=100, blank=True)
    quantityTwo = models.CharField(max_length=2, null=True, blank=True)
    modelNoTwo = models.CharField(max_length=100, blank=True)
    purchaseDate = models.DateField(auto_now=False, auto_now_add=False)
    totalAmount = models.IntegerField()
    advanceAmount = models.IntegerField()
    dueAmount = models.IntegerField(null=True)

    def __str__(self):
        return self.name

    def amount_due(self):  # for due amount
        payable = self.totalAmount
        paid = self.total_paid_amount()
        return payable - paid

    def total_paid_amount(self):  # for total paid amount
        tt = self.advanceAmount
        ap = self.amount_paid()
        return tt + ap

    def amount_paid(self):  # for paymennt
        items = paymentOnEmi.objects.filter(refNo=self.custimerId)
        total = 0
        for item in items:
            total += item.paidAmount
        return total

    def service_1(self):
        td = timedelta(days=73)
        pDate = self.purchaseDate
        return pDate + td

    def service_2(self):
        td = timedelta(days=73)
        return self.service_1() + td

    def service_3(self):
        td = timedelta(days=73)
        return self.service_2() + td

    def service_4(self):
        td = timedelta(days=73)
        return self.service_3() + td

    def one_year_from_purchase_date(self):
        years = timedelta(days=364)
        return self.purchaseDate + years

    def count(self):
        exp = self.one_year_from_purchase_date()
        tday = date.today()
        cou = exp - tday
        return cou.days


# Payment Receipt........................................................
class paymentOnEmi(models.Model):
    refNo = models.IntegerField()
    paidAmount = models.IntegerField()
    paymentDate = models.DateField(auto_now=False, auto_now_add=False)
    cashCheque = models.CharField(max_length=100, null=True)
    chequeNo = models.CharField(max_length=10, null=True, blank=True)

    def __str__(self):
        return str(self.refNo)

# Technician Registrations...............................................


class techName(models.Model):
    technicianName = models.CharField(max_length=100)
    disignation = models.CharField(max_length=50)
    contactNo = models.CharField(max_length=15)

    def __str__(self):
        return self.technicianName

# For Parts Registrations................................................


class partsName(models.Model):
    reqPartName = models.CharField(max_length=100)
    price = models.IntegerField()

    def __str__(self):
        return self.reqPartName


class serviceModel(models.Model):
    status_choice = [
        ("Pending", "Pending"),
        ("Processing", "Processing"),
        ("Done","Done")
    ]
    customerRefId = models.CharField(max_length=10)
    attendTech = models.ForeignKey(techName, on_delete=models.CASCADE)
    parts = models.ForeignKey(partsName, on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=status_choice, null=True)

    def __str__(self):
        return str(self.attendTech)
