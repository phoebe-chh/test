import os
import time
from _pytest import logging
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import logging

from logs.logger import Logger

logger = Logger(logger='seleniumdriver').getlog()
logger.setLevel(level=logging.INFO)


class SeleniumDriver:
    """
        基类，封装元素操作
    """

    def __init__(self,driver):
        self.driver=driver

    def getByType(self,locatorType):
        locatorType = locatorType.lower()
        if locatorType == "id":
            return By.ID
        elif locatorType == "name":
            return By.NAME
        elif locatorType == "xpath":
            return By.XPATH
        elif locatorType == "css":
            return By.CSS_SELECTOR
        elif locatorType == "linktxt":
            return By.LINK_TEXT
        elif locatorType == "class":
            return By.CLASS_NAME
        else:
            logger.info("元素类型不存在")
        return False

    def getElement(self,locator,locatorType="id"):
        element=None
        try:
            locatorType = locatorType.lower()
            byType = self.getByType(locatorType)
            element = self.driver.find_element(byType,locator)
            logger.info("找到该元素")
        except NoSuchElementException as e:
            logger.error("元素未找到，抛出异常{}".format(e))
            self.get_window_img()  # 截图

        return element

    def click(self,locator,locatorType="id"):
        try:
            element = self.getElement(locator,locatorType)
            element.click()
            logger.info("元素点击成功")
        except Exception as e:
            logger.error("元素点击失败,异常信息:{}".format(e))
            # print_stack()

    def text_input(self,data,locator,locatorType="id"):
        try:
            element = self.getElement(locator,locatorType)
            element.send_keys(data)
            logger.info("数据写入成功")
        except Exception as e:
            logger.info("数据写入失败,抛出异常: {}".format(e))
            self.get_window_img()

    def double_click(self,locator,locatorType= 'id'):
        try:
            ge = self.getElement(locator,locatorType)
            ActionChains(self.driver).double_click(ge).perform()
            logger.info("元素双击成功")
        except Exception as e:
            logger.info("元素双击失败,抛出异常{}".format(e))

    # 先清空内容在输入
    def clear_input(self, element, value):
        try:
            ge = self.getElement(element);
            ge.clear()
            ge.send_keys(value)
        except Exception as e:
            logger.info("出错了！", str(e))

    # 截图功能：得到截图并保存图片到项目image目录下
    def get_window_img(self):
        file_path = os.path.dirname(os.path.abspath('.')) + '\\errormg\\'  # 设置存放截图的路径
        logging.info('截图保存路径为：%s' % file_path)
        timeset = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))  # 按格式获取当前时间
        pic_name = file_path + timeset + '.png'  # 拼接截图文件名
        try:
            self.driver.get_screenshot_as_file(pic_name)
            logger.info('截图成功，图片保存路径为：{}'.format(file_path))
        except Exception as e:
            logger.error('截图出现异常', format(e))
            self.get_window_img()

    # 执行js脚本
    def excute_js(self,script,locator,locatorType="id"):
        try:
            target=self.getElement(locator,locatorType)
            self.driver.execute_script(script,target)
        except Exception as e:
            logger.info("js执行失败抛出异常{}".format(e))

    # 获取窗口弹窗的方法，并得到接收或是关闭提示框
    def get_alert(self):
        self.driver.switch_to.alert.accept()
        logger.info('确定关闭弹窗')

    # 获取页面标题
    def get_page_title(self):
        logger.info("当前页面标题为：{}".format(self.driver.title))
        return self.driver.title

    # 切换iframe，传入参数为下标
    def switch_iframe(self,number):
        frams = self.driver.find_elements_by_tag_name("iframe")
        logger.info("当前页面的ifram个数为{}".format(len(frams)))
        logger.info("当前页面iframe有{}".format(frams))
        framnum=frams[number]
        self.driver.switch_to.frame(framnum)

    # 切换窗口，传入参数为number
    def switch_win(self,number):
        all_windows = self.driver.window_handles
        logger.info("当前有{}个窗口,当前窗口句柄分别是{}".format(len(all_windows), all_windows))
        # logger.info("当前窗口句柄分别是{}".format(all_windows))
        self.driver.switch_to.window(all_windows[number])



    # def get_content(self):
    #     self.getElement()

    # def get_elements_by_tag(self,locator):
    #     return self.driver.find_elements_by_tag_name(locator)



