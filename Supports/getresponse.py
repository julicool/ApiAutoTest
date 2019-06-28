# -*-coding:utf-8-*-
import requests
import json


# headers_api 针对接口请求的header设置
headers_api = {
    "accept": "application/json, text/plain, */*",
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "en-IN,en;q=0.9,zh-CN;q=0.8,zh;q=0.7",
    "cache-control": "no-cache",
    "content-length": "56",
    "content-type": "application/json;charset=UTF-8",
    "pragma": "no-cache",
    "user-agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1",
    "x-g-token": "test",
    "Connection": "close"
}

# headers_html 针对页面请求的header设置
headers_html ={
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "en-IN,en;q=0.9,zh-CN;q=0.8,zh;q=0.7en-IN,en;q=0.9,zh-CN;q=0.8,zh;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "upgrade-insecure-requests": "1",
    "user-agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1"
}


# 以下都是一些reposts库的基本用法，我就不注释了，百度一下都有
def post_req(url, data) :
    try:
        req = requests.post(url, headers=headers_api, data=data, )
        res = req.text
        return json.loads(res)
    except Exception as e :
        return e


def get_req(url, data) :
    try:
        req = requests.get(url, params=data, headers=headers_api)
        res = req.text
        return json.loads(res)
    except Exception as e :
        return e


def get_stat(url):
    try:
        req = requests.get(url, headers=headers_html)
        res = req.status_code
        return res
    except Exception as e:
        return e


# cho_met函数是根据case中method值来选择用什么方式来发送请求
# 其中的get_status也是使用的get方法，不过结果校验的是请求http响应结果是不是正常，也就是检查页面是否能正常访问
def cho_met(data):
    if data['method'] == "post":
        res = post_req(data['url'], data['data'])
        return res
    elif data['method'] == "get":
        res = get_req(data['url'], data['data'])
        return res
    elif data["method"] == "status":
        res = get_stat(data['url'])
        return res
