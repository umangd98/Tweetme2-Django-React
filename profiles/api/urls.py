from django.urls import path
from .views import  user_follow_view
from django.conf.urls.static import static
from django.conf import settings

# Base endpoint /api/profile

urlpatterns = [

    path('<str:username>/follow', user_follow_view),


]
