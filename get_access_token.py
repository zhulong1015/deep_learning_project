import requests
import json


# 在这个过程中如果出现 KerError:有可能是IP地址没有加入到白名单中
def get_access_token():
    url = 'https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=wx406449ae268d7ed4&' \
          'secret=7471f78e0e031a15cc0f5b7ded181ffa'
    wb_data = requests.get(url).text
    data_comment = json.loads(wb_data)
    print(data_comment)
    access_token = data_comment['access_token']
    return access_token


print(get_access_token())

