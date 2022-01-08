from django.contrib import admin
from django.urls import path
from user import views


urlpatterns = [

    path('',views.home, name='home'),
    path('photo/',views.photo, name='photo'),
    path('login/',views.login, name='login'),
    path('user_logout/',views.user_logout, name='user_logout'),
    path('signup/',views.signup, name='signup'),
]
