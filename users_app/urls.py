from django.urls import path ,include
from .views import RegisterView,LoginAPIView,LogoutAPIView,ProfileView
from rest_framework_simplejwt.views import TokenRefreshView
from rest_framework import routers

router=routers.SimpleRouter()
router.register(r'profile' , ProfileView)

urlpatterns = [
    path('register/' , RegisterView.as_view() , name='register'),
    path('login/' , LoginAPIView.as_view() , name='login'),
    path('logout/' , LogoutAPIView.as_view() , name='logout'),
    path('api/token/refresh/', TokenRefreshView.as_view() , name='token_refresh'),
] + router.urls
