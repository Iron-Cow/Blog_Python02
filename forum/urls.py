from django.urls import path
from .views import post_details, post_list

urlpatterns = [
    path('', post_list, name='post_list'),
    path('<int:post_id>/post_details', post_details, name='post_details'),
]
