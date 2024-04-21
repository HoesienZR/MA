from django.db import models


from taggit.managers import TaggableManager
from django_resized import ResizedImageField

from account.models import SocialUser
from .tools import user_art_path

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=64)
    description = models.TextField()
    views = models.IntegerField(default=0)
    tag = TaggableManager()
    likes = models.ManyToManyField(SocialUser, blank=True, related_name='liked_posts', )
    saved_by = models.ManyToManyField(SocialUser, related_name='saved_posts_by', blank=True)
    published_at = models.DateTimeField(auto_now_add=True)
    last_change = models.DateTimeField(auto_now=True)
    auther = models.ForeignKey(SocialUser, related_name="post", on_delete=models.CASCADE,)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-last_change']
        indexes = [
            models.Index(fields=['-last_change',])
        ]


class Arts(models.Model):
    image = ResizedImageField(quality=80, upload_to=user_art_path,size=[500,300])
    post = models.ForeignKey(Post, related_name='images', on_delete=models.CASCADE)
    description = models.TextField(blank=True)


class SoftwareCategory(models.Model):
    name = models.CharField(max_length=128)
    slug = models.SlugField()
    post = models.ForeignKey(Post, related_name='software_categories', on_delete=models.CASCADE)




