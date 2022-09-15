from django.urls import path
from content.views import UploadFeed,Profile,Main,UploadReply,TogleLike,TogleBookmark

urlpatterns = [
    path('upload',UploadFeed.as_view()),
    path('reply',UploadReply.as_view()),
    path('profile',Profile.as_view()),
    path('main',Main.as_view()),
    path('like',TogleLike.as_view()),
    path('bookmark',TogleBookmark.as_view()),
]
