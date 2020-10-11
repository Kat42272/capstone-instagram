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


