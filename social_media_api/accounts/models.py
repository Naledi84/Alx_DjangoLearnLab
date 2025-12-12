from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """
    Custom user model for the Social Media API.
    """

    bio = models.TextField(blank=True, null=True)

    # Profile image (optional)
    profile_image = models.ImageField(upload_to='profiles/', blank=True, null=True)

    # Users THIS user follows
    following = models.ManyToManyField(
        'self',
        symmetrical=False,
        related_name='followers',  # users who follow this user
        blank=True
    )

    def __str__(self):
        return self.username


