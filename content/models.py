from pyexpat import model
from django.db import models

# Create your models here.
class Feed(models.Model):
    content=models.TextField()          #글내용
    image=models.TextField()            #피드 이미지
    profile_image=models.TextField()    #프로필이미지
    user_id=models.TextField()          #피드ID(글쓴이)
    like_count=models.IntegerField()    #좋아요 수
