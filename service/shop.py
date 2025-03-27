from dao.request import api_request
from model.header import SHOP_STORE_INFO, SHOP_COMMODITY_INFO, SHOP_ORDER_INFO, SHOP_LOGISTICS_INFO, SHOP_AFTERSALES_INFO, ModelConstants
from model.header import BaseResp

# 获取店铺信息
def shop_info_get_url(client_id, access_token, app_secret, req_json):
    url = SHOP_STORE_INFO.SHOP_INFO_GET_URL
    resp = api_request(req_json, url, ModelConstants.METHOD_GET, client_id, access_token, app_secret, ModelConstants.BILI_VERSION_V2)
    return BaseResp(resp.get('code', 0), resp.get('message', ''), resp.get('request_id', ''), resp.get('data', {}))

# 商品发布
def product_add(client_id, access_token, app_secret, req_json):
    url = SHOP_COMMODITY_INFO.PRODUCT_ADD_URL
    resp = api_request(req_json, url, ModelConstants.METHOD_POST, client_id, access_token, app_secret, ModelConstants.BILI_VERSION_V2)
    return BaseResp(resp.get('code', 0), resp.get('message', ''), resp.get('request_id', ''), resp.get('data', {}))

# 查询商品列表
def commodity_item_list(client_id, access_token, app_secret, req_json):
    url = SHOP_COMMODITY_INFO.COMMODITY_ITEM_LIST_URL
    resp = api_request(req_json, url, ModelConstants.METHOD_GET, client_id, access_token, app_secret, ModelConstants.BILI_VERSION_V2)
    return BaseResp(resp.get('code', 0), resp.get('message', ''), resp.get('request_id', ''), resp.get('data', {}))

# 查询发品配置
def product_get_publish_rule(client_id, access_token, app_secret, req_json):
    url = SHOP_COMMODITY_INFO.PRODUCT_GET_PUBLISH_RULE_URL
    resp = api_request(req_json, url, ModelConstants.METHOD_POST, client_id, access_token, app_secret, ModelConstants.BILI_VERSION_V2)
    return BaseResp(resp.get('code', 0), resp.get('message', ''), resp.get('request_id', ''), resp.get('data', {}))

# 获取商品详情
def product_detail(client_id, access_token, app_secret, req_json):
    url = SHOP_COMMODITY_INFO.PRODUCT_DETAIL
    resp = api_request(req_json, url, ModelConstants.METHOD_GET, client_id, access_token, app_secret, ModelConstants.BILI_VERSION_V2)
    return BaseResp(resp.get('code', 0), resp.get('message', ''), resp.get('request_id', ''), resp.get('data', {}))

# 编辑商品
def product_edit(client_id, access_token, app_secret, req_json):
    url = SHOP_COMMODITY_INFO.PRODUCT_EDIT
    resp = api_request(req_json, url, ModelConstants.METHOD_POST, client_id, access_token, app_secret, ModelConstants.BILI_VERSION_V2)
    return BaseResp(resp.get('code', 0), resp.get('message', ''), resp.get('request_id', ''), resp.get('data', {}))

# 删除商品
def product_del(client_id, access_token, app_secret, req_json):
    url = SHOP_COMMODITY_INFO.PRODUCT_DEL
    resp = api_request(req_json, url, ModelConstants.METHOD_POST, client_id, access_token, app_secret, ModelConstants.BILI_VERSION_V2)
    return BaseResp(resp.get('code', 0), resp.get('message', ''), resp.get('request_id', ''), resp.get('data', {}))

# 获取商品分类属性
def product_get_cate_property(client_id, access_token, app_secret, req_json):
    url = SHOP_COMMODITY_INFO.PRODUCT_GET_CATE_PROPERTY
    resp = api_request(req_json, url, ModelConstants.METHOD_GET, client_id, access_token, app_secret, ModelConstants.BILI_VERSION_V2)
    return BaseResp(resp.get('code', 0), resp.get('message', ''), resp.get('request_id', ''), resp.get('data', {}))

# 获取商品分类合格列表
def commodity_category_qualified_list(client_id, access_token, app_secret, req_json):
    url = SHOP_COMMODITY_INFO.COMMODITY_CATEGORY_QUALIFIED_LIST
    resp = api_request(req_json, url, ModelConstants.METHOD_GET, client_id, access_token, app_secret, ModelConstants.BILI_VERSION_V2)
    return BaseResp(resp.get('code', 0), resp.get('message', ''), resp.get('request_id', ''), resp.get('data', {}))

