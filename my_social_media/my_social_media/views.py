from django.shortcuts import render

def home(request):
    user = request.user
    return render(request, 'home.html', {'user':user})