from django.test import TestCase
from .models import Profile, Post


# Create your tests here.
class ProfileTestClass(TestCase):
    def setUp(self):
        self.profile = Profile(user='James Mutahi', name = 'Jamoh007', profile_pic = 'james.png')
        self.profile.save()

    def tearDown(self):
        Profile.objects.all().delete()

    def test_instance(self):
        self.assertTrue(isinstance(self.profile, Profile))

