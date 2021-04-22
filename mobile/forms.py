from django import forms
from django.forms import ModelForm
from .models import Brands,Mobile,Orders
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class BrandCreateform(ModelForm):
    class Meta:
        model=Brands
        fields='__all__'

class BrandUpdateForm(ModelForm):
    class Meta:
        model=Brands
        fields='__all__'

class MobileCreateForm(ModelForm):
    class Meta:
        model=Mobile
        fields="__all__"

class UserRegForm(UserCreationForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','email','password1','password2']

class OrderForm(ModelForm):
    # product=forms.CharField(max_length=120)
    class Meta:
        model=Orders
        fields='__all__'