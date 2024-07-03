from django.urls import path
from . import views

app_name = 'interaction'

urlpatterns = [
    path('chat/<slug:slug>/', views.chat_view, name='chat_view')
]