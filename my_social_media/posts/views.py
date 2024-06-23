from typing import Any
from django.db.models.base import Model as Model
from django.shortcuts import render, redirect
from django.views import generic
from django.shortcuts import get_object_or_404
from django.http import JsonResponse



from .forms import CreatePostForm
from .models import Post, Like
from comments.forms import CommentForm
# Create your views here.

class PostDetail(generic.DetailView):
    template_name = 'posts/post_detail.html'
    model = Post
    slug_field = 'slug'
    context_object_name = 'post'

    def get_object(self, queryset=None):
        slug = self.kwargs.get('slug')
        return get_object_or_404(Post, slug=slug)
    
    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        post = self.get_object()
        context['form'] =  CommentForm()
        context['comments'] = post.comments.all()
        return context


def create_post(request):
    if request.method == 'POST':
        form = CreatePostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('home')

    else:
        form = CreatePostForm()
    
    return render(request, 'posts/post_form.html', {'form':form})


def like_post(request, slug):
    post = get_object_or_404(Post, slug=slug)
    like_obj, created = Like.objects.get_or_create(user=request.user, post=post)
    if not created:
        like_obj.delete()
        return JsonResponse({'likes_count': post.likes_count, 'liked': False})

    else:      
        return JsonResponse({'likes_count': post.likes_count, 'liked':True})




