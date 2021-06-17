from django.db import models
from django.utils import timezone
import uuid

from rarestudy.models.user import User
from rarestudy.models.article import Article

class Comment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    body = models.TextField(max_length=1000)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='Comments')
    created_at = models.DateTimeField(default=timezone.now)
    valid = models.BooleanField(default=True)

    ## getter
    def get_id(self):
        try:
            return self.id
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

    def get_article(self):
        try:
            return self.article
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
    def set_body(self, body):
        if body is not None:
            self.body = body
            self.save()

    def set_user(self, User):
        if User is not None:
            self.user = User
            self.save()

    def set_article(self, Article):
        if Article is not None:
            self.article = Article
            self.save()

    def delete(self):
        self.valid = False
        self.save()