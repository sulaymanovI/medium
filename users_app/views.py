from django.shortcuts import get_object_or_404
from rest_framework import generics, status, permissions, viewsets
from rest_framework.response import Response
from .models import Profile,Blog
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .serializers import RegisterSerializer,LoginSerializer,LogoutSerializer,ProfileSerializer,BlogSerializer
from rest_framework_simplejwt.tokens import RefreshToken,TokenError

class RegisterView(generics.GenericAPIView):
    serializer_class=RegisterSerializer
    permission_classes=permissions.AllowAny,

    def post(self, request,*args, **kwargs):
        user=request.data
        serializer=self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        user_data=serializer.data
        return Response(user_data , status=status.HTTP_201_CREATED)

class LoginAPIView(generics.GenericAPIView):
    serializer_class=LoginSerializer
    permission_classes = permissions.AllowAny,

    def post(self,request,*args, **kwargs):
        serializer=self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data , status=status.HTTP_200_OK)

class LogoutAPIView(generics.GenericAPIView):
    serializer_class=LogoutSerializer
    permission_classes=[permissions.IsAuthenticated]

    def post(self,request,*args, **kwargs):
        serializer=self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            RefreshToken(request.data['refresh']).blacklist()
        except TokenError:
            self.fail('bad token')
        return Response(status=status.HTTP_204_NO_CONTENT)


class ProfileView(generics.GenericAPIView):
    serializer_class=ProfileSerializer
    permission_classes=[IsAuthenticated]

    def post(self,request,*args, **kwargs):
        try:
            if Profile.objects.filter(user=request.user).exists():
                raise Exception("Profile exists for this user")
            profile_data = request.data.copy()
            profile_data['user'] = request.user.id
            serializer=self.get_serializer(data=profile_data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response(e.args)

class BlogViewSet(viewsets.ModelViewSet):
    queryset=Blog.objects.all()
    serializer_class=BlogSerializer

class DeleteProfileView(APIView):
    def delete(self, request, pk):
        profile = get_object_or_404(Profile, pk=pk)
        profile.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)