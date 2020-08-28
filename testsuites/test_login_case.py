# coding=utf-8
import time,os
import unittest
from framework.browser_engine import BrowserEngine
from WebPages.LoginPage import LoginPage
from framework.CommonUtil import CommonUtil
from framework.zqexcelutils import ZqOperationExcel
from framework.sendmail import SendEmail
from BeautifulReport import BeautifulReport

class UserLogin(unittest.TestCase):

    def open_browse(self):
        browse = BrowserEngine(self)
        self.driver = browse.open_browser(self)

    def quit_browse(self):
        self.driver.quit()


    def test_login_success(self):

        self.zqsendmail = SendEmail()
        self.com_util = CommonUtil()
        self.opera_excel = ZqOperationExcel()
        # 定义两个列表
        pass_count = []
        fail_count = []
        # 获取用例行数

        exl_path = os.path.abspath(os.path.join("data"))
        exl_name = exl_path + '\\testCase.xls'
        rows_count = ZqOperationExcel(file_name=exl_name, sheet_id=1).get_lines()


        # 定义行
        a = 1

        for i in range(1, rows_count):
            self.open_browse()
            case_name = ZqOperationExcel(file_name=exl_name, sheet_id=1).get_cell_value(a, 0)
            user_name = ZqOperationExcel(file_name=exl_name, sheet_id=1).get_cell_value(a, 1)
            user_pwd = ZqOperationExcel(file_name=exl_name, sheet_id=1).get_cell_value(a, 2)
            excepted = ZqOperationExcel(file_name=exl_name, sheet_id=1).get_cell_value(a, 3)
            remarks = ZqOperationExcel(file_name=exl_name, sheet_id=1).get_cell_value(a, 4)
            login = LoginPage(self.driver)
            login.user_account_search(user_name)  # 调用页面对象中的方法
            login.password_search(user_pwd)
            login.send_submit_btn()  # 调用页面对象类中的点击搜索按钮方法
            time.sleep(1)
            get_fail_text = login.get_page_url()
            get_except_text = excepted
            self.__dict__['_testMethodDoc'] = remarks  #将EXLcase_name赋值给页面用例描述
            # 调用基类截图方法

            login.save_img()
            # 断言
            # assert get_except_text in get_fail_text
            a = a + 1

            try:
                if self.com_util.is_contain(get_except_text, get_fail_text):
                    print("预期结果：" + excepted)
                    print("实际结果：" + get_fail_text)
                    print(case_name + '-----√-Test Pass.--------' + remarks)
                    pass_count.append(i)
                else:
                    print("预期结果：" + excepted)
                    print("实际结果：" + get_fail_text)
                    print(case_name + '-----×-Test Fail.--------' + remarks)
                    fail_count.append(i)
            except Exception as e:
                print('Fail', format(e))
            self.quit_browse()

        print("登录有效用例的总数", len(pass_count) + len(fail_count))
        print("登录有效用例成功的个数", len(pass_count))
        print("登录有效用例失败个数", len(fail_count))
        # 发送自动化测试报告
        # self.zqsendmail.send_main2(pass_count, fail_count)

    def test_login_fail(self):

        """
        测试登录失败用例
        """
        self.zqsendmail = SendEmail()
        self.com_util = CommonUtil()
        self.opera_excel = ZqOperationExcel()
        # 定义两个列表
        pass_count = []
        fail_count = []
        # 获取用例行数

        exl_path = os.path.abspath(os.path.join("data"))
        exl_name = exl_path + '\\testCase.xls'
        rows_count = ZqOperationExcel(file_name=exl_name, sheet_id=0).get_lines()
        # 定义行
        a = 1
        for i in range(1, rows_count):
            self.open_browse()
            case_name = ZqOperationExcel(file_name=exl_name, sheet_id=0).get_cell_value(a, 0)
            user_name = ZqOperationExcel(file_name=exl_name, sheet_id=0).get_cell_value(a, 1)
            user_pwd = ZqOperationExcel(file_name=exl_name, sheet_id=0).get_cell_value(a, 2)
            excepted = ZqOperationExcel(file_name=exl_name, sheet_id=0).get_cell_value(a, 3)
            remarks = ZqOperationExcel(file_name=exl_name, sheet_id=0).get_cell_value(a, 4)
            login = LoginPage(self.driver)
            login.user_account_search(user_name)  # 调用页面对象中的方法
            login.password_search(user_pwd)
            time.sleep(2)
            login.send_submit_btn()  # 调用页面对象类中的点击搜索按钮方法
            time.sleep(1)
            get_fail_text = login.get_real_text()
            get_except_text = excepted
            self.__dict__['_testMethodDoc'] = remarks #将EXLcase_name赋值给页面用例描述
            # 调用基类截图方法
            login.save_img()
            # 断言
            # assert get_except_text in get_fail_text

            a = a + 1
            try:
                if self.com_util.is_contain(get_except_text, get_fail_text):
                    print("预期结果：" + excepted)
                    print("实际结果：" + get_fail_text)
                    print(case_name + '-----√-Test Pass.--------' + remarks)
                    pass_count.append(i)
                else:
                    print("预期结果：" + excepted)
                    print("实际结果：" + get_fail_text)
                    print(case_name + '-----×-Test Fail.--------' + remarks)
                    fail_count.append(i)
            except Exception as e:
                print('Fail', format(e))
            self.quit_browse()

        print("登录无效用例的总数", len(pass_count) + len(fail_count))
        print("登录无效用例成功的个数", len(pass_count))
        print("登录无效用例失败个数", len(fail_count))
        # 发送自动化测试报告
        # self.zqsendmail.send_main2(pass_count, fail_count)

if __name__ == '__main__':
    unittest.main()
