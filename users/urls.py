from django.urls import path

from . import views

urlpatterns = [
    path('users', views.users, name='users'),
    path('<int:user_id>', views.user, name='user'),
    path('search', views.search, name='search'),
] 
