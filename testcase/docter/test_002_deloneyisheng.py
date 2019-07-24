import pytest
from pages.index import loginPage
from pages.index import MainPage
from pages.index import jigouPage
from pages.index import docterPage
from selenium import webdriver
from allure import MASTER_HELPER


@MASTER_HELPER.feature("心之力添加医生")
class TestAdd():

    @MASTER_HELPER.step("初始化启动浏览器")
    def setup_class(self):
        '''用例执行前，启动浏览器，创建chrome实例'''
        driver = webdriver.Chrome()
        driver.maximize_window()
        self.login_page = loginPage.LoginPage(driver)
        self.jigou_page = jigouPage.jigouPage(driver)
        self.docter_page=docterPage.docterPage(driver)
        self.main_page = MainPage.MainPage(driver)

    @MASTER_HELPER.step("关闭浏览器")
    def teardown_class(self):
        '''用例执行完毕，关闭浏览器'''
        self.login_page.quit()



    @MASTER_HELPER.testcase("用例名：删除单个医生")
    def test_delonedocter_001(self):

        with MASTER_HELPER.step("删除单个医生"):
            self.login_page.xinzhili_login(username="beifang", password="111111")
            self.jigou_page.xinzhili_clickyiyuanguanli()
            self.jigou_page.xinzhili_clcikjigouname()
            self.jigou_page.xinzhili_clickkeshi()
            self.docter_page.xinzhili_delonedocter()
            assert_xzl_deloneyisheng=('xpath','//*[@id="wrapper"]/div/div/div[2]/div/section/div[2]/div/div/div/div[3]/div/div/div/div/div[2]/span')
            assert "暂无数据"==self.docter_page.get_text(assert_xzl_deloneyisheng)






if __name__ == '__main__':
    pytest.main(['-s', 'test_login.py'])