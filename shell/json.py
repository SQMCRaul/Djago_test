from django.shortcuts import render,HttpResponse
import simplejson
import json

def rejson(request):
    js = {'a': 1,
          'b': 2
          }
    jsl=json.dumps(js)

    content={}
    content['data']=jsl
    response=HttpResponse(content['data'],content_type="application/json")
    # response["Access-Control-Allow-Origin"] = "*"
    # response["Access-Control-Allow-Methods"] = "POST,GET,OPTIONS"
    # response["Access-Control-Max-Age"] = "1000"
    # response["Access-Control-Allow-headers"]="*"
    return response

    # return render(request,'a.html',content)
