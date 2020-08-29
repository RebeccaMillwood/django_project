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
    image = models.TextField(default="https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/golden-retriever-royalty-free-image-506756303-1560962726.jpg")
    
    @property
    def ret_image(self):
        if self.image.startswith("http"):
            return self.image
        return "https://picsum.photos/600"