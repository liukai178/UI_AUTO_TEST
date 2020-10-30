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
url = login.get_url()
usernamenum = login.get_username()
codenum = login.get_code()
pwdnum = login.get_pwd()
login_success = login.get_login_success()
class Test_Browse_Goods(B):
    @classmethod
    def setUpClass(cls):
        L().login()
        B.sleep(3)

    @classmethod
    def tearDownClass(cls):
        B.sleep(3)
        B.goto_homeself()
        B.quit()
    # def setUp(self):
    #     print("方法开始")
    #
    # def tearDown(self):
    #     print("方法结束")

    def test01_browse_goods(self):
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
        offline_text = B.get_text(P.offlinegoods)
        print(offline_text)
        try:
            assert offline_text == "线下平台商品"
        except Exception as e:
            # raise NameError("当前页面不包含%s" % (login_sucees_text))
            log.error('用例%s执行不通过'%(sys._getframe().f_code.co_name))
            # # format格式化，把case中的title写入{}中
            log.exception(e)
            raise e
        else:
            log.info('用例%s执行通过'%(sys._getframe().f_code.co_name))
            # print("通过")
if __name__ == '__main__':
    unittest.main()