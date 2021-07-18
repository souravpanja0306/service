from django.contrib import admin
from .models import customerDetails, paymentOnEmi, techName, serviceModel, partsName
from .forms import techNameForm


admin.site.register(customerDetails)
admin.site.register(paymentOnEmi)
admin.site.register(techName)
admin.site.register(serviceModel)
admin.site.register(partsName)
