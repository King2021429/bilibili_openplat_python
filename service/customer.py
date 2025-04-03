from dao.request import api_request
from model.header import SHOP_BA_CHAT, ModelConstants
from model.param import OpenMarketCustomerSendMsgReq


# 客服系统 消息发送
def conversation_send_msg(client_id, access_token, app_secret, req_json):
    url = SHOP_BA_CHAT.CONVERSATION_SEND_MSG_URL
    req_json = input("请输入reqJson串: ")
    resp = api_request(req_json, url, ModelConstants.METHOD_POST, client_id, access_token, app_secret, ModelConstants.BILI_VERSION_V2)
    if resp.get('code') != 0:
        print(f"SendMsg err: {resp.get('message', '')}")
    print(f"queryResp: {resp}")
    return resp


# 客服系统 获取用户来源
def conversation_customer_user_from(client_id, access_token, app_secret, req_json):
    url = SHOP_BA_CHAT.CONVERSATION_CUSTOMER_USER_FROM
    req_json = input("请输入reqJson串: ")
    resp = api_request(req_json, url, ModelConstants.METHOD_POST, client_id, access_token, app_secret, ModelConstants.BILI_VERSION_V2)
    return resp


# 客服系统 修改客服状态
def conversation_staff_status_update(client_id, access_token, app_secret, req_json):
    url = SHOP_BA_CHAT.CONVERSATION_STAFF_STATUS_UPDATE
    req_json = input("请输入reqJson串: ")
    resp = api_request(req_json, url, ModelConstants.METHOD_POST, client_id, access_token, app_secret, ModelConstants.BILI_VERSION_V2)
    return resp


# 客服系统 关闭
def conversation_close(client_id, access_token, app_secret, req_json):
    url = SHOP_BA_CHAT.CONVERSATION_CLOSE
    req_json = input("请输入reqJson串: ")
    resp = api_request(req_json, url, ModelConstants.METHOD_POST, client_id, access_token, app_secret, ModelConstants.BILI_VERSION_V2)
    return resp