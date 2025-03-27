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
