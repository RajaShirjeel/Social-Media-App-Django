from django.urls import path

from . import views

app_name = 'users'

urlpatterns = [
    path('profile/<slug:slug>', views.UserProfile.as_view(), name='user_profile'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('follow_user/<int:pk>', views.follow, name='follow_user'),
    path('unfollow<int:pk>', views.unfollow, name='unfollow_user'),
    path('edit_profile/<slug:slug>/', views.edit_profile, name='edit_profile')
]