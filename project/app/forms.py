from django import forms
from django.db import models
from django.db.models import fields
from .models import customerDetails, paymentOnEmi, techName, partsName, serviceModel

class customerDetailsForm(forms.ModelForm):
    class Meta:
        model = customerDetails
        fields = "__all__"

class paymentOnEmiForm(forms.ModelForm):
    class Meta:
        model = paymentOnEmi
        fields = "__all__"

class techNameForm(forms.ModelForm):
    class Meta:
        model = techName
        fields = "__all__"

class partsNameForm(forms.ModelForm):
    class Meta:
        model = partsName
        fields = "__all__"

class serviceModelForm(forms.ModelForm):
    class Meta:
        model = serviceModel
        fields = "__all__"