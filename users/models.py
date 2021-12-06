from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.DO_NOTHING)
    full_name = models.CharField(max_length=100)
    father_name = models.CharField(max_length=100)
    mother_name = models.CharField(max_length=100)
    profession = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    main_title = models.CharField(max_length=150)
    dob = models.DateField(null=True, auto_now=False)
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    nationality = models.CharField(max_length=50)
    website = models.CharField(max_length=100)
    gender = models.IntegerField(default=1)
    religion = models.CharField(max_length=20)
    marital_state = models.IntegerField(default=1)
    is_published = models.BooleanField(default=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.full_name


class Image(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    image_path = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return str(self.user)


class HirePlatform(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    platform_title = models.CharField(max_length=100)
    platform_description = models.TextField(blank=True)
    platform_profile_link = models.CharField(max_length=100)
    platform_hire_link = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.platform_title


class Skill(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    skill_name = models.CharField(max_length=100)
    skill_level = models.IntegerField()
    skill_details = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.skill_name


class Experience(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    company_name = models.CharField(max_length=100)
    designation = models.CharField(max_length=50)
    location = models.CharField(max_length=100)
    start_date = models.DateField(auto_now=False)
    end_date = models.DateField(auto_now=False)
    responsibility = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.company_name


class Education(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    institute_name = models.CharField(max_length=100)
    degree = models.CharField(max_length=50)
    location = models.CharField(max_length=100)
    start_date = models.DateField(auto_now=False)
    end_date = models.DateField(auto_now=False)
    description = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.degree


class Category(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    category_name = models.CharField(max_length=50)

    def __str__(self):
        return self.category_name


class Portfolio(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    category_id = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    portfolio_title = models.CharField(max_length=100)
    portfolio_desc = models.TextField(blank=True)
    web_link = models.CharField(max_length=100)
    image_path = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.portfolio_title


class Training(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    training_name = models.CharField(max_length=100)
    institute = models.CharField(max_length=100)
    start_date = models.DateField(auto_now=False)
    end_date = models.DateField(auto_now=False)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.training_name
