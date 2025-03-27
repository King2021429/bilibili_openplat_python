import json

# ------------- 用户信息相关 URL -------------
class USER_INFO:
    ACCOUNT_INFO_URL = "/arcopen/fn/user/account/info"   # 获取用户公开信息 GET
    USER_SCOPES_URL = "/arcopen/fn/user/account/scopes" # 查询用户已授权权限列表 GET


# ------------- 稿件相关 URL -------------
class ARC_BASE:
    ARC_INIT_URL = "/arcopen/fn/archive/video/init"                  # 文件上传预处理
    ARC_COMPLETE = "/arcopen/fn/archive/video/complete?upload_token=7213c24789bf42b3a3482b7c7d9a597f"  # 文件分片合片
    ARC_ADD_URL = "/arcopen/fn/archive/add"                         # 稿件提交 POST
    ARC_ADD_FETCH = "/arcopen/fn/archive/add-fetch"                 # 稿件提交fetch模式
    ARC_EDIT = "/arcopen/fn/archive/edit"                          # 稿件编辑
    ARC_DEL = "/arcopen/fn/archive/delete"                        # 稿件删除
    ARC_VIEW = "/arcopen/fn/archive/view"                          # 稿件查询
    ARC_VIEW_LIST = "/arcopen/fn/archive/viewlist"                # 稿件列表查询


# ------------- 专栏/文集相关 URL -------------
class ATC_BASE:
    # 文章
    ARTICLE_ADD_URL = "/arcopen/fn/article/add"       # 投稿 POST
    ARTICLE_EDIT = "/arcopen/fn/article/edit"
    ARTICLE_DELETE = "/arcopen/fn/article/delete"
    ARTICLE_DETAIL = "/arcopen/fn/article/detail"
    ARTICLE_LIST = "/arcopen/fn/article/list"
    ARTICLE_CATEGORIES = "/arcopen/fn/article/category"
    ARTICLE_CARD = "/arcopen/fn/article/card"         # 获取视频、文章卡片信息 GET

    # 文集
    ANTHOLOGY_ADD = "/arcopen/fn/article/anthology/add"      # 文集提交
    ANTHOLOGY_EDIT = "/arcopen/fn/article/anthology/edit"    # 文集信息编辑
    ARTICLE_BELONG = "/arcopen/fn/article/belong"            # 文集下文章列表修改
    ANTHOLOGY_DELETE = "/arcopen/fn/article/anthology/delete"# 文集删除
    ANTHOLOGY_LIST = "/arcopen/fn/article/anthology/list"    # 文集列表查询
    ANTHOLOGY_DETAIL = "/arcopen/fn/article/anthology/detail"# 文集详情查询


# ------------- 资源共享 URL -------------
class RESOURCE_BASE:
    RESOURCE_ADD_SHARE_URL = "/arcopen/fn/resource/add_share"  # 新增共享 POST


# ------------- 数据统计 URL -------------
class USER_DATA:
    DATA_USER_STAT_URL = "/arcopen/fn/data/user/stat"  # 获取用户数据 GET


class ARC_DATA:
    ARC_STAT_URL = "/arcopen/fn/data/arc/stat"        # 获取单个稿件数据 GET
    ARC_INC_STATS = "/arcopen/fn/data/arc/inc-stats"  # 获取整体稿件增量数据 GET


class ATC_DATA:
    ART_STAT_URL = "/arcopen/fn/data/art/stat"        # 获取单一专栏数据 GET
    ART_INC_STATS = "/arcopen/fn/data/art/inc-stats"  # 获取整体投稿增量数据 GET


# ------------- 店铺/商品相关 URL -------------
class SHOP_STORE_INFO:
    SHOP_INFO_GET_URL = "/arcopen/fn/v2/market/shop/info/get"  # 获取店铺信息 GET


class SHOP_COMMODITY_INFO:
    PRODUCT_ADD_URL = "/arcopen/fn/market/common/product_add"                       # 商品发布 POST
    COMMODITY_ITEM_LIST_URL = "/arcopen/fn/v2/market/commodity/item/list"           # 查询商品列表 GET
    PRODUCT_GET_PUBLISH_RULE_URL = "/arcopen/fn/market/common/product_get_product_publish_rule"  # 查询发品配置 POST
    PRODUCT_DETAIL = "/arcopen/fn/market/common/product/detail"
    PRODUCT_EDIT = "/arcopen/fn/market/common/product/edit"
    PRODUCT_DEL = "/arcopen/fn/market/common/product/del"
    PRODUCT_GET_CATE_PROPERTY = "/arcopen/fn/market/common/product/get_cate_property"
    COMMODITY_CATEGORY_QUALIFIED_LIST = "/arcopen/fn/market/commodity/category/qualified/list"


# ------------- 订单相关 URL -------------
class SHOP_ORDER_INFO:
    ORDER_BATCH_DECRYPT = "/arcopen/fn/market/common/order_batch_decrypt"  # 订单敏感信息解密
    ORDER_REVIEW = "/arcopen/fn/market/common/order_review"               # 流量卡审核信息回传
    ORDER_REMARK = "/arcopen/fn/market/common/order_remark"               # 商家备注
    ORDER_DETAIL = "/arcopen/fn/market/common/order_detail"               # 订单详情查询
    ORDER_SEARCH_LIST = "/arcopen/fn/market/common/order_searchList"       # 订单列表查询


