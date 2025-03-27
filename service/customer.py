from dao.request import api_request
from model.header import SHOP_BA_CHAT, ModelConstants
from model.param import OpenMarketCustomerSendMsgReq

# 客服系统 消息发送
def conversation_send_msg(client_id, access_token, app_secret, req_json):
    url = SHOP_BA_CHAT.CONVERSATION_SEND_MSG_URL
    query_req = OpenMarketCustomerSendMsgReq(
        biz_id=1,  # 假设业务方类型id为1，可根据实际情况修改
        staff_id=0,  # 可根据实际情况修改
        shop_id=0,  # 可根据实际情况修改
        msg_type=1,
        conversation_id=115957154487296,
        msg='{"content":"888"}',
        user_open_id=""
    )
    import json
    query_req_json = json.dumps(query_req.__dict__)
    resp = api_request(query_req_json, url, ModelConstants.METHOD_POST, client_id, access_token, app_secret, ModelConstants.BILI_VERSION_V2)
    if resp.get('code') != 0:
        print(f"SendMsg err: {resp.get('message', '')}")
    print(f"queryResp: {resp}")
    return resp


# 客服系统 获取用户来源
def conversation_customer_user_from(client_id, access_token, app_secret, req_json):
    url = SHOP_BA_CHAT.CONVERSATION_CUSTOMER_USER_FROM
    return api_request(req_json, url, ModelConstants.METHOD_GET, client_id, access_token, app_secret, ModelConstants.BILI_VERSION_V2)


# 客服系统 修改客服状态
def conversation_staff_status_update(client_id, access_token, app_secret, req_json):
    url = SHOP_BA_CHAT.CONVERSATION_STAFF_STATUS_UPDATE
    return api_request(req_json, url, ModelConstants.METHOD_POST, client_id, access_token, app_secret, ModelConstants.BILI_VERSION_V2)


# 客服系统 关闭
def conversation_close(client_id, access_token, app_secret, req_json):
    url = SHOP_BA_CHAT.CONVERSATION_CLOSE
    return api_request(req_json, url, ModelConstants.METHOD_POST, client_id, access_token, app_secret, ModelConstants.BILI_VERSION_V2)