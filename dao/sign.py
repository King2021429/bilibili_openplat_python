import hmac
import hashlib
from typing import Dict
from model import * # 假设 CommonHeader 定义在 model.py 中

def create_signature(header: model.CommonHeader, access_key_secret: str) -> str:
    """生成 Authorization 加密串"""
    s_str = to_sorted_string(header)
    print(f"\n签名:参与加密的字符串:{s_str}")
    return hmac_sha256(access_key_secret, s_str)


def md5(text: str) -> str:
    """MD5 加密"""
    print(f"\n签名:参与md5的字符串:{text}")
    return hashlib.md5(text.encode()).hexdigest()


def hmac_sha256(key: str, data: str) -> str:
    """HMAC-SHA256 算法"""
    return hmac.new(
        key.encode(),
        data.encode(),
        hashlib.sha256
    ).hexdigest()


def to_map(h: CommonHeader) -> Dict[str, str]:
    """所有字段转字典"""
    return {
        model.BILI_TIMESTAMP_HEADER: h.timestamp,
        model.BILI_SIGNATURE_METHOD_HEADER: h.signature_method,
        model.BILI_SIGNATURE_NONCE_HEADER: h.nonce,
        model.BILI_ACCESS_KEY_ID_HEADER: h.access_key_id,
        model.BILI_SIGN_VERSION_HEADER: h.signature_version,
        model.BILI_CONTENT_MD5_HEADER: h.content_md5,
        model.AUTHORIZATION_HEADER: h.authorization,
        model.CONTENT_TYPE_HEADER: h.content_type,
        model.ACCEPT_HEADER: h.content_accept_type,
        model.ACCESS_TOKEN: h.access_token,
    }


def to_sort_map(h: CommonHeader) -> Dict[str, str]:
    """参与加密的字段转字典"""
    return {
        model.BILI_TIMESTAMP_HEADER: h.timestamp,
        model.BILI_SIGNATURE_METHOD_HEADER: h.signature_method,
        model.BILI_SIGNATURE_NONCE_HEADER: h.nonce,
        model.BILI_ACCESS_KEY_ID_HEADER: h.access_key_id,
        model.BILI_SIGN_VERSION_HEADER: h.signature_version,
        model.BILI_CONTENT_MD5_HEADER: h.content_md5,
    }


def to_sorted_string(h: CommonHeader) -> str:
    """生成需要加密的文本（按键排序）"""
    h_map = to_sort_map(h)
    sorted_keys = sorted(h_map.keys())  # 按键排序
    sign_parts = [f"{k}:{v}" for k, v in sorted((k, h_map[k]) for k in sorted_keys)]
    return "\n".join(sign_parts)