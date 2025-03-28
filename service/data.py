from model.header import USER_DATA, ModelConstants, ARC_DATA, ATC_DATA
from dao.request import api_request


# USER_DATA 获取用户数据 GET
def UserData(client_id, access_token, app_secret, req_json):
    url = USER_DATA.DATA_USER_STAT_URL
    return api_request(req_json, url, ModelConstants.METHOD_GET, client_id, access_token, app_secret, ModelConstants.BILI_VERSION_V2)


# 获取单个稿件数据 GET
def ArcStat(client_id, access_token, app_secret, req_json):
    url = ARC_DATA.ARC_STAT_URL
    return api_request(req_json, url, ModelConstants.METHOD_GET, client_id, access_token, app_secret, ModelConstants.BILI_VERSION_V2)


# 获取整体稿件增量数据 GET
def ArcIncStats(client_id, access_token, app_secret, req_json):
    url = ARC_DATA.ARC_INC_STATS
    return api_request(req_json, url, ModelConstants.METHOD_GET, client_id, access_token, app_secret, ModelConstants.BILI_VERSION_V2)


# 获取单一专栏数据 GET
def ArtStat(client_id, access_token, app_secret, req_json):
    url = ATC_DATA.ART_STAT_URL
    return api_request(req_json, url, ModelConstants.METHOD_GET, client_id, access_token, app_secret, ModelConstants.BILI_VERSION_V2)


# 获取整体投稿增量数据 GET
def ArtIncStats(client_id, access_token, app_secret, req_json):
    url = ATC_DATA.ART_INC_STATS
    return api_request(req_json, url, ModelConstants.METHOD_GET, client_id, access_token, app_secret, ModelConstants.BILI_VERSION_V2)
