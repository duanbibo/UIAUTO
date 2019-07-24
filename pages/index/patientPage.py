'''
 患者页面
'''
from common import basePage
import time


class PatientPage (basePage.BasePage):


    '''
        心之力机构患者相关元素
    '''


    xzl_intohuanzhe=('xpath','//*[@class="institution-department"]/ul/li[3]/a')
    xzl_addone=('xpath','//*[@id="wrapper"]/div/div/div[2]/div/section/div[2]/div/div/div/div[2]/div[1]/button[1]')
    xzl_tel=('id','tel')
    xzl_clickchoseyiyuan=('xpath','//*[@class="choose__role"]/div/div/div/div/div')
    xzl_choseyiyuan=('xpath','//*[@title="测试新建一级医院机构"]')
    xzl_choseyisheng=('xpath','//*[@class="choose__role-content"]/div/div/img')  #选择第一个医师
    xzl_addok=('xpath','//*[@class="patient--add-btn"]')




    '''
        患者护士页面相关操作
    '''
    def xinzhili_intopatient(self):
        '''点击进入患者页签页面'''
        self.click(self.xzl_intohuanzhe)
        time.sleep(3)
    def xinzhili_addone(self,tel=0):
        '''单个添加患者'''
        self.click(self.xzl_addone)
        self.sendKeys(self.xzl_tel,text=tel)
        self.click(self.xzl_clickchoseyiyuan)
        time.sleep(1)
        self.click(self.xzl_choseyiyuan)
        time.sleep(1)
        self.click(self.xzl_choseyisheng)
        self.click(self.xzl_addok)
        time.sleep(1)
        self.get_screen(file_name="患者添加成功")
        time.sleep(1)





















