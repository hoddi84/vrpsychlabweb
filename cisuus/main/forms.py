from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.core import validators

class SignUpForm(forms.Form):
    username = forms.CharField(label='Username:', max_length=20)
    email = forms.EmailField(label="Email:", max_length=50)
    password1 = forms.CharField(label="Password:", max_length=30, widget=forms.PasswordInput)
    password2 = forms.CharField(label="Password (again):", max_length=30, widget=forms.PasswordInput)
    invitation = forms.CharField(label="Invitation Token:", max_length=50)

    def clean(self):
        username = self.cleaned_data.get('username')
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        invitation = self.cleaned_data.get('invitation')

        INVITATION_PHRASE = "WHO KILLED ROGER RABBIT?"

        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("This username exists")
        if not password2:
            raise forms.ValidationError("You must confirm your password")
        if password1 != password2:
            raise forms.ValidationError("Your passwords do not match")
        if invitation != INVITATION_PHRASE:
            raise forms.ValidationError("Did you really get an invitation?")
        return self.cleaned_data

class LogInForm(forms.Form):
    username = forms.CharField(max_length=20)
    password = forms.CharField(max_length=30)

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        if not user:
            raise forms.ValidationError("Sorry, that login was invalid. Please try again.")
        return self.cleaned_data

    def login(self, request):
            username = self.cleaned_data.get('username')
            password = self.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            return user
