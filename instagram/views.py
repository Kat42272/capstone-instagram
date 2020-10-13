from django.shortcuts import render, HttpResponseRedirect, reverse
from django.contrib.auth.decorators import login_required
from . import forms 
from . import models
from instapost.models import PostModel

# Create your views here.
def index_view(request):
    posts =  PostModel.objects.all().order_by('-date_created')
    return render(request, 'index.html', {'posts': posts})


@login_required
def edit_profile_view(request, user_name):
    user= models.InstaProfileModel.objects.get(username=user_name)
    if request.method == "POST":
        form = forms.AddProfileForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.cleaned_data
            print(data)
            # print(request.FILES)
            user.bio= data["bio"]
            user.email= data["email"]
            user.phone = data["phone"]
            user.picture= data["picture"]
            user.save()
        return HttpResponseRedirect(reverse("profilepage", args=[user.username]))

    data = {
            "bio": user.bio,
            "email": user.email,
            "phone": user.phone,
            "picture": user.picture
    }

    form = forms.AddProfileForm()
    return render(request, 'edit_profile.html', {'form': form})


def profile_view(request, user_name):
    user_profile = models.InstaProfileModel.objects.get(username=user_name)
    posts = PostModel.objects.filter(author__username=user_name).order_by('-date_created')
    total_posts = posts.count()
    return render(request, 'profile.html', {'posts': posts, 'total_posts': total_posts, 'user_profile': user_profile})