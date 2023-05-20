import uuid, datetime
from django.utils import timezone
from django.db import models

# Create your models here.

class Post(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    content = models.CharField(max_length=1000)
    timestamp = models.DateTimeField(auto_now_add=True)
    # timestamp = models.DateTimeField(default=timezone.now)
    view_count = models.IntegerField(default=0)

class Comment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.CharField(max_length=1000)
    timestamp = models.DateTimeField(auto_now_add=True)