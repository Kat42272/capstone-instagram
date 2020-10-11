from django.shortcuts import render, HttpResponseRedirect, reverse
from django.contrib.auth.decorators import login_required
from . import forms 
from . import models
from instapost.models import PostModel

# Create your views here.
def index_view(request):
    posts =  PostModel.objects.all()
    return render(request, 'index.html', {'posts': posts})


@login_required
def edit_profile_view(request):
    if request.method == "POST":
        login_user= models.InstaProfileModel.objects.get(username=request.user)
        form = forms.AddProfileForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.cleaned_data
            print(data)
            print(request.FILES)
            login_user.bio= data["bio"]
            login_user.email= data["email"]
            login_user.phone = data["phone"]
            login_user.picture= data["picture"]
            login_user.save()
            return HttpResponseRedirect(reverse("profilepage"))
    form = forms.AddProfileForm()
    return render(request, 'edit_profile.html', {'form': form})


def profile_view(request):
    return render(request, 'profile.html')