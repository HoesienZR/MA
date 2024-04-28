from django.shortcuts import render,get_object_or_404

from account.models import SocialUser
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST

from .models import Post
# Create your views here.


def show_details(request):
    post = get_object_or_404(Post, id=1)
    auther = request.user
    print(auther.id)
    print(request.user.id)
    print ('check that auther is equal to request user ',auther == request.user)
    arts = post.images.all()
    print('print profile executed')
    print(auther in post.saved_by.all())
    post.views += 1
    context = {
        'post': post,
        'auther': auther,
        'arts': arts,
        'is_in_auther': auther in post.saved_by.all(),
    }
    print(context['is_in_auther'])
    return render(request, 'views/post_details.html', context=context)


@login_required
@require_POST
def update_like(request):
    if request.method == 'POST':
        post_id = request.POST.get('item_id')
        user = request.user
        if post_id is not None:
            post = get_object_or_404(Post, id=post_id)
            if user in post.likes.all():
                post.likes.remove(user)
            else:
                post.likes.add(user)
            post_likes = post.likes.count()
            response_data = {
                'post_likes': post_likes,
                'success': True,
            }
        else:
            response_data = {'error': 'invalid post', 'success': False}
        return JsonResponse(response_data,)


@require_POST
@login_required
def save_post(request):
    if request.method == 'POST':
        post_id = request.POST.get('post_id')
        user = request.user
        if post_id is not None:
            post = get_object_or_404(Post, id=post_id)
            if user in post.saved_by.all():
                post.saved_by.remove(user)
                saved = False
            else:
                post.saved_by.add(user)
                saved = True

            response_data = {
                'saved': saved,
                'success': True,

            }
        else:
            response_data = {'error': 'invalid post', 'success': False}
        print('this is in ajax',user in post.saved_by.all())
        return JsonResponse(response_data)
