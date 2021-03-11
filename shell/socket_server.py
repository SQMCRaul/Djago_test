#-*-coding:utf-8-*-
from django.shortcuts import render
import socket
import shell.views
cmd=shell.views.cmd
def socket_server():
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.bind(('127.0.0.1',8088))
    s.listen(5)
    while True:
        conn,addr=s.accept()
        recvdata = conn.recv(1024)
        conn.sendall(bytes("HTTP/1.1 201 OK\r\n\r\n", "utf-8"))
        conn.send(bytes('hhheeee','utf-8'))
if __name__ == '__main__':
    socket_server()