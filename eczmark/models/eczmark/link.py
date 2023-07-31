from django.db import models

from eczmark.models.abstract import Timestamp
from django.core.validators import MaxLengthValidator, MinLengthValidator

class Link(Timestamp):
    link = models.URLField(
        verbose_name="Supporting link",
        null=True,
        blank=True,
    )
    answer = models.ForeignKey(
        to="eczmark.Answer", 
        help_text="""Select the answer to which this supporting link belong,
        leave blank for default value; Empty""",
        on_delete=models.CASCADE,
        null=True,
        blank=False,
    )
    note = models.CharField(
        verbose_name="Note",
        help_text="""A quick note about this supporting link. Must have words between 15 and 100.""",
        max_length=[
            MinLengthValidator(limit_value=15),
            MaxLengthValidator(limit_value=100),
        ],
        null=True,
        blank=True,
    )
    
    def __str__(self):
        return self.link
