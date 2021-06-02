from django.db import models
from django.utils import timezone
import uuid

from .user import User

class Article(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=100)
    body = models.CharField(max_length=10000)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)
    valid = models.BooleanField(default=True)

    ## getter
    def get_id(self):
        try:
            return self.id
        except:
            return False

    def get_title(self):
        try:
            return self.title
        except:
            return False

    def get_body(self):
        try:
            return self.body
        except:
            return False

    def get_user(self):
        try:
            return self.user
        except:
            return False

    def get_created_at(self):
        try:
            return self.created_at
        except:
            return False

    def get_valid(self):
        try:
            return self.valid
        except:
            return False

    ## setter
    def set_title(self, title):
        if title is not None:
             self.title = title

    def set_body(self, body):
        if body is not None:
            self.body = body

    def set_user(self, User):
        if User is not None:
            self.user = User

    def delete(self):
        self.valid = 0
