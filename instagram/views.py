from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, Http404
from django.contrib.auth.decorators import login_required
from .models import Post, Profile
from .forms import NewPostForm


# Create your views here.
@login_required(login_url='/accounts/login/')
def index(request):
    posts = Post.objects.all()
    return render(request, 'index.html', locals())


@login_required(login_url='/accounts/login/')
def profile(request):
    return render(request, 'profile.html')


@login_required(login_url='/accounts/login/')
def new_post(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewPostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = current_user
            post.save()
        return redirect('index')
    else:
        form = NewPostForm()
    return render(request, 'new_post.html', {"form": form})
