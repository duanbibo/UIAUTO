'''
    统一登陆界面

'''
from common import basePage
from selenium import webdriver
import time


class LoginPage(basePage.BasePage):

    '''统一登录网址'''
    url="http://ys.test.xzlcorp.com/#/login"

    '''
        心之力系统登录页面相关元素
    '''

    xzl_username=('id','username')
    xzl_password=('id','password')
    xzl_login_button=('xpath','//*[@id="wrapper"]/div/div/div[2]/div/form/div[4]/div/div/button')


    '''
        心之力系统相关组件
    '''
    def xinzhili_login(self,username=0,password=0):
        '''登陆心之力系统，账号：xinzhiliAdmin，密码：111111'''
        self.get(self.url)
        self.clear(self.xzl_username)
        self.sendKeys(self.xzl_username,text=username)
        self.clear(self.xzl_password)
        self.sendKeys(self.xzl_password,text=password)
        self.click(self.xzl_login_button)
        time.sleep(2)








