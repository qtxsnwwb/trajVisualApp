from .models import UserModel
from rest_framework import serializers


# 自定义登录/注册序列化器
class UserSerializers(serializers.ModelSerializer):
    """用户信息序列化类型"""
    class Meta:
        model = UserModel      # 关联数据模型
        fields = '__all__'     # 关联所有字段属性
