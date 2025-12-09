from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    """
    Custom user model for social media API.
    - bio: short biography text
    - profile_picture: optional image upload (requires Pillow)
    - followers: many-to-many to self to represent followers (symmetrical=False)
    """
    bio = models.TextField(blank=True, null=True)
    # Use ImageField if you want uploads (install pillow). Otherwise change to URLField for image URLs.
    profile_picture = models.ImageField(upload_to='profiles/', blank=True, null=True)

    # Users who follow this user. symmetrical=False so following vs followers are distinct.
    followers = models.ManyToManyField(
        'self',
        symmetrical=False,
        related_name='following',
        blank=True
    )

    def __str__(self):
        return self.username

