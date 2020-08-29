from django.db import models

# # Create your models here.

from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    # this is where i would put custom fields, e.g. profile picture
    # pass
    bio = models.TextField(max_length=500, blank=True)

    def __str__(self):
        # return f'{self.username} Profile'
        return self.username

