from django.db.models import Q
from django.dispatch import receiver
from django.db.models.signals import (
    post_save,
    pre_save,
)

from django.db.models.signals import (
    post_save
)
from django.db.models import Q
from django.dispatch import receiver

from eczmark.models import (
    User,
    Profile,
)

def user_profile_validator(user, profile):
    if not user.profile:
        user.profile = profile
        user.save()
        return
    return


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, *args, **kwargs):
    if created:
        user_profile = Profile.objects.create(
            user_id=instance.pk,
            email=instance.email,
        )
        user_profile_validator(user=instance, profile=user_profile)
