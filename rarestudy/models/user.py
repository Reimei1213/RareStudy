from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.core.mail import send_mail
from django.utils import timezone
import uuid
from rarestudy.models.user_manager import UserManager

class User(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=50)
    icon_tag = models.PositiveSmallIntegerField(default=0)
    bio = models.CharField(max_length=300, null=True)
    created_at = models.DateTimeField(default=timezone.now)
    valid = models.BooleanField(default=False)

    objects = UserManager()

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def clean(self):
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)

    def email_user(self, subject, message, from_email=None, **kwargs):
        """Send an email to this user."""
        send_mail(subject, message, from_email, [self.email], **kwargs)