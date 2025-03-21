
import requests
import json
import hashlib
import time
import urllib.parse

# 定义常量
BILI_VERSION_V2 = "v2"
JSON_TYPE = "application/json"
HMAC_SHA256 = "HMAC-SHA256"

# 构建 URL 参数的函数
def build_url(base_url, params):
    url_parts = list(urllib.parse.urlparse(base_url))
    query = dict(urllib.parse.parse_qsl(url_parts[4]))
    query.update(params)
    url_parts[4] = urllib.parse.urlencode(query)
    return urllib.parse.urlunparse(url_parts)

# 计算 MD5
def md5(text):
    return hashlib.md5(text.encode()).hexdigest()

# 进行 API 请求
def api_request(req_json, url, method, client_id, access_token, app_secret, version):
    headers = {
        "Content-Type": JSON_TYPE,
        "Accept": JSON_TYPE
    }
    if method == "POST":
        response = requests.post(url, data=req_json, headers=headers)
    elif method == "GET":
        response = requests.get(url, params=json.loads(req_json), headers=headers)
    return response.json()

# 稿件列表查询
def arc_view_list(client_id, access_token, app_secret, req_json):
    url = "ArcViewList"  # 需要替换为实际的 URL
    return api_request(req_json, url, "POST", client_id, access_token, app_secret, BILI_VERSION_V2)

# 售后列表查询
def after_sale_query_list(client_id, access_token, app_secret, req_json):
    url = "AfterSaleQueryList"  # 需要替换为实际的 URL
    return api_request(req_json, url, "GET", client_id, access_token, app_secret, BILI_VERSION_V2)

# 文章删除
def article_delete(client_id, access_token, app_secret, req_json):
    url = "ArticleDelete"  # 需要替换为实际的 URL
    return api_request(req_json, url, "POST", client_id, access_token, app_secret, BILI_VERSION_V2)

# 库存查询
def stock_query(client_id, access_token, app_secret):
    url = "StockQuery"  # 需要替换为实际的 URL
    resp = api_request("", url, "GET", client_id, access_token, app_secret, BILI_VERSION_V2)
    return resp

# 库存更新
def stock_update(client_id, access_token, app_secret):
    url = "StockUpdate"  # 需要替换为实际的 URL
    query_req = {}
    query_req_json = json.dumps(query_req)
    resp = api_request(query_req_json, url, "POST", client_id, access_token, app_secret, BILI_VERSION_V2)
    return resp

# 文件上传预处理
def video_init(client_id, access_token, app_secret):
    url = "ArcInitUrl"  # 需要替换为实际的 URL
    video_init_req = {
        "Name": "test.mp4",
        "Utype": "0"
    }
    video_init_req_json = json.dumps(video_init_req)
    resp = api_request(video_init_req_json, url, "POST", client_id, access_token, app_secret, BILI_VERSION_V2)
    return resp

# 文件分片合片
def video_arc_complete(client_id, access_token, app_secret):
    url = "ArcComplete"  # 需要替换为实际的 URL
    resp = api_request("", url, "POST", client_id, access_token, app_secret, BILI_VERSION_V2)
    return resp

# 稿件提交 POST
def arc_add_url(client_id, access_token, app_secret, req_json):
    url = "ArcAddUrl"  # 需要替换为实际的 URL
    return api_request(req_json, url, "POST", client_id, access_token, app_secret, BILI_VERSION_V2)

# 稿件提交fetch模式
def arc_add_fetch(client_id, access_token, app_secret, req_json):
    url = "ArcAddFetch"  # 需要替换为实际的 URL
    return api_request(req_json, url, "POST", client_id, access_token, app_secret, BILI_VERSION_V2)

# 稿件编辑
def arc_edit(client_id, access_token, app_secret, req_json):
    url = "ArcEdit"  # 需要替换为实际的 URL
    return api_request(req_json, url, "POST", client_id, access_token, app_secret, BILI_VERSION_V2)

# 稿件删除
def arc_del(client_id, access_token, app_secret, req_json):
    url = "ArcDel"  # 需要替换为实际的 URL
    return api_request(req_json, url, "POST", client_id, access_token, app_secret, BILI_VERSION_V2)

# 稿件查询
def arc_view(client_id, access_token, app_secret, req_json):
    url = "ArcView"  # 需要替换为实际的 URL
    return api_request(req_json, url, "POST", client_id, access_token, app_secret, BILI_VERSION_V2)

# 文章编辑
def article_edit(client_id, access_token, app_secret, req_json):
    url = "ArticleEdit"  # 需要替换为实际的 URL
    return api_request(req_json, url, "POST", client_id, access_token, app_secret, BILI_VERSION_V2)

