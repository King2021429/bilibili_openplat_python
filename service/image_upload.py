import dao.pic
from dao import *
from model.header import IMAGE_UPLOAD, ModelConstants


# 稿件图片上传
def image_upload_arc(pic_path, client_id, access_token, app_secret):
    url = IMAGE_UPLOAD.IMAGE_UPLOAD_ARC_URL
    return dao.pic.PicRequest(url, pic_path, client_id, access_token, app_secret, ModelConstants.BILI_VERSION_V2)


# 专栏稿件上传
def image_upload_article(pic_path, client_id, access_token, app_secret):
    url = IMAGE_UPLOAD.IMAGE_UPLOAD_ARTICLE_URL
    return dao.pic.PicRequest(url, pic_path, client_id, access_token, app_secret, ModelConstants.BILI_VERSION_V2)


# 商品图片上传
def image_upload_commodity(pic_path, client_id, access_token, app_secret):
    url = IMAGE_UPLOAD.IMAGE_UPLOAD_COMMODITY_URL
    return dao.pic.PicRequest(url, pic_path, client_id, access_token, app_secret, ModelConstants.BILI_VERSION_V2)


# 客服图片上传
def image_upload_customer(pic_path, client_id, access_token, app_secret):
    url = IMAGE_UPLOAD.IMAGE_UPLOAD_CUSTOMER
    return dao.pic.PicRequest(url, pic_path, client_id, access_token, app_secret, ModelConstants.BILI_VERSION_V2)