# ------------- 物流相关 URL -------------
class SHOP_LOGISTICS_INFO:
    LOGISTICS_ADD = "/arcopen/fn/market/common/logistics_add"                    # 发货回掉
    LOGISTICS_EDIT = "/arcopen/fn/market/common/logistics_edit"                   # 物流编辑
    LOGISTICS_COMPANY_LIST = "/arcopen/fn/market/common/logistics_company_list"   # 获取快递公司列表
    ADDRESS_CREATE = "/arcopen/fn/market/common/address_create"                   # 地址库创建
    ADDRESS_LIST = "/arcopen/fn/market/common/address/list"                       # 批量查询地址库列表
    ADDRESS_GET_PROVINCE = "/arcopen/fn/market/common/address_get_province"       # 获取全量省份信息
    ADDRESS_GET_AREAS_BY_PROVINCE = "/arcopen/fn/market/common/address_get_areas_by_province"  # 根据省获取全量三级地址
    LOGISTICS_FREIGHT_TEMPLATE_LIST = "/arcopen/fn/market/common/logistics_freight_template_list"  # 运费模板列表查询


# ------------- 售后相关 URL -------------
class SHOP_AFTERSALES_INFO:
    AFTER_SALE_QUERY_LIST = "/arcopen/fn/market/common/after_sale_query_list"        # 售后列表查询
    AFTER_SALE_QUERY_DETAIL = "/arcopen/fn/market/common/after_sale_query_detail"      # 售后详情查询
    AFTER_SALE_CHECK_AFTER_SALE = "/arcopen/fn/market/common/after_sale_check_after_sale"  # 售后审核
    AFTER_SALE_CONFIRM_RECEIPT = "/arcopen/fn/market/common/after_sale_confirm_receipt"   # 确认收货
    AFTER_SALE_BARTER_SHIP = "/arcopen/fn/market/common/after_sale_barter_ship"         # 换货发货
    AFTER_SALE_STOP = "/arcopen/fn/market/common/after_sale_stop"                    # 售后终止


# ------------- 库存相关 URL -------------
class SHOP_STOCK_INFO:
    STOCK_QUERY = "/arcopen/fn/v2/market/stock/query"   # 库存查询 GET
    STOCK_UPDATE = "/arcopen/fn/v2/market/stock/update"  # 库存更新 POST


# ------------- 客服系统 URL -------------
class SHOP_BA_CHAT:
    CONVERSATION_SEND_MSG_URL = "/arcopen/fn/market/customer/conversation/send_msg"             # 客服系统 消息发送
    CONVERSATION_CUSTOMER_USER_FROM = "/arcopen/fn/market/customer/conversation/user_from"      # 客服系统 获取用户来源
    CONVERSATION_STAFF_STATUS_UPDATE = "/arcopen/fn/market/customer/conversation/staff_status_update"  # 客服系统 修改客服状态
    CONVERSATION_CLOSE = "/arcopen/fn/market/customer/conversation/close"                      # 客服系统 关闭


# ------------- 音乐版权 URL -------------
class COPYRIGHT_MUSIC_DATA:
    MUSIC_META_LIST_URL = "/arcopen/fn/music/meta/list"  # 音乐列表 获取媒体元数据
    MUSIC_LIST_URL = "/arcopen/fn/music/list"           # 音乐列表 获取媒体资源信息
    MUSIC_SEARCH_URL = "/arcopen/fn/music/search"       # 音乐搜索


# ------------- 图片上传 URL -------------
class IMAGE_UPLOAD:
    # 稿件图片上传
    IMAGE_UPLOAD_ARC_URL = "https://member.bilibili.com/arcopen/fn/archive/cover/upload"
    # 专栏稿件上传
    IMAGE_UPLOAD_ARTICLE_URL = "https://member.bilibili.com/arcopen/fn/article/upload/image"
    # 商品图片上传
    IMAGE_UPLOAD_COMMODITY_URL = "https://member.bilibili.com/arcopen/fn/v2/market/commodity/image/upload"
    # 客服图片上传
    IMAGE_UPLOAD_CUSTOMER = "https://member.bilibili.com/arcopen/fn/market/customer/image_upload"

class ModelConstants:
    ACCEPT_HEADER = "Accept"
    CONTENT_TYPE_HEADER = "Content-Type"
    AUTHORIZATION_HEADER = "Authorization"
    JSON_TYPE = "application/json"
    HMAC_SHA256 = "HMAC-SHA256"
    BILI_TIMESTAMP_HEADER = "x-bili-timestamp"
    BILI_SIGNATURE_METHOD_HEADER = "x-bili-signature-method"
    BILI_SIGNATURE_NONCE_HEADER = "x-bili-signature-nonce"
    BILI_ACCESS_KEY_ID_HEADER = "x-bili-accesskeyid"
    BILI_SIGN_VERSION_HEADER = "x-bili-signature-version"
    BILI_CONTENT_MD5_HEADER = "x-bili-content-md5"
    ACCESS_TOKEN = "access-token"

    BILI_VERSION = "1.0"
    BILI_VERSION_V2 = "2.0"

    METHOD_GET = "GET"
    METHOD_POST = "POST"


class BaseResp:
    def __init__(self, code: int, message: str, request_id: str, data):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.data = data

    def to_json(self):
        return json.dumps(self.__dict__)


# 域名
UAT_MAIN_OPEN_PLATFORM_HTTP_HOST = "https://uat-member.bilibili.com"
MAIN_OPEN_PLATFORM_HTTP_HOST = "https://member.bilibili.com"

SCENE_CODE = "ARC_APP_SHARE"


class CommonHeader:
    def __init__(
        self,
        content_type: str = "",
        content_accept_type: str = "",
        timestamp: str = "",
        signature_method: str = "",
        signature_version: str = "",
        authorization: str = "",
        nonce: str = "",
        access_key_id: str = "",
        content_md5: str = "",
        access_token: str = ""
    ):
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



