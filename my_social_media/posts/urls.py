from django.urls import path

from . import views

app_name = 'Post'

urlpatterns = [
    path('new-post', views.create_post, name='create_post')
]