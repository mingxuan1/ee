# -*- coding: utf-8 -*-
# @Author   : Slowly
# @FileName : main.py
# @Software : PyCharm
# @version  ：1.0
# @LastEdit : 2020/12/15 11:42

import sys
from apis.oldApi import OldApi
from apis.newApi import NewApi
from utils.Compare import compare
from utils.MyLogger import Logger


def get_file():
    """
    打开一个简历名字的文件
    :return: 简历名字的列表
    """
    with open('../files/resume_file_names.out', 'r', encoding='utf-8')as fp:
        files = [x.strip() for x in fp.readlines()]
    return files


def get_diff(file, old_api, new_api):
    """
    - 比较old-api和new-api对简解析的不同
    :param new_api: 新的api接口的实例化对象
    :param old_api: 旧的api接口的实例化对象
    :param file: 简历文件名字  --> user_resume/556e71683c59d0.30288772.pdf
    """
    print('**************************开始对比***************************')
    r_new = new_api.analyze(file)
    r_old = old_api.analyze(file)
    if r_new and r_old:
        print(f'file: {file}')
        print('\ttips:下方无输出则old-api和new-api识别结果一致:\n\n')
        compare(r_old, r_new)
        print('************************************************************\n\n')
    else:
        print(f'file: {file}')
        print('ERROR MESSAGE: 简历识别错误或为空...\n')
        print('************************************************************\n\n')


if __name__ == '__main__':
    sys.stdout = Logger('../files/log/log.log', sys.stdout)
    new, old = NewApi(), OldApi()
    files_list = get_file()
    count = 1
    for file_ in files_list[0:]:
        print(count)
        get_diff(file_, old_api=old, new_api=new)
        count += 1
