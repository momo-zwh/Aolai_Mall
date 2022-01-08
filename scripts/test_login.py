import time
from base.base_driver import init_driver
from page.page import Page


class TestLogin:

    def setup(self):
        self.driver = init_driver()
        self.page = Page(self.driver)

    def teardown(self):
        time.sleep(1)
        self.driver.quit()

    def test_login(self):
        # 点击协议弹窗中的同意按钮
        self.page.login.click_agreement_button()
        # 输入手机号
        self.page.login.input_phonenum("03819921001")
        # 输入验证码
        self.page.login.input_verification_code("000000")
        # 勾选协议
        self.page.login.click_check_agreement()
        # 点击登录按钮
        self.page.login.click_login_button()
        time.sleep(20)

        assert self.page.home.get_adolescent_model_text() == "我知道了", "没找到<我知道了>,登录校验失败"
