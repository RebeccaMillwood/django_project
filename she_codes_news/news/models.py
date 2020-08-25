from django.db import models
from django.contrib.auth import get_user_model


class NewsStory(models.Model):
    title = models.CharField(max_length=200)
    # author = models.CharField(max_length=200)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE
        # ^ if we delete the user, it will also delete their stories
    )
    pub_date = models.DateTimeField()
    content = models.TextField()
    image = models.FileField(upload_to='uploads')
    