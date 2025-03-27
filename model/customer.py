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
