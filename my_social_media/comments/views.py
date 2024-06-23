from django.shortcuts import render, redirect, get_object_or_404

from .models import Comment
from .forms import CommentForm
from posts.models import Post
# Create your views here.

def create_comment(request, slug):
    user = request.user
    post = get_object_or_404(Post, slug=slug)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = user
            comment.post = post
            comment.save()
            return redirect('post:post_detail', slug=slug)
    
    else:
        form = CommentForm()
    return render(request, 'comments/comment_form.html', {'form': form})
    

def delete_comment(request, pk, slug):
    comment = get_object_or_404(Comment, pk=pk)
    if comment.user == request.user:
        comment.delete()
        return redirect('post:post_detail', slug=slug)
    else:
        return redirect('post:post_detail', slug=slug)

    

