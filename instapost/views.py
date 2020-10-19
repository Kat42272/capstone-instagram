from django.shortcuts import render, HttpResponseRedirect, reverse, redirect
from django.contrib.auth.decorators import login_required
from .models import PostModel
from photogram.models import InstaProfileModel
from comments.models import CommentModel
from comments.forms import AddCommentForm, AddNewCommentForm
from notification.models import NotificationModel
from . import forms 
from django.http import Http404
from django.http import HttpResponseForbidden
from django.core.exceptions import PermissionDenied
import re

@login_required
def add_post_view(request):
    if request.method == "POST":
        form = forms.AddPostForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.cleaned_data
            print(data)
            new_post = PostModel.objects.create(
                caption = data['caption'],
                picture = data['picture'],
                author = request.user
            )
            if new_post:
                return HttpResponseRedirect(reverse("homepage"))
    form = forms.AddPostForm()
    return render(request, 'add_post.html', {'form': form})


def like_view(request, post_id):
    print(post_id)
    post = PostModel.objects.get(id=post_id)
    
    if post.like.filter(id=request.user.id).exists():
        post.like.remove(request.user)
        post.liked=False
        post.save()
    else:
        post.like.add(request.user)
        post.liked=True
        post.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
   

@login_required
def add_comment_view(request, post_id):
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
                    new_match = InstaProfileModel.objects.get(username=match)
                    if new_match:
                        NotificationModel.objects.create(
                            user_receive=new_match,
                            post_receive=new_comment_post
                        )
            return HttpResponseRedirect(reverse("homepage"))
            

    form = AddNewCommentForm()
    return render(request, 'generic.html', {'form': form, 'post': post})



@login_required
def post_detail_view(request, post_id):
    post = PostModel.objects.get(id=post_id)
    new_comment = None
    all_comments = post.comments.all()
    if request.method == "POST":
        form = AddCommentForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            print(data)
            new_comment = CommentModel.objects.create(
                body = data['body'],
                author_comment = request.user,
                post_comment = post
            )
            

    form = AddCommentForm()
    return render(request, 'post_detail.html', {'form': form, 'post': post, 'all_comments': all_comments, 'new_comment': new_comment })


def delete_comment_view(request, comment_id):
    try:
        CommentModel.objects.get(id=comment_id).delete()
    except CommentModel.DoesNotExist:
        raise(Http404)
    return redirect('/')


def delete_view(request, post_id):
    try:
        user = PostModel.objects.get(id=post_id)
    except PostModel.DoesNotExist:
        raise(Http404)
    if user.author.username == request.user.username:
        PostModel.objects.get(id=post_id).delete()
        return redirect('/')
    else:
        raise PermissionDenied


# def handler404(request):
#     return render(request, '404.html', status=404)


def handler500(request):
    return render(request, '500.html', status=500)
