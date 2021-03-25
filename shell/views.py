#coding:UTF-8
from django.shortcuts import render,HttpResponse
import paramiko
import time
import random
import pymssql
import socket
from django.contrib.admin.views.decorators import staff_member_required
# Create your views here.
cmd=''
def index(request):

    print(request.GET['name'])
    context={}

    context['name']=request.GET['name']
    cmd=context['name']
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy)
    ssh.connect(hostname='10.10.12.94', port=22, username='root', password='sanquan123*')
    stdin, stdout, stderr = ssh.exec_command(request.GET['name'])
    data=stdout.read().decode('utf-8')
    data1=stdout.read()
    print(data)
    ssh.close()
    content={}
    if  data=='':
        content['result']='输入错误'
    else:
        content['result']=data
    return render(request,'index.html',content)
def linux(request):
    print(request.GET['name'])
    content = {}
    content['name'] = request.GET['name']
    ssh = paramiko.Transport('10.10.12.94', 22)
    ssh.start_client()
    ssh.auth_password('root', 'sanquan123*')
    channel = ssh.open_session()
    channel.get_pty()

    # ssh.connect(hostname='10.10.12.94',port=22,username='root',password='sanquan123*')
    channel.invoke_shell()
    time.sleep(1)
    print(channel.recv(1024).decode())
    # time.sleep(1)
    while True:
        cmd = content['name']
        channel.send(cmd + '\n')
        if cmd == 'exit':
            channel.close()
            ssh.close()
            break
        time.sleep(1)
        # while channel.recv_ready():
        # print(result.decode())
        result = channel.recv(65535)
        data = result.decode().strip(cmd).strip()
        # data_list=data.split('RX bytes:')
        # download=data_list[1].split(' ')[0]
        content['result'] = data
        return render(request, 'index.html', content)
        # break

def socket_conn(request):
    return render(request,'socket.html')
def post(request):
    return render(request,'upload.html')
def check(request):
    
    return render(request,'checkinout.html')
check=staff_member_required(check)#验证用户是否登录
def checkinout(request):
    data=request.POST
    print(data)
    if data['name']=='' or data['time']=='' or data['local']=='':
        return render(request,'error.html')
    userinfo={
        '王玮':'428',
        '谢静':'65'
    }
    sn={
        '图书馆':'3696160800099',
        '教学楼':'3696160100158',
        '餐厅':'3696160100178',
        '基础楼':'3696160100198',
        '行政楼西':'3696160800064',
        '行政楼南': '3696160800072',
        '行政楼北':'ACL9183460256',
        '闻德礼堂':'AB7S174760063',
        '新乡校区':'3696160100155'
    }
    name=userinfo[data['name']]
    time=data['time']
    local=sn[data['local']]
    date=time.split('T')
    print(date)
    ran1=random.randint(0,5)
    ran2=random.randint(0,5)
    sec=':'+(str(ran1)+str(ran2))
    print(sec)
    checktime=date[0]+' '+date[1]+sec+':000'
    print(checktime)
    try:
        sqlserver(name,checktime,local)
        return HttpResponse("下不为例哦")
    except Exception as e:
        return HttpResponse(e)
def sqlserver(userid,time,local):
    host='10.10.10.43'
    user='sa'
    password='sa123!@#$'
    database='kaoqin2'
    sql="INSERT INTO checkinout (userid,checktime,checktype,verifycode,sensorid,WorkCode,sn) VALUES (%s,'%s','I',16,1,'0',%s)" %(userid,time,local)
    # sql="select * from checkinout where userid = %s ORDER BY checktime DESC" %'326'
    conn = pymssql.connect(host, user, password, database)
    cursor=conn.cursor()
    cursor.execute(sql)
    # cursor.close()
    # conn.close()
    conn.commit()
    cursor.close()
    conn.close()
