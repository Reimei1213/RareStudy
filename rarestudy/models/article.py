from django.db import models
from django.utils import timezone
import uuid

from .user import User

class Article(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=100)
    body = models.CharField(max_length=10000)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)
    valid = models.BooleanField(default=False)