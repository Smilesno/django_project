from django.shortcuts import render
from rest_framework.generics import GenericAPIView, CreateAPIView

# Create your views here.

class UserView(CreateAPIView):
    serializer_class = CreateUserSerializer

