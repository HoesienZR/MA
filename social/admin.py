from django.contrib import admin
from django.contrib.admin import TabularInline

from account.models import SocialUser
from .models import Post, Arts, SoftwareCategory


class ArtsInline(TabularInline):
    model = Arts
    extra = 2


class SoftwareInline(TabularInline):
    model = SoftwareCategory
    extra = 2




@admin.register(Post)
class PostsAdmin(admin.ModelAdmin):
    list_display = ['title']
    inlines = [ArtsInline, SoftwareInline,]

