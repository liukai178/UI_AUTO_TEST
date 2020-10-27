from public.pages.BaseTestCase import BaseTestCase as B
import unittest
from public.utils.Login_Data import Login_Data as login
from selenium import webdriver
#显式等待（只等待某个元素）
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from common.handlelog import log
import time
import sys
#导入页面所有的元素值作为P
from public.pages.Page_Element import Page_Element as P
class Testdemo(B):
    # url = login.get_url()
    @classmethod
    def setUpClass(cls):
        #设置driver（打开浏览器）
        driver = webdriver.Firefox()
        #设置driver为全局
        B.set_driver(driver)
    @classmethod
    def tearDownClass(cls):
        #每次跑完用例之后的清理工作，此处是回到首页
        B.sleep(3)
        # B.goto_home()

    def test001_demo(self):
        '''
        第一个用例为登录，需要打开浏览器，输入网址并登录;
        后续如果不用重新打开浏览器，则不用调用get_driver
        :return:
        '''
        #调用set好的driver，后续其他用例如果需要重新打开此浏览器也可如此调用，浏览器没关则不用
        driver = B.get_driver()
        B.wait(3)
        # driver.get(url)
        # BaseTestCaase.get_driver().get(url)
        driver.maximize_window()
        driver.get("https://www.baidu.com/")#打开测试网址
        shuru = B.find_element(P.baidushuru)
        text = "csdn"
        B.send_keys(shuru,text)
        baidu = B.find_element(P.baidu)
        B.click(baidu)

        try:
            assert text in self.driver.page_source, u"当前页面是否包含关键字，%s"%(text)
        except Exception as e:
            raise NameError("当前页面不包含%s"%(text))
            # log.error('用例{}执行不通过'.format(sys._getframe().f_code.co_name)
        else:
            print("用例{}通过".format(sys._getframe().f_code.co_name))
if __name__ == '__main__':
    unittest.main()