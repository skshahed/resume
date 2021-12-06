from django.http import request
from django.contrib.auth.models import Group
from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from users.models import Profile
from users.models import Skill, Image, HirePlatform, Education, Experience, Category, Portfolio, Training

def register(request):
    if request.method == 'POST':
        #Get form values
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        password2 = request.POST['password2']

        #Check if password match
        if password == password2:
            #check username exists
            if User.objects.filter(username=username).exists():
                messages.error(request, 'That username is taken')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'That email is being used')
                    return redirect('register')
                else:
                    user = User.objects.create_user(first_name=first_name, last_name=last_name, username=username, password=password, email=email, is_staff=True)
                    profile = Profile.objects.create(user=User.objects.latest('id'), full_name = first_name +' '+ last_name, email=email)
                    #Login after register
                    # auth.login(request, user)
                    # messages.success(request, 'You are now logged In')
                    # return redirect('index')
                    group = Group.objects.get(name='General')
                    user.groups.add(group)
                    #user.is_staff=True
                    user.save()
                    profile.save()
                    messages.success(request, 'You are now registered and can Log In')
                    return redirect('login')
        else:
            messages.error(request, 'Passwords do not match')
            return redirect('register')
    else:
        return render(request, 'accounts/register.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You are now logged in')
            return redirect('/admin')
        else:
            messages.error(request, 'Invalid username or password')
            return redirect('login')
    else:
        return render(request, 'accounts/login.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request, 'You are now logged out')
        return redirect('login')

def myprofile(request):
    user_auth_id = request.user.id
    #user_auth_id = 3
    auth_users = User.objects.filter(id=request.user.id)
    profiles = Profile.objects.filter(is_published=True, user=user_auth_id)
    images = Image.objects.filter(is_active=True, user=user_auth_id)
    hireplatforms = HirePlatform.objects.filter(is_active=True, user=user_auth_id)
    skills = Skill.objects.filter(is_active=True, user=user_auth_id)
    educations = Education.objects.filter(is_active=True, user=user_auth_id)
    experiences = Experience.objects.filter(is_active=True, user=user_auth_id)
    categories = Category.objects.filter(user=user_auth_id)
    portfolios = Portfolio.objects.filter(is_active=True, user=user_auth_id)
    trainings = Training.objects.filter(is_active=True, user=user_auth_id)


    context = {
        'auth_users': auth_users,
        'users': profiles,
        'images': images,
        'hireplatforms': hireplatforms,
        'skills': skills,
        'educations': educations,
        'experiences': experiences,
        'categories': categories,
        'portfolios': portfolios,
        'trainings': trainings
    }

    return render(request, 'accounts/myprofile.html', context)

def dashboard(request):
    # user_auth_id = request.user.id
    # #user_auth_id = 3
    # auth_users = User.objects.filter(id=request.user.id)
    # profiles = Profile.objects.filter(is_published=True, user=user_auth_id)
    


    # context = {
    #     'auth_users': auth_users,
    #     'users': profiles,
    # }

    return redirect('/admin')
