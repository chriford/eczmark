from django.db import models

from eczmark.models.abstract import Timestamp

class Subject(Timestamp):
    name = models.CharField(
        verbose_name="Subject",
        help_text="The subject of the question paper e.g English, Science, ...",
        max_length=100,
        null=True,
        blank=False,
    )
    
    def __str__(self):
        return self.name
