import requests
import os
import hashlib
import time
from model.header import CommonHeader, ModelConstants
from dao.sign import create_signature, md5

def PicRequest(requestUrl, picUrl, clientId, accessToken, appSecret, version):
    # 准备表单数据
    payload = {
        "staff_id": "42002"
    }
    files = {
        "file": (os.path.basename(picUrl), open(picUrl, 'rb'))
    }

    # 计算 MD5
    bodyStrMds = md5("")

    # 生成时间戳和随机数
    timestamp = str(int(time.time()))
    nonce = str(time.time_ns())

    # 创建请求头
    header = CommonHeader(
        ContentType="multipart/form-data",
        ContentAcceptType=ModelConstants.JSON_TYPE,
        Timestamp=timestamp,
        SignatureMethod=ModelConstants.HMAC_SHA256,
        SignatureVersion=version,
        Nonce=nonce,
        AccessKeyId=clientId,
        ContentMD5=bodyStrMds,
        AccessToken=accessToken
    )

    # 计算签名
    header.Authorization = create_signature(header, appSecret)

    # 构造请求头
    headers = {
        "Accept": ModelConstants.JSON_TYPE,
        "x-bili-timestamp": timestamp,
        "x-bili-signature-method": ModelConstants.HMAC_SHA256,
        "x-bili-signature-version": version,
        "x-bili-signature-nonce": nonce,
        "x-bili-accesskeyid": clientId,
        "x-bili-content-md5": bodyStrMds,
        "access-token": accessToken,
        "Authorization": header.Authorization
    }

    try:
        # 发送请求
        response = requests.post(requestUrl, data=payload, files=files, headers=headers)
        response.raise_for_status()

        # 打印响应
        print(response.text)

        return response.json()

    except requests.exceptions.RequestException as e:
        print(f"请求错误: {e}")
        return {"code": -1, "message": str(e)}
    except ValueError as e:
        print(f"响应解析错误: {e}")
        return {"code": -1, "message": str(e)}