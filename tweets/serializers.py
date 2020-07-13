from rest_framework import serializers
from .models import Tweet
from django.conf import settings
from profiles.serializers import PublicProfileSerializer
TWEET_ACTION_OPTIONS = ["like", "unlike", "retweet"]

class TweetCreateSerializer(serializers.ModelSerializer):
  likes = serializers.SerializerMethodField(read_only=True)
  user = PublicProfileSerializer(source='user.profile',read_only=True)


  class Meta:
    model = Tweet
    fields = ['content','likes','id', 'user', 'timestamp']  
  def get_likes(self, obj):
    return obj.likes.count()
  def validate_content(self, value):
    if len(value) > settings.MAX_LENGTH:
        raise serializers.ValidationError("This tweet is too long")
    return value
  
  # def get_user(self, obj):
  #   return obj.user.id
  
class TweetSerializer(serializers.ModelSerializer):
  # user = serializers.SerializerMethodField(read_only=True)
  user = PublicProfileSerializer(source='user.profile',read_only=True)
  likes = serializers.SerializerMethodField(read_only=True)
  # content = serializers.SerializerMethodField(read_only=True)
  parent = TweetCreateSerializer(read_only=True)
  class Meta:
    model = Tweet
    fields = ['content','likes','id','is_retweet','parent','user','timestamp']  
  def get_likes(self, obj):
    return obj.likes.count()
  # def get_user(self, obj):
  #   return obj.user.id
  # def get_content(self, obj):
  #   content = obj.content
  #   if obj.is_retweet:
  #     content = obj.parent.content
  #   return content

    
class TweetActionSerializer(serializers.Serializer):
  id = serializers.IntegerField()
  action = serializers.CharField()
  content = serializers.CharField(allow_blank=True, required=False)

  def validate_action(self, value):
    value = value.lower().strip()
    if not value in TWEET_ACTION_OPTIONS:
      raise serializers.ValidationError("this is not a valid action for the tweets")
    return value
