from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser


class User(AbstractBaseUser):
    '''
    -유저 프로필 사진
    -유저 ID(닉네임(화면표시))
    -유저 이름(실제 사용자 이름)
    -유저이메일 주소(회원가입할 때 사용하는 아이디)
    -유저 비밀번호->default

    '''
    profile_image=models.TextField()                   #프로필이미지
    nickname=models.CharField(max_length=24,unique=True)          #유저ID(닉네임)
    name=models.CharField(max_length=24)
    email=models.EmailField(unique=True)

    USERNAME_FIELD='nickname'


    #테이블 이름을 정하는 클래스
    class Meta:
        db_table="User"
        
