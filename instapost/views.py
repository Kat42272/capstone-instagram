from django.shortcuts import render, HttpResponseRedirect, reverse, redirect
from django.contrib.auth.decorators import login_required
from .models import PostModel
from . import forms 

@login_required
def add_post_view(request):
    if request.method == "POST":
        form = forms.EditPostForm(request.POST, request.FILES)
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
    form = forms.EditPostForm()
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
   





def delete_view(request, post_id):
    PostModel.objects.filter(id=post_id).delete()
    return redirect('/')


