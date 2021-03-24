# coding:utf-8
import json
import urllib
from urllib import request,response
import requests
import time,datetime

url = "http://10.10.12.92/zabbix/api_jsonrpc.php"
header = {"Content-Type":"application/json"}

def get_token(user,password):
    # auth user and password
    data1 = json.dumps(
        {
            "jsonrpc": "2.0",
    	    "method": "user.login",
    	    "params": {
    	    "user": user,            #修改用户名
    	    "password": password     #修改密码
    	    },
    	    "id": 0
        })
    req = request.Request(url, method='post',data=data1.encode())
    # print(req)
    for key in header:
        req.add_header(key,header[key])
    # auth and get authid
    try:
        result = request.urlopen(req)
        # print(result.read())
        # print(result.read().decode())
    except request.URLError as e:
        print ("Auth Failed, Please Check Your Name AndPassword:",e)
    else:
        response = json.loads(result.read(),encoding='utf-8')
        token=response['result']
        print(response)
        print(token)
        result.close()
        return token

def get_host():

    data = json.dumps(
    {
      "jsonrpc": "2.0",
      "method": "host.get",
      "params":{
          "output": "extend",
          "search":{"name":"核心交换机"}
    },
    "auth":get_token('Admin','zabbix'),
    "id": 1,
    })


# create request object
    req = request.Request(url,data.encode())
    for key in header:
        req.add_header(key,header[key])
# auth and get authid
    try:
        result = request.urlopen(req)

    except request.URLError as e:
         print ("Auth Failed, Please Check Your Name AndPassword:",e)
    else:
        response = json.loads(result.read(),encoding='utf-8')
        for i in response['result']:
            print(i)
        # print(response['result'])
        print(len(response['result']))
        # print(response)
        result.close()


def get_graph():
    data = json.dumps(
        {
            "jsonrpc": "2.0",
            "method": "graph.get",
            "params": {
                "output": "extend",
                "hostid":10084,

            },
            "auth": get_token('Admin', 'zabbix'),
            "id": 1,
        })

    # create request object
    req = request.Request(url, data.encode())
    for key in header:
        req.add_header(key, header[key])
    # auth and get authid
    try:
        result = request.urlopen(req)

    except request.URLError as e:
        print("Auth Failed, Please Check Your Name AndPassword:", e)
    else:
        response = json.loads(result.read(), encoding='utf-8')
        print(response['result'])
        print(len(response['result']))
        # print(response)
        result.close()
def get_png():
    token = get_token('Admin','zabbix')
    print(token)
    header = {
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Cache-Control": "no-cache",
        "Connection": "keep-alive",
        "Cookie": "PHPSESSID=2bvctu9rva99ppd74gaopb8i42; zbx_sessionid=" + token,
        "Pragma": "no-cache",
        "Upgrade-Insecure-Requests": "1"
    }
    charUrl = "http://10.10.12.92/zabbix/chart2.php?graphid=1110&from=now-6h&to=now&profileIdx=web.graphs.filter&profileIdx2=1110&width=1302&_=uh23868v"
    resp = requests.get(charUrl, headers=header)
    with open("test_img.png", 'wb') as f:
        f.write(resp.content)
def get_speed(token):

    data = json.dumps(
        {
            "jsonrpc": "2.0",
            "method": "item.get",
            "params": {
                "output": "extend",
                "hostids": "10279",
                "search": {
                    "key_": "cpu"
                },
                "sortfield": "name"
            },
            "auth": token,
            "id": 1
        })


# create request object
    req = request.Request(url,data.encode())
    for key in header:
        req.add_header(key,header[key])
# auth and get authid
    try:
        result = request.urlopen(req)

    except request.URLError as e:
         print ("Auth Failed, Please Check Your Name AndPassword:",e)
    else:

        response = json.loads(result.read(),encoding='utf-8')
        for i in response['result']:

        # print(response['result'])
        # print(response)
            return i['itemid']
        result.close()
def get_interface():

    data = json.dumps(
        {
            "jsonrpc": "2.0",
            "method": "hostinterface.get",
            "params": {
                "output": "extend",
                "hostids": "10264"
            },
            "auth": get_token('Admin','zabbix'),
            "id": 1
        })


# create request object
    req = request.Request(url,data.encode())
    for key in header:
        req.add_header(key,header[key])
# auth and get authid
    try:
        result = request.urlopen(req)

    except request.URLError as e:
         print ("Auth Failed, Please Check Your Name AndPassword:",e)
    else:
        response = json.loads(result.read(),encoding='utf-8')
        for i in response['result']:
            print(i)
        print(len(response['result']))
        # print(response)
        result.close()
def get_item():

    data = json.dumps(
        {
            "jsonrpc": "2.0",
            "method": "history.get",
            "params": {
                "history": 0,
                "itemids": "28647",
                "sortfield": "clock",
                "sortorder": "DESC",
                "limit": 1,
                "output": "extend"
            },
            "auth": get_token('Admin','zabbix'),
            "id": 1
        })
# create request object
    req = request.Request(url,data.encode())
    for key in header:
        req.add_header(key,header[key])
# auth and get authid
    try:
        result = request.urlopen(req)

    except request.URLError as e:
         print ("Auth Failed, Please Check Your Name AndPassword:",e)
    else:
        response = json.loads(result.read(),encoding='utf-8')
        for i in response['result']:
            print(i)

        # print(response)
        result.close()
if __name__ =='__main__':
    token=get_token('Admin','zabbix')
    get_speed(token)