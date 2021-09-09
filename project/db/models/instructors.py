from django.db import models
import uuid
from django.conf import settings


class Instructor(models.Model):
    id = models.UUIDField(unique=True, primary_key=True, default=uuid.uuid4, editable=False)
    user_id = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    bio = models.TextField(null=True, blank=True)
    facebook = models.URLField(null=True, blank=True, max_length=200)
    twitter = models.URLField(null=True, blank=True, max_length=200)
    instagram = models.URLField(null=True, blank=True, max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.user_id}'
    
