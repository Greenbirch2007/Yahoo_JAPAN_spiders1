# ! -*- coding:utf-8 -*-
import csv
import datetime
import os
import re
import time
import xlrd
import requests
from requests.exceptions import RequestException


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





if __name__ == '__main__':
    big_list = []
    TS_lang = 'Python,scrapy,seleinum,flask,sqlalchemy,Django,Golang,beego,buffalo,Echo,Gin,Iris,Revel,perl,java,spring,ruby,rust,C++,Github,git,AWS,Highcharts,pandas,numpy,TCP'
    TS_db = 'mysql,mongodb,redis,Docker,k8s,Postgresql,Oracle'
    TS_certificate = 'CentOS,LPIC,LPIC1,LPIC2,LPIC3,CCNA,CCNP,CFA,TOEIC'
    f_FS =TS_lang+TS_db+TS_certificate
    f_tsn = f_FS.split(",")
    for code in f_tsn:
        url = 'https://job.yahoo.co.jp/jobs/?q=&l=%E6%9D%B1%E4%BA%AC%E9%83%BD&keyword={0}&side=1'.format(code)

        html = call_page(url)
        print(url)
        patt = re.compile('<h1 class="titleArea__title ttl--leftLine"><span>.*?</span>関連の求人検索結果（(.*?)件）</h1>',re.S)
        items = re.findall(patt, html)

        for it in items:
            f = "".join(it.split(","))

            big_list.append(f)
    ff_l = []
    for i1,i2 in zip(f_tsn,big_list):
        ff_l.append((i1,i2))

    writerDt_csv(f_tsn,ff_l)

    print("数据导出完成～")










