from django.db import models

# # Create your models here.

from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    # this is where i would put custom fields, e.g. profile picture
    # pass
    first_name = models.TextField(max_length=30, blank=True)
    last_name = models.TextField(max_length=30, blank=True)
    location = models.TextField(max_length=30, blank=True)
    about_me = models.TextField(max_length=500, blank=True)
    favourite_dog_breed = models.TextField(max_length=50, blank=True)
    favourite_cupcake_flavour = models.TextField(max_length=50, blank=True)
    # profile_picture = models.ImageField(blank=True)

    def __str__(self):
        # return f'{self.username} Profile'
        return self.username

