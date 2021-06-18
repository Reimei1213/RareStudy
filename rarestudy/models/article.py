from django.db import models
from django.utils import timezone
import uuid
from mdeditor.fields import MDTextField
from rarestudy.models.user import User

class Article(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=100, verbose_name='タイトル')
    body = MDTextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Articles')
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
            self.save()

    def set_body(self, body):
        if body is not None:
            self.body = body
            self.save()

    def set_user(self, User):
        if User is not None:
            self.user = User
            self.save()

    def delete(self):
        self.valid = False
        self.save()
