'''
 单个机构登录后的页面
'''
from common import basePage
from selenium import webdriver
import time


class jigouPage(basePage.BasePage):


    '''
        心之力机构主页面相关元素
    '''

    xzl_yiyuangunali = ('xpath','//*[@id="wrapper"]/div/div/div[2]/div/div/div[1]/button[1]')
    #进入首页的医院管理按钮

    xzl_jigouname=('xpath','//*[@class="group-side__hospital-name"]')
    xzl_addkeshiya =('xpath','//*[@id="wrapper"]/div/div/div[2]/div/section/div[1]/div/div/div/div[2]/div[1]/span')
    xzl_keshiname =('xpath','//*[@placeholder="请输入科室名字" and @type="text"]')
    xzl_xuanzekeshi=('xpath','/html/body/div[2]/div/div[2]/div/div[1]/div[2]/div/div[2]/div/div/div')
    xzl_shenjingneike=('xpath','//*[@id="wrapper"]/../div[3]/div/div/div/ul/li[3] ')
    xzl_tianjiakeshi=('xpath','//*[@class="ant-btn ant-btn-primary"]')
    #添加科室元素按钮

    xzl_clickkeshi=('xpath','//*[@id="wrapper"]/div/div/div[2]/div/section/div[1]/div/div/ul/li[2]/div/span')
    #点击科室，是医生、护士、患者唯一入口
    xzl_clickhushis=('xpath','//*[@id="wrapper"]/div/div/div[2]/div/section/div[1]/div/div/ul/li/div/span')
    #点击护士团队，是添加护士的入口
    xzl_xinxiongwaike=('xpath','//*[@id="wrapper"]/div/div/div[2]/div/section/div[1]/div/div/ul/li[3]/div/span')
    # 点击心胸外科

    xzl_updatakeshiya=('xpath','//*[@id="wrapper"]/div/div/div[2]/div/section/div[1]/div/div/ul/li[2]/div/span/i')
    xzl_updatekeshiname=('xpath','//*[@value="内分泌科" and @type="text"]')
    xzl_updatekeshiok = ('xpath', '//*[@class="ant-modal-body"]/div/div[3]/button')
    #修改科室名称内分泌科
    xzl_delkeshi=('xpath','//*[@id="wrapper"]/div/div/div[2]/div/section/div[1]/div/div/ul/li[6]/div/span/img')
    xzl_delok=('xpath','//*[@class="ant-btn stop ant-btn-primary"]')
    #删除科室按钮

    xzl_addyiyuan =('xpath','//*[@class="group-side__hospital-operatings"]/div[2]')
    xzl_inputyiyuanname=('xpath','//*[@placeholder="请输入医院名字"]')
    xzl_inputyiyuanusername=('xpath','//*[@placeholder="请输入管理员账号"]')
    xzl_addok=('xpath','//*[@class="group-side__add-panel-btn"]/button[2]')
    #添加医院页面元素

    xzl_updateyiyuan=('xpath','//*[@id="wrapper"]/div/div/div[2]/div/section/div[1]/div/div/ul/li[7]/div/div/div[2]/div/i')
    xzl_updateyiyuanname=('xpath','//*[@class="group-side__edit-panel-item"]/input')
    xzl_updatanameok=('xpath','//*[@class="group-side__edit-panel"]/div[3]/button')
    xzl_close=('xpath','//*[@class="group-side__edit-panel"]/div[3]/button[2]')
    xzl_closeok=('xpath','//*[@class="ant-btn ant-btn-primary"]')
    xzl_assert_close=('xpath','//*[@id="wrapper"]/div/div/div[2]/div/section/div[1]/div/div/ul/li[7]/div/div/div[2]/div[3]/span')

    xzl_openinto=('xpath','//*[@id="wrapper"]/div/div/div[2]/div/section/div[1]/div/div/ul/li[7]/div/div/div[2]/div/span')
    xzl_openok=('xpath','//*[@class="ant-btn ant-btn-primary"]')
    #修改医院名称和关闭、开启医院操作的元素


    '''
        心之力系统相关组件
    '''
    def xinzhili_clickyiyuanguanli(self):
        '''   点击医院医生管理，进入主页面'''
        self.click(self.xzl_yiyuangunali)
        time.sleep(1)

    def xinzhili_clcikjigouname(self):
        '''点击机构名称，展开科室下拉列表'''
        self.click(self.xzl_jigouname)

    def xinzhili_clickkeshi(self):
        '''点击内分泌科室科室，目的是为了出现右侧医生、护士、患者信息'''
        self.click(self.xzl_clickkeshi)
        time.sleep(1)

    def xinzhili_clickhushituandui(self):
        '''点击护士团队，目的是为了出现右侧护士，进行添加'''
        self.click(self.xzl_clickhushis)
    def xinzhili_clickxinxiongwaike(self):
        '''点击心胸外科，为了护士团队的移除科室定位'''
        self.click(self.xzl_xinxiongwaike)
        time.sleep(1)


    def xinzhili_addkeshi(self,keshiname=0):
        '''添加科室'''
        self.click(self.xzl_addkeshiya)
        time.sleep(1)
        self.sendKeys(self.xzl_keshiname,text=keshiname)
        self.click(self.xzl_xuanzekeshi)
        time.sleep(1)
        self.click(self.xzl_shenjingneike)
        self.click(self.xzl_tianjiakeshi)
        time.sleep(2)
        self.click(self.xzl_jigouname)
        time.sleep(1)


    def xinzhili_xiugaikeshi(self,keshiname=0):
        '''选择'内分泌科'进行修改按钮'''
        self.click(self.xzl_updatakeshiya)
        self.clear(self.xzl_updatekeshiname)
        self.sendKeys(self.xzl_updatekeshiname, text=keshiname)
        self.click(self.xzl_updatekeshiok)
        time.sleep(1)

    def xinzhili_delkeshipass(self):
        '''删除科室'''
        self.click(self.xzl_delkeshi)
        time.sleep(2)
        self.click(self.xzl_delok)
        time.sleep(2)
        self.get_screen(file_name="删除科室成功")
    def xinzhili_addyiyuan(self,name=0,yiyuanzhanghao=0):
        '''添加医院'''
        self.click(self.xzl_addyiyuan)
        self.sendKeys(self.xzl_inputyiyuanname,text=name)
        self.sendKeys(self.xzl_inputyiyuanusername,text=yiyuanzhanghao)
        self.click(self.xzl_addok)
        self.get_screen(file_name="添加医院成功")

    def xinzhili_clickupdateyiyuan(self):
        '''点击修改按钮'''
        self.click(self.xzl_updateyiyuan)
        time.sleep(0.4)

    def xinzhili_updatayiyuanmae(self,name):
        '''修改医院名字'''
        time.sleep(1)
        self.click(self.xzl_updateyiyuanname)
        self.clear(self.xzl_updateyiyuanname)
        self.sendKeys(self.xzl_updateyiyuanname,text=name)
        self.click(self.xzl_updatanameok)
        time.sleep(2)
        self.get_screen(file_name="修改医院名字")

    def xinzhili_closeyiyuan(self):
        '''医院停止服务'''
        self.click(self.xzl_close)
        time.sleep(2)
        self.click(self.xzl_closeok)
        time.sleep(1)



    def xinzhili_openyiyuan(self):
        '''开启医院服务'''
        self.click(self.xzl_openinto)
        time.sleep(2)
        self.click(self.xzl_openok)
        time.sleep(2)








