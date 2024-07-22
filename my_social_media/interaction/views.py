from django.shortcuts import render, get_object_or_404
from django.contrib.auth import get_user_model
from django.db.models import Q

from users.models import CustomUser
from .models import Message

# Create your views here.

User = get_user_model()

def chat_view(request, slug):
    other_user = get_object_or_404(User, slug=slug)
    messages = Message.objects.filter(
        Q(sender=request.user, receiver=other_user) | 
        Q(sender=other_user, receiver=request.user)
    ).order_by('timestamp')
    
    context = {
        'messages': messages,
        'other_user': other_user,
        'user': request.user
    }
    return render(request, 'interaction/chat.html', context)