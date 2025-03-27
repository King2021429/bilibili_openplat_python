
import os
import io
import hashlib
import hmac
import time
import json
from datetime import datetime
import requests
import sign


class CommonHeader:
    def __init__(self, content_type, content_accept_type, timestamp, signature_method, signature_version, authorization, nonce, access_key_id, content_md5, access_token):
        self.ContentType = content_type
        self.ContentAcceptType = content_accept_type
        self.Timestamp = timestamp
        self.SignatureMethod = signature_method
        self.SignatureVersion = signature_version
        self.Authorization = authorization
        self.Nonce = nonce
        self.AccessKeyId = access_key_id
        self.ContentMD5 = content_md5
        self.AccessToken = access_token

    def to_dict(self):
        return {
            "Content-Type": self.ContentType,
            "Content-Accept-Type": self.ContentAcceptType,
            "Timestamp": self.Timestamp,
            "Signature-Method": self.SignatureMethod,
            "Signature-Version": self.SignatureVersion,
            "Authorization": self.Authorization,
            "Nonce": self.Nonce,
            "Access-Key-Id": self.AccessKeyId,
            "Content-MD5": self.ContentMD5,
            "Access-Token": self.AccessToken
        }



def PicRequest(request_url, pic_url, client_id, access_token, app_secret, version):
    with open(pic_url, 'rb') as f:
        files = {'file': (os.path.basename(pic_url), f)}

    data = {
        'staff_id': '42002'
    }

    timestamp = str(int(time.time()))
    nonce = str(int(datetime.now().timestamp() * 1e9))
    body_str_mds = sign.md5("")

    headers = {
        "Accept": "application/json",
        "x-bili-timestamp": timestamp,
        "x-bili-signature-method": "HMAC-SHA256",
        "x-bili-signature-version": version,
        "x-bili-signature-nonce": nonce,
        "x-bili-accesskeyid": client_id,
        "x-bili-content-md5": body_str_mds,
        "access-token": access_token
    }

    header_obj = CommonHeader(
        ContentType=headers["Content-Type"],
        ContentAcceptType="application/json",
        Timestamp=timestamp,
        SignatureMethod="HMAC-SHA256",
        SignatureVersion=version,
        Authorization="",
        Nonce=nonce,
        AccessKeyId=client_id,
        ContentMD5=body_str_mds,
        AccessToken=access_token
    )

    headers["Authorization"] = sign.create_signature(header_obj.to_dict(), app_secret)

    response = requests.post(request_url, files=files, data=data, headers=headers)
    if response.status_code != 200:
        print(response.text)
        return None, Exception(f"Request failed with status code {response.status_code}")

    return response.json(), None

# 示例调用
# resp, err = PicRequest("https://example.com/upload", "/path/to/image.jpg", "your_client_id", "your_access_token", "your_app_secret", "1.0")
# if err is not None:
#     print(err)
# else:
#     print(resp)


