from pyexpat import model
from django.db import models

# Create your models here.
class Feed(models.Model):
    content=models.TextField()          #글내용
    image=models.TextField()            #피드 이미지
    email=models.EmailField(default='')           #글쓴이
    # profile_image=models.TextField()    #프로필이미지
    # user_id=models.TextField()          #피드ID(글쓴이)
    # like_count=models.IntegerField(default=2)    #좋아요 수

class Like(models.Model):
    feed_id=models.IntegerField(default=0)   #좋아요 수
    email=models.EmailField(default='')         #좋아요를 누른 사람
    is_like=models.BooleanField(default=True)   #좋아하는 가?

class Reply(models.Model):
    feed_id=models.IntegerField(default=0)   #좋아요 수
    email=models.EmailField(default='')         #좋아요를 누른 사람
    reply_content=models.TextField()

class BookMark(models.Model):
    feed_id=models.IntegerField(default=0)   #좋아요 수
    email=models.EmailField(default='')         #좋아요를 누른 사람
    is_marked=models.BooleanField(default=True)
