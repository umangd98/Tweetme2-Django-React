from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib.auth import get_user_model
from django.http import HttpResponse, Http404, JsonResponse
from ..models import Profile
from django.utils.http import is_safe_url
import random
ALLOWED_HOSTS = settings.ALLOWED_HOSTS
from rest_framework import response
from rest_framework.authentication import SessionAuthentication
from rest_framework.decorators import api_view,permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
# Create your views here.
User = get_user_model()

@api_view(['GET','POST'])
@permission_classes([IsAuthenticated])
def user_follow_view(request,username, *args, **kwargs):
  current_user = request.user
  to_follow_user = User.objects.filter(username=username)
  if not to_follow_user.exists():
    return response.Response({}, status=400)
  other = to_follow_user.first()
  profile = other.profile
  data = {}
  try:
    data = request.data
  except:
    pass
  print(data)
  action = data.get("action")
  if action == "follow":
    profile.followers.add(current_user)
  elif action == "unfollow":
    profile.followers.remove(current_user)
  else: 
    pass
  # if current_user in profile.followers.all():
  #   profile.followers.remove(current_user)
  # else:
  #   profile.followers.add(current_user)
  current_followers_qs = profile.followers.all()
  return response.Response({"followers_count": current_followers_qs.count(), "user": profile.user.username}, status=200)

