"""Models for storing generic and homepage content."""

from django.db import models
from django.contrib.auth.models import AbstractUser

from .managers import CustomUserManager


class User(AbstractUser):
    """Staff user for managing site content."""

    username = None
    email = models.EmailField(unique=True, )
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']
    objects = CustomUserManager()

    def __str__(self):
        """Return a string representation of self."""
        return f"{self.first_name} {self.last_name} <{self.email}>"


class Notice(models.Model):
    """A site notice to be displayed on the home/landing pages."""

    INFO = 'info'
    WARNING = 'warning'
    DANGER = 'danger'

    NOTICE_CLASSES = (
        (INFO, 'info'),
        (WARNING, 'warning'),
        (DANGER, 'danger'),
    )

    notice_class = models.CharField(
        max_length=16, choices=NOTICE_CLASSES, default=INFO,
    )
    title = models.CharField(max_length=100)
    body = models.CharField(max_length=2000, help_text='Enter valid markdown')
    material_icon = models.CharField(
        max_length=50, null=True, blank=True,
        help_text=('A valid material design icon identifier.'
                   ' See: https://fonts.google.com/icons')
        )
