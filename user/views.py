from email import message
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.views import Response
from .models import User
from django.contrib.auth.hashers import make_password,check_password


# Create your views here.
class Join(APIView):
    def get(self,request):
        
        return render(request,"user/join.html")#./user/join.html
    def post(self,request):
        # TODO 회원가입
        email=request.data.get('email',None)
        nickname=request.data.get('nickname',None)
        name=request.data.get('name',None)
        password=request.data.get('password',None)

        User.objects.create(email=email,
                            nickname=nickname,
                            name=name,
                            password=make_password(password),
                            #장고안에 있는 hash모듈을 이용해 패스워드를 암호화한다.
                            profile_image="default_profile.jpg")
        return Response(status=200)

class Login(APIView):
    def get(self,request):
        return render(request,"user/login.html")

    def post(self,request):
        # TODO 로그인
        email=request.data.get('email',None)
        password=request.data.get('password',None)


        user=User.objects.get(email=email)

        #로그인이 됬을 때
        if check_password(password, user.password):
            #세션을 email로 지정
            request.session['email']=email
            return Response(status=200)
            
        #회원 정보가 잘못됬을 때
        else:
            return Response(status=400,data=dict(message="회원정보가 잘못되었습니다."))

#로그아웃(세션 지우기)
class LogOut(APIView):
    def get(self,request):
        request.session.flush()
        return render(request,"user/login.html")
