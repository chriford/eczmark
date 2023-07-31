from django.db import models

from eczmark.models.abstract import Timestamp
from django.core.validators import MaxLengthValidator, MinLengthValidator


class Question(Timestamp):
    """A model containing the meta data of the question paper uploaded."""
    user = models.ForeignKey(
        to="eczmark.User", verbose_name="Marker",
        on_delete=models.SET_NULL,
        null=True, blank=True,
    )
    question_paper = models.FileField(upload_to='question-papers/-%H-%M-%S-%m/', null=True, blank=False)
    grade = models.ForeignKey(
        to="eczmark.Grade",
        verbose_name="Grade",
        help_text="Select the grade to which this question paper belong",
        on_delete=models.PROTECT,
        null=True,
        blank=False,
    )
    year_uncleaned = models.DateField(
        verbose_name="Question paper year",
        help_text="Enter any date containing the same year as the question paper selected.",
        null=True,
        blank=False,
    )
    year_cleaned = models.CharField(
        default="0000",
        null=True,
        blank=True,
        validators=[
            MinLengthValidator(limit_value=4),
            MaxLengthValidator(limit_value=4),
        ]
    )
    subject = models.ForeignKey(
        to="eczmark.Subject",
        on_delete=models.SET_NULL,
        null=True,
        blank=False,
    )

    def save(self):
        unprocessed_year = self.year_uncleaned
        if unprocessed_year:
            self.year_cleaned = unprocessed_year.year
        else:
            raise ValueError("Expected a value for the field 'Question paper year'")
        return super().save()
