from django.urls import path, include
from rest_framework import routers
from . import views


app_name = 'users'
# router = routers.DefaultRouter()       # 定义默认的路由对象
# router.register(r'users', views.login)
urlpatterns = [
    # path(r'', include('users.urls'))
    path(r'userLogin/', views.LoginView),
]