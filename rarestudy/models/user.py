from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager
from django.db import models
from django.core.mail import send_mail
from django.utils import timezone
import uuid

class UserManager(UserManager):
    def _create_user(self, username, email, password, **extra_fields):
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(username, email, password, **extra_fields)

    def create_superuser(self, username, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self._create_user(username, email, password, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=50)
    icon_tag = models.PositiveSmallIntegerField(default=0)
    bio = models.CharField(max_length=300, null=True)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)
    valid = models.BooleanField(default=True)

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

    def get_id(self):
        try:
            return self.id
        except:
            return False

    def get_username(self):
        try:
            return self.username
        except:
            return False

    def get_email(self):
        try:
            return self.email
        except:
            return False

    def get_password(self):
        try:
            return self.password
        except:
            return False

    def get_icon_tag(self):
        try:
            return self.icon_tag
        except:
            return False

    def get_bio(self):
        try:
            return self.bio
        except:
            return False

    def get_created_at(self):
        try:
            return self.created_at
        except:
            return False

    def get_is_staff(self):
        try:
            return self.is_staff
        except:
            return False

    def get_valid(self):
        try:
            return self.valid
        except:
            return False