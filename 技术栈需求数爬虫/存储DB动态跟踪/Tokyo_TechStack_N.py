# -*- coding: utf-8 -*-


import csv
import datetime
import os
import re
import time
import sys
type = sys.getfilesystemencoding()
import pymysql
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


def insertDB(content):
    connection = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456', db='Yahoo_J',
                                 charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)

    cursor = connection.cursor()
    try:

        f_72 = "%s," *72
        cursor.executemany('insert into Tokyo_TSN ({0}) values ({1})'.format(f_FS_DB,f_72[:-1]), content)
        connection.commit()
        connection.commit()
        connection.close()
        print('向MySQL中添加数据成功！')
    except TypeError :
        pass



if __name__ == '__main__':
    big_list = []
    TS_lang_DB = 'Python,scrapy,flask,sqlalchemy,Django,Golang,beego,buffalo,Echo,Gin,Iris,Revel,perl,java,spring,ruby,rust,CPlus,Github,git,AWS,Highcharts,pandas,numpy,TCP,Ruby_on_Rails,shell,ccie'
    TS_lang_Web = 'Python,scrapy,flask,sqlalchemy,Django,Golang,beego,buffalo,Echo,Gin,Iris,Revel,perl,java,spring,ruby,rust,C++,Github,git,AWS,Highcharts,pandas,numpy,TCP,Ruby on Rails,shell,ccie'
    TS_db = 'mysql,mongodb,redis,Docker,k8s,Postgresql,Oracle'
    TS_certificate = 'CentOS,LPIC,LPIC1,LPIC2,LPIC3,CCNA,CCNP,CFA,TOEIC'
    add_cloumn_DB1 = 'API,FinTech,FundManagement,Bloomberg,PHP,laravel,gorm,IT_N3,selenium,fina_Python,fina_ruby,fina_perl,fina_Golang,fina_linux,secu_Python,secu_ruby,secu_perl,secu_Golang,secu_linux,fund_Python,fund_ruby,fund_perl,fund_Golang,fund_linux,VBA,javascript,vue,jQuery'
    add_cloumn_Web1 = 'API,FinTech,ファンドマネージャー,Bloomberg,PHP,laravel,gorm,IT+N3,selenium,金融業+Python,金融業+ruby,金融業+perl,金融業+Golang,金融業+linux,基金+Python,基金+ruby,基金+perl,基金+Golang,基金+linux,証券+Python,証券+ruby,証券+perl,証券+Golang,証券+linux,VBA,javascript,vue,jQuery'
    f_FS_web =TS_lang_Web+","+TS_db+","+TS_certificate+","+add_cloumn_Web1
    f_FS_DB =TS_lang_DB+","+TS_db+","+TS_certificate+","+add_cloumn_DB1
    f_tsn_web = f_FS_web.split(",")
    print(len(f_tsn_web))

    for code in f_tsn_web:
        url = 'https://job.yahoo.co.jp/jobs/?q=&l=%E6%9D%B1%E4%BA%AC%E9%83%BD&keyword={0}&side=1'.format(code)

        html = call_page(url)
        print(url)
        patt = re.compile('<h1 class="titleArea__title ttl--leftLine"><span>.*?</span>関連の求人検索結果（(.*?)件）</h1>',re.S)
        items = re.findall(patt, html)
        try:
            if len(items) != 0:
                for it in items:
                    f = "".join(it.split(","))
                    big_list.append(f)
            else:
                big_list.append("0")
        except:
            pass


    ff_l = []
    f_tup = tuple(big_list)
    ff_l.append((f_tup))
    print(ff_l)
    print(len(ff_l[0]))
    insertDB(ff_l)








# create table Tokyo_TSN (id int not null primary key auto_increment,Python  float,scrapy  float,flask  float,sqlalchemy  float,Django  float,Golang  float,beego  float,buffalo  float,Echo  float,Gin  float,Iris  float,Revel  float,perl  float,java  float,spring  float,ruby  float,rust  float,CPlus  float,Github  float,git  float,AWS  float,Highcharts  float,pandas  float,numpy  float,TCP  float,Ruby_on_Rails  float,shell  float,ccie  float,mysql  float,mongodb  float,redis  float,Docker  float,k8s  float,Postgresql  float,Oracle  float,CentOS  float,LPIC  float,LPIC1  float,LPIC2  float,LPIC3  float,CCNA  float,CCNP  float,CFA  float,TOEIC float, LastTime timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP) engine=InnoDB  charset=utf8;


# drop table Tokyo_TSN;


# 增加列字段
# API，FinTech，FundManagement，Bloomberg
# alter table Tokyo_TSN add column API float;
# alter table Tokyo_TSN add column FinTech float;
# alter table Tokyo_TSN add column FundManagement float;
# alter table Tokyo_TSN add column Bloomberg float;
#   alter table Tokyo_TSN add column PHP float;
#   alter table Tokyo_TSN add column laravel float;gorm
#   alter table Tokyo_TSN add column gorm float;
#   alter table Tokyo_TSN add column IT_N3 float;
#   alter table Tokyo_TSN add column selenium float;
#   alter table Tokyo_TSN add column fina_Python float;
#   alter table Tokyo_TSN add column fina_ruby float;
#   alter table Tokyo_TSN add column fina_perl float;
#   alter table Tokyo_TSN add column fina_Golang float;
#   alter table Tokyo_TSN add column fina_linux float;
#   alter table Tokyo_TSN add column secu_Python float;
#   alter table Tokyo_TSN add column secu_ruby float;
#   alter table Tokyo_TSN add column secu_perl float;
#   alter table Tokyo_TSN add column secu_Golang float;
#   alter table Tokyo_TSN add column secu_linux float;
#   alter table Tokyo_TSN add column fund_Python float;
#   alter table Tokyo_TSN add column fund_ruby float;
#   alter table Tokyo_TSN add column fund_perl float;
#   alter table Tokyo_TSN add column fund_Golang float;
#   alter table Tokyo_TSN add column fund_linux float;
# alter table Tokyo_TSN add column VBA float;
# alter table Tokyo_TSN add column javascript float;
# alter table Tokyo_TSN add column vue float;
# alter table Tokyo_TSN add column jQuery float;



# mei
#*/3 * * * * /home/w/pyenv/bin/python /home/w/SP500_Nasdap100/SP500.py





