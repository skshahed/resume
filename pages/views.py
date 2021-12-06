from django.http import request
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.mail import message, send_mail
from users.models import Profile
from users.models import Skill, Image, HirePlatform, Education, Experience, Category, Portfolio, Training

admin_id = Category.objects.get(category_name='Admin')
user_auth_id = admin_id.user_id


def index(request):
   # user_auth_id = 1
    if request.method == 'POST':
        name = request.POST['Name']
        email = request.POST['Email']
        mobile_no = request.POST['Mobile-number']
        message_body = request.POST['Message']

        if email and message_body and mobile_no:
            send_mail(
                'Web Contact Inquery From ' + name,
                message_body +  '\n Email: '+ email + '\n Phone No: '+ mobile_no + '\n N.B:It is auto genarated message.',
                'shahed007cse@gmail.com',
                ['shahed007cse@gmail.com', email],
                fail_silently=False,
            )
            messages.success(request, 'Your mail has been sent')

    auth_users = User.objects.filter(id=request.user.id)
    profiles = Profile.objects.filter(is_published=True, id=user_auth_id)
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
    return render(request, 'pages/index.html', context)


def about(request):
    return render(request, 'pages/about.html')

