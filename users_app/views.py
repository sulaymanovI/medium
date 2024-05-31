from rest_framework import generics, status, permissions, viewsets
from rest_framework.response import Response
from .models import Profile
from .serializers import RegisterSerializer,LoginSerializer,LogoutSerializer,ProfileSerializer
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

class ProfileView(viewsets.ModelViewSet):
    queryset=Profile.objects.all()
    serializer_class=ProfileSerializer

