from django.db import models
from django.contrib.auth.models import AbstractUser 
from django.utils import timezone
from .managers import CustomUserManager
from rest_framework_simplejwt.tokens import RefreshToken

class User(AbstractUser):
    email=models.EmailField(verbose_name='Email' ,  max_length=60 , unique=True)
    username=models.CharField(max_length=30, blank=True, null=True)
    birth_date=models.DateField(blank=True , null=True)
    USERNAME_FIELD='email'
    REQUIRED_FIELDS=[]

    objects=CustomUserManager()

    def __str__(self) -> str:
        return self.email

    def tokens(self):
        refresh = RefreshToken.for_user(self)
        return{
            'refresh':str(refresh),
            'access':str(refresh.access_token)
        }
    
class Profile(models.Model):
    user=models.OneToOneField(to=User , on_delete=models.CASCADE)
    first_name=models.CharField(verbose_name='Ism' , max_length=50)
    last_name=models.CharField(verbose_name='Familiya' , max_length=50)
    birth_date=models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Kodning so'rov vaqti")
    
    def full_name(self):
        return self.first_name + " " + self.last_name if self.first_name and self.last_name else self.user.email
    
    def __str__(self) -> str:
        return self.full_name() + "'s Profile" if self.first_name and self.last_name else self.user.email

class Blog(models.Model):
    author=models.ForeignKey(to=Profile, on_delete=models.CASCADE)
    title=models.CharField(max_length=200)
    content=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
