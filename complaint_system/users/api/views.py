from django.contrib.auth import login
from rest_framework import generics
from rest_framework.permissions import AllowAny , IsAuthenticated
from .serializers import UserLoginSerializer , UserRegisterSerializer , UserSerializer
from users.models import User

class Register(generics.GenericAPIView):

	permission_classes = (AllowAny,)
	serializer_class = UserRegisterSerializer
	allowed_methods = ('POST', 'OPTIONS', 'HEAD')

	


class Login(generics.GenericAPIView):

	permission_classes = (AllowAny,)
	serializer_class = UserLoginSerializer
	allowed_methods = ('POST', 'OPTIONS', 'HEAD')

	def login(self):
		self.user = self.serializer.user
		login(self.request, self.user)

   

class CreateAccountView(generics.ListCreateAPIView):
	permission_classes =(IsAuthenticated,)
	queryset = User.objects.all()
	serializer_class = UserSerializer

class DetailAccountView(generics.RetrieveUpdateDestroyAPIView):
	permission_classes =(IsAuthenticated,)
	queryset = User.objects.all()
	serializer_class = UserSerializer

	def get_queryset(self):
		user = self.request.user
		return User.objects.filter(id=user.id)
