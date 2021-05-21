#coding:utf-8
#プリントした時に見やすいよう色をつけました
PURPLE  = '\033[35m'
RED     = '\033[31m'
CYAN    = '\033[36m'
OKBLUE  = '\033[94m'
OKGREEN = '\033[92m'
WARNING = '\033[93m'
FAIL    = '\033[91m'
ENDC    = '\033[0m'

import csv
import sys
import codecs
import math
import random
import requests
from time import sleep
import re
args = sys.argv
shopName = args[1]
counter = 0
url = 'https://app.rakuten.co.jp/services/api/IchibaItem/Search/20170706'
payload = {
    'applicationId': 1005312593107358367,
    'hits': 30,
    'shopCode':shopName,
    'page':1,
    'postageFlag':1,
    #'genreId':101164,
    }
r = requests.get(url, params=payload)
resp = r.json()
print("【num of item】",resp['count'])
total = int(resp['count'])
Max = total/30 + 1
print('【total page】',Max)

if Max > 100:
    Max = 100
    print('100ページ（3000アイテム）を超えています．')
    print('カテゴリ別に回すことを勧めます.')
    sleep(3)
print('-'*40)
sleep(1)



a = open('output.csv','w')
a.write('JAN,NAME,PRICE,URL\n')

for i in range(1,int(Max+1)):
    url = 'https://app.rakuten.co.jp/services/api/IchibaItem/Search/20170706'
    payload = {
        'applicationId': 1005312593107358367,
        'hits': 30,
        'shopCode':shopName,
        'page':i,#リクエストするページ番号が1-Maxまで変化します
        'postageFlag':1,
        }
    r = requests.get(url, params=payload)
    resp = r.json()
    for i in resp['Items']:
        counter = counter + 1
        print('【No.】'+ PURPLE + str(counter) + ENDC)
        item = i['Item']
        name = item['itemName']
        if len(name) >= 30:
            # 文字列の長さが３５文字以上であれば３５文字以降は省略
            print('【Name】' + OKGREEN + str(name[:30].encode('utf-8')) + '...' + ENDC)
        else:
            print('【Name】' + OKGREEN + str(item['itemName'].encode('utf-8')) + ENDC)
        print('【Price】' + CYAN + '¥' +str(item['itemPrice']) + ENDC)

        # ポイント分（自分の場合は最低４倍）を差し引く
        price = int(item['itemPrice'] * 0.96)
        print('【URL】',item['itemUrl'])
        URL = item['itemUrl']
        print('【shop】',item['shopName'])
        text = item['itemCaption']

        #JANコードの抽出
        JAN = ''
        postCode_0 = re.findall('[0-9]{13}',URL)#URLにJANコード（１３桁の数字）があれば抽出
        if len(postCode_0) == 1:
            JAN = postCode_0[0]
            print('【JAN】' + OKGREEN + str(JAN) + ENDC)
            # a.write(str(JAN)+','+str(name.encode('utf-8'))+','+str(price)+    ','+str(URL)+'\n')
            a.write(str(JAN)+','+str(name)+','+str(price)+    ','+str(URL)+'\n')
        else:#URLにJANコードがなければキャプション（商品説明）から抽出
            postCode = re.findall('[0-9]{13}',text)
            len_postCode = len(postCode)
            if len_postCode == 1:
                JAN = postCode[0]
                print('【JAN】' + WARNING + str(postCode[0]) + ENDC)

                a.write(str(JAN)+','+str(name.encode('utf-8'))+','+str(price)+','+str(URL)+'\n')
            else:
                JAN = 'NONE'
                print('【JAN】' + WARNING + 'JAN: NONE' + ENDC)
        print('')
        sleep(0.1)
a.close()