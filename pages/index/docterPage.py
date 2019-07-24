'''
 医生页面
'''
from common import basePage
import time


class docterPage(basePage.BasePage):


    '''
        心之力机构主页面相关元素
    '''

    xzl_adddocter = ('xpath','//*[@id="wrapper"]/div/div/div[2]/div/section/div[2]/div/div/div/div[2]/div[1]/button[1]')
    #医生页的添加按钮
    xzl_inpudoctername=('xpath','//*[@class="doctor-status__base"]/div/div/input')
    xzl_inputdoctertel=('xpath','//*[@class="doctor-status__base"]/div[2]/div/input')
    xzl_inputprice=('xpath','//*[@class="consultation_video"]/div[2]/div/div/div/div/div[2]/input')
    xzl_addbtn=('xpath','//*[@class="add-doctor__btns"]/button[2]')
     #医生认证
    xzl_docter=('xpath','//*[@id="wrapper"]/div/div/div[2]/div/section/div[2]/div/div/div/div[3]/div/div/div/div/div/table/tbody/tr/td[3]/a')
    xzl_passdocter = ('xpath', '//*[@id="wrapper"]/div/div/div[2]/div/section/div[2]/div/div/div/div[1]/div[3]/div[2]/button[1]')
    #修改医生资料:性别
    xzl_updatedocter=('xpath','//*[@class="department"]/div[2]/button')
    xzl_uodatexingbie=('xpath','//*[@class="ant-modal-content"]/div[2]/div/div/div/div/div[2]/div[3]/div/div/label[2]')
    xzl_updateok=('xpath','//*[@class="ant-modal-content"]/div[2]/div/div/div[2]/div/button[2]')
    xzl_back=('xpath','//*[@class="department"]/../a')
    #删除医生：单个
    xzl_deldocter=('xpath','//*[@id="wrapper"]/div/div/div[2]/div/section/div[2]/div/div/div/div[3]/div/div/div/div/div/table/tbody/tr/td[10]/span/span')
    xzl_delok=('xpath','/html/body/div[3]/div/div/div/div[2]/div/div/div[2]/button[2]')





    '''
        心之力系统相关组件
    '''
    def xinzhili_adddocter(self,name=0,tel=0,price=0):
        '''   添加医生'''
        self.click(self.xzl_adddocter)
        time.sleep(1)
        self.sendKeys(self.xzl_inpudoctername,text=name)
        self.sendKeys(self.xzl_inputdoctertel,text=tel)
        self.sendKeys(self.xzl_inputprice,text=price)
        self.click(self.xzl_addbtn)
        time.sleep(2)

    def xinzhhili_passdocter(self):
        '''认证通过医生'''
        self.click(self.xzl_docter)
        time.sleep(1)
        self.click(self.xzl_passdocter)
        time.sleep(1)
    def xinzhili_updatedocter(self):
        '''修改医生资料'''
        self.click(self.xzl_docter)
        time.sleep(0.5)
        self.click(self.xzl_updatedocter)
        time.sleep(2)
        self.click(self.xzl_uodatexingbie)
        time.sleep(1)
        self.click(self.xzl_updateok)
        time.sleep(1)
        self.click(self.xzl_back)
        time.sleep(1)
    def xinzhili_delonedocter(self):
        '''单个删除医生'''
        self.click(self.xzl_deldocter)
        time.sleep(1)
        self.click(self.xzl_delok)
        time.sleep(1)














