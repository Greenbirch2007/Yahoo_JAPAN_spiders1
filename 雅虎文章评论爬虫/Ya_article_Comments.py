# ! -*- coding:utf-8 -*-
import csv
import datetime
import os
import re
import time
from lxml import etree
from selenium import webdriver

import pymysql
import xlrd
import requests
from requests.exceptions import RequestException


def call_page(url):
    driver = webdriver.Chrome()
    driver.get(url)
    html = driver.page_source
    time.sleep(10)
    driver.quit()
    return html

def RemoveDot(item):
    f_l = []
    for it in item:
        f_str = "".join(it.split(","))
        f_l.append(f_str)

    return f_l


def parse_html(html):

    f_jobname= remove_block(job_name)


    # 两种类型链接解析
    link = selector.xpath('//*[@id="sr"]/div/div/h3/a/@href')

    link_list = []
    for item in link:
        if item[0:4] == "http":
            link_list.append(item)
        else:

            f_item = 'https://job.yahoo.co.jp' + item
            link_list.append(f_item)

    type = selector.xpath('//*[@id="sr"]/div/div[2]/ul[1]/li[1]/text()')
    salary = selector.xpath('//*[@id="sr"]/div/div[2]/ul[1]/li[2]/text()')
    for i1,i2,i3,i4 in zip(salary,type,link_list,f_jobname):
        big_list.append((i1,i2,i3,i4))



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

        f_44 = "%s," *44
        cursor.executemany('insert into Tokyo_TSN ({0}) values ({1})'.format(f_FS_DB,f_44[:-1]), content)
        connection.commit()
        connection.commit()
        connection.close()
        print('向MySQL中添加数据成功！')
    except TypeError :
        pass



if __name__ == '__main__':
    url = 'https://headlines.yahoo.co.jp/cm/main?d=20200717-00010002-abema-soci&s=lost_points&o=desc&t=t&p=17'
    html = call_page(url)
    patt = re.compile('<iframe class="news-comment-plguin-iframe" scrolling="no" frameborder="0" name="news-cmt" src="(.*?)" style="width: 100%; height: 0px; border: none;"></iframe></div>',re.S)
    items = re.findall(patt,html)
    print(items)
    for conmmenturl_ in items:
        html = call_page(conmmenturl_)
        print(html)









#https://news.yahoo.co.jp/comment/plugin/v1/full/?origin=https%3A%2F%2Fheadlines.yahoo.co.jp&sort=lost_points&order=desc&page=1&type=t&keys=gC02jriDKGDP.234h8AE7rc_skcdiGszocUyaSbdQFGiSrc9cE35troxZMCgRiPIOLs6OogyxOpSIFrbEf6f9veewGheS9gGWYtye.YmoUH9GZG_xWjw6QKxDoNFzwcDoZdLffdAKRashx56el7ektwuNDCuzMnO.JPOjcbTmzcH8QyHaGDcmspsPdnWWW31yUDvUaZ1Me23VeDGQPLthqi.StmML5VpNruVVVx4j5d3HKKnbaVPr4lFJiMQ0RsDo9FJHxOOIQcy6b7jv1S8naMzzUjBuUyVo2Lk4GDFNVsJ39ufxqjHr2spEMjhtJHrOKI_XWRCnwRK7n4MTSjLiHEcWTWRV8cuHndIottUG.gy0FsfcnZ_csfn7ZHv7MjhTfTzt.eExvFmQmxN4.t2ewr.rn2FnNby3dvpFS7XeCQobgj6lNRvi2wpXrCMsYAuAKzku9srg3oTr7GyajXO6aNTkVh1FkFpjCjch93eWXTXAGddqxq58VHyfZyIyl0lbMNnhZ_eNKDQRw6juxyu3DqhEMS45fqbxtsVP_gZl9QoZUYJ6Hnl9ZFzGNw5qETXG8TdH5HKPC3SbeK_5e_KYSxX2eKZeWnrgiMye6x7WCdKWXn4Qz8y3s5ZkRuNH65y9JXspSGDWY5R8iMI7t8BLTxQx0opBGaUvjFmYeeoR5hfyd1.myNHQx6WqgbhS0emIAmJ4_1BxpNaFXzosXb9rHQRzWPksIW2TkPGhXDqw55koHwioP9tChFtmnkJrkjeeuLhfiXvaKhQXzDy69QWnJk4bpu.ts43G0..alCPLWAN&content_id=&full_page_url=https%3A%2F%2Fheadlines.yahoo.co.jp%2Fcm%2Fmain%3Fd%3D20200717-00010002-abema-soci&comment_num=10&ref=&bkt=HDL200105T01PC&flt=&grp=hdl&opttype=pc&disable_total_count=&compact=&compact_initial_view=&display_author_banner=off&ua=Mozilla%2F5.0+(Windows+NT+10.0%3B+Win64%3B+x64)+AppleWebKit%2F537.36+(KHTML%2C+like+Gecko)+Chrome%2F83.0.4103.116+Safari%2F537.36





