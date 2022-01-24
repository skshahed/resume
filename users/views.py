from django.db.models.fields import IntegerField
from django.db.models.query import QuerySet
from django.shortcuts import get_object_or_404, render
from django.db.models import Prefetch
from django.http import request
from django.contrib import messages, auth
from django.contrib.auth.models import User
from .models import Profile, Skill, Image, HirePlatform, Education, Experience, Category, Portfolio, Training


def users(request):
    #users = Image.objects.select_related('user__profile').all()
    #users = Profile.objects.raw('SELECT USERS_PROFILE.ID,USERS_PROFILE.USER_ID,FULL_NAME,PROFESSION,CITY,COUNTRY,USERS_IMAGE.USER_ID,IMAGE_PATH FROM USERS_PROFILE LEFT JOIN USERS_IMAGE ON USERS_PROFILE.USER_ID=USERS_IMAGE.USER_ID AND USERS_IMAGE.IS_ACTIVE=TRUE ORDER BY USERS_PROFILE.FULL_NAME')
    users = Profile.objects.raw('SELECT USERS_PROFILE.ID,USERS_PROFILE.USER_ID,FULL_NAME,PROFESSION,CITY,COUNTRY,MIN(IMAGE_PATH) FROM USERS_PROFILE LEFT JOIN USERS_IMAGE ON USERS_PROFILE.USER_ID=USERS_IMAGE.USER_ID AND USERS_IMAGE.IS_ACTIVE=TRUE GROUP BY USERS_PROFILE.ID,USERS_IMAGE.USER_ID ORDER BY USERS_PROFILE.FULL_NAME')
    #users = Profile.objects.raw('SELECT ID,USER_ID,FULL_NAME,PROFESSION,CITY,COUNTRY FROM USERS_PROFILE WHERE EXISTS (SELECT * FROM USERS_IMAGE WHERE USERS_PROFILE.USER_ID=USERS_IMAGE.USER_ID AND USERS_IMAGE.IS_ACTIVE=TRUE) GROUP BY USERS_PROFILE.USER_ID,USERS_PROFILE.ID ORDER BY USERS_PROFILE.FULL_NAME')
    #images = Image.objects.all()

    #users = Profile.objects.prefetch_related(Prefetch('user', queryset=Image.objects.select_related(None)))

    # users = Profile.objects.prefetch_related(user_profile,user_image)

    context = {
        'users': users,
        # 'images': images,
    }
    return render(request, 'users/users.html', context)


def user(request, user_id):
    user = get_object_or_404(Profile, pk=user_id)

    #user_auth_id = request.user.id
    #user_auth_id = 3
    find_user = Profile.objects.only('user_id').get(id=user_id).user_id
    profiles = Profile.objects.filter(is_published=True, user=find_user)
    images = Image.objects.filter(is_active=True, user=find_user)
    hireplatforms = HirePlatform.objects.filter(is_active=True, user=find_user)
    skills = Skill.objects.filter(is_active=True, user=find_user)
    educations = Education.objects.filter(is_active=True, user=find_user)
    experiences = Experience.objects.filter(is_active=True, user=find_user)
    categories = Category.objects.filter(user=find_user)
    portfolios = Portfolio.objects.filter(is_active=True, user=find_user)
    trainings = Training.objects.filter(is_active=True, user=find_user)

    context = {
        # 'auth_users': auth_users,
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

    return render(request, 'users/user.html', context)


def search(request):
    #queryset_list = Profile.objects.raw('SELECT USERS_PROFILE.ID,USERS_PROFILE.USER_ID,FULL_NAME,PROFESSION,CITY,COUNTRY,MIN(IMAGE_PATH) FROM USERS_PROFILE LEFT JOIN USERS_IMAGE ON USERS_PROFILE.USER_ID=USERS_IMAGE.USER_ID AND USERS_IMAGE.IS_ACTIVE=TRUE GROUP BY USERS_PROFILE.ID,USERS_IMAGE.USER_ID ORDER BY USERS_PROFILE.FULL_NAME')
    #queryset_list = Profile.objects.order_by('full_name')

    # Search keywords
    if 'query' in request.GET:
        # if request.method == 'GET':
        keywords = request.GET['query']

        if (keywords.isdecimal()):
            queryset_list = Profile.objects.raw(
                'SELECT USERS_PROFILE.ID,USERS_PROFILE.USER_ID,FULL_NAME,PROFESSION,CITY,COUNTRY,MIN(IMAGE_PATH) FROM USERS_PROFILE LEFT JOIN USERS_IMAGE ON USERS_PROFILE.USER_ID=USERS_IMAGE.USER_ID AND USERS_IMAGE.IS_ACTIVE=TRUE WHERE USERS_PROFILE.ID=%s GROUP BY USERS_PROFILE.ID,USERS_IMAGE.USER_ID ORDER BY USERS_PROFILE.FULL_NAME', [keywords])

        elif isinstance(keywords, str):
            name_keywords = ('%'+keywords+'%')
            #queryset_list = queryset_list.filter(full_name__icontains=keywords) or Profile.objects.filter(id=keywords)
            queryset_list = Profile.objects.raw(
                'SELECT USERS_PROFILE.ID,USERS_PROFILE.USER_ID,FULL_NAME,PROFESSION,CITY,COUNTRY,MIN(IMAGE_PATH) FROM USERS_PROFILE LEFT JOIN USERS_IMAGE ON USERS_PROFILE.USER_ID=USERS_IMAGE.USER_ID AND USERS_IMAGE.IS_ACTIVE=TRUE WHERE (USERS_PROFILE.FULL_NAME iLIKE %s) GROUP BY USERS_PROFILE.ID,USERS_IMAGE.USER_ID ORDER BY USERS_PROFILE.FULL_NAME', [name_keywords])

    context = {
        'users': queryset_list,
        # 'images': images
    }
    return render(request, 'users/search.html', context)
