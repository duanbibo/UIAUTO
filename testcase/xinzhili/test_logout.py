import pytest
from pages.index import loginPage
from pages.index import MainPage
from selenium import webdriver
from allure import MASTER_HELPER




@MASTER_HELPER.feature("心之力退出")
class TestLogin():

    @MASTER_HELPER.step("初始化启动浏览器")
    def setup_class(self):
        '''用例执行前，启动浏览器，创建chrome实例'''
        driver=webdriver.Chrome()
        driver.maximize_window()
        self.login_page=loginPage.LoginPage(driver)
        self.main_page = MainPage.MainPage(driver)


    @MASTER_HELPER.step("关闭浏览器")
    def teardown_class(self):
        '''用例执行完毕，关闭浏览器'''
        self.login_page.quit()



    @MASTER_HELPER.testcase("用例名：登录退出心之力系统")
    def test_logout_001(self):
        with MASTER_HELPER.step("正常退出心之力"):
            self.login_page.xinzhili_login(username="XinzhiliAdmin",password="111111")
            self.main_page.xinzhili_logout()
            self.main_page.get_screen(file_name="退出登录成功")
            jianchadian=('xpath','//*[@id="wrapper"]/div/div/div[2]/div/div')
            assert "账号登录" == self.login_page.get_text(jianchadian)












if __name__ == '__main__':
    pytest.main(['-s','test_login.py'])

