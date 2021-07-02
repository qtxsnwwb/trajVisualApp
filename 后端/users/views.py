from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework_mongoengine import generics
from rest_framework.response import Response
from rest_framework import status
from .serializers import *
from .models import UserModel

# Create your views here.

# def login(request):
#     userName = request.POST.get("userName")
#     userPass = request.POST.get("userPass")
#     print(userName, userPass)
#
#     return  HttpResponse("success")

# 登录视图
class LoginView(APIView):
    def post(self, request):
        data = request.data
        serializer = UserSerializers(UserModel.objects.all(), many=True)
        print(serializer.data)
        return Response("success", status=status.HTTP_200_OK)
