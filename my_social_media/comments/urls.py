from django.urls import path

from . import views

app_name = 'comment'

urlpatterns = [
    path('display_comments', views.display_comments, name='display_comments'),
    path('add_comment/', views.create_comment, name='create_comment'),
    path('delete_comment', views.delete_comment, name='delete_comment')
    
]