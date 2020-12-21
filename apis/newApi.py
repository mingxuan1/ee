# -*- coding: utf-8 -*-
# @Author   : Slowly
# @FileName : newApi.py
# @Software : PyCharm
# @version  ：1.0
# @LastEdit : 2020/12/14 14:23

from apis.oldApi import OldApi


class NewApi(OldApi):
    """
        向new api接口发送给请求，并将识别结果保存到本地
    """

    def __init__(self):
        self.name = 'new'
        self.headers = {
            'X-API-KEY': self.config['api-key']['X-API-KEY'], 'Content-Type': 'application/json'}
        self.payload = {"bucket": self.config['payload']['bucket'], "key": None}
        self.uri = self.config['url']['uri']
        self.url = self.uri + "/resume_parsing_url"
