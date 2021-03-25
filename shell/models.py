# coding:utf-8
from django.db import models
import datetime
from django.utils import timezone
# Create your models here.
from django import forms
from shell.utils import zabbix
import random

token=zabbix.get_token('Admin','zabbix')
#只是创建一个菜单的链接
class Monitor(models.Model):
    class Meta:
        managed=False
        permissions=(("monitor.monitor","can view monitor"),)

class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField()

class Department(models.Model):
    name=models.CharField(max_length=20,verbose_name="部门名称")
    manager=models.CharField(max_length=10,verbose_name="管理员")
    def __str__(self):
        return self.name
    class Meta:
        verbose_name="部门"
        verbose_name_plural="部门"


class CampusFiled(models.Model):
    name=models.CharField(max_length=10,verbose_name="校区")
    def __str__(self):
        return self.name
    class Meta:
        verbose_name="校区"
        verbose_name_plural="校区"


class Host(models.Model):
    host_name=models.CharField(max_length=100,verbose_name="主机名称")
    ip=models.CharField(max_length=20,verbose_name="IP地址")
    campus_filed=models.ForeignKey(CampusFiled,on_delete=models.CASCADE,verbose_name="校区")
    system=models.CharField(max_length=10,verbose_name="系统类型")
    host_model=models.CharField(max_length=20,verbose_name="型号")
    price=models.IntegerField(verbose_name="价格")
    buy_date=models.DateField(default=timezone.now,verbose_name="购置日期")
    app=models.CharField(max_length=20,verbose_name="应用名称")
    department=models.ForeignKey(Department,on_delete=models.CASCADE,verbose_name="所属部门")
    def __str__(self):
        return self.host_name
    class Meta:
        verbose_name="主机"
        verbose_name_plural="主机"
