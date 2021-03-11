import os,os.path
print(os.path.abspath('.'))
os.makedirs('./image')
open('./image/upload.jpg','wb+')