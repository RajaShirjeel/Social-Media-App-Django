from typing import Any
from django.db.models.base import Model as Model
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.views.generic import DetailView
from django.shortcuts import get_object_or_404
from django.db.utils import IntegrityError

from .forms import CustomUserForm, LoginForm
from .models import CustomUser, Follow
# Create your views here.

class UserProfile(DetailView):
    model = CustomUser
    template_name = 'users/profile.html'
    slug_field = 'slug'
    context_object_name = 'user'

    def get_object(self, queryset=None):
        slug = self.kwargs.get('slug')
        return get_object_or_404(CustomUser, slug=slug)
    
    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        profile_user = self.get_object()
        is_following = Follow.objects.filter(follower=self.request.user, following=profile_user).exists()
        context['is_following'] = is_following
        return context





def signup(request):
    if request.method == 'POST':
        form = CustomUserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()
            return redirect('users:login')

    else:
        form = CustomUserForm()

    return render(request, 'users/register.html', {'form': form})
    

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(email=email, password=password)

            if user is not None: 
                login(request, user)
                return redirect('home')
            
            else: 
                form.add_error('email', 'Invalid email or password')

    else:
        form = LoginForm()

    return render(request, 'users/login.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('home')  


def follow(request, pk):
    user = get_object_or_404(CustomUser, pk=pk)
    existing_follow = Follow.objects.filter(follower=request.user, following=user).exists()
    if not existing_follow:
        try: 
            follow = Follow.objects.create(follower=request.user, following=user)
        
        except IntegrityError:
            pass

    return redirect('users:user_profile', slug=user.slug)


def unfollow(request, pk):
    user = get_object_or_404(CustomUser, pk=pk)
    Follow.objects.filter(follower=request.user, following=user).delete()
    return redirect('users:user_profile', slug=user.slug)
