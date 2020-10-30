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
import time
def test01_delete_online_goods():
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
    time.sleep(1)
    B.click(B.find_element(P.gouxuan_online))
    time.sleep(1)
    B.hold(B.find_element(P.piliang_online))
    time.sleep(1)
    # 下架
    B.click(B.find_element(P.piliang_xiajia))
    time.sleep(1)
    # B.refresh()
    # time.sleep(2)
    # B.click(B.find_element(P.gouxuan_online))
    # time.sleep(2)
    a = B.find_element(P.piliang_2)
    B.hold(a)
    # 删除
    time.sleep(1)
    B.click(B.find_element(P.piliang_delete))
    time.sleep(1)
    # B.click(B.find_element(P.delete_alert))
    B.click(B.find_element(P.delete_confirm))
    del_suc_text = B.get_text(P.del_suc_text)
    print(del_suc_text)