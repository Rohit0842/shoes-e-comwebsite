from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Profile
from django.conf import settings


# This signal creates a profile when a new user is created
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        # Automatically create a Profile for the newly created user
        Profile.objects.create(user=instance)


# This signal ensures the user's profile is saved if there are changes to it
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def save_user_profile(sender, instance, **kwargs):
    # Ensure the profile is saved if any updates are made to the user
    if hasattr(instance, 'profile'):  # Check if the profile exists
        instance.profile.save()
