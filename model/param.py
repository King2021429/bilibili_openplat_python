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
