from django.db import models

from eczmark.models.abstract import Timestamp

class Profile(Timestamp):
    """A model that contains more details about a user. This model stores meta data about a user."""
    user = models.ForeignKey(
        to="eczmark.User",
        verbose_name="User",
        on_delete=models.CASCADE,
        null=True,
    )
    photo = models.ImageField(
        upload_to='profile-photos/%d-%M-%Y+%H:%M:%S',
        null=True, blank=True,
    )

    def __str__(self):
        return f'{self.user.username} profile'
