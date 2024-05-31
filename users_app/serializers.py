from rest_framework import serializers
from .models import User,Profile
from rest_framework.exceptions import AuthenticationFailed
from django.contrib import auth
from rest_framework.validators import ValidationError

class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=User
        fields=['email']

class RegisterSerializer(serializers.ModelSerializer):
    password=serializers.CharField(max_length=70 , min_length=8 , write_only=True)
    
    class Meta:
        model=User
        fields=['email' , 'password']
    
    def validate(self,attrs):
        email=attrs.get('email' , '')
        if User.objects.filter(email=email).exists():
            raise ValidationError('Email is exists')
        return attrs

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

class LoginSerializer(serializers.ModelSerializer):
    password=serializers.CharField(max_length=70 , min_length=8,write_only=True)
    email=serializers.EmailField(max_length=255 , min_length=3)
    token=serializers.SerializerMethodField()
    
    class Meta:
        model=User
        fields=['password' , 'email' , 'token']

    def get_token(self,obj):
        user=User.objects.get(email=obj ['email'])
        return user.tokens()
    
    def validate(self, attrs):
        email=attrs.get('email' , '')
        password = attrs.get('password' , '')
        user=auth.authenticate(email=email , password=password)
        if not user:
            raise AuthenticationFailed('Invalid credentials, try again')
        if not user.is_active:
            raise AuthenticationFailed('Account disabled , contact again')
        return {
            'email' : user.email,
            'token' : user.tokens()
        } 


class LogoutSerializer(serializers.Serializer):
    refresh=serializers.CharField()

    def validate(self, attrs):
        self.token=attrs['refresh']
        return attrs
    

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model=Profile
        fields=['id','user','first_name','last_name','birth_date']

