from django.db import models
from django.utils import timezone
# Create your models here.
class Profile(models.Model):
    user = models.TextField()
    name = models.TextField(default="Anonymous")
    profile_pic = models.ImageField(upload_to='users/', default='users/user.png')
    bio = models.TextField(default="Welcome Me!")

class Post(models.Model):
    image = models.ImageField(upload_to='posts/')
    user = models.ForeignKey(Profile)
    caption = models.TextField()
    dateTime = models.DateTimeField(default = timezone.now)