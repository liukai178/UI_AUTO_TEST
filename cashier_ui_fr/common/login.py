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
class Login():
    def __init__(self):
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get('https://sy.51wpu.net.cn/user/login?redirect=https%3A%2F%2Fsy.51wpu.net.cn%2F')
        B.set_driver(driver)
    def login(self):
        # driver = webdriver.Firefox()
        B.sleep(3)
        username = B.find_element(P.uservalue)
        B.send_keys(username,usernamenum)
        password = B.find_element(P.pwdvalue)
        B.send_keys(password,pwdnum)
        login = B.find_element(P.loginvalue)
        B.click(login)
if __name__ == '__main__':
    Login().login()