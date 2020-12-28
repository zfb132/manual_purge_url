#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: 'zfb'
# time: 2020-12-15 16:15

# CDN服务配置的域名（需要提前在腾讯云网页前端创建）
CDN_DOMAIN = "blog.whuzfb.cn"

# 腾讯云：https://console.cloud.tencent.com/cam/capi
SECRETID = "AKeee5555512345677777123456788889876"
SECRETKEY = "A71234567890abcdefedcba098765432"

# 控制功能开关
# 是否进行刷新URL的操作
PURGE_URL = True
# 自定义的预热URL（默认会预热sitemap.xml的所有链接）文件路径
# 该文件内，每行一个URL，例如
# https://blog.whuzfb.cn/img/me2.jpg
# https://blog.whuzfb.cn/img/home-bg.jpg
URLS_FILE = "urls.txt"
