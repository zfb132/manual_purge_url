#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: 'zfb'
# time: 2020-12-02 15:42
import json

from datetime import datetime
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
# 导入 cdn 产品模块的 models
from tencentcloud.cdn.v20180606 import models

from api.get_client_profile import get_client_instance

def get_cdn_client_instance(id, key):
    '''获取cdn的实例，用于后面对cdn的各种操作
    '''
    client = get_client_instance(id, key, "cdn")
    return client


def get_cdn_purge_url_info(client):
    '''查询CDN刷新URL配额和每日可用量
    '''
    try:
        req = models.DescribePurgeQuotaRequest()
        params = {}
        req.from_json_string(json.dumps(params))
        resp = client.DescribePurgeQuota(req)
        # print(resp.to_json_string())
        print("获取CDN刷新URL配额和每日可用量信息成功")
        return resp.UrlPurge

    except TencentCloudSDKException as err:
        print(err)
        return []


def update_cdn_purge_url(client, urls):
    '''指定 URL 资源的刷新，支持指定加速区域刷新
    默认情况下境内、境外每日刷新 URL 限额为各 10000 条，每次最多可提交 1000 条
    '''
    try:
        req = models.PurgeUrlsCacheRequest()
        params = {
            "Urls": urls
        }
        req.from_json_string(json.dumps(params))
        resp = client.PurgeUrlsCache(req)
        print(resp.to_json_string())
        print("URL:{}刷新成功".format(', '.join(urls)))
        return True

    except TencentCloudSDKException as err:
        print(err)
        return False