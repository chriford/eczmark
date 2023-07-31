
from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _

class CustomBaseUserManager(BaseUserManager):
    """
    A custom base user manager for overriding the default user model manager.
    Contains two main user creation actions:
    1. create_user: collects data from a form in the ui and then creates the user account.
    2. create_superuser: collects data from a commandline interface and then creates the user account.
    """
    def create_user(self, username, password, email=None, **kwargs):
        """Create and return a `User` with an email, username and password."""
        if not username:
            raise TypeError("Users must have a username.")

        if not password:
            raise TypeError("User must have a  papssword.")

        user = self.model(
            username=username, password=password, email=self.normalize_email(email)
        )
        user.set_password(password)
        user.save(using=self._db)

        return user
    
    def create_superuser(self, username, password, email=None, **kwargs):
        """
        Create and return a `User` with superuser (admin) permissions.
        """
        if not password:
            raise TypeError("Superusers must have a password.")

        if not username:
            raise TypeError("Superusers must have a unique username.")

        user = self.create_user(
            username=username, password=password, email=email, **kwargs
        )
        user.is_superuser = True
        user.is_staff = True
        user.is_active = True
        user.save(using=self._db)

        return user
    
    def has_module_perms(self, *args): # or add
        return True
