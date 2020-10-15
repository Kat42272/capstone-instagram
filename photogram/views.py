from django.shortcuts import render, HttpResponseRedirect, reverse
from django.views.generic import TemplateView

from . import forms
from . import models
from instapost.models import PostModel

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.
def index_view(request):
    posts = PostModel.objects.all().order_by('-date_created')
    return render(request, 'index.html', {'posts': posts})


@login_required
def edit_profile_view(request, user_name):
    user = models.InstaProfileModel.objects.get(username=user_name)
    if request.method == "POST":
        form = forms.AddProfileForm(request.POST, request.FILES)
        breakpoint()
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

    form = forms.AddProfileForm(initial=data)
    return render(request, 'edit_profile.html', {'form': form})


def profile_view(request, user_name):
    user_profile = models.InstaProfileModel.objects.get(username=user_name)
    posts = PostModel.objects.filter(author__username=user_name).order_by('-date_created')
    total_posts = posts.count()
    following_count = user_profile.following.all().count()
    # follower_count = user_profile.follower.all().count()
    return render(request, 'profile.html', {
        'posts': posts, 'total_posts': total_posts,
        'user_profile': user_profile,
        'following_count': following_count,
        # 'follower_count': follower_count
        })


class FollowingView(LoginRequiredMixin, TemplateView):

    def get(self, request, user_name):
        user = models.InstaProfileModel.objects.get(username=user_name)
        request.user.following.add(user)
        return HttpResponseRedirect(reverse('profilepage', args=[user.username]))


class UnfollowingView(LoginRequiredMixin, TemplateView):

    def get(self, request, user_name):
        user = models.InstaProfileModel.objects.get(username=user_name)
        request.user.following.remove(user)
        return HttpResponseRedirect(reverse('profilepage', args=[user.username]))


# class FollowerView(LoginRequiredMixin, TemplateView):

#     def get(self, request, user_name):
#         user = models.InstaProfileModel.objects.get(username=user_name)
#         request.user.follower.add(user)
#         return HttpResponseRedirect(reverse('profilepage', args=[user.username]))