# 批量查询地址库列表
def address_list(client_id, access_token, app_secret, req_json):
    url = "AddressList"  # 需要替换为实际的 URL
    return api_request(req_json, url, "GET", client_id, access_token, app_secret, BILI_VERSION_V2)

# 客服系统 消息发送
def conversation_send_msg(client_id, access_token, app_secret, req_json):
    url = "ConversationSendMsgUrl"  # 需要替换为实际的 URL
    query_req = {
        "MsgType": 1,
        "ConversationId": 115957154487296,
        "Msg": '{"content":"888"}',
        "UserOpenId": ""
    }
    query_req_json = json.dumps(query_req)
    resp = api_request(query_req_json, url, "POST", client_id, access_token, app_secret, BILI_VERSION_V2)
    return resp

# 客服系统 获取用户来源
def conversation_customer_user_from(client_id, access_token, app_secret, req_json):
    url = "ConversationCustomerUserFrom"  # 需要替换为实际的 URL
    return api_request(req_json, url, "GET", client_id, access_token, app_secret, BILI_VERSION_V2)

# 客服系统 修改客服状态
def conversation_staff_status_update(client_id, access_token, app_secret, req_json):
    url = "ConversationStaffStatusUpdate"  # 需要替换为实际的 URL
    return api_request(req_json, url, "POST", client_id, access_token, app_secret, BILI_VERSION_V2)

# 客服系统 关闭
def conversation_close(client_id, access_token, app_secret, req_json):
    url = "ConversationClose"  # 需要替换为实际的 URL
    return api_request(req_json, url, "POST", client_id, access_token, app_secret, BILI_VERSION_V2)

# 签名计算
def sign(client_id, access_token, app_secret):
    req_json = input("请输入reqJson串: ")
    version = input("请输入version: ")
    timestamp = str(int(time.time()))
    nonce = str(time.time_ns())
    content_md5 = md5(req_json)
    header = {
        "ContentType": JSON_TYPE,
        "ContentAcceptType": JSON_TYPE,
        "Timestamp": timestamp,
        "SignatureMethod": HMAC_SHA256,
        "SignatureVersion": version,
        "Authorization": "",
        "Nonce": nonce,
        "AccessKeyId": client_id,
        "ContentMD5": content_md5,
        "AccessToken": access_token
    }
    # 这里需要实现签名计算逻辑
    header["Authorization"] = ""
    print(f"\n请求头:{header}")
    return

# 获取授权
def oauth(client_id, app_secret):
    base_url = "https://api.bilibili.com/x/account-oauth2/v1/token"
    code = input("请输入 code: ")
    params = {
        "client_id": client_id,
        "client_secret": app_secret,
        "grant_type": "authorization_code",
        "code": code
    }
    full_url = build_url(base_url, params)
    print("Full URL:", full_url)
    response = requests.post(full_url)
    print(response.text)