# 订单敏感信息解密
def order_batch_decrypt(client_id, access_token, app_secret, req_json):
    url = SHOP_ORDER_INFO.ORDER_BATCH_DECRYPT
    resp = api_request(req_json, url, ModelConstants.METHOD_POST, client_id, access_token, app_secret, ModelConstants.BILI_VERSION_V2)
    return BaseResp(resp.get('code', 0), resp.get('message', ''), resp.get('request_id', ''), resp.get('data', {}))

# 流量卡审核信息回传
def order_review(client_id, access_token, app_secret, req_json):
    url = SHOP_ORDER_INFO.ORDER_REVIEW
    resp = api_request(req_json, url, ModelConstants.METHOD_POST, client_id, access_token, app_secret, ModelConstants.BILI_VERSION_V2)
    return BaseResp(resp.get('code', 0), resp.get('message', ''), resp.get('request_id', ''), resp.get('data', {}))

# 商家备注
def order_remark(client_id, access_token, app_secret, req_json):
    url = SHOP_ORDER_INFO.ORDER_REMARK
    resp = api_request(req_json, url, ModelConstants.METHOD_POST, client_id, access_token, app_secret, ModelConstants.BILI_VERSION_V2)
    return BaseResp(resp.get('code', 0), resp.get('message', ''), resp.get('request_id', ''), resp.get('data', {}))

# 订单详情查询
def order_detail(client_id, access_token, app_secret, req_json):
    url = SHOP_ORDER_INFO.ORDER_DETAIL
    resp = api_request(req_json, url, ModelConstants.METHOD_GET, client_id, access_token, app_secret, ModelConstants.BILI_VERSION_V2)
    return BaseResp(resp.get('code', 0), resp.get('message', ''), resp.get('request_id', ''), resp.get('data', {}))

# 订单列表查询
def order_search_list(client_id, access_token, app_secret, req_json):
    url = SHOP_ORDER_INFO.ORDER_SEARCH_LIST
    resp = api_request(req_json, url, ModelConstants.METHOD_GET, client_id, access_token, app_secret, ModelConstants.BILI_VERSION_V2)
    return BaseResp(resp.get('code', 0), resp.get('message', ''), resp.get('request_id', ''), resp.get('data', {}))

# 发货回掉
def logistics_add(client_id, access_token, app_secret, req_json):
    url = SHOP_LOGISTICS_INFO.LOGISTICS_ADD
    resp = api_request(req_json, url, ModelConstants.METHOD_POST, client_id, access_token, app_secret, ModelConstants.BILI_VERSION_V2)
    return BaseResp(resp.get('code', 0), resp.get('message', ''), resp.get('request_id', ''), resp.get('data', {}))

# 物流编辑
def logistics_edit(client_id, access_token, app_secret, req_json):
    url = SHOP_LOGISTICS_INFO.LOGISTICS_EDIT
    resp = api_request(req_json, url, ModelConstants.METHOD_POST, client_id, access_token, app_secret, ModelConstants.BILI_VERSION_V2)
    return BaseResp(resp.get('code', 0), resp.get('message', ''), resp.get('request_id', ''), resp.get('data', {}))

# 获取快递公司列表
def logistics_company_list(client_id, access_token, app_secret, req_json):
    url = SHOP_LOGISTICS_INFO.LOGISTICS_COMPANY_LIST
    resp = api_request(req_json, url, ModelConstants.METHOD_GET, client_id, access_token, app_secret, ModelConstants.BILI_VERSION_V2)
    return BaseResp(resp.get('code', 0), resp.get('message', ''), resp.get('request_id', ''), resp.get('data', {}))

# 地址库创建
def address_create(client_id, access_token, app_secret, req_json):
    url = SHOP_LOGISTICS_INFO.ADDRESS_CREATE
    resp = api_request(req_json, url, ModelConstants.METHOD_POST, client_id, access_token, app_secret, ModelConstants.BILI_VERSION_V2)
    return BaseResp(resp.get('code', 0), resp.get('message', ''), resp.get('request_id', ''), resp.get('data', {}))

# 批量查询地址库列表
def address_list(client_id, access_token, app_secret, req_json):
    url = SHOP_LOGISTICS_INFO.ADDRESS_LIST
    resp = api_request(req_json, url, ModelConstants.METHOD_GET, client_id, access_token, app_secret, ModelConstants.BILI_VERSION_V2)
    return BaseResp(resp.get('code', 0), resp.get('message', ''), resp.get('request_id', ''), resp.get('data', {}))

