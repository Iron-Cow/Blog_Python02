from django.urls import path
from .views import post_details, post_list, ajax_like

urlpatterns = [
    path('', post_list, name='post_list'),
    path('<int:post_id>/post_details', post_details, name='post_details'),
    path('<int:post_id>/like', ajax_like, name='ajax_like'),
]
