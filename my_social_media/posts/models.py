from django.db import models

from users.models import CustomUser
# Create your models here.

class Post(models.Model):
    text = models.CharField(max_length=700)
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(blank=True, upload_to='images/post_images')
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='posts')

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    def __str__(self):
        return f'Post of {self.user.username} at {self.created_at}'