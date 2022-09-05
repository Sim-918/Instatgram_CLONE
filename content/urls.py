from django.urls import path
from content.views import UploadFeed,Profile

urlpatterns = [
    path('upload',UploadFeed.as_view()),
    path('profile',Profile.as_view()),
]
