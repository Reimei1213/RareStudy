from django.contrib.auth.models import AbstractBaseUser, UserManager, PermissionsMixin
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.mail import send_mail
from django.utils import timezone
import uuid


class UserManager(UserManager):
    def _create_user(self, email, password, **extra_fields):
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=50, default='user')
    icon_tag = models.PositiveSmallIntegerField(default=0)
    bio = models.CharField(max_length=300, null=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=timezone.now)
    valid = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    objects = UserManager()

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def clean(self):
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)

    def email_user(self, subject, message, from_email=None, **kwargs):
        """Send an email to this user."""
        send_mail(subject, message, from_email, [self.email], **kwargs)

## getter
    def get_id(self):
        try:
            return self.id
        except:
            return False

    def get_name(self):
        try:
            return self.name
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

    def get_icon_path(self):
        try:
            return 'image/user_icon/icon_' + str(self.icon_tag) + '.png'
        except:
            return False

    ## setter
    def set_name(self, name):
        if name is not None:
            self.name = name

    def set_email(self, email):
        if email is not None:
            self.email = email

    def set_icon_tag(self, icon_tag):
        if icon_tag is not None:
            self.icon_tag = icon_tag

    def set_bio(self, bio):
        if bio is not None:
            self.bio = bio

    def set_is_staff(self, is_staff):
        if is_staff is not None:
            self.is_staff = is_staff

    def delete(self):
        self.valid = 0
