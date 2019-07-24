import pytest
from pages.index import loginPage
from pages.index import MainPage
from pages.index import jigouPage
from selenium import webdriver
from allure import MASTER_HELPER


@MASTER_HELPER.feature("心之力首次登陆")
class TestLogin():

    @MASTER_HELPER.step("初始化启动浏览器")
    def setup_class(self):
        '''用例执行前，启动浏览器，创建chrome实例'''
        driver = webdriver.Chrome()
        driver.maximize_window()
        self.login_page = loginPage.LoginPage(driver)
        self.main_page = MainPage.MainPage(driver)
        self.jiou_page=jigouPage.jigouPage(driver)

    @MASTER_HELPER.step("关闭浏览器")
    def teardown_class(self):
        '''用例执行完毕，关闭浏览器'''
        self.login_page.quit()



    @MASTER_HELPER.testcase("用例名：心之力系统首次登录设置密码")
    def test_loginnew_001(self):
        with MASTER_HELPER.step("首次登录页面"):
            self.login_page.xinzhili_login(username="beifang", password="xinzhili")
            self.main_page.xinzhili_shezhi()
            self.login_page.xinzhili_login(username="beifang", password="111111")
            self.jiou_page.xinzhili_clickyiyuanguanli()
            assert_xzl_jigouname=('xpath','//*[@class="group-side__hospital-name"]')
            assert "beifang"==self.jiou_page.get_text(assert_xzl_jigouname)


if __name__ == '__main__':
    pytest.main(['-s', 'test_login.py'])

