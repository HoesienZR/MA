from django.shortcuts import render,get_object_or_404
from .models import Post
from django.http import JsonResponse
# Create your views here.


def show_details(request):
    post = get_object_or_404(Post, id=1)
    auther = post.auther
    arts = post.images.all()
    print(auther)
    post.views += 1
    context = {
        'post': post,
        'auther': auther,
        'arts': arts,
    }
    return render(request, 'views/post_details.html', context=context)


def update_like(request):
    print('enterd this shit')
    post_id = request.GET.get('post_id')
    print(post_id)
    user = request.user
    if post_id is not None:
        post = get_object_or_404(Post, id=post_id)
        print(post.likes.all())
        if user is post.likes.all():
            post.likes.remove(user)
            liked = False
        else:
            post.likes.add(user)
            liked = True
        post_likes = post.likes.count()
        response_data = {
            'post_likes': post_likes,
            'liked': liked,
        }
    else:
        response_data = {'error': 'invalid post'}
    print(response_data)
    return JsonResponse(response_data,)
