#coding:utf-8
from shell import models
from django.shortcuts import render,HttpResponse

def get_host(request):
    rs=models.Host.objects.all()
    print(rs)

