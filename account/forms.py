from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import SocialUser


class ShopUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = SocialUser
        fields = ('phone', 'first_name', 'last_name', 'is_active', 'is_staff', 'is_superuser',)

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        if self.instance.pk:
            if SocialUser.objects.filter(phone=phone).exclude(pk=self.instance.pk).exists():
                raise forms.ValidationError('phone already exists1')
        else:
            if SocialUser.objects.filter(phone=phone).exists():
                raise forms.ValidationError('phone already exists2')

        if SocialUser.objects.filter(phone=phone).exists():
            raise forms.ValidationError('this user already exists')
        if not phone.isdigit():
            raise forms.ValidationError('this phone number is not valid')
        if not phone.startswith('09'):
            raise forms.ValidationError('it\'should start with 09')
        if len(phone) != 11:
            raise forms.ValidationError('it\'s should be 11 characters')
        return phone

class ShopUserChangeForm(UserChangeForm):

    class Meta(UserChangeForm.Meta):
        model = SocialUser
        fields = ('phone', 'first_name', 'last_name', 'is_active', 'is_staff', 'is_superuser')

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        if self.instance.pk:
            if SocialUser.objects.filter(phone=phone).exclude(pk=self.instance.pk).exists():
                raise forms.ValidationError('phone already exists1')
        else:
            if SocialUser.objects.filter(phone=phone).exists():
                raise forms.ValidationError('phone already exists2')

        if SocialUser.objects.filter(phone=phone).exists():
            raise forms.ValidationError('this user already exists')
        if not phone.isdigit():
            raise forms.ValidationError('this phone number is not valid')
        if not phone.startwith('09'):
            raise forms.ValidationError('it\'should start with 09')
        if len(phone) != 11:
            raise forms.ValidationError('it\'s should be 11 characters')

        return phone
