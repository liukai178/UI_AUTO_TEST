from selenium import webdriver
import sys
import time
def dawa():
    driver = webdriver.Firefox()
    url = "https://sy.51wpu.net.cn/index"
    driver.get(url)
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.find_element_by_css_selector("#username").send_keys("Y2087")
    driver.find_element_by_css_selector("#password").send_keys("Liu12345678")
    driver.find_element_by_css_selector(".ant-btn").click()
    driver.implicitly_wait(5)
    # logo = driver.find_element_by_css_selector("#logo > a:nth-child(1) > img:nth-child(1)")
    time.sleep(1)
    #不加固定等待，成功弹窗没有渲染好，导致定位和断言失败
    su_text = driver.find_element_by_css_selector(".ant-notification-notice-description").text
    print(su_text)
    sucess_text = "登录成功"
    try:
        assert su_text == sucess_text
    except Exception as e:
        raise NameError("当前面页面不包含'%s'这几个字"%(sucess_text))
    else:
        print("用例{}通过".format(sys._getframe().f_code.co_name))
if __name__ == '__main__':
    dawa()