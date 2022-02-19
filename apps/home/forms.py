from django import forms
from django.forms import ModelForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

from .models import UserProfile, Roles

class UserProfileForm(ModelForm):
    balance = forms.DecimalField(min_value=500)
    
    class Meta:
        model = UserProfile
        exclude = ['user',]


class RolesModel(ModelForm):
    class Meta:
        model = Roles
        fields = {'percentage',}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.add_input(Submit('save', 'save'))
        