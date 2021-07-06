from django.http import HttpResponse
# from django.shortcuts import render
# from rest_framework.response import Response
# from rest_framework.views import APIView
from .serializers import *
from .models import UserModel


def login(request):
    """
    登录视图
    :param request:
    :return:
    """
    userName = request.POST.get("userName")
    userPass = request.POST.get("userPass")

    result = UserModel.objects.filter(userName=userName, userPass=userPass).first()
    if result is not None:
        return HttpResponse("success")
    # serializers = UserSerializers(result)
    return HttpResponse("error")

# 用户视图集
# class UserView(APIView):
#
#     def get(self, request):
#         """
#         登录视图
#         :param request:
#         :return:
#         """
#         userName = request.GET.get("userName")
#         userPass = request.POST.get("userPass")
#         print(userName, userPass)
#         obj = UserModel.objects.filter(userName=userName, userPass=userPass).first()
#         print(obj)
#         print(type(obj))
#         print(obj.userName)
#         print(obj.userPass)
#         return Response("success")