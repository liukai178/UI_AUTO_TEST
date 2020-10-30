# coding=utf-8
'''
此模块是为了存放所有页面的元素
Java当中的设计模式
PO设计模式 ==》 全称叫做page_object(页面对象模型）
把所有页面上的元素都作为对象的或者类的属性
把元素和流程分开
降低代码的耦合度，容易维护
'''
class Page_Element:
    #登录模块
    #登录按钮的定位方式和元素值
    loginvalue = ("css", ".ant-btn")
    uservalue = ("css", "#username")
    codevalue = ("css", "#loginForm > div.verification > input")
    pwdvalue = ("css", "#password")
    agreevalue = ("css", "#loginForm > div.remember-agree > div > label")
    homevalue = ("xpath", "/html/body/div[1]/div/section/aside/div/div/a/h1")
    homevalueself = ("css", "#logo > a:nth-child(1) > h1:nth-child(2)")
    loginoutvalue = ("link", u"退出登录")
    #个人中心模块
    myself = ("css", "body > section.header-container > header > div.header-nav-wrap > nav > ul > li:nth-child(7) > a:nth-child(1)")
    selfinfor = ("link", u"个人信息")
    #登录弹窗
    submitvalue = ("css",".ant-notification-notice-description")
    goods = ('css','.ant-menu-dark > li:nth-child(2) > div:nth-child(1) > span:nth-child(1) > span:nth-child(2)')
    goodscentre = ('css','#\/goods\$Menu > li:nth-child(2) > div:nth-child(1)')
    goodsdata = ('css','#\/goods\/main\$Menu > li:nth-child(1) > a:nth-child(1)')
    offlinegoods_platform = ('css','label.ant-radio-button-wrapper:nth-child(1) > span:nth-child(2)')
    onlinegoods_platform = ('css','label.ant-radio-button-wrapper:nth-child(2) > span:nth-child(2)')
    addgoods = ('css','button.ant-btn:nth-child(3)')
    goodsname = ('css','#title')
    gencode = ('css','#root > div > section > section > main > div > div > div > div.ant-pro-page-header-wrap-children-content > div.ant-spin-nested-loading > div > div > div > form > div:nth-child(3) > div.ant-col.ant-col-6.ant-form-item-control > div > div > span > span > span > button')
    priceout = ('css','#price_out')
    pricein = ('css','#price_in')
    count = ('css','#count')
    submit = ('css','#root > div > section > section > main > div > div > div > div.ant-pro-page-header-wrap-children-content > div.ant-spin-nested-loading > div > div > div > form > div:nth-child(25) > div.ant-col.ant-col-6.ant-form-item-control > div > div > div > button.ant-btn.ant-btn-primary')
    add_success = ('css','.ant-notification-notice-description')
    edit = ('css','#root > div > section > section > main > div > div > div > div.ant-pro-page-header-wrap-children-content > div.ant-card.ant-card-bordered.ant-card-contain-tabs > div.ant-card-body > div > div > div > div > div > div > table > tbody > tr:nth-child(1) > td:nth-child(12) > a:nth-child(3)')
    online_goods = ('css','#root > div > section > section > main > div > div > div > div.ant-pro-page-header-wrap-children-content > div.ant-radio-group.ant-radio-group-solid > label:nth-child(2)')
    add_online = ('css','#root > div > section > section > main > div > div > div > div.ant-pro-page-header-wrap-children-content > div:nth-child(2) > div.ant-card.ant-card-bordered.ant-card-contain-tabs > div.ant-card-head > div.ant-tabs.ant-tabs-top.ant-tabs-large.ant-card-head-tabs > div.ant-tabs-nav > div.ant-tabs-extra-content > div > button:nth-child(1)')
    select_add_online = ('css','#root > div > section > section > main > div > div > div > div.ant-pro-page-header-wrap-children-content > div:nth-child(2) > div.ant-card.ant-card-bordered.ant-card-contain-tabs > div.ant-card-head > div.ant-tabs.ant-tabs-top.ant-tabs-large.ant-card-head-tabs > div.ant-tabs-nav > div.ant-tabs-extra-content > div > button:nth-child(2)')
    select_goods = ('css','#goods_id_basis > div:nth-child(2) > button:nth-child(1)')
    select_goods_confirm = ('css','tr.ant-table-row:nth-child(1) > td:nth-child(6) > button:nth-child(1)')
    select_stuff = ('css','#root > div > section > section > main > div > div > div > div.ant-pro-page-header-wrap-children-content > div > div > div > div > form > div:nth-child(20) > div.ant-col.ant-col-5.ant-form-item-label > label')
    stuff_1 = ('xpath',"//div*[@title='谷类及制品']")
    stuff_1_1 = ("xpath","//div*[@title='小麦']")
    stuff_1_1_1 = ('xpath','/html/body/div[4]/div/div/div/ul[3]/li[1]')
    add_online_confirm = ('css','#root > div > section > section > main > div > div > div > div.ant-pro-page-header-wrap-children-content > div > div > div > div > form > div:nth-child(21) > div > div > div > button')
    #商品原料下拉框
    yuanliao = ('css','body > div:nth-child(8) > div > div > div > ul')
    yuanliao2 = ('css','ul.ant-cascader-menu:nth-child(2)')
    yuanliao3 = ('css','body > div:nth-child(8) > div > div > div > ul:nth-child(3)')
    submit_add_onlinegoods = ('css','#root > div > section > section > main > div > div > div > div.ant-pro-page-header-wrap-children-content > div > div > div > div > form > div:nth-child(21) > div > div > div > button')
    submit_online_alert = ('css','.ant-message-custom-content > span:nth-child(2)')
    gouxuan_online = ('xpath','//*[@id="root"]/div/section/section/main/div/div/div/div[2]/div[2]/div[2]/div[2]/div/div/div/div/div/div/table/tbody/tr[1]/td[1]/label/span/input')
    piliang_online = ('xpath','//*[@id="root"]/div/section/section/main/div/div/div/div[2]/div[2]/div[2]/div[1]/div[2]/div[1]/div[3]/div/button[1]/span[1]')

    piliang_xiajia = ('css','li.ant-dropdown-menu-item:nth-child(3)')
    piliang_delete = ('css','li.ant-dropdown-menu-item:nth-child(1)')
    delete_alert = ('css','body > div:nth-child(9) > div > div.ant-modal-wrap > div > div.ant-modal-content')
    delete_confirm = ('css','.ant-modal-footer > button:nth-child(2)')
    xiala_online = ('css','body > div:nth-child(10) > div > div > ul')
    piliang_2 = ('css','#root > div > section > section > main > div > div > div > div.ant-pro-page-header-wrap-children-content > div:nth-child(2) > div.ant-card.ant-card-bordered.ant-card-contain-tabs > div.ant-card-head > div.ant-tabs.ant-tabs-top.ant-tabs-large.ant-card-head-tabs > div.ant-tabs-nav > div.ant-tabs-extra-content > div > button.ant-btn.ant-dropdown-trigger')
    del_suc_text = ('xpath','/html/body/div[4]/div/div/div/div/div/span[2]')