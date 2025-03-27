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
