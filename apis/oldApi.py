# -*- coding: utf-8 -*-
# @Author   : Slowly
# @FileName : oldApi.py
# @Software : PyCharm
# @version  ：1.0
# @LastEdit : 2020/12/14 14:22

import json
import requests
import configparser


class OldApi:
    """
    向old api接口发送给请求，并将识别结果保存到本地
    """
    config = configparser.ConfigParser()
    config.read('../files/config/config.ini')

    def __init__(self):
        self.name = 'old'
        self.headers = {'X-API-KEY': self.config['api-key']['X-API-KEY'], 'Content-Type': 'application/json'}
        self.payload = {"bucket": self.config['payload']['bucket'], "key": None}
        self.uri = self.config['url']['uri']
        self.url = self.uri + "/resume_parsing_url_old"

    def save(self, res, file):
        file = file.split('user_resume/')[-1]
        with open(f'../files/json/{file}-{self.name}.json', 'w', encoding='utf-8')as f:
            f.write(json.dumps(res, indent=4, ensure_ascii=False))

    def analyze(self, file):
        """
        new-api resume parsing
        :return: json.loads(response.text)
        """
        self.payload['key'] = file
        try:
            response = requests.post(self.url, data=json.dumps(self.payload), headers=self.headers, timeout=30)
            if response.status_code in [200, 201]:
                self.save(json.loads(response.text), file)
                return json.loads(response.text)
            else:
                return None
        except Exception as e:
            print('New-Api ERROR:', e)
            return None
