# accounts/models.py
from django.db import models

class TempEmail(models.Model):
    email = models.EmailField(unique=True)
    otp = models.CharField(max_length=6)
    verified = models.BooleanField(default=False)

class UserDetails(models.Model):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    password = models.CharField(max_length=128)  # Will store hashed password

    def __str__(self):
        return self.username
