from django import forms
from django.contrib.auth import authenticate


class loginForm(forms.ModelForm):

    username = forms.CharField(max_length=100)
    password = forms.PasswordInput()