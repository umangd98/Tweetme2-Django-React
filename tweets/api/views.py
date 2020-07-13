from django.shortcuts import render, redirect
from django.conf import settings
from django.http import HttpResponse, Http404, JsonResponse
from ..models import Tweet
from django.utils.http import is_safe_url
import random
from ..forms import TweetForm
from ..serializers import TweetSerializer, TweetActionSerializer,TweetCreateSerializer
ALLOWED_HOSTS = settings.ALLOWED_HOSTS
from rest_framework import response
from rest_framework.authentication import SessionAuthentication
from rest_framework.decorators import api_view,permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination
# Create your views here.

def get_paginated_queryset_response(qs, request):
  paginator = PageNumberPagination()
  paginator.page_size = 20
  paginated_qs = paginator.paginate_queryset(qs, request)
  serializer = TweetSerializer(paginated_qs, many=True)
  # return response.Response(serializer.data)
  return paginator.get_paginated_response(serializer.data)

@api_view(['GET'])
def tweet_list_view(request, *args, **kwargs):
  qs = Tweet.objects.all()
  username = request.GET.get('username')
  if username != None:
    qs = qs.by_username(username)
  return get_paginated_queryset_response(qs,request)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def tweet_feed_view(request, *args, **kwargs):
  user = request.user
  qs = Tweet.objects.feed(user)
  return get_paginated_queryset_response(qs,request)


@api_view(['GET'])
def tweet_detail_view(request,tweet_id, *args, **kwargs):
  qs = Tweet.objects.get(id=tweet_id)
  if not qs:
    return response.Response({}, status=404)
  serializer = TweetSerializer(qs)
  return response.Response(serializer.data)

@api_view(['DELETE','POST'])
@permission_classes([IsAuthenticated])
def tweet_delete_view(request,tweet_id, *args, **kwargs):
  qs = Tweet.objects.filter(id=tweet_id)
  if not qs.exists():
    return response.Response({}, status=404)
  qs = qs.filter(user=request.user)
  if not qs.exists():
    return response.Response({"message":"You cannot delete it"}, status=401)
  obj = qs.first()
  obj.delete()
  return response.Response({"message":"Tweet removed"}, status=200)


@api_view(['POST'])
# @authentication_classes([SessionAuthentication])
@permission_classes([IsAuthenticated])
def tweet_create(request, *args, **kwargs):
  data = request.data 
  serializer = TweetCreateSerializer(data=data)
  if serializer.is_valid(raise_exception=True):
    serializer.save(user=request.user)
    return response.Response(serializer.data, status=201)
  return response.Response({}, status=400)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def tweet_action_view(request, *args, **kwargs):
  "id is required. Action options are: like, unlike, retweet."
  serializer = TweetActionSerializer(data=request.data)
  if serializer.is_valid(raise_exception=True):
    data = serializer.validated_data
    tweet_id = data.get("id")
    action= data.get("action")
    content = data.get("content")
  qs = Tweet.objects.filter(id=tweet_id)
  if not qs.exists():
    return response.Response({}, status=404)
  obj = qs.first()
  if action == "like":
    obj.likes.add(request.user)
    serializer = TweetSerializer(obj)
    return response.Response(serializer.data, status=200)
  elif action == 'unlike':
    obj.likes.remove(request.user)
    serializer = TweetSerializer(obj)
    return response.Response(serializer.data, status=200)
  elif action == 'retweet':
    parent_obj = obj
    new_tweet = Tweet.objects.create(user=request.user, parent=parent_obj, content=content)
    serializer = TweetSerializer(new_tweet)
    return response.Response(serializer.data, status=201)

  return response.Response({"message":"Tweet removed"}, status=200)



def tweet_list_view_pure_django(request, *args, **kwargs):
  qs = Tweet.objects.all()
  # tweets_list = [{"id": x.id, "content": x.content, "likes": random.randint(0,123)} for x in qs]
  tweets_list = [x.serialize() for x in qs]
  data = {
    "response": tweets_list
  }
  return JsonResponse(data)



def tweet_create_pureDjango(request, *args, **kwargs):
  user = request.user
  if not request.user.is_authenticated:
    user = None
    if request.is_ajax():
      return JsonResponse({}, status=401)
    return redirect(settings.LOGIN_URL)
  # print("ajax",request.is_ajax())
  form = TweetForm(request.POST or None)
  next_url = request.POST["next"] or None
  if form.is_valid():
    obj = form.save(commit=False)
    obj.user = user
    obj.save()
    if request.is_ajax():
      return JsonResponse(obj.serialize(), status=201)
    if next_url != None and is_safe_url(next_url, ALLOWED_HOSTS):
      return redirect(next_url)
    form = TweetForm()
  if form.errors:
    if request.is_ajax():
      return JsonResponse(form.errors, status=400)
  return render(request, 'components/form.html', context={"form":form})

def tweet_detail_view_pure_django(request,tweet_id, *args, **kwargs):
  data = {
    "id": tweet_id, 
  }
  status = 200
  try:
    obj = Tweet.objects.get(id=tweet_id)
    data['content'] = obj.content
  except:
    data['message'] = "not found"
    status = 404
  
  return JsonResponse(data, status=status)
