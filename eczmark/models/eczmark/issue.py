from django.db import models

from eczmark.models.abstract import Timestamp
from django.core.validators import MaxLengthValidator, MinLengthValidator

class Issue(Timestamp):
    name = models.CharField(
        verbose_name="name",
        help_text="A brief title of the common issue",
        validators=[
            MinLengthValidator(5),
            MaxLengthValidator(100),
        ],
        null=True
    )

    def __str__(self):
        return self.name
