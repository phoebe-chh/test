import os
import logging
import configparser
from selenium import webdriver
from common.logger import Logger
logger = Logger(logger='browserdriver').getlog()
logger.setLevel(level=logging.INFO)


class BrowserDriver():
    dir = os.path.dirname(os.path.abspath('.'))
    bpath=os.path.abspath('.')
    chrome_driver_path = dir +'/tools/driver/chromedriver.exe'
    ie_driver_path = dir + '/tools/driver/IEDriverServer.exe'

    def __init__(self,driver):
        self.driver = driver

    def open_browser(self,driver,dw):
        configer = configparser.ConfigParser()
        file_path = os.path.dirname(os.path.abspath('.')) + '/config/config.ini'
        configer.read(file_path)
        browser = configer.get("browserType", "browserName")
        logger.info("当前选择的浏览器为 %s " % browser)
        if dw == "ga":
            url = configer.get("testServer", "ga")
        else:
            url = configer.get("testServer", "zf")
        logger.info("测试的URL: %s" % url)
        if browser == "Firefox":
            driver = webdriver.Firefox()
            driver.implicitly_wait(10)
            logger.info("启动Firefox浏览器")
        elif browser == "Chrome":
            # driver = webdriver.Chrome(self.chrome_driver_path)
            optons = webdriver.ChromeOptions()
            optons.add_argument('disable-infobars')
            driver = webdriver.Chrome(self.chrome_driver_path,options=optons,desired_capabilities = None)
            driver.implicitly_wait(10)
            logger.info("启动Chrome浏览器")
        elif browser == "IE":
            driver = webdriver.Ie(self.ie_driver_path)
            driver.implicitly_wait(10)
            logger.info("启动IE浏览器")
        driver.get(url)

        # logger.info("打开的url %s" % url)
        driver.maximize_window()
        # logger.info("最大化窗口")
        driver.implicitly_wait(10)
        # logger.info("最长等待时间10s")

        return driver

    # 切换窗口句柄，参数为number
    def switch_window(self,number):
        configer = configparser.ConfigParser()
        file_path = os.path.dirname(os.path.abspath('.')) + '/config/config.ini'
        configer.read(file_path)
        browser = configer.get("browserType", "browserName")
        if browser == 'Firefox' or browser == 'Chrome' or browser == 'IE':
            self.driver =webdriver.Chrome()
            all_windows = self.driver.window_handles
            self.driver.switch_to.window(all_windows[number])
        else:
            logger.info("当前浏览器不支持")

    def quit_browser(self):
        logger.info("关闭浏览器")
        self.driver.quit()


if __name__ == '__main__':
    browser = BrowserDriver(driver=webdriver)
    webdriver.driver = browser.open_browser(webdriver)



