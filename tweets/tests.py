from django.test import TestCase
from .models import Tweet
from rest_framework.test import APIClient

from django.contrib.auth import get_user_model
User = get_user_model()
# Create your tests here.
class TweetTestCase(TestCase):
  def setUp(self):
    self.user = User.objects.create_user(username='cfe', password='somepassword')
    Tweet.objects.create(content="My 1st Tweet", user=self.user)
    Tweet.objects.create(content="My 2nd Tweet", user=self.user)
    Tweet.objects.create(content="My 3rd Tweet", user=self.user)
  def test_tweet_created(self):
      tweet = Tweet.objects.create(content="My 4nd Tweet", user=self.user)
      self.assertEqual(tweet.id, 4)
      self.assertEqual(tweet.user, self.user)
  def get_client(self):
    client = APIClient()
    client.login(username=self.user.username, password='somepassword')  
    return client
  def test_tweet_list(self):
    client = self.get_client()
    res = client.get("/api/tweets/")
    self.assertEqual(res.status_code, 200)
    # print(res.json())
  def test_tweet_action_like(self):
    client = self.get_client()
    res = client.post("/api/tweets/action", {'id':1, 'action':'like'})
    self.assertEqual(res.status_code, 200)
    print(res.json())

