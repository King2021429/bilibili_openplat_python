import urllib.request
import urllib.parse
from typing import Dict, Tuple


def oauth_req(url: str) -> None:
    """
    发送 OAuth 请求（POST 方法）并打印响应内容

    :param url: 请求的 URL 地址
    """
    method = "POST"
    headers = {
        "Accept": "*/*",
        "Host": "api.bilibili.com",
        "Connection": "keep-alive"
    }

    # 创建请求对象
    req = urllib.request.Request(url, method=method, headers=headers)

    try:
        with urllib.request.urlopen(req) as res:
            body = res.read().decode("utf-8")
            print(body)
    except Exception as e:
        print(f"请求失败: {e}")


def build_url(base_url: str, params: Dict[str, str]) -> Tuple[str, Exception]:
    """
    拼接 URL 参数的函数

    :param base_url: 基础 URL
    :param params: 需要拼接的参数（键值对）
    :return: 拼接后的完整 URL 或错误信息
    """
    try:
        # 解析基础 URL
        parsed_url = urllib.parse.urlparse(base_url)

        # 解析原查询参数
        query_dict = urllib.parse.parse_qs(parsed_url.query)

        # 合并新参数
        for key, value in params.items():
            if key in query_dict:
                query_dict[key].append(value)
            else:
                query_dict[key] = [value]

        # 重新编码查询参数
        new_query = urllib.parse.urlencode(query_dict, doseq=True)

        # 构建新 URL
        new_url = urllib.parse.urlunparse((
            parsed_url.scheme,
            parsed_url.netloc,
            parsed_url.path,
            parsed_url.params,
            new_query,
            parsed_url.fragment
        ))
        return new_url, None
    except Exception as e:
        return "", e