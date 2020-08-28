from BeautifulReport import BeautifulReport
import unittest
import os
import time


report_path = os.path.abspath(os.path.join("report"))


now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))

# 报告地址&名称
report_title = now + '授备课三期测试报告' + ".html"     # 如果不能打开这个文件，可能是now的格式，不支持：和空格

# 报告描述
desc = '授备课三期测试报告'
suite = unittest.TestLoader().discover("testsuites")
if __name__ == '__main__':

    run = BeautifulReport(suite)
    run.report(description=desc, filename=report_title, log_path=report_path)




