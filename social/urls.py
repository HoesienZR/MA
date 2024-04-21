from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views
from . import views


app_name = 'social'
urlpatterns = [

    path('post_details/', views.show_details, name='post_details'),
    path('update_like/',views.update_like,name='update_like')





    ]