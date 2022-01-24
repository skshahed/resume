from django.contrib import admin
from django.contrib.auth.models import User

from .models import Profile
from .models import HirePlatform
from .models import Image
from .models import Skill
from .models import Education
from .models import Experience
from .models import Category
from .models import Portfolio
from .models import Training


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'main_title', 'profession',
                    'phone', 'country', 'website', 'is_published')
    list_display_links = ('id', 'main_title', 'website')
    list_filter = ('profession',)
    list_editable = ('is_published',)
    search_fields = ('main_title', 'phone', 'address',
                     'country', 'description')
    list_per_page = 20
    
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(user=request.user)
    
    
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if request.user.is_superuser:
            kwargs["queryset"] = User.objects.all()
            
        elif db_field.name == "user":
            kwargs["queryset"] = User.objects.filter(username=request.user.username)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


class ImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'image_path', 'is_active')
    list_filter = ('user',)
    list_editable = ('is_active',)
    list_per_page = 20
    
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(user=request.user)
    
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if request.user.is_superuser:
            kwargs["queryset"] = User.objects.all()
            #kwargs["queryset"] = Profile.objects.all()
            
        elif db_field.name == "user":
            kwargs["queryset"] = User.objects.filter(username=request.user.username)
           # kwargs["queryset"] = Profile.objects.filter(user=request.user)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)
    
   

class HirePlatformAdmin(admin.ModelAdmin):
    list_display = ('id', 'platform_title', 'platform_profile_link',
                    'platform_hire_link', 'is_active')
    list_display_links = ('id', 'platform_profile_link', 'platform_hire_link')
    list_filter = ('platform_title',)
    list_editable = ('is_active',)
    search_fields = ('id', 'platform_title')
    list_per_page = 20
    
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(user=request.user)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if request.user.is_superuser:
            kwargs["queryset"] = User.objects.all()
            
        elif db_field.name == "user":
            kwargs["queryset"] = User.objects.filter(username=request.user.username)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

class SkillAdmin(admin.ModelAdmin):
    list_display = ('id', 'skill_name', 'skill_level',
                    'skill_details', 'is_active')
    list_display_links = ('id', 'skill_name')
    list_filter = ('skill_name', 'skill_level')
    list_editable = ('is_active',)
    list_per_page = 20
    
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(user=request.user)
    
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if request.user.is_superuser:
            kwargs["queryset"] = User.objects.all()
            
        elif db_field.name == "user":
            kwargs["queryset"] = User.objects.filter(username=request.user.username)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

class EducationAdmin(admin.ModelAdmin):
    list_display = ('id', 'institute_name', 'degree',
                    'location', 'is_active')
    list_display_links = ('id', 'institute_name')
    list_filter = ('degree', 'location')
    list_editable = ('is_active',)
    list_per_page = 20
    
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(user=request.user)
    
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if request.user.is_superuser:
            kwargs["queryset"] = User.objects.all()
            
        elif db_field.name == "user":
            kwargs["queryset"] = User.objects.filter(username=request.user.username)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('id', 'company_name', 'designation',
                    'location', 'is_active')
    list_display_links = ('id', 'company_name')
    list_filter = ('designation', 'location')
    list_editable = ('is_active',)
    list_per_page = 20
    
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(user=request.user)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if request.user.is_superuser:
            kwargs["queryset"] = User.objects.all()
            
        elif db_field.name == "user":
            kwargs["queryset"] = User.objects.filter(username=request.user.username)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'category_name')
    list_display_links = ('id',)
    list_editable = ('category_name',)
    list_per_page = 20

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(user=request.user)
    
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if request.user.is_superuser:
            kwargs["queryset"] = User.objects.all()
            
        elif db_field.name == "user":
            kwargs["queryset"] = User.objects.filter(username=request.user.username)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

class PortfolioAdmin(admin.ModelAdmin):
    list_display = ('id', 'category_id', 'portfolio_title',
                    'web_link', 'is_active')
    list_display_links = ('id', 'category_id', 'portfolio_title')
    list_filter = ('category_id', 'is_active')
    list_editable = ('is_active',)
    list_per_page = 20
    
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(user=request.user)
    
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if request.user.is_superuser:
            kwargs["queryset"] = User.objects.all()
            #kwargs["queryset"] = Category.objects.filter(user=request.user)
            
        elif db_field.name == "user":
            kwargs["queryset"] = User.objects.filter(username=request.user.username)
   
        if db_field.name == "category_id":
            if request.user.is_superuser:
                
                kwargs["queryset"] = Category.objects.all()
            else:
                kwargs["queryset"] = Category.objects.filter(user=request.user)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)
    
    
    
class TrainingAdmin(admin.ModelAdmin):
    list_display = ('id', 'training_name', 'institute', 'is_active')
    list_display_links = ('id', 'training_name', 'institute')
    list_filter = ('id', 'is_active')
    list_editable = ('is_active',)
    list_per_page = 20
    
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(user=request.user)
    
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if request.user.is_superuser:
            kwargs["queryset"] = User.objects.all()
            
        elif db_field.name == "user":
            kwargs["queryset"] = User.objects.filter(username=request.user.username)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


admin.site.register(Profile, ProfileAdmin)
admin.site.register(Image, ImageAdmin)
admin.site.register(HirePlatform, HirePlatformAdmin)
admin.site.register(Skill, SkillAdmin)
admin.site.register(Education, EducationAdmin)
admin.site.register(Experience, ExperienceAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Portfolio, PortfolioAdmin)
admin.site.register(Training, TrainingAdmin)
