'''
 患者详情页面
'''
from common import basePage
import time


class huanzhePage(basePage.BasePage):


    '''
        心之力机构主页面相关元素
    '''
     #进入患者详情页面
    xzl_clicklook = ('xpath','//*[@id="wrapper"]/div/div/div[2]/div[2]/div/div/div[1]/div[1]/div[1]/div/p')
    xzl_intohuanzhe=('xpath','//*[@class="ant-table-body"]/table/tbody/tr/td[2]/a')
    #
    xzl_clickadd=('xpath','//*[@class="operation"]/div[3]/img')

    xzl_show=('xpath','//*[@id="stage1"]/div[2]')
    xzl_addone=('xpath','//*[@id="stage1"]/div[2]/div/div/div[3]/div/input')
    xzl_chosezhenduan=('xpath','/html/body/div[2]/div/div/div/ul/li[1]')
    xzl_commitzhenduan=('xpath','//*[@class="ant-form ant-form-horizontal operate__diagnose add"]/div[4]/button[2]')
    #添加一级诊断元素

    xzl_bianji=('xpath','//*[@class="operation__item modify-item"]/li/div/div/div/div[2]/span')
    xzl_chosezhenduan2=('xpath','/html/body/div[3]/div/div/div/ul/li[1]')
    xzl_updatecommit=('xpath','//*[@class="edit"]/form/div[4]/button[2]')
   #修改一级诊断，修改后2分钟后xzl_bianji的xpath的class属性会变化

    xzl_del=('xpath','//*[@class="operation__item modify-item"]/li/div/div/div/div[2]/span[2]')
    xzl_delok=('xpath','//*[@class="ant-popover-buttons"]/button[2]')
    #删除一级诊断
    xzl_yongyaodabiao=('xpath','//*[@id="patientPanel"]/div/div[2]/div[2]/div[1]/div/div[2]/div/div[3]/div')
    #用药达标
    xzl_inputdabiaovalue=('xpath','//*[@class="inspection"]/div/ul/li[2]/div[2]/div/div[2]/input')
    xzl_dabiaook=('xpath','//*[@class="common__btn"]/button[2]')
    #生活达标
    xzl_shenghuo=('xpath','//*[@id="wrapper"]/div/div/div[1]/div/div/div/div/div/div[4]/div[1]')
    #调整用药
    xzl_tiaozhengyao=('xpath','//*[@id="wrapper"]/div/div/div[1]/div/div/div/div/div/div[4]/div[4]')
    xzl_addnewyao=('xpath','//*[@class="ant-modal-content"]/div[2]/div/form/div')

    xzl_showyongyao=('xpath','//*[@class="adjust-plan__list"]/div/div/div')
    xzl_addinput=('xpath','//*[@class="ant-modal-body"]/div/form/ul/li[2]/div/div/div/div/div[3]/div/input')
    xzl_choseyaopin=('xpath','//*[@class="ant-select-dropdown-menu ant-select-dropdown-menu-vertical  ant-select-dropdown-menu-root"]/li')

    xzl_showjiliang=('xpath','//*[@class="adjust-plan__list"]/ul/li/div/div/div[2]')
    xzl_inputjiliang=('xpath','//*[@class="adjust-plan__list"]/ul/li/div/div/div[2]/input')

    xzl_showtime=('path','//*[@class="adjust-plan__list"]/ul/li/div[2]/div/div')
    xzl_choseyongyaotime=('xpath','//*[@class="ant-select-dropdown adjust-plan__time ant-select-dropdown--multiple ant-select-dropdown-placement-bottomLeft  ant-select-dropdown-hidden" ]/div/ul/li[2]/ul/li')
    xzl_yongyaook=('xpath','/html/body/div[3]/div/div[2]/div/div[1]/div[2]/div/div/button[2]')
    xzl_fasongyongyao=('xpath','/html/body/div[3]/div/div[2]/div/div[1]/div[2]/div/div[2]/button[1]')

     #医生建议和操作历史
    xzl_intocaozuolishi=('xpath','//*[@id="actionPanel"]/div[2]/div[1]/ul/li[3]/a')
    xzl_clickjianyi=('xpath','//*[@id="actionPanel"]/div[2]/div[2]/div[2]/button')
    xzl_inputjianyi=('id','advice')
    xzl_inputjianyiok=('xpath','//*[@class="ant-col-12 ant-col-offset-4 ant-form-item-control-wrapper"]/div/button')
    # 会诊，发送会诊邀请
    xzl_intohuizhen=('xpath','//*[@id="actionPanel"]/div[2]/div[1]/ul/li[4]/span/a')
    xzl_clickhuizhen=('xpath','//*[@id="actionPanel"]/div[2]/div[2]/div[4]/div/div[1]/button[2]')
    xzl_choseyiyuan=('xpath','//*[@class="consultation-departments"]/div[2]/div/div/div[2]/li/label')
    xzl_next=('xpath','//*[@class="consultation-departments"]/div[4]')
    xzl_inputbingqing=('xpath','//*[@placeholder="请输入患者详情"]')
    xzl_inputmudi=('xpath','//*[@placeholder="请输入会诊目的"]')
    xzl_huizhenok=('xpath','//*[@class="consultation-question"]/div[4]/button[2]')





    '''
        心之力系统患者详情页面
    '''
    def xinzhili_seehuanzhe(self):
        '''点击查看进入患者列表页面'''
        self.click(self.xzl_clicklook)
        time.sleep(2)
    def xinzhili_intohuanzhe(self):
        '''点击患者列表中，第一个用户的名称，进入详情页面'''
        self.click(self.xzl_intohuanzhe)
        time.sleep(2)
    def xinzhili_addonezhenduan(self,zhenduan=0):
        '''添加一级诊断'''

        self.click(self.xzl_clickadd)
        time.sleep(1)
        self.click(self.xzl_show)
        time.sleep(2)
        self.sendKeys(self.xzl_addone,text=zhenduan)
        time.sleep(2)
        self.click(self.xzl_chosezhenduan)
        time.sleep(2)
        self.click(self.xzl_commitzhenduan)

    def xinzhili_updatezhenduan(self,zhenduan=0):
        '''修改一级诊断'''
        self.click(self.xzl_bianji)
        time.sleep(1)
        self.click(self.xzl_show)
        time.sleep(1)
        self.clear(self.xzl_addone)
        time.sleep(1)
        self.sendKeys(self.xzl_addone,text=zhenduan)
        time.sleep(2)
        self.click(self.xzl_chosezhenduan2)
        time.sleep(2)
        self.click(self.xzl_updatecommit)
        time.sleep(2)

    def xinzhili_delzhenduan(self):
        '''删除一级诊断'''
        self.click(self.xzl_del)
        time.sleep(1)
        self.click(self.xzl_delok)
        time.sleep(1)
    def xinzhili_updateyongyaodabiao(self,value=0):
        '''修改用药达标'''
        self.click(self.xzl_yongyaodabiao)
        time.sleep(1)
        self.click(self.xzl_inputdabiaovalue)
        self.clear(self.xzl_inputdabiaovalue)
        self.sendKeys(self.xzl_inputdabiaovalue,text=value)
        self.click(self.xzl_dabiaook)
        time.sleep(1)
        self.click(self.xzl_dabiaook)
        time.sleep(1)
    def xinzhili_seeshenghuo(self):
        self.click(self.xzl_shenghuo)
        time.sleep(2)
    def xinzhili_addnewyao(self,yaopin=0,jiliang=0):
        self.click(self.xzl_tiaozhengyao)
        time.sleep(3)
        self.click(self.xzl_addnewyao)
        time.sleep(5)
        self.click(self.xzl_showyongyao)
        self.sendKeys(self.xzl_addinput,text=yaopin)
        time.sleep(5)
        self.click(self.xzl_choseyaopin)
        time.sleep(1)
        self.move_to_element(self.xzl_showjiliang)
        time.sleep(2)
        self.click(self.xzl_inputjiliang)
        self.sendKeys(self.xzl_inputjiliang,text=jiliang)
        time.sleep(2)
        self.click(self.xzl_showtime)
     #   self.js_showtime()
        time.sleep(2)
        self.click(self.xzl_choseyongyaotime)
        time.sleep(2)
        self.click(self.xzl_yongyaook)
        time.sleep(2)
        self.click(self.xzl_fasongyongyao)
        time.sleep(2)

    def xinzhili_intocaozuolishi(self):
        self.click(self.xzl_intocaozuolishi)

    def xinzhili_addjianyi(self,jianyi=0):
        time.sleep(2)
        self.click(self.xzl_clickjianyi)
        self.sendKeys(self.xzl_inputjianyi,text=jianyi)
        self.click(self.xzl_inputjianyiok)
        self.refresh()
    def xinzhili_intohuizhen(self):
        self.click(self.xzl_intohuizhen)

    def xinzhili_addhuizhen(self,bingqing=0,mudi=0):
        time.sleep(2)
        self.click(self.xzl_clickhuizhen)
        time.sleep(1)
        self.click(self.xzl_choseyiyuan)
        self.click(self.xzl_next)
        time.sleep(1)
        self.sendKeys(self.xzl_inputbingqing,text=bingqing)
        self.sendKeys(self.xzl_inputmudi,text=mudi)
        self.click(self.xzl_huizhenok)
        time.sleep(2)




























