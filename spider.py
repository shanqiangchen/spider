# coding=utf-8
import requests
import json
import sys

query_string = 'you shut up'

headers = {"User-Agent":"Mozilla/5.0 (Linux; Android 5.1.1; Nexus 6 Build/LYZ28E) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Mobile Safari/537.36"}

post_data = {
    "query":query_string,
    "from":"en",
    "to":"zh",
}

post_url = "http://fanyi.baidu.com/basetrans"

r = requests.post(post_url,data=post_data,headers=headers)
print(r.content.decode())
dict_ret = json.loads(r.content.decode())
ret = dict_ret["trans"][0]["dst"]
print("query_string is :",query_string)
print("result is :",ret)