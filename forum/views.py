from django.shortcuts import render
from .models import Post
from django.http import Http404, JsonResponse
from django.core.paginator import Paginator


def post_list(request):
    data = {}
    all_posts = Post.objects.all()

    # # to delete
    # last_post = all_posts[0]
    # last_post.id = None
    # last_post.save()
    # # end to delete

    paginator = Paginator(all_posts, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    # data['posts'] = all_posts
    data['page_obj'] = page_obj

    return render(request, 'forum/post_list.html', context=data)


def post_details(request, post_id: int):
    if not Post.objects.filter(id=post_id).exists():
        raise Http404
    post = Post.objects.get(id=post_id)
    data = dict()
    data['post'] = post
    # fixme
    # data['liked'] = post.likes.filter(request.user)
    return render(request, 'forum/post_details.html', context=data )


def ajax_like(request, post_id):
    response = dict()
    response['status'] = 'error'
    if request.user.is_authenticated:
        if not Post.objects.filter(id=post_id).exists():
            raise Http404
        post = Post.objects.get(id=post_id)
        like_action = request.GET.get('like_action')
        if like_action == 'add':
            post.likes.add(request.user)
            response['status'] = 'ok'
        elif like_action == 'remove':
            post.likes.remove(request.user)
            response['status'] = 'ok'
    return JsonResponse(response)











