from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField
# Create your models here.
class Profile(models.Model):
    profile_photo= models.ImageField(upload_to = 'articles/', blank = True)
    bio=models.CharField(max_length =50)
    username = models.CharField(max_length=30, blank=True)
    user_id = models.IntegerField(default=0)

    def __str__(self):
        return self.bio
    def save_profile(self):
        self.save()
