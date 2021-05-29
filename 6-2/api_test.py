from api import *

# python -m pytest api_test.py::test_main -s によりテスト
def test_main():
    # url = 'https://app.rakuten.co.jp/services/api/IchibaItem/Search/20170706'
    # res = get_api(url=url)
    
    # チェック
    # 正常系
    res = get_api()
    # Itemsにより商品情報が（一つでも）返されればOK
    assert len(res['Items']) >= 1
    # "itemName"の情報返されればOK（中身は問わない）
    assert res['Items'][0]["Item"]["itemName"]
    # その他のprintしたい情報についても返ってくるかチェック
    assert res['Items'][0]["Item"]["itemPrice"]
    assert res['Items'][0]["Item"]["itemUrl"]
    assert res['Items'][0]["Item"]["itemCaption"]
