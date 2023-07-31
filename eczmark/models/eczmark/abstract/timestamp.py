from django.db import models

class Timestamp(models.Model):
    """A model to be inheritted by other models: contains fields; date created, date updated."""
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=False)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=False)

    def __str__(self):
        return f"{self.created_at}"
    
    class Meta:
        abstract = True
