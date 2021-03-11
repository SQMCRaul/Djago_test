#coding:utf-8
import os,os.path
from django.shortcuts import render,HttpResponse
from .models import UploadFileForm
from django.http import request
import django.http.request
def upload(request):

    return render(request,'upload.html')
def upload_file(request):
    file = request.FILES['file']
    # print(os.path.split(file))
    print(request.FILES)
    post=request.POST
    print(post)
    # form = UploadFileForm(request.POST, request.FILES)
    # with open('some/file/name.txt', 'wb+') as destination:
    #     for chunk in file.chunks():
    #         destination.write(chunk)
    print(type(file))
    #
    with open('./upload.jpg','wb+') as f:
        for chunk in file.chunks():

            f.write(chunk)
            print('ok')
    return HttpResponse('上传成功')