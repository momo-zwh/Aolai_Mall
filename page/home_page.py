import time
from selenium.webdriver.common.by import By
from base.base_action import BaseAction


class HomePage(BaseAction):
    # 首页协议弹窗同意按钮
    tick_button0 = By.ID, "cn.neoclub.uki.debug:id/tv_agree"
    # 首页协议弹窗不同意按钮
    tick_button1 = By.ID, "cn.neoclub.uki.debug:id/tv_disagree"
    # 青少年模式我知道了按钮
    adolescent_model = By.ID, "cn.neoclub.uki.debug:id/btn_know"
    # 签到弹窗点我签到按钮
    sign_in = By.ID, "cn.neoclub.uki.debug:id/tv_confirm"
    # 关闭签到弹窗按钮
    close_sign_in = By.ID, "cn.neoclub.uki.debug:id/iv_close"
    # 跳过引导
    skip_boot = By.XPATH, "跳过引导"
    # 首页导航
    bottom_navigation = By.CLASS_NAME, "android.widget.LinearLayout"

    # 点击首页协议弹窗中的同意
    def click_tick_button0(self):
        self.click(self.tick_button0)

    # 点击首页协议弹窗中的不同意
    def click_tick_button1(self):
        self.click(self.tick_button1)

    # 点击首页的跳过引导
    def click_skip_boot(self):
        self.click(self.skip_boot)

    # 点击青少年弹窗
    def click_adolescent_model(self):
        self.click(self.adolescent_model)

    # 获取青少年弹窗按钮的文本
    def get_adolescent_model_text(self):
        return self.find_element(self.adolescent_model).text

    # 获取home页面中所有的底导按钮
    def bottom_navigation_list1(self):
        """
        底导按钮无法通过id和xpath属性获取,只要classname属性,且当前页面底导的classname都相同,
        所以通过find_elements拿到所有同名classname,并生成一个列表,
        将列表赋值并return供其它函数通过列表下标的方式调用某一个底导元素;
        :return:
        """
        bottom_navigation_list = self.find_elements(self.bottom_navigation)
        return bottom_navigation_list

    # 点击底导按钮 首页
    def click_home_page(self):
        """
             调用底导按钮函数,通过接收底导按钮函数返回的列表生成一个新的列表,
             利用新的列表取下标值,然后.click()方法点击它
             :return:
             """
        # bottom_navigation_list = self.find_elements(self.bottom_navigation)
        # bottom_navigation_list[5].click()  # 另一种写法
        home_button = self.bottom_navigation_list1()  # 接收底导按钮函数的return值
        home_button[3].click()

    # 点击底导按钮 广场
    def click_place_page(self):
        place_button = self.bottom_navigation_list1()
        place_button[4].click()

    # 点击底导按钮 娱乐
    def click_party_page(self):
        party_button = self.bottom_navigation_list1()
        party_button[5].click()

    # 点击底导按钮 消息
    def click_message_page(self):
        message_button = self.bottom_navigation_list1()
        message_button[5].click()

    # 点击底导按钮 我的
    def click_me_page(self):
        me_button = self.bottom_navigation_list1()
        # time.sleep(0.5)
        me_button[7].click()