# 获取全量省份信息
def address_get_province(client_id, access_token, app_secret, req_json):
    url = SHOP_LOGISTICS_INFO.ADDRESS_GET_PROVINCE
    resp = api_request(req_json, url, ModelConstants.METHOD_GET, client_id, access_token, app_secret, ModelConstants.BILI_VERSION_V2)
    return BaseResp(resp.get('code', 0), resp.get('message', ''), resp.get('request_id', ''), resp.get('data', {}))

# 根据省获取全量三级地址
def address_get_areas_by_province(client_id, access_token, app_secret, req_json):
    url = SHOP_LOGISTICS_INFO.ADDRESS_GET_AREAS_BY_PROVINCE
    resp = api_request(req_json, url, ModelConstants.METHOD_GET, client_id, access_token, app_secret, ModelConstants.BILI_VERSION_V2)
    return BaseResp(resp.get('code', 0), resp.get('message', ''), resp.get('request_id', ''), resp.get('data', {}))

# 运费模板列表查询
def logistics_freight_template_list(client_id, access_token, app_secret, req_json):
    url = SHOP_LOGISTICS_INFO.LOGISTICS_FREIGHT_TEMPLATE_LIST
    resp = api_request(req_json, url, ModelConstants.METHOD_GET, client_id, access_token, app_secret, ModelConstants.BILI_VERSION_V2)
    return BaseResp(resp.get('code', 0), resp.get('message', ''), resp.get('request_id', ''), resp.get('data', {}))

# 售后列表查询
def after_sale_query_list(client_id, access_token, app_secret, req_json):
    url = SHOP_AFTERSALES_INFO.AFTER_SALE_QUERY_LIST
    resp = api_request(req_json, url, ModelConstants.METHOD_GET, client_id, access_token, app_secret, ModelConstants.BILI_VERSION_V2)
    return BaseResp(resp.get('code', 0), resp.get('message', ''), resp.get('request_id', ''), resp.get('data', {}))

# 售后详情查询
def after_sale_query_detail(client_id, access_token, app_secret, req_json):
    url = SHOP_AFTERSALES_INFO.AFTER_SALE_QUERY_DETAIL
    resp = api_request(req_json, url, ModelConstants.METHOD_GET, client_id, access_token, app_secret, ModelConstants.BILI_VERSION_V2)
    return BaseResp(resp.get('code', 0), resp.get('message', ''), resp.get('request_id', ''), resp.get('data', {}))

# 售后审核
def after_sale_check_after_sale(client_id, access_token, app_secret, req_json):
    url = SHOP_AFTERSALES_INFO.AFTER_SALE_CHECK_AFTER_SALE
    resp = api_request(req_json, url, ModelConstants.METHOD_POST, client_id, access_token, app_secret, ModelConstants.BILI_VERSION_V2)
    return BaseResp(resp.get('code', 0), resp.get('message', ''), resp.get('request_id', ''), resp.get('data', {}))

# 确认收货
def after_sale_confirm_receipt(client_id, access_token, app_secret, req_json):
    url = SHOP_AFTERSALES_INFO.AFTER_SALE_CONFIRM_RECEIPT
    resp = api_request(req_json, url, ModelConstants.METHOD_POST, client_id, access_token, app_secret, ModelConstants.BILI_VERSION_V2)
    return BaseResp(resp.get('code', 0), resp.get('message', ''), resp.get('request_id', ''), resp.get('data', {}))

# 换货发货
def after_sale_barter_ship(client_id, access_token, app_secret, req_json):
    url = SHOP_AFTERSALES_INFO.AFTER_SALE_BARTER_SHIP
    resp = api_request(req_json, url, ModelConstants.METHOD_POST, client_id, access_token, app_secret, ModelConstants.BILI_VERSION_V2)
    return BaseResp(resp.get('code', 0), resp.get('message', ''), resp.get('request_id', ''), resp.get('data', {}))

# 售后终止
def after_sale_stop(client_id, access_token, app_secret, req_json):
    url = SHOP_AFTERSALES_INFO.AFTER_SALE_STOP
    resp = api_request(req_json, url, ModelConstants.METHOD_POST, client_id, access_token, app_secret, ModelConstants.BILI_VERSION_V2)
    return BaseResp(resp.get('code', 0), resp.get('message', ''), resp.get('request_id', ''), resp.get('data', {}))