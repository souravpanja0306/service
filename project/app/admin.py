from django.contrib import admin
from .models import customerDetails, paymentOnEmi, techName

# Register your models here.
admin.site.register(customerDetails)
admin.site.register(paymentOnEmi)
admin.site.register(techName)