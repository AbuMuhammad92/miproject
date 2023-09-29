from rest_framework import generics
from .models import User
from .serializers import UserSerializer
from django.http import HttpResponse


def index(request):
    return HttpResponse("Добро пожаловать на мой тестовый сайт!")


class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer