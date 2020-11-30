from django.shortcuts import render
from .models import Post
from django.http import Http404, JsonResponse
from django.core.paginator import Paginator
from django.db.models import Q


def post_list(request):
    data = {}
    all_posts = Post.objects.all()

    # # to delete
    # last_post = all_posts[0]
    # last_post.id = None
    # last_post.save()
    # # end to delete

    search = request.GET.get('search')
    print(search)
    if search:

        # слишком просто
        # result_posts = all_posts.filter(title__icontains=search)
        # all_posts = result_posts

        # круто
        result_posts = all_posts.filter(
            Q(title__icontains=search) |
            Q(author__username__icontains=search)
            # & Q(author__is_superuser=True)
        )
        all_posts = result_posts
        data['search'] = search



    paginator = Paginator(all_posts, 6)
    page_number = request.GET.get('page')


    # if int(page_number) > paginator.num_pages:
    #     page_number = paginator.num_pages
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
    data['liked'] = request.user in post.likes.all()
    print(post.likes.all())


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











