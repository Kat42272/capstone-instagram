from django.shortcuts import render, HttpResponseRedirect, reverse
from django.contrib.auth.decorators import login_required
from .models import PostModel
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
    return render(request, 'generic.html', {'form': form})


def like_view(request, likes_id):
    print(likes_id)
    post = PostModel.objects.get(id=likes_id)
    post.likes = post.likes + 1
    post.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def dislike_view(request, dislikes_id):
    print(dislikes_id)
    post = PostModel.objects.get(id=dislikes_id)
    post.dislikes = post.dislikes - 1
    post.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


