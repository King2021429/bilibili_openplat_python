import hashlib
import hmac
import json
from collections import OrderedDict


def create_signature(header: dict, access_key_secret: str) -> str:
    """生成Authorization加密串"""
    s_str = to_sorted_string(header)
    print(f"\n签名:参与加密的字符串:{s_str}")
    return hmac_sha256(access_key_secret, s_str)


def md5_encrypt(data: str) -> str:
    """MD5加密"""
    print(f"\n签名:参与md5的字符串:{data}")
    return hashlib.md5(data.encode()).hexdigest()


def hmac_sha256(key: str, data: str) -> str:
    """HMAC-SHA256算法"""
    key_bytes = key.encode()
    data_bytes = data.encode()
    return hmac.new(key_bytes, data_bytes, hashlib.sha256).hexdigest()


def to_map(header: dict) -> dict:
    """所有字段转字典"""
    return {
        "X-Bili-Timestamp": header.get("X-Bili-Timestamp"),
        "X-Bili-Signature-Method": header.get("X-Bili-Signature-Method"),
        "X-Bili-Signature-Nonce": header.get("X-Bili-Signature-Nonce"),
        "X-Bili-AccessKey-ID": header.get("X-Bili-AccessKey-ID"),
        "X-Bili-Sign-Version": header.get("X-Bili-Sign-Version"),
        "X-Bili-Content-MD5": header.get("X-Bili-Content-MD5"),
        "Authorization": header.get("Authorization"),
        "Content-Type": header.get("Content-Type"),
        "Accept": header.get("Accept"),
        "X-Bili-AccessToken": header.get("X-Bili-AccessToken"),
    }


def to_sort_map(header: dict) -> dict:
    """参与加密的字段转字典"""
    return {
        "X-Bili-Timestamp": header.get("X-Bili-Timestamp"),
        "X-Bili-Signature-Method": header.get("X-Bili-Signature-Method"),
        "X-Bili-Signature-Nonce": header.get("X-Bili-Signature-Nonce"),
        "X-Bili-AccessKey-ID": header.get("X-Bili-AccessKey-ID"),
        "X-Bili-Sign-Version": header.get("X-Bili-Sign-Version"),
        "X-Bili-Content-MD5": header.get("X-Bili-Content-MD5"),
    }


def to_sorted_string(header: dict) -> str:
    """生成需要加密的文本"""
    sorted_map = OrderedDict(sorted(to_sort_map(header).items()))
    sign_str = '\n'.join([f"{k}:{v}" for k, v in sorted_map.items()])
    return sign_str.rstrip('\n')


# 示例用法
if __name__ == "__main__":
    # 示例请求头
    headers = {
        "X-Bili-Timestamp": "1638508800",
        "X-Bili-Signature-Method": "HMAC-SHA256",
        "X-Bili-Signature-Nonce": "123456",
        "X-Bili-AccessKey-ID": "AKIDEXAMPLE",
        "X-Bili-Sign-Version": "1.0",
        "X-Bili-Content-MD5": "d41d8cd98f00b204e9800998ecf8427e",
        "Authorization": "",
        "Content-Type": "application/json",
        "Accept": "application/json",
        "X-Bili-AccessToken": "token123"
    }
    access_key_secret = "YOUR_ACCESS_KEY_SECRET"

    signature = create_signature(headers, access_key_secret)
    print(f"生成的签名: {signature}")