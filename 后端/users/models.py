from django.db import models


class UserModel(models.Model):
    userName = models.CharField(verbose_name="用户名", max_length=30)
    userPass = models.CharField(verbose_name="密码", max_length=30)

    class Meta:
        db_table = "user"
        verbose_name = "用户信息"
        verbose_name_plural = verbose_name
