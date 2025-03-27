import json

import model
import dao


# 文件上传预处理
def VideoInit(clientId, accessToken, appSecret):
    url = model.ArcInitUrl
    videoInitReq = {
        "Name": "test.mp4",
        "Utype": "0"
    }
    videoInitReqJson = json.dumps(videoInitReq)
    resp, err = dao.ApiRequest(videoInitReqJson, url, model.MethodPost, clientId, accessToken, appSecret,
                               model.BiliVersionV2)
    if err is not None:
        print(f"VideoInit err:{err}")
    return resp, err


# 文件分片合片
def VideoArcComplete(clientId, accessToken, appSecret):
    url = model.ArcComplete
    resp, err = dao.ApiRequest("", url, model.MethodPost, clientId, accessToken, appSecret, model.BiliVersionV2)
    if err is not None:
        print(f"VideoArcComplete err:{err}")
    return resp, err


# 稿件提交 POST
def ArcAddUrl(clientId, accessToken, appSecret, reqJson):
    url = model.ArcAddUrl
    return dao.ApiRequest(reqJson, url, model.MethodPost, clientId, accessToken, appSecret, model.BiliVersionV2)


# 稿件提交 fetch 模式
def ArcAddFetch(clientId, accessToken, appSecret, reqJson):
    url = model.ArcAddFetch
    return dao.ApiRequest(reqJson, url, model.MethodPost, clientId, accessToken, appSecret, model.BiliVersionV2)


# 稿件编辑
def ArcEdit(clientId, accessToken, appSecret, reqJson):
    url = model.ArcEdit
    return dao.ApiRequest(reqJson, url, model.MethodPost, clientId, accessToken, appSecret, model.BiliVersionV2)


# 稿件删除
def ArcDel(clientId, accessToken, appSecret, reqJson):
    url = model.ArcDel
    return dao.ApiRequest(reqJson, url, model.MethodPost, clientId, accessToken, appSecret, model.BiliVersionV2)


# 稿件查询
def ArcView(clientId, accessToken, appSecret, reqJson):
    url = model.ArcView
    return dao.ApiRequest(reqJson, url, model.MethodPost, clientId, accessToken, appSecret, model.BiliVersionV2)


# 稿件列表查询
def ArcViewList(clientId, accessToken, appSecret, reqJson):
    url = model.ArcViewList
    return dao.ApiRequest(reqJson, url, model.MethodPost, clientId, accessToken, appSecret, model.BiliVersionV2)
