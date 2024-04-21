from django.contrib import admin
from account.models import SocialUser
from django.contrib.auth.admin import UserAdmin
from .forms import ShopUserChangeForm , ShopUserCreationForm

# Register your models here.



@admin.register(SocialUser)
class ShopUserAdmin(UserAdmin):
    ordering = ['phone']
    add_form = ShopUserCreationForm
    form = ShopUserChangeForm
    model = SocialUser
    list_display = ['phone', 'first_name', 'last_name', 'is_staff', 'is_active']
    fieldsets = (
        (None, {'fields': ('phone', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'job', 'birthdate',)}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined',)}),
        ('User info', {'fields': ('profile', 'nickname', 'bio', 'access_for_work', 'role')})
    )

    add_fieldsets = (
        (None, {'fields': ('phone', 'password1','password2')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'job', 'birthdate',)}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined',)}),
        ('User info', {'fields': ('profile', 'nickname', 'bio', 'access_for_work', 'role' )})
    )