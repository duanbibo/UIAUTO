import pytest
import runCase
from pages.index import loginPage
from pages.index import huanzhepage
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
        self.huanzhe_page=huanzhepage.huanzhePage(driver)


    @MASTER_HELPER.step("关闭浏览器")
    def teardown_class(self):
        '''用例执行完毕，关闭浏览器'''
        self.login_page.quit()



    @MASTER_HELPER.testcase("用例名：医生为患者添加一级诊断")
    def test_001_addzhenduan(self):
        with MASTER_HELPER.step("添加一级诊断"):
            self.login_page.xinzhili_login(username="13666666666",password="xinzhili")
            self.huanzhe_page.xinzhili_seehuanzhe()
            self.huanzhe_page.xinzhili_intohuanzhe()
            self.huanzhe_page.xinzhili_addonezhenduan(zhenduan="综合")
            assert_addzhenduan=('xpath','//*[@class="operation__item modify-item"]/li/div/div/div/div')
            assert "沃-弗综合征"== self.huanzhe_page.get_text(assert_addzhenduan)


    @MASTER_HELPER.testcase("用例名：医生为患者修改一级诊断")
    def test_002_updatezhenduan(self):
         with MASTER_HELPER.step("修改一级诊断"):
             self.login_page.xinzhili_login(username="13666666666", password="xinzhili")
             self.huanzhe_page.xinzhili_seehuanzhe()
             self.huanzhe_page.xinzhili_intohuanzhe()
             self.huanzhe_page.xinzhili_updatezhenduan(zhenduan="人类")
             assert_updatezhenduan = ('xpath', '//*[@class="operation__item modify-item"]/li/div/div/div/div')
             assert "人类免疫缺陷病毒病伴分枝杆菌性感染" == self.huanzhe_page.get_text(assert_updatezhenduan)


    @MASTER_HELPER.testcase("用例名：医生为患者删除一级诊断")
    def test_003_delzhenduan(self):
          with MASTER_HELPER.step("删除一级诊断"):
             self.login_page.xinzhili_login(username="13666666666", password="xinzhili")
             self.huanzhe_page.xinzhili_seehuanzhe()
             self.huanzhe_page.xinzhili_intohuanzhe()
             self.huanzhe_page.xinzhili_delzhenduan()
             assert_delzhenduan = ('xpath', '//*[@class="operation__item modify-item"]/li')
             assert "暂无诊断信息" == self.huanzhe_page.get_text(assert_delzhenduan)

    @MASTER_HELPER.testcase("用例名：医生为修改用药达标值")
    def test_004_xiugaiyongyao(self):
        with MASTER_HELPER.step("修改用药达标值"):
            self.login_page.xinzhili_login(username="13666666666", password="xinzhili")
            self.huanzhe_page.xinzhili_seehuanzhe()
            self.huanzhe_page.xinzhili_intohuanzhe()
            self.huanzhe_page.xinzhili_updateyongyaodabiao(value="120")
            assert_updatedabiao = ('xpath', '//*[@id="patientPanel"]/div/div[2]/div[2]/div[1]/div/div[2]/ul/li[1]/div[2]/div/div/span')
            assert "120" in self.huanzhe_page.get_text(assert_updatedabiao)

    @MASTER_HELPER.testcase("用例名：医生查看患者生活达标信息")
    def test_005_seeshenghuo(self):
        with MASTER_HELPER.step("查看生活达标"):
            self.login_page.xinzhili_login(username="13666666666", password="xinzhili")
            self.huanzhe_page.xinzhili_seehuanzhe()
            self.huanzhe_page.xinzhili_intohuanzhe()
            self.huanzhe_page.xinzhili_seeshenghuo()
            assert_seeshenghuo = ('xpath', '//*[@class="life-condition__item"]/div')
            assert "5月" in self.huanzhe_page.get_text(assert_seeshenghuo)

    # @MASTER_HELPER.testcase("用例名：医生添加患者用药达标")
    # def test_006_addyongyao(self):
    #     with MASTER_HELPER.step("添加用药"):
    #         self.login_page.xinzhili_login(username="13666666666", password="xinzhili")
    #         self.huanzhe_page.xinzhili_seehuanzhe()
    #         self.huanzhe_page.xinzhili_intohuanzhe()
    #         self.huanzhe_page.xinzhili_addnewyao(yaopin="阿莫",jiliang="20")

    @MASTER_HELPER.testcase("用例名：医生待审核问题")
    def test_007_shenhewenti(self):
        with MASTER_HELPER.step("医生审核问题"):
            self.login_page.xinzhili_login(username="13666666666", password="xinzhili")
            self.huanzhe_page.xinzhili_seehuanzhe()
            self.huanzhe_page.xinzhili_intohuanzhe()
            assert_shenhewenti=('xpath','//*[@id="actionPanel"]/div[2]/div[2]/div[1]/div/div/ul[1]/li/div[3]/div')
            assert "调整"== self.huanzhe_page.get_text(assert_shenhewenti)

    @MASTER_HELPER.testcase("用例名：医生建议及操作历史")
    def test_008_addjianyi(self):
        with MASTER_HELPER.step("医生填写建议"):
            self.login_page.xinzhili_login(username="13666666666", password="xinzhili")
            self.huanzhe_page.xinzhili_seehuanzhe()
            self.huanzhe_page.xinzhili_intohuanzhe()
            self.huanzhe_page.xinzhili_intocaozuolishi()
            self.huanzhe_page.xinzhili_addjianyi(jianyi="好好吃药")
            self.huanzhe_page.xinzhili_intocaozuolishi()
            assert_jianyi = ('xpath', '//*[@id="actionPanel"]/div[2]/div[2]/div[2]/div/div/ul[1]/li[1]/ul/li/div')
            assert "好好吃药" == self.huanzhe_page.get_text(assert_jianyi)

    @MASTER_HELPER.testcase("用例名：医生像患者发送会诊邀请")
    def test_009_addhuizhen(self):
        with MASTER_HELPER.step("医生会诊邀请"):
            self.login_page.xinzhili_login(username="13666666666", password="xinzhili")
            self.huanzhe_page.xinzhili_seehuanzhe()
            self.huanzhe_page.xinzhili_intohuanzhe()
            self.huanzhe_page.xinzhili_intohuizhen()
            self.huanzhe_page.xinzhili_addhuizhen(bingqing="我有病",mudi="看病呀")
            assert_bingqing = ('xpath', '//*[@class="consultation__lists"]/div/div[2]/div[2]/p')
            assert "我有病" == self.huanzhe_page.get_text(assert_bingqing)


if __name__ == '__main__':
    pytest.main(['-s', 'test_login.py'])