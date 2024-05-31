from django.db import models
from versatileimagefield.fields import VersatileImageField,PPOIField
from users_app.models import Profile
from medium_project import settings

class UploadImage(models.Model):
    file=models.FileField(upload_to="blog_images/" )

class Blog(models.Model):
    author=models.ForeignKey(Profile, on_delete=models.CASCADE)
    title=models.CharField(max_length=200)
    content=models.TextField()
    images = models.ManyToManyField(UploadImage)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

