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
