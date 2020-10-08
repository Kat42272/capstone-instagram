from django.shortcuts import render, HttpResponseRedirect, reverse
from django.contrib.auth import authenticate, login, logout
from . import forms
from instagram.models import InstaProfileModel
from django.contrib.auth.decorators import login_required




def login_view(request):
    if request.method == "POST":
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            
            user = authenticate(request, username=data.get('username'), password=data.get("password"))
            if user:
                login(request, user)
                return HttpResponseRedirect(request.GET.get('next', reverse("homepage")))

        
    form = forms.LoginForm()
    return render(request, 'login.html', {'form': form})


def signup_view(request):
    if request.method == "POST":
        form = forms.SignupForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            signup_user = InstaProfileModel.objects.create_user(
                username=data.get('username'),
                password=data.get('password'),
                displayname=data.get('displayname')
            )
            if signup_user:
                login(request, signup_user)
                return HttpResponseRedirect(reverse("loginpage"))
    form = forms.SignupForm()
    return render(request, 'signup.html', {'form': form})



def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("loginpage"))

