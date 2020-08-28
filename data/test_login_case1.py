# coding=utf-8
import time,os
import unittest
from framework.browser_engine import BrowserEngine
from WebPages.LoginPage import LoginPage
from framework.CommonUtil import CommonUtil
from framework.zqexcelutils import ZqOperationExcel
from framework.sendmail import SendEmail
from BeautifulReport import BeautifulReport

# 定义两个列表
pass_count = []
fail_count = []
# 获取用例行数

exl_path = os.path.abspath(os.path.join("data"))
exl_name = exl_path + '\\testCase.xls'
success_rows_count = ZqOperationExcel(file_name=exl_name, sheet_id=1).get_lines()
fail_rows_count = ZqOperationExcel(file_name=exl_name, sheet_id=0).get_lines()
# 定义行












class UserLogin(unittest.TestCase):
    global img_file
    a = 1
    b = 1
    def open_browse(self):
        browse = BrowserEngine(self)
        self.driver = browse.open_browser(self)

    def quit_browse(self):
        self.driver.quit()

    # 遍历EXL中用例
    # def circle_case(self):
    #     global a, b
    #     for x in range(a, success_rows_count):
    #         UserLogin.test_login_fail(self)
    #         a = a + 1
    #     for y in range(b, fail_rows_count):
    #         UserLogin.test_login_fail(self)
    #         b = b + 1

    def test_login_success(self):

        self.zqsendmail = SendEmail()
        self.com_util = CommonUtil()
        self.opera_excel = ZqOperationExcel()
        self.open_browse()
        success_case_name = ZqOperationExcel(file_name=exl_name, sheet_id=1).get_cell_value(UserLogin.a, 0)
        success_user_name = ZqOperationExcel(file_name=exl_name, sheet_id=1).get_cell_value(UserLogin.a, 1)
        success_user_pwd = ZqOperationExcel(file_name=exl_name, sheet_id=1).get_cell_value(UserLogin.a, 2)
        success_excepted = ZqOperationExcel(file_name=exl_name, sheet_id=1).get_cell_value(UserLogin.a, 3)
        success_remarks = ZqOperationExcel(file_name=exl_name, sheet_id=1).get_cell_value(UserLogin.a, 4)
        login = LoginPage(self.driver)
        login.user_account_search(success_user_name)  # 调用页面对象中的方法
        login.password_search(success_user_pwd)
        login.send_submit_btn()  # 调用页面对象类中的点击搜索按钮方法
        time.sleep(1)
        get_fail_text = login.get_page_url()
        get_except_text = success_excepted
        self.__dict__['_testMethodDoc'] = success_case_name  #将EXLcase_name赋值给页面用例描述
        # 调用基类截图方法
        login.save_img()
        # 断言
        # assert get_except_text in get_fail_text
        try:
            if self.com_util.is_contain(get_except_text, get_fail_text):
                print("预期结果：" + success_excepted)
                print("实际结果：" + get_fail_text)
                print(success_case_name + '-----√-Test Pass.--------' + success_remarks)
                print("\n")
                pass_count.append(UserLogin.a)
            else:
                print("预期结果：" + success_excepted)
                print("实际结果：" + get_fail_text)
                print(success_user_name + '-----×-Test Fail.--------' + success_remarks)
                print("\n")
                fail_count.append(UserLogin.a)
        except Exception as e:
                print('Fail', format(e))
        self.quit_browse()
        for x in range(UserLogin.a+1, success_rows_count):
            UserLogin.a +=  1
            UserLogin.test_login_fail(self)


        # print("登录有效用例的总数", len(pass_count) + len(fail_count))
        # print("登录有效用例成功的个数", len(pass_count))
        # print("登录有效用例失败个数", len(fail_count))
        # 发送自动化测试报告
        # self.zqsendmail.send_main2(pass_count, fail_count)

    def test_login_fail(self):

        self.zqsendmail = SendEmail()
        self.com_util = CommonUtil()
        self.opera_excel = ZqOperationExcel()
        self.open_browse()
        fail_case_name = ZqOperationExcel(file_name=exl_name, sheet_id=0).get_cell_value(UserLogin.b, 0)
        fail_user_name = ZqOperationExcel(file_name=exl_name, sheet_id=0).get_cell_value(UserLogin.b, 1)
        fail_user_pwd = ZqOperationExcel(file_name=exl_name, sheet_id=0).get_cell_value(UserLogin.b, 2)
        fail_excepted = ZqOperationExcel(file_name=exl_name, sheet_id=0).get_cell_value(UserLogin.b, 3)
        fail_remarks = ZqOperationExcel(file_name=exl_name, sheet_id=0).get_cell_value(UserLogin.b, 4)
        login = LoginPage(self.driver)
        login.user_account_search(fail_user_name)  # 调用页面对象中的方法
        login.password_search(fail_user_pwd)
        login.send_submit_btn()  # 调用页面对象类中的点击搜索按钮方法
        time.sleep(1)
        get_fail_text = login.get_real_text()
        get_except_text = fail_excepted
        self.__dict__['_testMethodDoc'] = fail_case_name #将EXLcase_name赋值给页面用例描述
        # 调用基类截图方法
        login.save_img()
        # 断言
        # assert get_except_text in get_fail_text
        try:
            if self.com_util.is_contain(get_except_text, get_fail_text):
                print("预期结果：" + fail_excepted)
                print("实际结果：" + get_fail_text)
                print(fail_case_name + '-----√-Test Pass.--------' + fail_remarks)
                print("\n")
                pass_count.append(UserLogin.b)
            else:
                print("预期结果：" + fail_excepted)
                print("实际结果：" + get_fail_text)
                print(fail_case_name + '-----×-Test Fail.--------' + fail_remarks)
                print("\n")
                fail_count.append(UserLogin.b)
        except Exception as e:
                print('Fail', format(e))
        self.quit_browse()
        for y in range(UserLogin.b+1, fail_rows_count):
            UserLogin.b += 1
            UserLogin.test_login_fail(self)

        # print("登录无效用例的总数", len(pass_count) + len(fail_count))
        # print("登录无效用例成功的个数", len(pass_count))
        # print("登录无效用例失败个数", len(fail_count))
        # 发送自动化测试报告
        # self.zqsendmail.send_main2(pass_count, fail_count)


if __name__ == '__main__':
    unittest.main()
