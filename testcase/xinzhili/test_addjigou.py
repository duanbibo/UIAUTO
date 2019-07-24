import pytest
from pages.index import loginPage
from pages.index import MainPage
from selenium import webdriver
from allure import MASTER_HELPER


@MASTER_HELPER.feature("心之力添加机构")
class TestAdd():

    @MASTER_HELPER.step("初始化启动浏览器")
    def setup_class(self):
        '''用例执行前，启动浏览器，创建chrome实例'''
        driver = webdriver.Chrome()
        driver.maximize_window()
        self.login_page = loginPage.LoginPage(driver)
        self.main_page = MainPage.MainPage(driver)

    @MASTER_HELPER.step("关闭浏览器")
    def teardown_class(self):
        '''用例执行完毕，关闭浏览器'''
        self.login_page.quit()



    @MASTER_HELPER.testcase("用例名：心之力添加机构")
    def test_addjigou(self):
        '''xzl_jigouaddname = ('xpath', '//*[@text="beifang" and @class="group-side__hospital-name"]')'''
        with MASTER_HELPER.step("添加机构"):
            self.login_page.xinzhili_login(username="XinzhiliAdmin", password="111111")
            self.main_page.xinzhili_main(jigouname="beifang",jigouuname="beifang")



if __name__ == '__main__':
    pytest.main(['-s', 'test_login.py'])

