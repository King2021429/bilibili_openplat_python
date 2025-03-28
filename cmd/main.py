import requests
import json
import hashlib
import time
import urllib.parse
from service import arc, article, customer, image_upload, music, share, shop, signAndOuath, stock, user, data
# 入口启动函数
def main():
    client_id = input("请输入 client_id: ")
    access_token = input("请输入 access_token: ")
    app_secret = input("请输入 app_secret: ")

    print("请输入对应方法:" +
          "0: 计算签名\n" +
          "1: 获取授权\n" +
          "2: USER_INFO-获取已授权用户基础公开信息\n" +
          "3: USER_INFO-查询用户已授权权限列表\n" +
          "4: ARC_BASE-文件上传预处理\n" +
          "7: ARC_BASE-文件分片合片\n" +
          "8: ARC_BASE-视频稿件提交\n" +
          "9: ARC_BASE-获取用于投稿的连接\n" +
          "10: ARC_BASE-查询单一视频稿件详情\n" +
          "11: ARC_BASE-查询用户视频稿件列表\n" +
          "12: ATC_BASE-文章提交\n" +
          "13: ATC_BASE-文章编辑\n" +
          "14: ATC_BASE-文章删除\n" +
          "15: ATC_BASE-文章详情\n" +
          "16: ATC_BASE-文章列表查询\n" +
          "17: ATC_BASE-文章分类查询\n" +
          "18: ATC_BASE-获取视频、文章卡片信息\n" +
          "19: ATC_BASE-文集提交\n" +
          "20: ATC_BASE-文集信息编辑\n" +
          "21: ATC_BASE-文集下文章列表修改\n" +
          "22: ATC_BASE-文集删除\n" +
          "23: ATC_BASE-文集列表查询\n" +
          "24: ATC_BASE-文集详情查询\n" +
          "26: USER_DATA-获取用户数据\n" +
          "27: ARC_DATA-获取单个稿件数据\n" +
          "28: ARC_DATA-获取整体稿件增量数据\n" +
          "29: ATC_DATA-获取单一专栏数据\n" +
          "30: ATC_DATA-获取整体投稿增量数据\n" +
          "31: SHOP_STORE_INFO-获取店铺信息\n" +
          "32: SHOP_COMMODITY_INFO-商品发布\n" +
          "33: SHOP_COMMODITY_INFO-商品编辑\n" +
          "34: SHOP_COMMODITY_INFO-商品删除\n" +
          "35: SHOP_COMMODITY_INFO-商品列表查询\n" +
          "36: SHOP_COMMODITY_INFO-商品详情查询\n" +
          "37: SHOP_COMMODITY_INFO-查询发品配置\n" +
          "38: SHOP_COMMODITY_INFO-查询商品类目属性列表\n" +
          "39: SHOP_COMMODITY_INFO-获取类目列表\n" +
          "40: SHOP_ORDER_INFO-订单列表查询\n" +
          "41: SHOP_ORDER_INFO-订单详情查询\n" +
          "42: SHOP_ORDER_INFO-订单敏感信息解密\n" +
          "43: SHOP_ORDER_INFO-流量卡审核信息回传\n" +
          "44: SHOP_ORDER_INFO-商家备注\n" +
          "45: SHOP_LOGISTICS_INFO-发货回掉\n" +
          "46: SHOP_LOGISTICS_INFO-物流编辑\n" +
          "47: SHOP_LOGISTICS_INFO-获取快递公司列表\n" +
          "48: SHOP_LOGISTICS_INFO-地址库创建\n" +
          "49: SHOP_LOGISTICS_INFO-批量查询地址库列表\n" +
          "50: SHOP_LOGISTICS_INFO-获取全量省份信息\n" +
          "51: SHOP_LOGISTICS_INFO-根据省获取全量三级地址\n" +
          "52: SHOP_LOGISTICS_INFO-运费模板列表查询\n" +
          "53: SHOP_AFTERSALES_INFO-售后列表查询\n" +
          "54: SHOP_AFTERSALES_INFO-售后详情查询\n" +
          "55: SHOP_AFTERSALES_INFO-售后审核\n" +
          "56: SHOP_AFTERSALES_INFO-确认收货\n" +
          "57: SHOP_AFTERSALES_INFO-换货发货\n" +
          "58: SHOP_AFTERSALES_INFO-售后终止\n" +
          "59: SHOP_STOCK_INFO-库存查询\n" +
          "60: SHOP_STOCK_INFO-库存更新\n" +
          "61: SHOP_BA_CHAT-客服系统 消息发送\n" +
          "62: SHOP_BA_CHAT-客服系统 获取用户来源\n" +
          "63: SHOP_BA_CHAT-客服系统 修改客服状态\n" +
          "64: SHOP_BA_CHAT-客服系统 关闭\n" +
          "65: COPYRIGHT_MUSIC_DATA-音乐列表 获取媒体元数据\n" +
          "66: COPYRIGHT_MUSIC_DATA-音乐列表 获取媒体资源信息\n" +
          "67: COPYRIGHT_MUSIC_DATA-音乐搜索\n" +
          "68:稿件图片上传\n" +
          "69:专栏稿件上传\n" +
          "70:商品图片上传\n" +
          "71:客服图片上传\n" +
          "q: 退出 ")
    input_choice = input()

    if input_choice == "0":
        signAndOuath.Sign(client_id, access_token, app_secret)
    elif input_choice == "1":
        signAndOuath.Oauth(client_id, app_secret)
    elif input_choice == "2":
        user.AccountInfo(client_id, access_token, app_secret)
    elif input_choice == "3":
        user.AccountScope(client_id, access_token, app_secret)
    elif input_choice == "4":
        arc.VideoInit(client_id, access_token, app_secret)
    elif input_choice == "7":
        arc.VideoArcComplete(client_id, access_token, app_secret)
    elif input_choice == "8":
        arc.ArcAddUrl(client_id, access_token, app_secret, "")
    elif input_choice == "9":
        share.common_add_share(client_id, access_token, app_secret, "")
    elif input_choice == "10":
        arc.ArcView(client_id, access_token, app_secret, "")
    elif input_choice == "11":
        arc.ArcViewList(client_id, access_token, app_secret, "")
    elif input_choice == "12":
        req_json = ""
        article.article_add(client_id, access_token, app_secret, req_json)
    elif input_choice == "13":
        req_json = ""
        article.article_edit(client_id, access_token, app_secret, req_json)
    elif input_choice == "14":
        req_json = ""
        article.article_delete(client_id, access_token, app_secret, req_json)
    elif input_choice == "15":
        req_json = ""
        article.article_detail(client_id, access_token, app_secret, req_json)
    elif input_choice == "16":
        req_json = ""
        article.article_list(client_id, access_token, app_secret, req_json)
    elif input_choice == "17":
        req_json = ""
        article.article_categories(client_id, access_token, app_secret, req_json)
    elif input_choice == "18":
        req_json = ""
        article.article_card(client_id, access_token, app_secret, req_json)
    elif input_choice == "19":
        req_json = ""
        article.anthology_add(client_id, access_token, app_secret, req_json)
    elif input_choice == "20":
        req_json = ""
        article.anthology_edit(client_id, access_token, app_secret, req_json)
    elif input_choice == "21":
        req_json = ""
        article.article_belong(client_id, access_token, app_secret, req_json)
    elif input_choice == "22":
        req_json = ""
        article.article_delete(client_id, access_token, app_secret, req_json)
    elif input_choice == "23":
        req_json = ""
        article.anthology_list(client_id, access_token, app_secret, req_json)
    elif input_choice == "24":
        req_json = ""
        article.anthology_detail(client_id, access_token, app_secret, req_json)
    elif input_choice == "26":
        req_json = ""
        data.UserData(client_id, access_token, app_secret, req_json)
    elif input_choice == "27":
        req_json = ""
        data.ArcStat(client_id, access_token, app_secret, req_json)
    elif input_choice == "28":
        req_json = ""
        data.ArcIncStats(client_id, access_token, app_secret, req_json)
    elif input_choice == "29":
        req_json = ""
        data.ArtStat(client_id, access_token, app_secret, req_json)
    elif input_choice == "30":
        req_json = ""
        data.ArtIncStats(client_id, access_token, app_secret, req_json)
    elif input_choice == "31":
        req_json = ""
        shop.shop_info_get_url(client_id, access_token, app_secret, req_json)
    elif input_choice == "32":
        req_json = ""
        shop.product_add(client_id, access_token, app_secret, req_json)
    elif input_choice == "33":
        req_json = ""
        shop.product_edit(client_id, access_token, app_secret, req_json)
    elif input_choice == "34":
        req_json = ""
        shop.product_del(client_id, access_token, app_secret, req_json)
    elif input_choice == "35":
        req_json = ""
        shop.commodity_item_list(client_id, access_token, app_secret, req_json)
    elif input_choice == "36":
        req_json = ""
        shop.product_detail(client_id, access_token, app_secret, req_json)
    elif input_choice == "37":
        req_json = ""
        shop.product_get_publish_rule(client_id, access_token, app_secret, req_json)
    elif input_choice == "38":
        req_json = ""
        shop.product_get_cate_property(client_id, access_token, app_secret, req_json)
    elif input_choice == "39":
        req_json = ""
        shop.commodity_category_qualified_list(client_id, access_token, app_secret, req_json)
    elif input_choice == "40":
        req_json = ""
        shop.order_search_list(client_id, access_token, app_secret, req_json)
    elif input_choice == "41":
        req_json = ""
        shop.order_detail(client_id, access_token, app_secret, req_json)
    elif input_choice == "42":
        req_json = ""
        shop.order_batch_decrypt(client_id, access_token, app_secret, req_json)
    elif input_choice == "43":
        req_json = ""
        shop.order_review(client_id, access_token, app_secret, req_json)
    elif input_choice == "44":
        req_json = ""
        shop.order_remark(client_id, access_token, app_secret, req_json)
    elif input_choice == "45":
        req_json = ""
        shop.logistics_add(client_id, access_token, app_secret, req_json)
    elif input_choice == "46":
        req_json = ""
        shop.logistics_edit(client_id, access_token, app_secret, req_json)
    elif input_choice == "47":
        req_json = ""
        shop.logistics_company_list(client_id, access_token, app_secret, req_json)
    elif input_choice == "48":
        req_json = ""
        shop.address_create(client_id, access_token, app_secret, req_json)
    elif input_choice == "49":
        req_json = ""
        shop.address_list(client_id, access_token, app_secret, req_json)
    elif input_choice == "50":
        req_json = ""
        shop.address_get_province(client_id, access_token, app_secret, req_json)
    elif input_choice == "51":
        req_json = ""
        shop.address_get_areas_by_province(client_id, access_token, app_secret, req_json)
    elif input_choice == "52":
        req_json = ""
        shop.logistics_freight_template_list(client_id, access_token, app_secret, req_json)
    elif input_choice == "53":
        req_json = ""
        shop.after_sale_query_list(client_id, access_token, app_secret, req_json)
    elif input_choice == "54":
        req_json = ""
        shop.after_sale_query_detail(client_id, access_token, app_secret, req_json)
    elif input_choice == "55":
        req_json = ""
        shop.after_sale_check_after_sale(client_id, access_token, app_secret, req_json)
    elif input_choice == "56":
        req_json = ""
        shop.after_sale_confirm_receipt(client_id, access_token, app_secret, req_json)
    elif input_choice == "57":
        req_json = ""
        shop.after_sale_barter_ship(client_id, access_token, app_secret, req_json)
    elif input_choice == "58":
        req_json = ""
        shop.after_sale_stop(client_id, access_token, app_secret, req_json)
    elif input_choice == "59":
        stock.StockQuery(client_id, access_token, app_secret)
    elif input_choice == "60":
        stock.StockUpdate(client_id, access_token, app_secret)
    elif input_choice == "61":
        customer.conversation_send_msg(client_id, access_token, app_secret, "")
    elif input_choice == "62":
        customer.conversation_customer_user_from(client_id, access_token, app_secret, "")
    elif input_choice == "63":
        customer.conversation_staff_status_update(client_id, access_token, app_secret, "")
    elif input_choice == "64":
        customer.conversation_close(client_id, access_token, app_secret, "")
    elif input_choice == "65":
        music.music_meta_list(client_id, access_token, app_secret, "")
    elif input_choice == "66":
        music.music_list(client_id, access_token, app_secret, "")
    elif input_choice == "67":
        music.music_search(client_id, access_token, app_secret, "")
    elif input_choice == "68":
        pic_url = ""
        image_upload.image_upload_arc(pic_url, client_id, access_token, app_secret)
    elif input_choice == "69":
        pic_url = ""
        image_upload.image_upload_article(pic_url, client_id, access_token, app_secret)
    elif input_choice == "70":
        pic_url = ""
        image_upload.image_upload_commodity(pic_url, client_id, access_token, app_secret)
    elif input_choice == "71":
        pic_url = ""
        image_upload.image_upload_customer(pic_url, client_id, access_token, app_secret)
    elif input_choice == "q":
        print("退出程序")
        return
    else:
        print("无效的命令，请重新输入")


if __name__ == "__main__":
    main()
