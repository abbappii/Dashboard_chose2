from django import forms
from django.forms import ModelForm

from .models import UserProfile

class UserProfileForm(ModelForm):
    balance = forms.DecimalField(min_value=500)
    
    class Meta:
        model = UserProfile
        exclude = ['user',]