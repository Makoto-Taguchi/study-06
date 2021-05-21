import requests
import urllib


def get_api():
    serch_keyword = '鬼滅"'
    APP_ID = '1005312593107358367'
    url = 'https://app.rakuten.co.jp/services/api/IchibaItem/Search/20170706'
    payload = {
        'applicationId': APP_ID,
        'keyword': serch_keyword,
        'hits': 30,#一度のリクエストで返してもらう最大個数（MAX30)
        'page':1,#何ページ目か
        }
    result = requests.get(url, params=payload)
    resp = result.json()

    counter = 0
    for i in resp['Items']:
        counter = counter + 1
        # Jsonの出力形式に従い、Itemsの中のi番目のItemの内容を取得
        item = i['Item']
        name = item['itemName']
        print('【No.】'+ str(counter))
        print('【Name】' + str(name[:30]) + '...')
        print('【Price】' + '¥' +str(item['itemPrice']))
        print('【URL】',item['itemUrl'])
        print('【text】', item['itemCaption'])

get_api()

# def main():

# main()