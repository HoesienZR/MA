from django import template
from social.models import Post,Arts
from django.shortcuts import render,get_object_or_404

register = template.Library()

@register.inclusion_tag('partials/more_arts.html')
def more_works(post_id,):
    current_post = get_object_or_404(Post,id=post_id)
    user = current_post.auther
    more_posts = Post.objects.filter(auther_id=user.id).exclude(id=current_post.id).order_by('-published_at')[:9]
    more_arts = Arts.objects.filter()
    image_obj = []
    for post in more_posts:
        image_obj.append(post.images)
    print(image_obj[0].first().image)
    context = {
        'user': user,
        'more_posts': more_posts,
        'image_obj': image_obj
    }

    return context
