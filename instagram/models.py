from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from tinymce.models import HTMLField
from django.dispatch import receiver
from django.db.models.signals import post_save
from PIL import Image


# Create your models here.

class Post(models.Model):
    image = models.ImageField(upload_to='posts/')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    caption = HTMLField()
    post_date = models.DateTimeField(default=timezone.now)

    @property
    def get_comments(self):
        return self.comments.all()

    @property
    def count_likes(self):
        return self.photolikes.count()

    class Meta:
        ordering = ["-pk"]


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    name = models.TextField(default="Anonymous")
    image = models.ImageField(upload_to='profile_pics/', default='profile_pics/default.jpg')
    bio = models.TextField(default="Welcome Me!")

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()

    @classmethod
    def find_profile(cls, name):
        return cls.objects.filter(user__username__icontains=name).all()

    def togglefollow(self, profile):
        if self.following.filter(followee=profile).count() == 0:
            Follows(followee=profile, follower=self).save()
            return True
        else:
            self.following.filter(followee=profile).delete()
            return False

    def like(self, photo):
        if self.mylikes.filter(photo=photo).count() == 0:
            Likes(photo=photo, user=self).save()

    def save_image(self, photo):
        if self.saves.filter(photo=photo).count() == 0:
            Saves(photo=photo, user=self).save()
        else:
            self.saves.filter(photo=photo).delete()

    def unlike(self, photo):
        self.mylikes.filter(photo=photo).all().delete()

    def post(self, form):
        image = form.save(commit=False)
        image.user = self
        image.save()

    @property
    def follows(self):
        return [follow.followee for follow in self.following.all()]


class Likes(models.Model):
    user = models.ForeignKey(Profile, related_name='mylikes')
    photo = models.ForeignKey(Post, related_name='photolikes')


class Saves(models.Model):
    user = models.ForeignKey(Profile, related_name='saves')
    photo = models.ForeignKey(Post)

    class Meta:
        ordering = ["-pk"]


class Follows(models.Model):
    follower = models.ForeignKey(Profile, related_name='following')
    followee = models.ForeignKey(Profile, related_name='followers')
