from django.db import models
from django.db.utils import IntegrityError
from django.utils.text import slugify


import uuid

from users.models import CustomUser
# Create your models here.

class Post(models.Model):
    text = models.CharField(max_length=700)
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(blank=True, upload_to='images/post_images')
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='posts')
    slug = models.SlugField(unique=True, blank=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    def __str__(self):
        return f'Post of {self.user.username} at {self.created_at}'
    
    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.text)
            while True: 
                unique_id = uuid.uuid4().hex[:10]
                slug = f"{base_slug}-{unique_id}"
            
                try:
                    self.slug = slug
                    super().save(*args, **kwargs)
                
                except IntegrityError:
                    unique_id = uuid.uuid4().hex[:10]
                    slug = f"{base_slug}-{unique_id}"
                
                else:
                    break

        else:
            super().save(*args, **kwargs)

    @property
    def likes_count(self):
        return self.likes.count()


class Like(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='likes')
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='liked_posts')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Like of {self.user.username} on {self.post.text} at {self.created_at}'
