from public.pages.BaseTestCase import BaseTestCase as B
import unittest
from public.utils.Login_Data import Login_Data as login
from selenium import webdriver
from common.readexcel import *
from common.handlepath import *
#显式等待（只等待某个元素）
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import time
#导入页面所有的元素值作为P
from public.pages.Page_Element import Page_Element as P
from common.handlelog import log
import sys
import time
url = login.get_url()
usernamenum = login.get_username()
codenum = login.get_code()
pwdnum = login.get_pwd()
login_success = login.get_login_success()
print(login_success)
filename = os.path.join(DATADIR,"Data.xlsx")
print(filename)
RD = ReadExcel(filename,"Sheet1")
class TestLogin(B):
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
        B.goto_home()

    def test01_login(self):
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
        driver.get(url)#打开测试网址
        B.wait(20)
        #输入用户名
        user = B.find_element(P.uservalue)
        #此处的usernamenum是从excel读取的
        B.send_keys(user,usernamenum)
        #输入验证码
        # codevalue = ("css","#loginForm > div.verification > input")
        # code = BaseTestCaase.find_element(P.codevalue)
        # BaseTestCaase.send_keys(code,codenum)
        #输入密码
        # pwdvalue = ("css","#loginForm > div.password-login > div.password-wrap > input")
        pwd = B.find_element(P.pwdvalue)
        B.send_keys(pwd,pwdnum)
        # 点击同意协议
        # agreevalue = ("css","#loginForm > div.remember-agree > div > label")
        # agree = BaseTestCaase.find_element(P.agreevalue)
        # BaseTestCaase.click(agree)
        # 点击确定提交
        # submitvalue = ("css","#loginForm > button")
        # submit = BaseTestCaase.find_element(P.submitvalue)
        # BaseTestCaase.click(submit)
        # 点击登录按钮
        # 登录按钮的定位方式和值
        # loginvalue = ("css","body > section.header-container > header > div.header-nav-wrap > nav > ul > li:nth-child(7) > a:nth-child(1)")
        # 定位登录按钮（参数为上方面的login或者P中的对应元素值,下面方式一样）
        loginbutton = B.find_element(P.loginvalue)
        # 点击登录按钮(参数为上面的定位到的登录按钮loginbutton)
        B.click(loginbutton)
        time.sleep(1)
        #登录成功弹窗
        # login_success = B.find_element(P.submitvalue)
        # B.click(login_success)
        login_sucees_text = B.get_text(P.submitvalue)
        print(login_sucees_text)
        #断言
        #获取提交后弹窗文字
        #显式等待
        # submit = BaseTestCaase.find_element(P.submitvalue)
        # submit_alert = BaseTestCaase.webdriverwait(submit)
        # # submit_alert = BaseTestCaase.find_element(P.submitvalue)
        # submit_text = submit_alert.text()
        # print(submit_text)
        # submit_text = BaseTestCaase.get_text(submit_alert)
        # print(submit_text)

        try:
            assert login_sucees_text == login_success
        except Exception as e:
            RD.write_data(row=2, column=6, value='未通过')
            # raise NameError("当前页面不包含%s" % (login_sucees_text))
            log.error('用例%s执行不通过'%(sys._getframe().f_code.co_name))
            # # format格式化，把case中的title写入{}中
            log.exception(e)
            raise e
            # 抛出异常
            # 手动触发异常
        else:
            # 否则就正常，正常又如何
            log.info('用例%s执行通过'%(sys._getframe().f_code.co_name))
            RD.write_data(row=2, column=6, value='通过')
            # self.excel.write_data(row=row, column=8, value='通过')
            # log.info('用例{}执行通过'.format(sys._getframe().f_code.co_name)
if __name__ == '__main__':
        unittest.main()