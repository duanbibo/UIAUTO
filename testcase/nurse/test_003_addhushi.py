import pytest
from pages.index import loginPage
from pages.index import MainPage
from pages.index import jigouPage
from pages.index  import nursePage
from selenium import webdriver
from allure import MASTER_HELPER


@MASTER_HELPER.feature("心之力添护士")
class TestAdd():

    @MASTER_HELPER.step("初始化启动浏览器")
    def setup_class(self):
        '''用例执行前，启动浏览器，创建chrome实例'''
        driver = webdriver.Chrome()
        driver.maximize_window()
        self.login_page = loginPage.LoginPage(driver)
        self.jigou_page = jigouPage.jigouPage(driver)
        self.nurse_page = nursePage.nursePage(driver)
        self.main_page = MainPage.MainPage(driver)

    @MASTER_HELPER.step("关闭浏览器")
    def teardown_class(self):
        '''用例执行完毕，关闭浏览器'''
        self.login_page.quit()



    @MASTER_HELPER.testcase("用例名：心之力添加护士")
    def test_addnurse_001(self):

        with MASTER_HELPER.step("添加护士"):
            self.login_page.xinzhili_login(username="beifang", password="111111")
            self.jigou_page.xinzhili_clickyiyuanguanli()
            self.jigou_page.xinzhili_clcikjigouname()
            self.jigou_page.xinzhili_clickhushituandui()
            self.nurse_page.xinzhili_clickintonurse()
            self.nurse_page.xinzhili_addnurse(name="王五",tel=13868475865)
            xzl_hushi=('xpath','//*[@class="lists__table--name"]')
            assert "王五" == self.nurse_page.get_text(xzl_hushi)






if __name__ == '__main__':
    pytest.main(['-s', 'test_login.py'])