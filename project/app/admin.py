from django.contrib import admin
from .models import customerDetails, paymentOnEmi

# Register your models here.
admin.site.register(customerDetails)
admin.site.register(paymentOnEmi)