from django import forms
from django.contrib.auth.forms import (
    UserCreationForm,
    UserChangeForm
)

from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ['username', 'email']


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ['username', 'first_name', 'last_name', 'email', 'location', 'about_me', 'favourite_dog_breed', 'favourite_cupcake_flavour']



