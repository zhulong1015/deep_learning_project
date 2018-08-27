import requests
import json


# 微信聊天小程序
def get_data_from(query):
    url = 'http://solr.iyuba.com/solr/collection/select?wt=json&indent=true&q={}&start=0&rows=1'.format(query)
    wb_data = requests.get(url).text
    data_comment = json.loads(wb_data)
    print(data_comment)
    return data_comment


get_data_from("阿里")
data = get_data_from('英语')
print(data)
print(type(data['response']))
print(data['response']['docs'])
print(data['response']['docs'][0]['url'])
print(list(data['response']['docs'][0].keys()))
keys = list(data['response']['docs'][0].keys())
if 'pic' in keys:
        pic = data['response']['docs'][0]['pic']
        print("图片：", pic)
else:
    pic = "null"
    print(pic)
if 'title' in keys:
        title = data['response']['docs'][0]['title'][0]
        print("标题：", title)
else:
    title = data['response']['docs'][0]['title_cn_text'] + '\n' + data['response']['docs'][0]['title_en'][0]
    print(title)

