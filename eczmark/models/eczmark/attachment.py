from django.db import models

from eczmark.models.abstract import Timestamp
from django.core.validators import MaxLengthValidator, MinLengthValidator

class Attachment(Timestamp):
    file = models.ImageField(upload_to='attachments/%Y-%M-%d/')
    note = models.CharField(
        verbose_name="Note",
        help_text="""A quick note about this supporting image. Must have words between 20 and 100.""",
        max_length=100,
        max_length=[
            MinLengthValidator(limit_value=15),
            MaxLengthValidator(limit_value=100),
        ],
        null=True,
        blank=True,
    )

    def __str__(self):
        if self.file:
            file_name = self.file.name
            return file_name
        else:
            return None
