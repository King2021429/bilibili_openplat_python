import json
from dao.request import api_request
from model.header import RESOURCE_BASE, ModelConstants
from model.param import CommonMsg, CommonAddShareReq


# 唯一一个v1签名
# 新增共享
def common_add_share(client_id, access_token, app_secret, biz_code):
    # 创建一个 CommonMsg 对象
    common_msg = CommonMsg(
        source="",
        cover="",
        title="投稿标题",
        type_id=172,
        topic_id=1173894,
        video_material_url=[
            "https://1400335750.vod2.myqcloud.com/ff539f7evodcq1400335750/4d9970f01397757888517111156/QGeorKmhB2kA.mp4"
        ]
    )

    # 将对象编码为 JSON 字符串
    try:
        json_string = json.dumps(common_msg.__dict__)
        print(json_string)
    except Exception as e:
        print(f"Error marshaling JSON: {e}")
        return

    common_add_share_req = CommonAddShareReq(
        common_msg=json_string,
        biz_code=biz_code,
        scene_code=ModelConstants.SCENE_CODE
    )

    common_add_share_req_json = json.dumps(common_add_share_req.__dict__)

    return api_request(
        common_add_share_req_json,
        RESOURCE_BASE.RESOURCE_ADD_SHARE_URL,
        ModelConstants.METHOD_POST,
        client_id,
        access_token,
        app_secret,
        ModelConstants.BILI_VERSION
    )