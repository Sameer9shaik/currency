from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import CurrencyOrder, Currency,kyc


# class CreateUserForm(UserCreationForm):
#     class Meta:
#         model = User
#         fields = ['username','fname','lname','email','pass1']


class CreateCurrencyOrderForm(forms.ModelForm):
    class Meta:
        model = CurrencyOrder
        fields = ['id','currency_from','currency_to','forex_amount','inr_amount']


class CreateKycForm(forms.ModelForm):
    class Meta:
        model = kyc
        fields = ['pancard','aadhar']
