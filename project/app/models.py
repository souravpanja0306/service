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

    def amount_due(self): #for due amount 
        payable = self.totalAmount
        paid = self.total_paid_amount()
        return payable - paid

    def total_paid_amount(self): #for total paid amount
        tt = self.advanceAmount
        ap = self.amount_paid()
        return tt + ap

    def amount_paid(self): #for paymennt
        items = paymentOnEmi.objects.filter(refNo=self.custimerId)
        total = 0
        for item in items:
            total += item.paidAmount
        return total

    def service_Calculation(self):
        if self.service == 4:
            td = timedelta(days = 73)
            first_ser = self.purchaseDate
            return first_ser + td

        elif self.service == 3:
            tdd = timedelta(days = 91)
            first_service = self.purchaseDate
            return first_service  + tdd
            
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
    customerRefId = models.CharField(max_length=10)
    attendTech = models.ForeignKey(techName, on_delete=models.CASCADE)
    parts = models.ForeignKey(partsName, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.attendTech)