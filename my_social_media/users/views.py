from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from .forms import CustomUserForm, LoginForm

# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = CustomUserForm(request.POST)
        if form.is_valid():
            form.save()

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
            
            else: 
                messages.error(request, 'Invalid email or password')

    else:
        form = LoginForm()
        return render(request, 'users/login.html', {'form': form})
