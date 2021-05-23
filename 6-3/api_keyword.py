import requests
import urllib

# キーワードを指定して上位30件の製品を調べる
def get_api():
    search_keyword = input("検索ワードを入力してください：")
    APP_ID = '1005312593107358367'
    url = 'https://app.rakuten.co.jp/services/api/Product/Search/20170426'
    payload = {
        'applicationId': APP_ID,
        'keyword': search_keyword,
        'hits': 30,#一度のリクエストで返してもらう最大個数（MAX30)
        'page':1,#何ページ目か
        }
    result = requests.get(url, params=payload)
    resp = result.json()
    return resp

def main():
    resp1 = get_api()
    counter = 0
    for i in resp1['Products']:
        counter = counter + 1
        # Jsonの出力形式に従い、Productsの中のi番目のProductの内容を取得
        product = i['Product']
        name = product['productName']
        print('【No.】'+ str(counter))
        print('【Name】' + str(name[:30]) + '...')
        print('【URL】',product['productUrlPC'])
        print('【MaxPrice】' + '¥' +str(product['maxPrice']))
        print('【minPrice】' + '¥' +str(product['minPrice']))

main()
