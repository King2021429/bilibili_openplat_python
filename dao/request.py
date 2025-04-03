import json
import time
import hashlib
import requests
from typing import Dict, Any
from dao.sign import create_signature, md5  # 假设签名相关函数在 dao/sign.py 中
from model.header import MAIN_OPEN_PLATFORM_HTTP_HOST,ModelConstants,CommonHeader # 调整实际导入路径


def api_request(
        req_json: str,
        request_url: str,
        method: str,
        client_id: str,
        access_token: str,
        app_secret: str,
        version: str
) -> Dict[str, Any]:
    """
    HTTP 请求方法
    :param req_json: 请求参数 JSON 字符串
    :param request_url: 请求 URL
    :param method: 请求方法
    :param client_id: 应用 ID
    :param access_token: 应用 Token
    :param app_secret: 应用秘钥
    :param version: 版本号
    :return: 包含响应数据的字典
    """
    # 生成请求头
    timestamp = str(int(time.time()))
    nonce = str(time.time_ns())
    content_md5 = md5(req_json)

    header = CommonHeader(
        ContentType=ModelConstants.JSON_TYPE,
        ContentAcceptType=ModelConstants.JSON_TYPE,
        Timestamp=timestamp,
        SignatureMethod=ModelConstants.HMAC_SHA256,
        SignatureVersion=version,
        Nonce=nonce,
        AccessKeyId=client_id,
        ContentMD5=content_md5,
        AccessToken=access_token
    )
    header.Authorization = create_signature(header, app_secret)

    # 构造请求
    headers = {
        "Content-Type": header.JsonType,
        **{
            "x-bili-timestamp": header.Timestamp,
            "x-bili-signature-method": header.SignatureMethod,
            "x-bili-signature-nonce": header.Nonce,
            "x-bili-accesskeyid": header.AccessKeyId,
            "x-bili-signature-version": header.SignatureVersion,
            "x-bili-content-md5": header.ContentMD5,
            "Authorization": header.Authorization,
            "access-token": header.AccessToken
        }
    }

    full_url = f"{MAIN_OPEN_PLATFORM_HTTP_HOST}{request_url}"
    print(f"\n请求url:{full_url}")
    print(f"\n请求头:{headers}")

    try:
        response = requests.request(
            method=method,
            url=full_url,
            headers=headers,
            data=req_json
        )
        response.raise_for_status()
        resp_data = response.json()

        # 处理响应打印
        print(f"\n返回参数code:{resp_data.get('code', 0)}")
        print(f"\n返回参数message:{resp_data.get('message', '')}")
        print(f"\n返回参数request_id:{resp_data.get('request_id', '')}")
        print("\n返回参数data:")
        print(json.dumps(resp_data.get('data', {}), indent=2))

        return resp_data
    except requests.exceptions.RequestException as e:
        print(f"请求错误: {e}")
        return {"code": -1, "message": str(e)}
    except json.JSONDecodeError as e:
        print(f"响应解析错误: {e}")
        return {"code": -1, "message": str(e)}