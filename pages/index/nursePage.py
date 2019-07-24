'''
 护士页面
'''
from common import basePage
import time


class nursePage (basePage.BasePage):


    '''
        心之力机构主页面相关元素
    '''

    #添加护士元素
    xzl_addhushi=('xpath','//*[@class="group-content"]/div/div/div[2]/div/button')
    xzl_inputhushiname=('xpath','//*[@class="ant-modal-body"]/div/form/div/div[2]/div/input')
    xzl_inputhushitel=('xpath','//*[@class="ant-modal-body"]/div/form/div[3]/div[2]/div/input')
    xzl_xiayibu=('xpath','//*[@class="ant-modal-body"]/div/div/button')
    xzl_chosekeshi=('xpath','//*[@class="ant-modal-body"]/div/div/label/span')
    xzl_addend=('xpath','//*[@class="ant-modal-body"]/div/div[2]/button')
    #认证护士元素
    xzl_clickname=('xpath','//*[@class="ant-table-body"]/table/tbody/tr/td[3]/a')
    xzl_renzhengpass=('xpath','//*[@class="department"]/div[3]/div[2]/button[1]')
    xzl_renzhengback=('xpath','//*[@class="department"]/../a')
    #给护士分配科室
    xzl_gouxuan=('xpath','//*[@class="ant-table-body"]/table/tbody/tr/td/span/label/span/input')
    xzl_fenpei=('xpath','//*[@class="group-content"]/div/div/div[2]/div/button[4]')
    xzl_xuanzekeshi=('xpath','//*[@class="ant-modal-body"]/label[2]/span/input')
    xzl_queren=('xpath','//*[@class="ant-modal-footer"]/button[2]')
    #移除科室下的护士
    xzl_hushi=('xpath','//*[@id="wrapper"]/div/div/div[2]/div/section/div[2]/div/ul/li[2]/a')
    xzl_yichu=('xpath','//*[@id="wrapper"]/div/div/div[2]/div/section/div[2]/div/div/div/div[2]/div/button[2]')
    xzl_yichuok=('xpath','//*[@class="ant-modal-wrap "]/div/div/div[2]/div/button[2]')
    #删除护士
    xzl_delonehushhi=('xpath','//*[@class="ant-table-body"]/table/tbody/tr/td[9]/span/span')
    xzl_deloneok=('xpath','/html/body/div[3]/div/div/div/div[2]/div/div/div[2]/button[2]')
    #批量添加护士
    xzl_piliangadd=('xpath','//*[@class="group-content"]/div/div/div[2]/div/button[2]')
    xzl_inputload=('xpath','//*[@class="ant-modal-body"]/div/span/div/span/input')
    xzl_upload=('xpath','//*[@class="ant-modal-body"]/div/span/div/span/button')








    '''
        护士页面相关操作
    '''
    def xinzhili_clickintonurse(self):
        '''点击进入护士添加页面'''
        self.click(self.xzl_addhushi)
        time.sleep(3)

    def xinzhili_addnurse(self,name=0,tel=0):
        '''   添加护士信息页面-内分泌科'''
        self.sendKeys(self.xzl_inputhushiname,text=name)
        self.sendKeys(self.xzl_inputhushitel,text=tel)
        self.click(self.xzl_xiayibu)
        time.sleep(1)
        self.click(self.xzl_chosekeshi)
        self.click(self.xzl_addend)
        time.sleep(2)
    def xinzhili_passnurse(self):
        '''认证护士页面'''
        self.click(self.xzl_clickname)
        time.sleep(1)
        self.click(self.xzl_renzhengpass)
        time.sleep(0.5)
        self.click(self.xzl_renzhengback)
        time.sleep(0.5)
    def xinzhili_fenpei(self):
        '''分配科室页面-心胸外科'''
        self.click(self.xzl_gouxuan)
        time.sleep(1)
        self.click(self.xzl_fenpei)
        time.sleep(1)
        self.click(self.xzl_xuanzekeshi)
        time.sleep(0.5)
        self.click(self.xzl_queren)
        time.sleep(0.5)
    def xinzhili_yichu(self):
        '''移除科室内护士'''
        self.click(self.xzl_hushi)
        time.sleep(1)
        self.click(self.xzl_gouxuan)
        time.sleep(1)
        self.click(self.xzl_yichu)
        time.sleep(0.5)
        self.click(self.xzl_yichuok)
        time.sleep(0.5)
    def xinzhili_delonehushi(self):
         '''删除单个护士'''
         self.click(self.xzl_delonehushhi)
         time.sleep(1)
         self.click(self.xzl_deloneok)
         time.sleep(0.5)
    def xinzhili_piliangaddhushi(self,file=0):
        '''批量上传护士'''
        self.click(self.xzl_piliangadd)
        time.sleep(1)
        #选中页面input=file，发送本地文件
        self.js_set_attribute("body > div:nth-child(12) > div > div.ant-modal-wrap > div > div.ant-modal-content > div.ant-modal-body > div.upload__panel > span > div.ant-upload.ant-upload-select.ant-upload-select-text > span > input[type=file]","style","block")
        time.sleep(2)
        self.sendKeys(self.xzl_inputload,text=file)













