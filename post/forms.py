from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Sendemail


class ContactForm(forms.Form):
    body    = forms.CharField(required=True, widget=forms.Textarea)

class Emailsender(forms.Form):
    email   = forms.EmailField(max_length=30)
    subject = forms.CharField(max_length=20)
    body    = forms.CharField(required=True, widget=forms.Textarea)

class AuthenthecationForm(forms.Form):
    username = forms.CharField(max_length=30)
    password = forms.CharField(max_length=20)

class RegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=20, help_text = 'Required a valid name')
    last_name = forms.CharField(max_length=15, help_text = 'Required a valid name')

    class meta:
        model = Sendemail
        
        fields = ['username', 'first_name', 'last_name', 'email', 'password' 'password2']

        def save(self, commit=True):
            user = super(RegisterForm, self).save(commit=True)
            user = self.cleaned_data['username']
            user = self.cleaned_data['first_name']
            user = self.cleaned_data['last_name']
            user = self.cleaned_data['password']

            if commit:
                user.save()

            return user