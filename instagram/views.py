from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *
from django.template import RequestContext


# Create your views here.
@login_required(login_url='/accounts/login/')
def index(request):
    c = RequestContext(request, {
        'likes': 'likes',
    })

    posts = Post.objects.all().order_by('-post_date')
    return render(request, 'index.html', locals())


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


@login_required(login_url='/accounts/login/')
def profile(request):
    posts = Post.objects.all().order_by('-post_date')
    return render(request, 'profile.html', locals())


@login_required(login_url='/accounts/login/')
def mine(request):
    images = request.user.profile.posts.all()
    user_object = request.user
    user_images = user_object.profile.posts.all()
    user_saved = [save.photo for save in user_object.profile.saves.all()]
    user_liked = [like.photo for like in user_object.profile.mylikes.all()]
    print(user_liked)
    return render(request, 'myprofile.html', locals())


@login_required(login_url='/accounts/login/')
def edit(request):
    if request.method == 'POST':
        print(request.FILES)
        new_profile = ProfileForm(
            request.POST,
            request.FILES,
            instance=request.user.profile
        )
        if new_profile.is_valid():
            new_profile.save()
            print(new_profile.fields)
            # print(new_profile.fields.profile_picture)
            return redirect('profile')
    else:
        new_profile = ProfileForm(instance=request.user.profile)
    return render(request, 'edit.html', locals())


@login_required(login_url='/accounts/login/')
def user(request, user_id):
    user_object = get_object_or_404(User, pk=user_id)
    if request.user == user_object:
        return redirect('myaccount')
    isfollowing = user_object.profile not in request.user.profile.follows
    user_images = user_object.profile.posts.all()
    user_liked = [like.photo for like in user_object.profile.mylikes.all()]
    return render(request, 'profile.html', locals())


@login_required(login_url='/accounts/login/')
def like(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    request.user.profile.like(post)
    return JsonResponse(post.count_likes, safe=False)


@login_required(login_url='/accounts/login/')
def save(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    request.user.profile.save_image(post)
    return JsonResponse({}, safe=False)


@login_required(login_url='/accounts/login/')
def unlike(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    request.user.profile.unlike(post)
    return JsonResponse(post.count_likes, safe=False)


@login_required(login_url='/accounts/login/')
def togglefollow(request, user_id):
    target = get_object_or_404(User, pk=user_id).profile
    request.user.profile.togglefollow(target)
    response = [target.followers.count(), target.following.count()]
    return JsonResponse(response, safe=False)

