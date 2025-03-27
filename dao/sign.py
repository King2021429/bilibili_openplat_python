import hmac
import hashlib
from typing import Dict
from model.header import CommonHeader
from model.header import ModelConstants

def create_signature(header: CommonHeader, access_key_secret: str) -> str:
    """生成 Authorization 加密串"""
    s_str = to_sorted_string(header)
    print(f"\n签名:参与加密的字符串:{s_str}")
    return hmac_sha256(access_key_secret, s_str)

def md5(text: str) -> str:
    """MD5 加密"""
    print(f"\n签名:参与 md5 的字符串:{text}")
    hash_obj = hashlib.md5(text.encode("utf-8"))
    return hash_obj.hexdigest()

def hmac_sha256(key: str, data: str) -> str:
    """HMAC-SHA256 算法"""
    mac = hmac.new(
        key.encode("utf-8"),
        data.encode("utf-8"),
        hashlib.sha256
    )
    return hex.from_bytes(mac.digest())

def to_map(h: CommonHeader) -> Dict[str, str]:
    """所有字段转字典"""
    return {
        ModelConstants.BiliTimestampHeader: h.Timestamp,
        ModelConstants.BiliSignatureMethodHeader: h.SignatureMethod,
        ModelConstants.BiliSignatureNonceHeader: h.Nonce,
        ModelConstants.BiliAccessKeyIdHeader: h.AccessKeyId,
        ModelConstants.BiliSignVersionHeader: h.SignatureVersion,
        ModelConstants.BiliContentMD5Header: h.ContentMD5,
        ModelConstants.AuthorizationHeader: h.Authorization,
        ModelConstants.ContentTypeHeader: h.ContentType,
        ModelConstants.AcceptHeader: h.ContentAcceptType,
        ModelConstants.AccessToken: h.AccessToken,
    }

def to_sort_map(h: CommonHeader) -> Dict[str, str]:
    """参与加密的字段转字典"""
    return {
        ModelConstants.BiliTimestampHeader: h.Timestamp,
        ModelConstants.BiliSignatureMethodHeader: h.SignatureMethod,
        ModelConstants.BiliSignatureNonceHeader: h.Nonce,
        ModelConstants.BiliAccessKeyIdHeader: h.AccessKeyId,
        ModelConstants.BiliSignVersionHeader: h.SignatureVersion,
        ModelConstants.BiliContentMD5Header: h.ContentMD5,
    }

def to_sorted_string(h: CommonHeader) -> str:
    """生成需要加密的文本（按键排序）"""
    h_map = to_sort_map(h)
    sorted_keys = sorted(h_map.keys())
    return "\n".join([f"{k}:{h_map[k]}" for k in sorted_keys])