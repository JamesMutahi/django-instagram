from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from tinymce.models import HTMLField

# Create your models here.
class Profile(models.Model):
    user = models.TextField()
    name = models.TextField(default="Anonymous")
    profile_pic = models.ImageField(upload_to='users/', default='users/user.png')
    bio = models.TextField(default="Welcome Me!")

class Post(models.Model):
    image = models.ImageField(upload_to='posts/')
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    caption = HTMLField()
    post_date = models.DateTimeField(default = timezone.now)

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()