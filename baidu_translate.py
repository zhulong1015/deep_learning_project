import http.client
import json
import hashlib
import urllib.parse
import random
import pymysql.cursors
import pymysql
import urllib.request


def init_database():
    sqlconn = pymysql.connect(host='127.0.0.1', user='root', password='root', database='article_spider', charset='utf8')
    return sqlconn


def baidu_translate(src):
    appid = '20180725000188823'  # 你的appid
    secretKey = 'LINlmVAQJqZf_8pj_TA2'  # 你的密钥
    httpClient = None
    myurl = '/api/trans/vip/translate'
    q = src  # 这里是要翻译的内容
    fromLang = 'en'
    toLang = 'zh'
    salt = random.randint(32768, 65536)
    sign = appid + q + str(salt) + secretKey
    m1 = hashlib.md5()
    m1.update(sign.encode('utf8'))
    sign = m1.hexdigest()
    myurl = myurl + '?appid=' + appid + '&q=' + urllib.parse.quote(
        q) + '&from=' + fromLang + '&to=' + toLang + '&salt=' + str(salt) + '&sign=' + sign

    try:
        httpClient = http.client.HTTPConnection('api.fanyi.baidu.com')
        httpClient.request('GET', myurl)

        # response是HTTPResponse对象
        response = httpClient.getresponse()
        result = response.read()
        json_line = json.loads(result)
        new_result = json_line["trans_result"][0]["dst"]
        print(new_result)
    except Exception as e:
        print(e)
    finally:
        if httpClient:
            httpClient.close()


def translate():
    cur = init_database().cursor()
    sql = 'select Sentence from newstext'
    cur.execute(sql)
    results = cur.fetchall()
    for text in results:
        if text[0] != "Null":
            print("新闻翻译：")
            baidu_translate(text[0])


translate()
# baidu_translate("welcome to beijing ")