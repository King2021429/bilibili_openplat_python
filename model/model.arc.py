class VideoInitReq:
    def __init__(self, name, utype="0"):
        # name 文件名字，需携带正确的扩展名，例如test.mp4
        self.name = name
        # utype 上传类型：0，1。0-多分片，1-单个小文件（不超过100M）。默认值为0
        self.utype = utype