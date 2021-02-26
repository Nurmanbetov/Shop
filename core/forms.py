from django import forms
from django.forms import fields, models
from django.contrib.auth.models import User



class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'last_name']
       
        