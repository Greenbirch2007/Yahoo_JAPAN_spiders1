# ! -*- coding:utf-8 -*-
import csv
import re
import requests
from requests.exceptions import RequestException
import asyncio
import aiohttp


def call_page(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        return None


def RemoveDot(item):
    f_l = []
    for it in item:
        f_str = "".join(it.split(","))
        f_l.append(f_str)

    return f_l


def remove_block(items):
    new_items = []
    for it in items:
        f = "".join(it.split())
        new_items.append(f)
    return new_items


def writerDt_csv(headers, rowsdata):
    # rowsdata列表中的数据元组,也可以是字典数据
    with open('tokyoTSN.csv', 'w',newline = '') as f:
        f_csv = csv.writer(f)
        f_csv.writerow(headers)
        f_csv.writerows(rowsdata)






def run_forever(func):
    def wrapper(obj):
        while True:
            func(obj)
    return wrapper

def find_longest_str(str_list):
    '''
    找到列表中字符串最长的位置索引
    先获取列表中每个字符串的长度，查找长度最大位置的索引值即可
    '''
    num_list = [len(one) for one in str_list]
    index_num = num_list.index(max(num_list))
    return str_list[int(index_num)]


def remove_block(items):
    new_items = []
    for it in items:
        f = "".join(it.split())
        new_items.append(f)
    return new_items



async def get_title(i):


    url = 'https://job.yahoo.co.jp/jobs/?q=&l=%E6%9D%B1%E4%BA%AC%E9%83%BD&keyword={0}&side=1'.format(i)


    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            print(resp.status)
            text = await resp.text()
            print('start', i)


        html = call_page(url)
        print(url)
        patt = re.compile('<h1 class="titleArea__title ttl--leftLine"><span>.*?</span>関連の求人検索結果（(.*?)件）</h1>', re.S)
        items = re.findall(patt, html)

        for it in items:
            f = "".join(it.split(","))

            big_list.append((i,f))
            print((i,f))









if __name__ =="__main__":
    big_list = []
    TS_lang = 'Python,scrapy,seleinum,flask,sqlalchemy,Django,Golang,beego,buffalo,Echo,Gin,Iris,Revel,perl,java,spring,ruby,rust,C++,Github,git,AWS,Highcharts,pandas,numpy,TCP,Ruby on Rails,shell,ccie'

    TS_db = 'mysql,mongodb,redis,Docker,k8s,Postgresql,Oracle'
    TS_certificate = 'CentOS,LPIC,LPIC1,LPIC2,LPIC3,CCNA,CCNP,CFA,TOEIC'

    f_FS =TS_lang+","+TS_db+","+TS_certificate
    f_tsn = f_FS.split(",")
    headers = ["keyword","nums"]

    loop = asyncio.get_event_loop()
    fun_list = (get_title(i) for i in f_tsn)
    loop.run_until_complete(asyncio.gather(*fun_list))

    writerDt_csv(headers, big_list)

    print("数据导出完成～")


