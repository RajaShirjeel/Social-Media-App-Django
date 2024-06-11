from django.shortcuts import render, redirect

from .forms import CreatePostForm
# Create your views here.

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
