#断言判断
# coding:utf-8
import xlrd
import time,os
filePath = os.path.split(os.path.dirname(__file__))[0]


class CommonUtil:
    # 定义规则  比较预期和实际
    @staticmethod
    def is_contain(str_one, str_two):
        # str_one 代表查找的字符串
        # str_two 被查找的字符串
        flag = None
        if str_one in str_two:
            flag = True
        else:
            flag = False
        return flag

