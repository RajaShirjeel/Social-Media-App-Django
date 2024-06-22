from django.db import models

from users.models import CustomUser
from posts.models import Post
# Create your models here.
class Comment(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='comments')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    text = models.CharField(max_length=1000)
    created_at = models.DateField(auto_now_add=True)


    def __str__(self):
        return f"{self.user.username}'s comment on {self.post.text}"
