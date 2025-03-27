from dao.request import api_request
from model.header import COPYRIGHT_MUSIC_DATA, ModelConstants, BaseResp

# 音乐列表 获取媒体元数据
def music_meta_list(client_id, access_token, app_secret, req_json):
    url = COPYRIGHT_MUSIC_DATA.MUSIC_META_LIST_URL
    resp = api_request(req_json, url, ModelConstants.METHOD_GET, client_id, access_token, app_secret, ModelConstants.BILI_VERSION_V2)
    return BaseResp(resp.get('code', 0), resp.get('message', ''), resp.get('request_id', ''), resp.get('data', {}))

# 音乐列表 获取媒体资源信息
def music_list(client_id, access_token, app_secret, req_json):
    url = COPYRIGHT_MUSIC_DATA.MUSIC_LIST_URL
    resp = api_request(req_json, url, ModelConstants.METHOD_GET, client_id, access_token, app_secret, ModelConstants.BILI_VERSION_V2)
    return BaseResp(resp.get('code', 0), resp.get('message', ''), resp.get('request_id', ''), resp.get('data', {}))

# 音乐搜索
def music_search(client_id, access_token, app_secret, req_json):
    url = COPYRIGHT_MUSIC_DATA.MUSIC_SEARCH_URL
    resp = api_request(req_json, url, ModelConstants.METHOD_GET, client_id, access_token, app_secret, ModelConstants.BILI_VERSION_V2)
    return BaseResp(resp.get('code', 0), resp.get('message', ''), resp.get('request_id', ''), resp.get('data', {}))