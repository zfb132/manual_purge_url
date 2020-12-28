# -*- coding: utf8 -*-
import json
from api import cdn, tools
import config

def run_purge_url(id, key, domain, urls_file):
    '''为CDN推送刷新URL
    '''
    from time import sleep
    from os.path import isfile
    urls = tools.get_sitemap_urls("https://{}/sitemap.xml".format(domain))
    if isfile(urls_file):
        urls = urls + tools.get_urls_from_file(urls_file)
    cdn_client = cdn.get_cdn_client_instance(id, key)
    info = cdn.get_cdn_purge_url_info(cdn_client)
    # 统计刷新url数量
    cnt = 0
    # 只对国内进行刷新
    for i in info:
        if i.Area == "mainland":
            grp_size = i.Batch
            available = i.Available
            print("正在对区域{0}进行url刷新，剩余配额{1}条".format(i.Area, available))
            new_urls = tools.resize_url_list(urls, grp_size)
            for url_grp in new_urls:
                res = cdn.update_cdn_purge_url(cdn_client, url_grp)
                if res:
                    cnt = cnt + len(url_grp)
                    sleep(0.1)
                else:
                    break
    print("成功刷新{}个URL".format(cnt))


def main_handler(event, context):
    # print("Received event: " + json.dumps(event, indent = 2)) 
    # print("Received context: " + str(context))
    # print("Hello world")
    SECRETID = config.SECRETID
    SECRETKEY = config.SECRETKEY
    my_domain = config.CDN_DOMAIN
    if config.PURGE_URL:
        run_purge_url(SECRETID, SECRETKEY, my_domain, config.URLS_FILE)