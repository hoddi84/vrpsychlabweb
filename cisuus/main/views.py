from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from main.forms import SignUpForm, LogInForm

# Create your views here.

def home_view(request):
    return render(request, 'home.html')

def thanks_view(request):
    return render(request, 'thanks.html')

@login_required
def convert_view(request):
    return render(request, 'convert.html')

@login_required
def live_view(request):
    return render(request, 'live.html')


################## LOGIN RELATED ########################

@login_required
def success_view(request):
    return render(request, 'success.html')

@login_required
def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')

def login_view(request):
    if request.method == 'POST':
        form = LogInForm(request.POST)

        if form.is_valid():
            user = form.login(request)

            if user:
                login(request, user)

                return HttpResponseRedirect('/success/')
    else:
        form = LogInForm()

    return render(request, 'login.html', {'form':form})

def signup_view(request):

    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password1']

            User.objects.create_user(username, email, password)

            return HttpResponseRedirect('/thanks/')
    else:
        form = SignUpForm()

    return render(request, 'signup.html', {'form':form})
