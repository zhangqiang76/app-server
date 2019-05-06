# coding: utf-8
import requests
from bs4 import BeautifulSoup
import json


def getnews():
    r = requests.get('http://www.chinadaily.com.cn/world/aroundtheworld/')
    soup = BeautifulSoup(r.text, "html.parser")
    urls = soup.select('.tw3_01_2_p')
    h4 = soup.select('.tw3_01_2_t')
    l = len(h4)
    news = []
    for i in range(0, l-1):
        info = {}
        info['url'] = 'http:' + urls[i].select('a')[0]['href']
        info['img'] = 'http:' + urls[i].select('img')[0]['src']
        info['title'] = h4[i].select('a')[0].text
        info['time'] = h4[i].select('b')[0].text
        news.append(info)
        # getdetails(news[i].get('url'))
    return json.dumps(news)


def getdetails(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")
    content = soup.select('#Content')
    print(content[0].text)
    detail = []
    info = {}
    temp = ''
    p = content[0].select('p')
    img = content[0].select('img')
    if img:
        info['img'] = 'http:' + content[0].select('img')[0]['src']
    else:
        info['img'] = ''
    for i in range(len(p)):
        temp = temp + p[i].text + '\n\n'
    info['p'] = temp
    detail.append(info)
    return json.dumps(detail)

