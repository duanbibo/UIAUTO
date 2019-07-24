import pytest
from pages.index import loginPage
from selenium import webdriver
from allure import MASTER_HELPER




@MASTER_HELPER.feature("心之力登陆")
class TestLogin():

    @MASTER_HELPER.step("初始化启动浏览器")
    def setup_class(self):
        '''用例执行前，启动浏览器，创建chrome实例'''
        driver=webdriver.Chrome()
        driver.maximize_window()
        self.login_page=loginPage.LoginPage(driver)


    @MASTER_HELPER.step("关闭浏览器")
    def teardown_class(self):
        '''用例执行完毕，关闭浏览器'''
        self.login_page.quit()

    @MASTER_HELPER.testcase("用例名：登陆心之力——异常场景")
    def test_login_001(self):
        with MASTER_HELPER.step("异常登陆心之力"):
            self.login_page.xinzhili_login(username="abc", password="123456")
            self.login_page.get_screen(file_name="用户或密码不正确登录")

    @MASTER_HELPER.testcase("用例名：登陆心之力——正常场景")
    def test_login_002(self):
        with MASTER_HELPER.step("正常登陆心之力"):
            self.login_page.xinzhili_login(username="XinzhiliAdmin",password="111111")
            self.login_page.get_screen(file_name="正常登录首页")










if __name__ == '__main__':
    pytest.main(['-s','test_login.py'])

    