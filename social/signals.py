from django.db.models.signals import post_delete,pre_delete
from django.dispatch import receiver
import os
from .models import Post


def delete_images(post: Post):
    images = post.images.all()
    for image in images:
        if os.path.isfile(image.image.path):
            os.remove(image.image.path)


@receiver(pre_delete, sender=Post)
def imageclear(sender, instance, using, **kwargs):
    delete_images(instance)