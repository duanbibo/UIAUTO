import pytest
from pages.index import loginPage
from pages.index import MainPage
from pages.index import jigouPage
from selenium import webdriver
from allure import MASTER_HELPER


@MASTER_HELPER.feature("心之力机构添加科室")
class TestAdd():

    @MASTER_HELPER.step("初始化启动浏览器")
    def setup_class(self):
        '''用例执行前，启动浏览器，创建chrome实例'''
        driver = webdriver.Chrome()
        driver.maximize_window()
        self.login_page = loginPage.LoginPage(driver)
        self.main_page = MainPage.MainPage(driver)
        self.jigou_page=jigouPage.jigouPage(driver)

    @MASTER_HELPER.step("关闭浏览器")
    def teardown_class(self):
        '''用例执行完毕，关闭浏览器'''
        self.login_page.quit()



    @MASTER_HELPER.testcase("用例名：心之力机构登录修改科室")
    def test_updatekeshi(self):

        with MASTER_HELPER.step("修改科室用例"):
            self.login_page.xinzhili_login(username="beifang", password="111111")
            self.jigou_page.xinzhili_clickyiyuanguanli()
            self.jigou_page.xinzhili_clcikjigouname()
            self.jigou_page.xinzhili_xiugaikeshi(keshiname="修改后")
            xzl_assert_updatekeshi = (
            'xpath', '//*[@id="wrapper"]/div/div/div[2]/div/section/div/div/div/ul/li[2]/div/span')
            assert "修改后" == self.jigou_page.get_text(xzl_assert_updatekeshi)




if __name__ == '__main__':
    pytest.main(['-s', 'test_login.py'])