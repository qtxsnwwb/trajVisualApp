from rest_framework_mongoengine import serializers
from .models import UserModel

# 自定义登录/注册序列化器
class UserSerializers(serializers.DocumentSerializer):
    class Meta:
        model = UserModel
        fields = '__all__'
