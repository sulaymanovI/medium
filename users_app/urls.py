from django.urls import path ,include
from .views import RegisterView,LoginAPIView,LogoutAPIView,ProfileView,BlogViewSet,DeleteProfileView
from rest_framework_simplejwt.views import TokenRefreshView
from rest_framework import routers

router=routers.SimpleRouter()
router.register(r'blog' , BlogViewSet)

urlpatterns = [
    path('register/' , RegisterView.as_view() , name='register'),
    path('login/' , LoginAPIView.as_view() , name='login'),
    path('logout/' , LogoutAPIView.as_view() , name='logout'),
    path('api/token/refresh/', TokenRefreshView.as_view() , name='token_refresh'),
    path('add-profile/' , ProfileView.as_view() , name='add profile'),
    path('delete-profile/<int:pk>/' , DeleteProfileView.as_view() ,name='delete-profile')
] + router.urls
