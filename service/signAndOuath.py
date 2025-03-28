import time
import hashlib
import requests
from model.header import CommonHeader, ModelConstants
from dao.sign import create_signature, md5
from dao.ouath import build_url, oauth_req



def Sign(client_id, access_token, app_secret):
    # 输入 reqJson 串
    req_json = input("请输入reqJson串: ")
    # 输入 version
    version = input("请输入version: ")

    timestamp = str(int(time.time()))
    nonce = str(time.time_ns())
    content_md5 = md5(req_json)

    header = CommonHeader(
        content_type=ModelConstants.JSON_TYPE,
        content_accept_type=ModelConstants.JSON_TYPE,
        timestamp=timestamp,
        signature_method=ModelConstants.HMAC_SHA256,
        signature_version=version,
        authorization="",
        nonce=nonce,
        access_key_id=client_id,
        content_md5=content_md5,
        access_token=access_token
    )
    header.Authorization = create_signature(header, app_secret)
    header_dict = {
        "ContentType": header.ContentType,
        "ContentAcceptType": header.ContentAcceptType,
        "Timestamp": header.Timestamp,
        "SignatureMethod": header.SignatureMethod,
        "SignatureVersion": header.SignatureVersion,
        "Authorization": header.Authorization,
        "Nonce": header.Nonce,
        "AccessKeyId": header.AccessKeyId,
        "ContentMD5": header.ContentMD5,
        "AccessToken": header.AccessToken
    }
    print(f"\n请求头:{header_dict}")


def Oauth(client_id, app_secret):
    # 基础 URL
    base_url = "https://api.bilibili.com/x/account-oauth2/v1/token"
    # 输入 code
    code = input("请输入 code: ")
    # 参数字典
    params = {
        "client_id": client_id,
        "client_secret": app_secret,
        "grant_type": "authorization_code",
        "code": code
    }
    # 调用拼接函数
    full_url, err = build_url(base_url, params)
    if err:
        print("Error:", err)
        return
    # 打印拼接好的完整 URL
    print("Full URL:", full_url)
    oauth_req(full_url)