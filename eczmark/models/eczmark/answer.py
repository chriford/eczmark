from django.db import models

from eczmark.models.abstract import Timestamp
from django.core.validators import MaxLengthValidator, MinLengthValidator

class Answer(Timestamp):
    user = models.ForeignKey(
        to="eczmark.User",
        verbose_name="Marker",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    question = models.ForeignKey(
        to="eczmark.Question", verbose_name="Question",
        help_text="Select the question to be answered",
        on_delete=models.CASCADE,
        null=True, blank=True,
    )
    attachments = models.ManyToManyField(
        to="eczmark.Attachment",
        verbose_name="Supporting images",
        blank=True,
    )
    links = models.ManyToManyField(
        to="eczmark.Link",
        verbose_name="Supporting link",
        blank=True,
    )
    body = models.TextField(
        null=True,
        blank=False,
        validators=[
            MinLengthValidator(50),
            MaxLengthValidator(1200),
        ],
    )
    
    def __str__(self):
        if self.user:
            full_name = f"{self.user.first_name} {self.user.last_name}"
            return full_name
        else:
            return self.user.username
