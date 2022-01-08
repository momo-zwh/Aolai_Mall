from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


# 初始化设备信息
def init_driver():
    desired_caps = dict()
    # 设备信息
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '9'
    desired_caps['deviceName'] = 'vivo X21'
    desired_caps['udid'] = '50d3ca13'  # 填入手机唯一识别码:adb device查询
    # 打开uki测试包
    desired_caps['appPackage'] = 'cn.neoclub.uki.debug'
    desired_caps['appActivity'] = 'cn.neoclub.uki.login.SplashActivity'

    # 不重置应用
    desired_caps['noReset'] = True
    # 使用 Uiautomator2 框架
    desired_caps['automationName'] = 'Uiautomator2'

    driver = webdriver.Remote('http://localhost:4725/wd/hub', desired_caps)
    return driver


# 查询当前屏幕上弹出的toast
def find_toast(driver, message, timeout=3):
    """
    # message: 预期要获取的toast的部分消息
    """
    message = "//*[contains(@text,'" + message + "')]"  # 使用包含的方式定位

    element = WebDriverWait(driver, timeout, 0.1).until(lambda x: x.find_element(By.XPATH, message))
    return element.text


