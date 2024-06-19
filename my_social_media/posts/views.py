from django.db.models.base import Model as Model
from django.shortcuts import render, redirect
from django.views import generic
from django.shortcuts import get_object_or_404
from django.http import JsonResponse



from .forms import CreatePostForm
from .models import Post, Like
# Create your views here.

class PostDetail(generic.DetailView):
    template_name = 'posts/post_detail.html'
    model = Post
    slug_field = 'slug'
    context_object_name = 'post'

    def get_object(self, queryset=None):
        slug = self.kwargs.get('slug')
        return get_object_or_404(Post, slug=slug)

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
    Like.objects.create(user=request.user, post=post)
    return JsonResponse({'likes_count': post.likes_count, 'liked':True})


def unlike_post(request, slug):
    post = get_object_or_404(Post, slug)
    Like.objects.filter(user=request.user, post=post).delete()
    return JsonResponse({'likes_count': post.likes_count, 'liked': False})




