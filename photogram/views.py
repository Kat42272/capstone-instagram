from django.shortcuts import render, HttpResponseRedirect, reverse
from django.views.generic import TemplateView

from . import forms
from . import models
from comments.models import CommentModel
from instapost.forms import AddNewCommentForm
from instapost.models import PostModel
from notification.models import NotificationModel
from notification import views

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
import re


@login_required(login_url="loginpage")
def index_view(request):
    comment_form = AddNewCommentForm()
    all_users = models.InstaProfileModel.objects.all()
    # posts = PostModel.objects.all().order_by('-date_created')
    user_posts = PostModel.objects.filter(author=request.user).order_by('-date_created')
    following_posts = PostModel.objects.filter(author__in=request.user.follower.all()).order_by('-date_created')
    posts = user_posts | following_posts
    notif_count = views.total_count(request) 
    following_list = request.user.follower.all()
   
    return render(request, 'index.html', {'posts': posts, 'notif_count': notif_count, 'comment_form': comment_form, 'all_users': all_users, 'following_list': following_list})

@login_required
def post_comment_view(request, post_id):
    
    post = PostModel.objects.get(id=post_id)
    if request.method == "POST":
        form = AddNewCommentForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            print(data)
            new_comment_post = CommentModel.objects.create(
                body = data['body'],
                author_comment = request.user,
                post_comment = post
            )
            match_users = re.findall(r'@(\w+)', data.get('body'))
            if match_users:
                for match in match_users:
                    new_match = models.InstaProfileModel.objects.get(username=match)
                    if new_match:
                        NotificationModel.objects.create(
                            user_receive=new_match,
                            post_receive=new_comment_post
                        )
            return HttpResponseRedirect(f'/#{post_id}')
            

    


@login_required
def edit_profile_view(request, user_name):
    user = models.InstaProfileModel.objects.get(username=user_name)
    if request.method == "POST":
        form = forms.AddProfileForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.cleaned_data
            print(data)
            user.bio= data["bio"]
            user.url= data["url"]
            user.email= data["email"]
            user.phone = data["phone"]
            user.picture= data["picture"]
            user.save()
        return HttpResponseRedirect(reverse("profilepage", args=[user.username]))

    data = {
            "bio": user.bio,
            "url": user.url,
            "email": user.email,
            "phone": user.phone,
            "picture": user.picture
    }

    form = forms.AddProfileForm(initial=data)
    return render(request, 'edit_profile.html', {'form': form})


class ProfileView(LoginRequiredMixin, TemplateView):
    def get(self, request, user_name):
        user_profile = models.InstaProfileModel.objects.get(username=user_name)
        posts = PostModel.objects.filter(author__username=user_name).order_by('-date_created')
        total_posts = posts.count()
    
        if request.user.is_authenticated:
            following_list = request.user.follower.all()
        else:
            following_list = []
        return render(request, 'profile.html', {
            'posts': posts, 'total_posts': total_posts,
            'user_profile': user_profile,
            'following_list': following_list,
            })



class FollowingView(LoginRequiredMixin, TemplateView):

    def get(self, request, user_name):
        user_follow = models.InstaProfileModel.objects.get(username=user_name)
        request.user.follower.add(user_follow)
        return HttpResponseRedirect(reverse('profilepage', args=[user_follow.username]))


class UnfollowingView(LoginRequiredMixin, TemplateView):

    def get(self, request, user_name):
        user_unfollow = models.InstaProfileModel.objects.get(username=user_name)
        request.user.follower.remove(user_unfollow)
        return HttpResponseRedirect(reverse('profilepage', args=[user_unfollow.username]))
