from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Feed
from user.models import User
from uuid import uuid4
import os
from InstaProject.settings import MEDIA_ROOT


# Create your views here.
class Main(APIView):
    def get(self,request):
        feed_list=Feed.objects.all().order_by('-id') #models.py에 있는 Feed의 모든객체를 feed_list에 할당
                                    #order_by-> id를 역순으로 가져옴
        email=request.session.get('email')
        #print('로그인 한 사람: ',request.session.get('email'))
        
        #로그인을 안한 상태로 main을 들어왔을 때(회원정보가 없을때)
        if email is None:
            return render(request,"user/login.html")

        user=User.objects.filter(email=email).first()
        # #이메일 주소가 회원이 아닐때
        if user is None:
            return render(request,"user/login.html")

        return render(request,"InstaProject/main.html",context=dict(feeds=feed_list,user=user))     #feed_list는 키:값 형태의 딕션너리형태로 지정
        
class UploadFeed(APIView):
    def post(self,request):

        #파일 불러오는 코드
        file=request.FILES['file']
        uuid_name=uuid4().hex        #이미지파일을 서버로 저장하기위해 이미지 주소를 16진수로 변환 하는 작업
        save_path=os.path.join(MEDIA_ROOT,uuid_name)    #저장경로는 settigs.py에 있는 MEDIA_ROOT를 통해 uuid_name으로 /media에 저장

        #파일을 실제로 저장하는 코드
        with open(save_path,'wb+') as destination:
            for chunk in file.chunks():
                destination.write(chunk)

        image=uuid_name
        content=request.data.get('content')
        user_id=request.data.get('user_id')
        profile_image=request.data.get('profile_image')
       
        Feed.objects.create(image=image,content=content,user_id=user_id,profile_image=profile_image,like_count=0)

        #http 응답코드 200은 성공
        return Response(status=200)

class Profile(APIView):
    def get(self,request):
        email=request.session.get('email')
        #print('로그인 한 사람: ',request.session.get('email'))
        
        #로그인을 안한 상태로 main을 들어왔을 때(회원정보가 없을때)
        if email is None:
            return render(request,"user/login.html")

        user=User.objects.filter(email=email).first()
        # #이메일 주소가 회원이 아닐때
        if user is None:
            return render(request,"user/login.html")

        return render(request,"content/profile.html",context=dict(user=user,email=email))