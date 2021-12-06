from django.shortcuts import render

from .models import Profile, Image


def index(request):
    users = Profile.objects.all()
    images = Image.objects.all()


    context = {
        'users': users,
        'images': images
    }
    return render(request, 'users/users.html', context)


def user(request):
    return render(request, 'users/user.html')


def search(request):
    return render(request, 'users/search.html')
