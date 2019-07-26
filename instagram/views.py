from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, Http404
from django.contrib.auth.decorators import login_required
# from .models import User


# Create your views here.
@login_required(login_url='/accounts/login/')
def index(request):
    return render(request, 'index.html')

@login_required(login_url='/accounts/login/')
def profile(request):
    return render(request, 'profile.html')
