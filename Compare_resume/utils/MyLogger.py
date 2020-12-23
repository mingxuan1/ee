# -*- coding: utf-8 -*-
# @Author   : Slowly
# @FileName : MyLogger.py
# @Software : PyCharm
# @version  ：1.0
# @LastEdit : 2020/12/16 14:06


import sys


class Logger(object):

    def __init__(self, filename='default.log', stream=sys.stdout):
        self.terminal = stream
        self.log = open(filename, 'a')

    def write(self, message):
        self.terminal.write(message)
        self.log.write(message)

    def flush(self):
        pass


if __name__ == '__main__':
    sys.stdout = Logger('a.log', sys.stdout)  # 控制台输出日志
    sys.stderr = Logger('a.log_file', sys.stderr)