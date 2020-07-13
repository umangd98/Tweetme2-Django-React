from django.test import TestCase

# Create your tests here.
from django.contrib.auth import get_user_model
from .models import Profile

User = get_user_model()


class ProfileTestCase(TestCase):
  def setUp(self):
    self.user = User.objects.create_user(username='cfe', password='somepassword')
    self.userb = User.objects.create_user(username='-cfe', password='somepassword')

  def test_profile_created(self):
    qs = Profile.objects.all()
    self.assertEqual(qs.count(), 2)
  
  def test_following(self):
    first = self.user
    second = self.userb
    first_profile = first.profile
    first_profile.followers.add(second)
    second_user_following_whom = second.following.all()
    qs = second_user_following_whom.filter(user=first)
    self.assertTrue(qs.exists())
    


