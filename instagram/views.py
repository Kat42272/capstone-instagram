from django.shortcuts import render, HttpResponseRedirect, reverse
from django.contrib.auth.decorators import login_required
from . import forms
from . import models


# Create your views here.
def index_view(request):
    return render(request, 'index.html')


@login_required
def profile_view(request):
    if request.method == "POST":
        form = forms.AddProfileForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            new_user = models.InstaProfileModel.objects.create(
                displayname=data['displayname'],
                bio=data['bio'],
                url=data['url'],
                picture=data['picture'],
            )
            if new_user:
                login(request, new_user)
                return HttpResponseRedirect(reverse("profilepage"))
    form = forms.AddProfileForm()
    return render(request, 'generic.html', {'form': form})
