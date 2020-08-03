from django.urls import path,include
from .views import movieinfo

urlpatterns = [
    path('index/',movieinfo),
]