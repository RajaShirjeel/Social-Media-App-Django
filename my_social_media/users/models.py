from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.text import slugify
from django.db import transaction
from django.db.utils import IntegrityError

import uuid
# Create your models here.
class CustomUser(AbstractUser):
    username = models.CharField(max_length=150)
    email = models.EmailField(unique=True)
    bio = models.TextField()
    profile_picture = models.ImageField(upload_to='profile_pics', blank=True)
    slug = models.SlugField(unique=True, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.username
    
    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.username)
            while True:
                unique_id = uuid.uuid4().hex[:6]
                slug = f"{base_slug}-{unique_id}"
                try:
                    with transaction.atomic():
                        self.slug = slug
                        super().save(*args, **kwargs)
                except IntegrityError:
                    unique_id = uuid.uuid4().hex[:6]
                    slug = f"{base_slug}-{unique_id}"
                
                else:
                    break
        else:  
            super().save(*args, **kwargs)



class Follow(models.Model):
    follower = models.ForeignKey(CustomUser, related_name='following', on_delete=models.CASCADE)
    following = models.ForeignKey(CustomUser, related_name='followers', on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)

    class Meta:
        unique_together = ('follower', 'following')

    def __str__(self):
        return f"{self.follower} follows {self.following}"
    
