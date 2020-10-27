from public.pages.BaseTestCase import BaseTestCase as B
import unittest
from public.utils.Login_Data import Login_Data as login
from selenium import webdriver
import time
import sys
from testcases.test_login import TestLogin as L
#导入页面所有的元素值作为P
from public.pages.Page_Element import Page_Element as P
from common.handlelog import log
from public.utils.Login_Data import Login_Data as login
from common.login import Login as L
#上传文件插件
# import win32com.client
# shell=win32com.client.Dispatch("WScript.Shell")
# shell.Sendkeys(r"C:\Users\Administrator\a.jpg"+"\r\n") 这里的\r\n模拟回车符
url = login.get_url()
usernamenum = login.get_username()
codenum = login.get_code()
pwdnum = login.get_pwd()
login_success = login.get_login_success()

#随机生成6位数
import random
ran = ""
for i in range(6):
    ch = chr(random.randrange(ord('0'), ord('9') + 1))
    ran += ch

class Add_Online_Goods(B):
    @classmethod
    def setUpClass(cls):
        #执行用例前先登录
        L().login()
        B.sleep(3)

    @classmethod
    def tearDownClass(cls):
        #执行用例后返回首页
        B.sleep(3)
        B.goto_homeself()

    # def setUp(self):
    #     print("方法开始")
    #
    # def tearDown(self):
    #     print("方法结束")

    def test01_add_online_goods(self):
        # try:
        # 定位个人中心，然后点击
        goods = B.find_element(P.goods)
        B.click(goods)
        # 定位个人中心页面中的个人中心字样
        time.sleep(2)
        goodscentre = B.find_element(P.goodscentre)
        B.click(goodscentre)
        time.sleep(2)
        goodsdata = B.find_element(P.goodsdata)
        B.click(goodsdata)
        time.sleep(3)
        B.click(B.find_element(P.onlinegoods_platform))
        addonline = B.find_element(P.add_online)
        B.click(addonline)
        time.sleep(1)
        B.click(B.find_element(P.select_goods))
        time.sleep(2)
        B.click(B.find_element(P.select_goods_confirm))
        time.sleep(2)
        B.scroll()
        time.sleep(1)
        B.click(B.find_element(P.select_stuff))
        time.sleep(1)
        #先定位到原料下拉框
        yuanliao = B.find_elements(P.yuanliao)
        stuff1 = yuanliao.find_elements(P.stuff_1)
        print(stuff1)
        # B.moveto(stuff1)
        # B.click(stuff1)
        # stuff2 = B.find_element(P.stuff_1_1)
        # B.moveto(stuff2)
        # B.click(stuff2)
        # stuff3 = B.find_element(P.stuff_1_1_1)
        # B.moveto(stuff3)
        # B.click(stuff3)
        # B.click(B.find_element(P.add_online_confirm))
        # ran = random.choice('abcdefghiklmnopqrstuvwxyz')
        # B.send_keys(B.find_element(P.goodsname), ran)
        # B.click(B.find_element(P.gencode))
        # B.send_keys(B.find_element(P.priceout), ran)
        # B.send_keys(B.find_element(P.pricein), ran)
        # B.send_keys(B.find_element(P.count), ran)
        # B.scroll()
        # B.click(B.find_element(P.submit))
        # time.sleep(1)
        # add_success_text = B.get_text(P.add_success)
        # print(add_success_text)
        # try:
        #     assert add_success_text == "添加成功"
        # except Exception as e:
        #     # raise NameError("当前页面不包含%s" % (login_sucees_text))
        #     log.error('用例%s执行不通过'%(sys._getframe().f_code.co_name))
        #     # # format格式化，把case中的title写入{}中
        #     log.exception(e)
        #     raise e
        # else:
        #     log.info('用例%s执行通过'%(sys._getframe().f_code.co_name))
        #     # print("通过")
if __name__ == '__main__':
    unittest.main()