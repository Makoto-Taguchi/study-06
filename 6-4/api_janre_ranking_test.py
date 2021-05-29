from api_janre_ranking import *

# 関数名指定しないと以下全部チェック
# python -m pytest ./api_janre_ranking_test.py -s
# 関数指定するとそれだけチェック
# python -m pytest ./api_janre_ranking_test.py::test_get_api -s

# ジャンルID : 101361 ： アクション
def test_get_api():
    res = get_api()
    # Itemsにより商品情報が（一つでも）返されればOK
    assert len(res['Items']) >= 1
    # "itemName"の情報返されればOK（中身は問わない）
    assert res['Items'][0]["Item"]["itemName"]
    assert res['Items'][0]["Item"]["itemPrice"]

def test_get_api2():
    res = get_api()
    assert res['Items'][0]["Item"]["itemUrl"]