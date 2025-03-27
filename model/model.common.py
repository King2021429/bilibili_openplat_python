import json


class BaseResp:
    def __init__(self, code: int, message: str, request_id: str, data):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.data = data

    def to_json(self):
        return json.dumps(self.__dict__)


# 域名
UAT_MAIN_OPEN_PLATFORM_HTTP_HOST = "https://uat-member.bilibili.com"
MAIN_OPEN_PLATFORM_HTTP_HOST = "https://member.bilibili.com"

SCENE_CODE = "ARC_APP_SHARE"

