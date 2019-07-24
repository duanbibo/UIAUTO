import pytest
from common import readYaml
from selenium import webdriver
import os
import sys

if __name__ == '__main__':

    '''读取重跑次数,项目路径'''
    dit = readYaml.read("testcase.yaml")
    dit2 = readYaml.read("project.yaml")  #定义项目的绝对路径
    dit3 =readYaml.read("allure.yaml")
    dit4 = readYaml.read("webdriver.yaml")
    retrys = dit['retrys']
    modules = dit['testSuite']['module'].split(" ")
    command = ["-s", "-q", "--reruns", str(retrys), "--alluredir", "./reports/xml"]
    dirname = dit2['project']['path']
    allure =dit3['allure']['path']         #tools\allure-2.7.0\bin
    webdri = dit4['webdriver']['path']     # tools/chromedriver.exe
    absallure=os.path.abspath(allure)
    abswebdri=os.path.abspath(webdri)
    #os.putenv('path',absallure)
    os.environ['path']=abswebdri
    # os.environ['path']=absallure
    #print(os.environ['path'])
    print(modules)



    sys.path.append(abswebdri)

    # sys.path.append(absallure)
    #
    # print(sys.path[18])
    #print(sys.path[19])

    '''拼接路径'''
    for i in modules:
        i = dirname + '/testcase/' + i
        command.insert(2, i)
    print(command)

    '''执行pytest和allure命令'''
    pytest.main(command)
    # os.system("allure generate --clean reports/xml -o  reports/html")
    #os.system 执行cmd命令

