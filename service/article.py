from dao.request import api_request
from model.header import (
    ATC_BASE,
    ModelConstants
)


# 文章投稿
def article_add(client_id, access_token, app_secret, req_json):
    url = ATC_BASE.ARTICLE_ADD_URL
    return api_request(req_json, url, ModelConstants.METHOD_POST, client_id, access_token, app_secret,
                       ModelConstants.BILI_VERSION_V2)


# 文章编辑
def article_edit(client_id, access_token, app_secret, req_json):
    url = ATC_BASE.ARTICLE_EDIT
    return api_request(req_json, url, ModelConstants.METHOD_POST, client_id, access_token, app_secret,
                       ModelConstants.BILI_VERSION_V2)


# 文章删除
def article_delete(client_id, access_token, app_secret, req_json):
    url = ATC_BASE.ARTICLE_DELETE
    return api_request(req_json, url, ModelConstants.METHOD_POST, client_id, access_token, app_secret,
                       ModelConstants.BILI_VERSION_V2)


# 文章详情
def article_detail(client_id, access_token, app_secret, req_json):
    url = ATC_BASE.ARTICLE_DETAIL
    return api_request(req_json, url, ModelConstants.METHOD_GET, client_id, access_token, app_secret,
                       ModelConstants.BILI_VERSION_V2)


# 文章列表
def article_list(client_id, access_token, app_secret, req_json):
    url = ATC_BASE.ARTICLE_LIST
    return api_request(req_json, url, ModelConstants.METHOD_GET, client_id, access_token, app_secret,
                       ModelConstants.BILI_VERSION_V2)


# 文章分类
def article_categories(client_id, access_token, app_secret, req_json):
    url = ATC_BASE.ARTICLE_CATEGORIES
    return api_request(req_json, url, ModelConstants.METHOD_GET, client_id, access_token, app_secret,
                       ModelConstants.BILI_VERSION_V2)


# 获取视频、文章卡片信息
def article_card(client_id, access_token, app_secret, req_json):
    url = ATC_BASE.ARTICLE_CARD
    return api_request(req_json, url, ModelConstants.METHOD_GET, client_id, access_token, app_secret,
                       ModelConstants.BILI_VERSION_V2)


# 文集提交
def anthology_add(client_id, access_token, app_secret, req_json):
    url = ATC_BASE.ANTHOLOGY_ADD
    return api_request(req_json, url, ModelConstants.METHOD_POST, client_id, access_token, app_secret,
                       ModelConstants.BILI_VERSION_V2)


# 文集信息编辑
def anthology_edit(client_id, access_token, app_secret, req_json):
    url = ATC_BASE.ANTHOLOGY_EDIT
    return api_request(req_json, url, ModelConstants.METHOD_POST, client_id, access_token, app_secret,
                       ModelConstants.BILI_VERSION_V2)


# 文集下文章列表修改
def article_belong(client_id, access_token, app_secret, req_json):
    url = ATC_BASE.ARTICLE_BELONG
    return api_request(req_json, url, ModelConstants.METHOD_POST, client_id, access_token, app_secret,
                       ModelConstants.BILI_VERSION_V2)


# 文集删除
def anthology_delete(client_id, access_token, app_secret, req_json):
    url = ATC_BASE.ANTHOLOGY_DELETE
    return api_request(req_json, url, ModelConstants.METHOD_POST, client_id, access_token, app_secret,
                       ModelConstants.BILI_VERSION_V2)


# 文集列表查询
def anthology_list(client_id, access_token, app_secret, req_json):
    url = ATC_BASE.ANTHOLOGY_LIST
    return api_request(req_json, url, ModelConstants.METHOD_GET, client_id, access_token, app_secret,
                       ModelConstants.BILI_VERSION_V2)


# 文集详情查询
def anthology_detail(client_id, access_token, app_secret, req_json):
    url = ATC_BASE.ANTHOLOGY_DETAIL
    return api_request(req_json, url, ModelConstants.METHOD_GET, client_id, access_token, app_secret,
                       ModelConstants.BILI_VERSION_V2)