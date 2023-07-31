from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import PermissionsMixin, AbstractUser

from eczmark.models.abstract import Timestamp
from eczmark.managers import CustomBaseUserManager

class User(AbstractUser, PermissionsMixin, Timestamp):
    """A model that keeps some details about a user."""
    username = models.CharField(
        verbose_name=_("Username"), 
        db_index=True, 
        unique=True, 
        max_length=255
    )
    first_name = models.CharField(
        verbose_name=_("First Name"), 
        max_length=255, 
        null=True, 
        blank=True,
    )
    last_name = models.CharField(
        verbose_name=_("Last Name"), 
        max_length=255, 
        null=True, 
        blank=True
    )
    phone_number = models.CharField(
        verbose_name=_("Phone number"), 
        max_length=15, 
        null=True, 
        blank=True
    )
    email = models.EmailField(
        verbose_name=_("Email"), 
        unique=True,
        null=True,
        blank=True,
        error_messages={
            'unique': _("A user with that email already exists."),
        }
    )
    created_at = models.DateTimeField(
        verbose_name=_("Created At"), 
        auto_now_add=True,
        null=True,
        blank=False,
    )
    updated_at = models.DateTimeField(
        verbose_name=_("Updated At"),
        auto_now=True,
        null=True,
        blank=False,
    )
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)
    date = models.DateTimeField(auto_now_add=True)
    
    objects = CustomBaseUserManager()
    
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    class Meta(AbstractUser.Meta):
        pass

    def __str__(self):
        return self.username
