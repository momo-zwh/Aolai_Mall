# 同意协议按钮
from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class LoginPage(BaseAction):

    # 点击协议弹窗中的同意
    agreement_button = By.ID, "cn.neoclub.uki.debug:id/tv_agree"
    # 输入手机号
    send_phonenum = By.ID, "cn.neoclub.uki.debug:id/appCompatEditTextPhone"
    # 输入验证码
    verification_code = By.ID, "cn.neoclub.uki.debug:id/appCompatEditTextCode"
    # 登录按钮
    login_button = By.ID, "cn.neoclub.uki.debug:id/roundTextViewLogin"
    # 勾选协议按钮 checked字段为false是未勾选,true是已勾选
    check_agreement = By.ID,"cn.neoclub.uki.debug:id/check_protocol"

    # 点击协议弹窗的同意
    def click_agreement_button(self):
        self.click(self.agreement_button)

    # 输入手机号
    def input_phonenum(self, text):
        self.input(self.send_phonenum, text)

    # 输入验证码
    def input_verification_code(self, text):
        self.input(self.verification_code, text)

    # 勾选协议
    def click_check_agreement(self):
        self.click(self.check_agreement)

    # 点击登录
    def click_login_button(self):
        self.click(self.login_button)