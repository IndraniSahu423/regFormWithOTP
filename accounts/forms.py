# accounts/forms.py
from django import forms
from .models import User

class EmailForm(forms.Form):
    email = forms.EmailField()

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email' ,'username', 'phone', 'password']
        