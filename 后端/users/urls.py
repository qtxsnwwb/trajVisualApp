from django.urls import path, include
from rest_framework import routers
from . import views


app_name = 'users'
# router = routers.DefaultRouter()       # 定义默认的路由对象
# router.register(r'userLogin', views.UserViewSet)      # 注册用户视图集
urlpatterns = [
    # path(r'', include(router.urls))       # 添加路由映射关系
    path(r'userLogin/', views.login),
]