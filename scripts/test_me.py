import time

from appium import webdriver

from base.base_driver import init_driver
from page.page import Page


class TestMe:
    def setup(self):
        self.driver = init_driver()
        self.page = Page(self.driver)

    def teardown(self):
        time.sleep(1)
        self.driver.quit()

    def test_me(self):
        time.sleep(5)
        self.page.home.click_adolescent_model()
        # # 使用find_elements方法通过classname查找到所有符合条件的元素并返回一个列表
        # navigation_bar_list = self.driver.find_elements_by_class_name("android.widget.LinearLayout")
        # # 打印列表中获取到的元素个数
        # print(len(navigation_bar_list))
        # # 点击列表中第五个元素
        # navigation_bar_list[5].click()
        self.page.home.click_me_page()
        # self.page.home.bottom_navigation_list1()
        time.sleep(3)
