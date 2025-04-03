import requests
from requests_toolbelt.multipart import MultipartEncoder
import hashlib
import time
import uuid

import model
from dao.sign import create_signature, md5
from model.header import MAIN_OPEN_PLATFORM_HTTP_HOST, ModelConstants
from model.header import CommonHeader



def ArticleAdd(requestUrl, clientId, accessToken, appSecret, version):
    # 构建 multipart 表单数据
    fields = {
        'title': (None, input("请输入title: ").rstrip('\n')),
        'category': (None, input("请输入category: ").rstrip('\n')),
        'template_id': (None, input("请输入template_id: ").rstrip('\n')),
        'summary': (None, input("请输入summary: ").rstrip('\n')),
        'content': (None, input("请输入content: ").rstrip('\n'))
    }
    mp_encoder = MultipartEncoder(fields=fields)

    # 构建请求头
    timestamp = str(int(time.time()))
    nonce = str(uuid.uuid4())
    headers = {
        'Accept': 'application/json',
        'x-bili-timestamp': timestamp,
        'x-bili-signature-method': 'HMAC-SHA256',
        'x-bili-signature-version': version,
        'x-bili-signature-nonce': nonce,
        'x-bili-accesskeyid': clientId,
        'x-bili-content-md5': md5(""),
        'access-token': accessToken,
        'Content-Type': mp_encoder.content_type
    }

    # 生成签名（需要实现 CreateSignature 函数）
    common_header = CommonHeader (
        ContentType="multipart/form-data",
        ContentAcceptType=ModelConstants.JSON_TYPE,
        Timestamp=timestamp,
        SignatureMethod=ModelConstants.HMAC_SHA256,
        SignatureVersion=version,
        Nonce=nonce,
        ContentMD5=md5(""),
        AccessToken=accessToken
    )
    headers['Authorization'] = create_signature(common_header, appSecret)

    # 发送请求
    response = requests.post(
        url=f"{MAIN_OPEN_PLATFORM_HTTP_HOST}{requestUrl}",
        data=mp_encoder,
        headers=headers
    )

    print(response.text)
    return response.json()