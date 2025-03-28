import json
from model.param import StockQueryReq, StockUpdateReq, StockInfo, StockUpdateResp
from dao.request import api_request
from model.header import SHOP_STOCK_INFO
from typing import Dict

BILI_VERSION_V2 = "v2"

# 库存查询
def StockQuery(client_id: str, access_token: str, app_secret: str) -> Dict[str, any]:
    url = SHOP_STOCK_INFO.STOCK_QUERY
    req = StockQueryReq()
    req_json = json.dumps(req.__dict__)
    resp = api_request(req_json, url, "GET", client_id, access_token, app_secret, BILI_VERSION_V2)
    # 解析返回值
    if resp.get('code') == 0:
        data = resp.get('data', [])
        stock_infos = []
        for item in data:
            stock_info = StockInfo(**item)
            stock_infos.append(stock_info)
        print(f"StockQuery: {[info.__dict__ for info in stock_infos]}")
    return resp

# 库存更新
def StockUpdate(client_id: str, access_token: str, app_secret: str) -> Dict[str, any]:
    url = SHOP_STOCK_INFO.STOCK_UPDATE
    req = StockUpdateReq()
    req_json = json.dumps(req.__dict__)
    resp = api_request(req_json, url, "POST", client_id, access_token, app_secret, BILI_VERSION_V2)
    # 解析返回值
    if resp.get('code') == 0:
        data = resp.get('data', {})
        stock_update_resp = StockUpdateResp(**data)
        print(f"StockUpdate: {stock_update_resp.__dict__}")
    return resp