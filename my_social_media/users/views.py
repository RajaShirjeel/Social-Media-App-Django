from django.shortcuts import render


from .forms import CustomUserForm

# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = CustomUserForm(request.POST)
        if form.is_valid():
            form.save()

    else:
        form = CustomUserForm()
        return render(request, 'users/register.html', {'form': form})