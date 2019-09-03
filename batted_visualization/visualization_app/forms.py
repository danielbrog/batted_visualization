from django import forms
from django.core import validators


class NameSearch(forms.Form):
    name= forms.CharField(label='Search By Name')
    
