from django.db import models

from eczmark.models.abstract import Timestamp

class Report(Timestamp):
    user = models.ForeignKey(
        to="eczmark.User",
        verbose_name="Marker",
        on_delete=models.SET_NULL,
        default=True,
        null=True,
        blank=True,
    )
    issue = models.ForeignKey(
        to="eczmark.Issue",
        verbose_name="Title",
        on_delete=models.SET_NULL,
        null=True,
        blank=False,
    )
    message = models.TextField(
        max_length=350,
        verbose_name="Message body",
        help_text="Report an issue to the support team",
        null=True,
        blank=False,
    )
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.issue.name
