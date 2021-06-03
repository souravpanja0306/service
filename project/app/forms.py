from django import forms
from django.db import models
from django.db.models import fields
from .models import customerDetails, paymentOnEmi

class customerDetailsForm(forms.ModelForm):
    class Meta:
        model = customerDetails
        fields = "__all__"

class paymentOnEmiForm(forms.ModelForm):
    class Meta:
        model = paymentOnEmi
        fields = "__all__"