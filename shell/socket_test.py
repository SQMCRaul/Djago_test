from django.shortcuts import render
import paramiko
import time
from dwebsocket import *
from django.http import HttpResponse
@accept_websocket
def socket_server(request):
    ssh=paramiko.Transport('10.10.12.94',22)
    ssh.connect(username='root',password='sanquan123*')
    shell=ssh.open_session()
    shell.get_pty()
    shell.invoke_shell()
    while True:
        message = request.websocket.wait()
        print(message)
        shell.send(message.decode()+'\n')
        while True:
            time.sleep(1)
            result=shell.recv(65535)
            request.websocket.send(result)
            print(result)
            if result==''or result==None:
                break

