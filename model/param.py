class MusicSearchReq:
    def __init__(self, keyword="", page=0, page_size=0):
        # 模糊搜索字段（从歌曲名、歌手名称中模糊搜索）
        self.keyword = keyword
        self.page = page
        self.page_size = page_size


class AuthedMetaInfo:
    def __init__(self, metadata_id="", title="", artist_name=""):
        # metadata_id
        self.metadata_id = metadata_id
        # 歌曲名
        self.title = title
        # 歌手名称
        self.artist_name = artist_name


class MusicSearchResp:
    def __init__(self, infos=None, total=0):
        if infos is None:
            infos = []
        self.infos = infos
        self.total = total


class MusicMetaListReq:
    def __init__(self, metadata_ids=None):
        if metadata_ids is None:
            metadata_ids = []
        # metadata_id 列表
        self.metadata_ids = metadata_ids


class MusicMetaInfo:
    def __init__(self, metadata_id="", title="", artist_name="", album="", cover_url=""):
        self.metadata_id = metadata_id
        # 歌曲标题
        self.title = title
        # 歌手名称
        self.artist_name = artist_name
        # 专辑名称
        self.album = album
        # 封面地址
        self.cover_url = cover_url


class MusicMetaListResp:
    def __init__(self, infos=None):
        if infos is None:
            infos = {}
        self.infos = infos


class MusicListReq:
    def __init__(self, metadata_ids=None):
        if metadata_ids is None:
            metadata_ids = []
        self.metadata_ids = metadata_ids


class TranscodeResourceInfo:
    def __init__(self, resource_id="", transcode_url="", duration=0, size=0, format=""):
        # 资源ID
        self.resource_id = resource_id
        # 转码链接
        self.transcode_url = transcode_url
        # 时长（微妙）
        self.duration = duration
        # 资源大小
        self.size = size
        # 码率格式
        self.format = format


class TranscodeResourceList:
    def __init__(self, infos=None):
        if infos is None:
            infos = []
        self.infos = infos


class MusicListResp:
    def __init__(self, info=None):
        if info is None:
            info = {}
        self.info = info

class CommonMsg:
    def __init__(self, source="", cover="", title="", type_id=0, topic_id=0, video_material_url=None):
        if video_material_url is None:
            video_material_url = []
        self.source = source
        self.cover = cover
        self.title = title
        self.type_id = type_id
        self.topic_id = topic_id
        self.video_material_url = video_material_url


class CommonAddShareReq:
    def __init__(self, common_msg="", biz_code="", scene_code=""):
        # common_msg 通用信息 大json串
        self.common_msg = common_msg
        # biz_code
        self.biz_code = biz_code
        # scene_code 场景码
        self.scene_code = scene_code


class CommonAddShareRespData:
    def __init__(self, link_url=""):
        # link_url
        self.link_url = link_url

class VideoInitReq:
    def __init__(self, name, utype="0"):
        # name 文件名字，需携带正确的扩展名，例如test.mp4
        self.name = name
        # utype 上传类型：0，1。0-多分片，1-单个小文件（不超过100M）。默认值为0
        self.utype = utype

class StockQueryReq:
    def __init__(self, sku_id_list=None):
        if sku_id_list is None:
            sku_id_list = []
        self.sku_id_list = sku_id_list


class StockInfo:
    def __init__(self, isolate_stock=0, performs_stock=0, sku_id=0, stock=0):
        self.isolate_stock = isolate_stock
        self.performs_stock = performs_stock
        self.sku_id = sku_id
        self.stock = stock


class ModifyStockInfo:
    def __init__(self, sku_id=0, zp_entity_stock_offset=0):
        self.sku_id = sku_id
        self.zp_entity_stock_offset = zp_entity_stock_offset


class StockUpdateReq:
    def __init__(self, uid=0, client_id="", mode=0, modify_stock_list=None):
        if modify_stock_list is None:
            modify_stock_list = []
        self.uid = uid
        self.client_id = client_id
        self.mode = mode
        self.modify_stock_list = modify_stock_list


class FailedSku:
    def __init__(self, stock_id=0, message=""):
        self.stock_id = stock_id
        self.message = message


class StockUpdateResp:
    def __init__(self, failed_skus=None):
        if failed_skus is None:
            failed_skus = []
        self.failed_skus = failed_skus

class OpenMarketCustomerSendMsgReq:
    def __init__(self, biz_id, staff_id, shop_id, msg_type, msg, conversation_id=0, user_open_id=""):
        # 业务方类型id: 1-商家，2-带货,3-经营号
        self.biz_id = biz_id
        # 会话id
        self.conversation_id = conversation_id
        # 客服id
        self.staff_id = staff_id
        # 用户openid
        self.user_open_id = user_open_id
        # 商家id
        self.shop_id = shop_id
        # 消息类型
        self.msg_type = msg_type
        # 消息内容
        self.msg = msg


class OpenMarketCustomerSendMsgResp:
    def __init__(self, msg_key):
        # 消息key
        self.msg_key = msg_key


class OpenMarketCustomerConversationCloseReq:
    def __init__(self, conversation_id, staff_id):
        # 会话id
        self.conversation_id = conversation_id
        # 客服id
        self.staff_id = staff_id


class OpenMarketCustomerConversationCloseResp:
    pass


class OpenMarketCustomerStaffStatusUpdateReq:
    def __init__(self, status, staff_id, is_close_conversation=0):
        # 客服状态,1-上线,2-忙碌,3-离线
        self.status = status
        # 客服id
        self.staff_id = staff_id
        # 离线是否关闭会话  1-是 0-否,默认0
        self.is_close_conversation = is_close_conversation


class OpenMarketCustomerStaffStatusUpdateResp:
    pass


class MarketCustomerImageUploadReq:
    def __init__(self, staff_id):
        # 客服id
        self.staff_id = staff_id


class MarketCustomerImageUploadResp:
    def __init__(self, url):
        # 图片url
        self.url = url
