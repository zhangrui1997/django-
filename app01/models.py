from django.db import models

# Create your models here.

class UserGroup(models.Model):
    uid = models.AutoField(primary_key=True)
    caption = models.CharField(max_length=32)
# app01_userinfo
class UserInfo(models.Model):
    # id列，自增，主键
    # 用户名列：字符串类型，指定长度
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=64)
    email = models.EmailField(max_length=19, null=True)

