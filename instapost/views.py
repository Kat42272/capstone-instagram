from django.shortcuts import render, HttpResponseRedirect, reverse, redirect
from django.contrib.auth.decorators import login_required
from .models import PostModel
from comments.models import CommentModel
from comments.forms import AddCommentForm
from . import forms 

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
    CommentModel.objects.filter(id=comment_id).delete()
    return redirect('/')


def delete_view(request, post_id):
    PostModel.objects.filter(id=post_id).delete()
    return redirect('/')


