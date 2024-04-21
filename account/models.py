import django.utils.timezone
from django.db import models
from django.db import models
from django.contrib.auth.models import PermissionsMixin,BaseUserManager,AbstractBaseUser
from django.utils import timezone
from django_resized import ResizedImageField


from social.tools import user_profile_path

# Create your models here.


class SocialUserManager(BaseUserManager):
    def create_user(self,phone,password=None,**extra_fields):
        if not phone:
            raise ValueError('phone number is not valid')
        user = self.model(phone=phone,**extra_fields)
        user.set_password(password)
        user.save(using=self._db)

    def create_superuser(self, phone, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('is_staff most be true')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('is_superuser most be true')

        return self.create_user(phone, password, **extra_fields)


class SocialUser(AbstractBaseUser,PermissionsMixin):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=32)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    role = models.CharField(max_length=32, default='')
    job = models.CharField(max_length=32, default='')
    access_for_work = models.BooleanField(default=True)
    phone = models.CharField(max_length=11, unique=True)
    date_joined = models.DateTimeField(default=django.utils.timezone.now())
    objects = SocialUserManager()
    email = models.EmailField(null=True,blank=True)
    bio = models.TextField(default='')
    birthdate = models.DateField(default='2022-01-01')
    nickname = models.CharField(max_length=40,default='')
    profile = ResizedImageField(quality=80,upload_to=user_profile_path,null=True,blank=True)
    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.first_name
