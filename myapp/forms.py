from django import forms
from .models import *
class user_form(forms.ModelForm):
     first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'first_name'}),required=True,max_length=100)
     last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}),required=True,max_length=100)
     email =  forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}),required=True,max_length=100)
     password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}),required=True,max_length=100)
     address = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}),max_length=100)
     phone_no = forms.CharField(widget=forms.NumberInput(attrs={'class':'form-control'}),required=True,max_length=100)
     class Meta():
          model = users2
          fields = ["first_name","last_name","email","password","address","phone_no"]

