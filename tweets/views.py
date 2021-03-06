from django.shortcuts import render, redirect
from django.conf import settings
from django.http import HttpResponse, Http404, JsonResponse
from django.utils.http import is_safe_url
import random
ALLOWED_HOSTS = settings.ALLOWED_HOSTS

# Create your views here.
def home_view(request):
  userName = None
  if request.user.is_authenticated:
    username = request.user.username
  return render(request, 'pages/home.html', context={}, status=200)

def tweets_list_view(request):
  return render(request, 'tweets/list.html')

def tweets_detail_view(request, tweet_id):
  return render(request, 'tweets/detail.html', context={"tweet_id":tweet_id})

# def tweets_profile_view(request, username):
  # return render(request, 'tweets/profile.html', context={"profile_username": username})



# def tweet_list_view_pure_django(request, *args, **kwargs):
#   qs = Tweet.objects.all()
#   # tweets_list = [{"id": x.id, "content": x.content, "likes": random.randint(0,123)} for x in qs]
#   tweets_list = [x.serialize() for x in qs]
#   data = {
#     "response": tweets_list
#   }
#   return JsonResponse(data)



# def tweet_create_pureDjango(request, *args, **kwargs):
#   user = request.user
#   if not request.user.is_authenticated:
#     user = None
#     if request.is_ajax():
#       return JsonResponse({}, status=401)
#     return redirect(settings.LOGIN_URL)
#   # print("ajax",request.is_ajax())
#   form = TweetForm(request.POST or None)
#   next_url = request.POST["next"] or None
#   if form.is_valid():
#     obj = form.save(commit=False)
#     obj.user = user
#     obj.save()
#     if request.is_ajax():
#       return JsonResponse(obj.serialize(), status=201)
#     if next_url != None and is_safe_url(next_url, ALLOWED_HOSTS):
#       return redirect(next_url)
#     form = TweetForm()
#   if form.errors:
#     if request.is_ajax():
#       return JsonResponse(form.errors, status=400)
#   return render(request, 'components/form.html', context={"form":form})

# def tweet_detail_view_pure_django(request,tweet_id, *args, **kwargs):
#   data = {
#     "id": tweet_id, 
#   }
#   status = 200
#   try:
#     obj = Tweet.objects.get(id=tweet_id)
#     data['content'] = obj.content
#   except:
#     data['message'] = "not found"
#     status = 404
  
#   return JsonResponse(data, status=status)
