from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    ROLE_CHOICES = [
        ('student', 'Student'),
        ('instructor', 'Instructor'),
        ('admin', 'Admin'),
    ]
    # Default to 'student' for new user sign-ups
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='student')

    email = models.EmailField(unique=True)

    def __str__(self):
        return self.username
