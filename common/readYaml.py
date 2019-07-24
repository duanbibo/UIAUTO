import yaml
import os

def read(yaml_name=None):
    # 获取当前脚本所在文件夹路径将    当前文件夹     ..
    curPath = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
    # 获取yaml文件路径
    yamlPath = os.path.join(curPath, "config/"+yaml_name)
    # open方法打开直接读出来
    f = open(yamlPath, 'r', encoding='utf-8')
    cfg = f.read()
    d = yaml.load(cfg)  # 用load方法转字典
    return d

# print(read(yaml_name="testcase.yaml"))
# {'testSuite': {'module': 'patient/test_004_addbingren.py nurse/test_003_delhushi.py nurse/test_003_yichuhushi.py nurse/test_003_fenpeihushi.py nurse/test_003_renzhenghushi.py nurse/test_003_addhushi.py docter/test_002_deloneyisheng.py docter/test_002_updateyisheng.py docter/test_002_renzhengyisheng.py docter/test_002_addyisheng.py xinzhili/test_delkeshipass.py xinzhili/test_openyiyuan.py xinzhili/test_closeyiyuan.py xinzhili/test_updateyiyuan.py xinzhili/test_addyiyuan.py xinzhili/test_updatakeshi.py xinzhili/test_addkeshi.py xinzhili/test_loginnew.py xinzhili/test_addjigou.py xinzhili/test_logout.py xinzhili/test_login.py'}, 'retrys': 0}