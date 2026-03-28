"""
apps/accounts/models.py

Custom User model. This is the foundation — always define a custom user
model at the start of a project. Changing it later is painful.

To use: AUTH_USER_MODEL = 'accounts.CustomUser' in settings/base.py
"""

from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    """
    Extends Django's built-in User with:
    - A profile picture field
    - A bio field
    - A role field (customize roles to fit your project)

    When cloning this starter:
    1. Update ROLE_CHOICES to match your project's user types
    2. Add or remove fields as needed
    3. Run: python manage.py makemigrations && python manage.py migrate
    """

    # ── Roles ──────────────────────────────────────────────────────────
    # Customize these for each project
    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('staff', 'Staff'),
        ('user', 'User'),
    ]

    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES,
        default='user',
    )

    # ── Profile fields ──────────────────────────────────────────────────
    bio = models.TextField(blank=True)

    profile_picture = models.ImageField(
        upload_to='profiles/',
        null=True,
        blank=True,
    )

    # ── Helper methods ──────────────────────────────────────────────────
    def get_full_name_or_username(self):
        """Returns full name if set, otherwise username."""
        full_name = self.get_full_name()
        return full_name if full_name.strip() else self.username

    def get_role_display_name(self):
        """Returns the human-readable role label."""
        return dict(self.ROLE_CHOICES).get(self.role, self.role)

    # ── Role check helpers (add more as needed per project) ─────────────
    @property
    def is_admin_user(self):
        return self.role == 'admin'

    @property
    def is_staff_user(self):
        return self.role == 'staff'

    def __str__(self):
        return f"{self.username} ({self.get_role_display_name()})"
