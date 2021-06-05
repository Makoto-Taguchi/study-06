import requests
import urllib
import csv
import datetime

now = datetime.datetime.now()


# ジャンルIDを指定してランキング上位30位を調べる
def get_api():
    search_genreid = input("ジャンルIDを入力してください：")
    # テスト用→ 101361 ： アクション
    APP_ID = '1005312593107358367'
    url = 'https://app.rakuten.co.jp/services/api/IchibaItem/Ranking/20170628'
    payload = {
        'applicationId': APP_ID,
        'genreId': search_genreid,
        'hits': 30,#一度のリクエストで返してもらう最大個数（MAX30)
        'page':1,#何ページ目か
        }
    result = requests.get(url, params=payload)
    resp = result.json()
    return resp

def main():
    resp1 = get_api()
    counter = 0
    filename = './log/output_' + now.strftime('%Y%m%d_%H%M%S') + '.csv'
    f = open(filename,'w')
    f.write('No.,NAME,PRICE,URL\n')
    for i in resp1['Items']:
        counter = counter + 1
        # Jsonの出力形式に従い、Itemsの中のi番目のItemの内容を取得
        item = i['Item']
        name = item['itemName']
        print(f"【No.】{str(counter)} ")
        print(f"【Name】{str(name)} ...")
        print(f"【Price】¥{str(item['itemPrice'])}")
        print(f"【URL】{item['itemUrl']}")
        f.write(f"{str(counter)},{str(name)},{str(item['itemPrice'])},{item['itemUrl']} \n")
        # print('【text】', item['itemCaption'])

main()
