from django.shortcuts import render

from users.models import CustomUser
def home(request):
    user = request.user
    return render(request, 'home.html', {'user':user})


def search_users(request):
    query = request.GET.get('query', '')
    if query:
        users = CustomUser.objects.filter(username__icontains=query)
    
    else:
        users = CustomUser.objects.none()

    return render(request, 'search_results.html', {'users':users, 'query':query})

