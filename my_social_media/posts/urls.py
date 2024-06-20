from django.urls import path

from . import views

app_name = 'post'

urlpatterns = [
    path('new-post', views.create_post, name='create_post'),
    path('view_post/<slug:slug>', views.PostDetail.as_view(), name='post_detail'),
    path('view_post/like_post/<slug:slug>', views.like_post, name='like_post'),
]