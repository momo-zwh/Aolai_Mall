from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class HomePage(BaseAction):

    tick_button = By.ID, "cn.neoclub.uki.debug:id/check_protocol"
    # 青少年模式我知道了按钮
    adolescent_model = By.ID, "cn.neoclub.uki.debug:id/btn_know"
    # 语音匹配
    speech_matching = By.XPATH, "语音匹配"
    # 群里派对
    group_chat_party = By.XPATH, "群里派对"

    def click_tick_button(self):
        self.click(self.tick_button)

    def click_group_chat_party(self):
        self.click(self.group_chat_party)