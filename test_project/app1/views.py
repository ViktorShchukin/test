from django.shortcuts import render
from django.http import HttpResponse, Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
#from django.contrib.auth.models import User

from app1.models import CustomUser
from app1.serializers import UserSerializer


def index(request):
	return HttpResponse("Hello, world. You're at the polls index.")

class UserList(generics.ListCreateAPIView):
	"""
	List all users or create new
	"""
	queryset = CustomUser.objects.all()
	serializer_class = UserSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
	"""
	Retrieve, update or delete user
	"""
	queryset = CustomUser.objects.all()
	serializer_class = UserSerializer

