from django.shortcuts import render


def post_list(request):
    return render(request, 'forum/post_list.html')


def post_details(request, post_id: int):
    return render(request, 'forum/post_details.html')
