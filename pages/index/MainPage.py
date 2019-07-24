'''
        主页页面：
'''
from common import basePage
from selenium import webdriver
import time


class MainPage(basePage.BasePage):

    '''
        心之力系统主页面相关元素
    '''

    xzl_doctor=('xpath','//*[@id="wrapper"]/div/div/div[2]/div/div/div[1]/button[1]')
    # 首页的医院医生管理
    xzl_add=('xpath','//*[@id="wrapper"]/div/div/div[2]/div/section/div[1]/div[2]')
    # 主页面的添加机构
    xzl_jigouname=('xpath', '//*[@placeholder="请输入医院名字"]')
    xzl_jigouuname=('xpath', '//*[@placeholder="请输入管理员账号"]')
    xzl_jigouadd=('xpath','//*[@class="ant-btn ant-btn-primary"]')
    # 添加机构的弹窗输入框，以及提交按钮


    xzl_usertouxiang=('xpath','//*[@id="wrapper"]/div/div/div[1]/div[3]/div/span')
    # 总管理员的右侧头像
    xzl_userlogout=('xpath','/html/body/div[2]/div/div/ul/li[3]/div')
    # 总管理员的退出按钮

    xzl_shezhimima=('id','newPassword')
    xzl_shezhitijiao=('xpath','//*[@class="change-password__submit"]')
    # 首次登录设置密码 及提交




    def xinzhili_main(self,jigouname=0,jigouuname=0):
        '''登录进入主页面，添加机构'''
        self.click(self.xzl_doctor)
        self.click(self.xzl_add)
        time.sleep(1)
        self.sendKeys(self.xzl_jigouname, text=jigouname)
        self.sendKeys(self.xzl_jigouuname, text=jigouuname)
        time.sleep(1)
        self.click(self.xzl_jigouadd)
        time.sleep(1)

    def xinzhili_logout(self):
        '''退出登录'''
        self.click(self.xzl_usertouxiang)
        time.sleep(1)
        self.click(self.xzl_userlogout)
        time.sleep(1)

    def xinzhili_shezhi(self):
        '''首次登录后设置新密码'''
        self.click(self.xzl_doctor)
        time.sleep(0.5)
        self.sendKeys(self.xzl_shezhimima,text="111111")
        self.click(self.xzl_shezhitijiao)
        time.sleep(5)






