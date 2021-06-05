import requests
import urllib

# プロダクトIDを指定して特定の商品を調べる
def get_api():
    search_productid = input("楽天プロダクト製品IDを入力してください：")
    # テスト用→ 484ad5ad36cc16c6cd035d9c5f65e449 ： 鬼滅の刃 フィギュア付き同梱版 ２３ 特装版
    APP_ID = '1005312593107358367'
    url = 'https://app.rakuten.co.jp/services/api/Product/Search/20170426'
    payload = {
        'applicationId': APP_ID,
        'productId': search_productid,
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
        print(f"【No.】{str(counter)}")
        print(f"【Name】{str(name[:30])}...")
        print(f"【URL】{product['productUrlPC']}")
        print(f"【MaxPrice】¥{str(product['maxPrice'])}")
        print(f"【minPrice】¥{str(product['minPrice'])}")
main()
