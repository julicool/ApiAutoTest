import requests
import json


headers = {
    "accept": "application/json, text/plain, */*",
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "en-IN,en;q=0.9,zh-CN;q=0.8,zh;q=0.7",
    "cache-control": "no-cache",
    "content-length": "56",
    "content-type": "application/json;charset=UTF-8",
    "origin": "https://www.topgrowth.net",
    "pragma": "no-cache",
    "referer": "https://www.topgrowth.net/",
    "user-agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1",
    "x-g-token": "test",
}


def post_req(url, data) :
    try :
        req = requests.post(url, headers=headers, data=data)  # 进行请求
        res = req.text                                        # 获取请求内容
        return json.loads(res)
    except Exception as e :
        return e


def get_req(url, data) :
    try :
        req = requests.get(url, headers=headers, params=data)
        res = req.text
        return json.loads(res)
    except Exception as e :
        return e


def cho_met(data):
    if data['method'] == "post":
        res = post_req(data['url'], data['data'])
        return res
    elif data['method'] == "get":
        res = get_req(data['url'], data['data'])
        return res
