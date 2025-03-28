from dao.request import api_request
from model.header import USER_INFO, ModelConstants

# 查询用户账号信息
def AccountInfo(client_id, access_token, app_secret):
    url = USER_INFO.ACCOUNT_INFO_URL
    try:
        resp = api_request("", url, ModelConstants.METHOD_GET, client_id, access_token, app_secret, ModelConstants.BILI_VERSION_V2)
        return resp
    except Exception as err:
        print(f"AccountInfo err:{err}")
        return None

# 查询用户已授权权限列表
def AccountScope(client_id, access_token, app_secret):
    url = USER_INFO.USER_SCOPES_URL
    try:
        resp = api_request("", url, ModelConstants.METHOD_GET, client_id, access_token, app_secret, ModelConstants.BILI_VERSION_V2)
        return resp
    except Exception as err:
        print(f"AccountScope err:{err}")
        return None