from django.db import models

from eczmark.models.abstract import Timestamp
from django.core.validators import MaxLengthValidator, MinLengthValidator

class Grade(Timestamp):
    grade = models.SmallIntegerField(
        verbose_name="Grade",
        null=True,
        blank=False,
    )

    def __str__(self):
        return str(self.grade)
