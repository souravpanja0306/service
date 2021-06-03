from django.db import models

class customerDetails(models.Model):
    custimerId = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    phoneNo = models.CharField(max_length=100)
    email = models.EmailField()

    modelNameOne = models.CharField(max_length=100)
    quantityOne = models.CharField(max_length=2, null=True)
    modelNoOne = models.CharField(max_length=100)
    modelNameTwo = models.CharField(max_length=100)
    quantityTwo = models.CharField(max_length=2, null=True)
    modelNoTwo = models.CharField(max_length=100)
    purchaseDate = models.DateField(auto_now=False, auto_now_add=False)
    totalAmount = models.DecimalField(max_digits=10, decimal_places=2)
    advanceAmount = models.DecimalField(max_digits=10, decimal_places=2)
    dueAmount = models.DecimalField(max_digits=10, decimal_places=2, null=True)


    def __str__(self):
        return self.name


class paymentOnEmi(models.Model):
    refNo = models.IntegerField()
    paidAmount = models.DecimalField(max_digits=10, decimal_places=2)
    paymentDate = models.DateField(auto_now=False, auto_now_add=False)