# 入口启动函数
def main():
    client_id = input("请输入 client_id: ")
    access_token = input("请输入 access_token: ")
    app_secret = input("请输入 app_secret: ")

    print("请输入对应方法:" +
          "0: 计算签名\n" +
          "1: 获取授权\n" +
          "2: USER_INFO-获取已授权用户基础公开信息\n" +
          "3: USER_INFO-查询用户已授权权限列表\n" +
          "4: ARC_BASE-文件上传预处理\n" +
          "7: ARC_BASE-文件分片合片\n" +
          "8: ARC_BASE-视频稿件提交\n" +
          "9: ARC_BASE-获取用于投稿的连接\n" +
          "10: ARC_BASE-查询单一视频稿件详情\n" +
          "11: ARC_BASE-查询用户视频稿件列表\n" +
          "12: ATC_BASE-文章提交\n" +
          "13: ATC_BASE-文章编辑\n" +
          "14: ATC_BASE-文章删除\n" +
          "15: ATC_BASE-文章详情\n" +
          "16: ATC_BASE-文章列表查询\n" +
          "17: ATC_BASE-文章分类查询\n" +
          "18: ATC_BASE-获取视频、文章卡片信息\n" +
          "19: ATC_BASE-文集提交\n" +
          "20: ATC_BASE-文集信息编辑\n" +
          "21: ATC_BASE-文集下文章列表修改\n" +
          "22: ATC_BASE-文集删除\n" +
          "23: ATC_BASE-文集列表查询\n" +
          "24: ATC_BASE-文集详情查询\n" +
          "26: USER_DATA-获取用户数据\n" +
          "27: ARC_DATA-获取单个稿件数据\n" +
          "28: ARC_DATA-获取整体稿件增量数据\n" +
          "29: ATC_DATA-获取单一专栏数据\n" +
          "30: ATC_DATA-获取整体投稿增量数据\n" +
          "31: SHOP_STORE_INFO-获取店铺信息\n" +
          "32: SHOP_COMMODITY_INFO-商品发布\n" +
          "33: SHOP_COMMODITY_INFO-商品编辑\n" +
          "34: SHOP_COMMODITY_INFO-商品删除\n" +
          "35: SHOP_COMMODITY_INFO-商品列表查询\n" +
          "36: SHOP_COMMODITY_INFO-商品详情查询\n" +
          "37: SHOP_COMMODITY_INFO-查询发品配置\n" +
          "38: SHOP_COMMODITY_INFO-查询商品类目属性列表\n" +
          "39: SHOP_COMMODITY_INFO-获取类目列表\n" +
          "40: SHOP_ORDER_INFO-订单列表查询\n" +
          "41: SHOP_ORDER_INFO-订单详情查询\n" +
          "42: SHOP_ORDER_INFO-订单敏感信息解密\n" +
          "43: SHOP_ORDER_INFO-流量卡审核信息回传\n" +
          "44: SHOP_ORDER_INFO-商家备注\n" +
          "45: SHOP_LOGISTICS_INFO-发货回掉\n" +
          "46: SHOP_LOGISTICS_INFO-物流编辑\n" +
          "47: SHOP_LOGISTICS_INFO-获取快递公司列表\n" +
          "48: SHOP_LOGISTICS_INFO-地址库创建\n" +
          "49: SHOP_LOGISTICS_INFO-批量查询地址库列表\n" +
          "50: SHOP_LOGISTICS_INFO-获取全量省份信息\n" +
          "51: SHOP_LOGISTICS_INFO-根据省获取全量三级地址\n" +
          "52: SHOP_LOGISTICS_INFO-运费模板列表查询\n" +
          "53: SHOP_AFTERSALES_INFO-售后列表查询\n" +
          "54: SHOP_AFTERSALES_INFO-售后详情查询\n" +
          "55: SHOP_AFTERSALES_INFO-售后审核\n" +
          "56: SHOP_AFTERSALES_INFO-确认收货\n" +
          "57: SHOP_AFTERSALES_INFO-换货发货\n" +
          "58: SHOP_AFTERSALES_INFO-售后终止\n" +
          "59: SHOP_STOCK_INFO-库存查询\n" +
          "60: SHOP_STOCK_INFO-库存更新\n" +
          "61: SHOP_BA_CHAT-客服系统 消息发送\n" +
          "62: SHOP_BA_CHAT-客服系统 获取用户来源\n" +
          "63: SHOP_BA_CHAT-客服系统 修改客服状态\n" +
          "64: SHOP_BA_CHAT-客服系统 关闭\n" +
          "65: COPYRIGHT_MUSIC_DATA-音乐列表 获取媒体元数据\n" +
          "66: COPYRIGHT_MUSIC_DATA-音乐列表 获取媒体资源信息\n" +
          "67: COPYRIGHT_MUSIC_DATA-音乐搜索\n" +
          "68:稿件图片上传\n" +
          "69:专栏稿件上传\n" +
          "70:商品图片上传\n" +
          "71:客服图片上传\n" +
          "q: 退出 ")
    input_choice = input()

    if input_choice == "0":
        sign(client_id, access_token, app_secret)
    elif input_choice == "1":
        oauth(client_id, app_secret)
    elif input_choice == "4":
        video_init(client_id, access_token, app_secret)
    elif input_choice == "7":
        video_arc_complete(client_id, access_token, app_secret)
    elif input_choice == "8":
        arc_add_url(client_id, access_token, app_secret, "")
    elif input_choice == "10":
        arc_view(client_id, access_token, app_secret, "")
    elif input_choice == "11":
        arc_view_list(client_id, access_token, app_secret, "")
    elif input_choice == "13":
        article_edit(client_id, access_token, app_secret, "")
    elif input_choice == "14":
        article_delete(client_id, access_token, app_secret, "")
    elif input_choice == "49":
        address_list(client_id, access_token, app_secret, "")
    elif input_choice == "53":
        after_sale_query_list(client_id, access_token, app_secret, "")
    elif input_choice == "59":
        stock_query(client_id, access_token, app_secret)
    elif input_choice == "60":
        stock_update(client_id, access_token, app_secret)
    elif input_choice == "61":
        conversation_send_msg(client_id, access_token, app_secret, "")
    elif input_choice == "62":
        conversation_customer_user_from(client_id, access_token, app_secret, "")
    elif input_choice == "63":
        conversation_staff_status_update(client_id, access_token, app_secret, "")
    elif input_choice == "64":
        conversation_close(client_id, access_token, app_secret, "")
    elif input_choice == "q":
        print("退出程序")
        return
    else:
        print("无效的命令，请重新输入")

if __name__ == "__main__":
    main()