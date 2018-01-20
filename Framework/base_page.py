from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Framework.logger import Logger
from selenium.common.exceptions import *
import os
import time

logger = Logger('BaseP').getlog()


class BasePage(object):
    '''
    在每个页面类常用的一些方法
    '''

    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator, timeout=10):
        '''
        定位元素，参数locator为元祖类型
        locator = ('id','xxx')
        driver.find_element(locator)
        '''
        element = WebDriverWait(
            self.driver, timeout, 1
        ).until(EC.presence_of_element_located(locator))
        logger.info('Positioning to the %s%s element.' % locator)
        return element

    def find_elements(self, locator, timeout=10):
        '''
        定位一组元素
        :param locator:
        :param timeout:
        :return:
        '''
        elements = WebDriverWait(
            self.driver, timeout, 1
        ).until(EC.presence_of_all_elements_located(locator))
        logger.info('Positioning to the %s elements.' % locator)
        return elements

    def click(self, locator):
        '''
        点击操作，传入元素的定位器，调用findelement方法接收返回值后执行click操作
        '''
        element = self.find_element(locator)
        element.click()
        logger.info('click success %s%s element.' % locator)

    def send_keys(self, locator, text):
        '''
        发送文本，清空后输入
        locator = ('id','xxx')
        element.send_keys(locator,text)
        '''
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)
        logger.info('SendKeys %s in %s success.' % (text, locator))

    def is_text_in_element(self, locator, text, timeout=10):
        '''
        判断文本在元素里，没有元素返回false打印日志，定位到返回判断结果的布尔值
        result = driver.text_in_element(locator,text)
        '''
        try:
            result = WebDriverWait(
                self.driver, timeout, 1
            ).until(EC.text_to_be_present_in_element(locator, text))
        except TimeoutException:
            logger.info('No location to the element.')
            return False
        else:
            return result

    def is_text_in_value(self, locator, value, timeout=10):
        '''
        判断元素的value值，没定位到元素返回false，定位到返回判断结果布尔值
        result = dirver.text_to_be_present_in_element_value(locator,text)
        '''
        try:
            result = WebDriverWait(
                self.driver, timeout, 1
            ).until(EC.text_to_be_present_in_element_value(locator, value))
        except TimeoutException:
            logger.info('No location to the element.')
            return False
        else:
            return result

    def is_title(self, title, timeout=10):
        '''
        判断元素的title是否完全等于
        '''
        result = WebDriverWait(
            self.driver, timeout, 1
        ).until(EC.title_is(title))
        return result

    def is_title_contains(self, title, timeout=10):
        '''
        判断元素的title是否包含
        '''
        result = WebDriverWait(
            self.driver, timeout, 1
        ).until(EC.title_contains(title))
        return result

    def is_selected(self, locator, timeout=10):
        '''
        判断元素是否被选中
        '''
        result = WebDriverWait(
            self.driver, timeout, 1
        ).until(EC.element_located_to_be_selected(locator))
        return result

    def is_selected_be(self, locator, selected=True, timeout=10):
        '''
        判断元素的状态是不是符合期望的状态，selected是期望的状态
        '''
        result = WebDriverWait(
            self.driver, timeout, 1
        ).until(EC.element_located_selection_state_to_be(locator, selected))
        return result

    def is_alert_present(self, timeout=10):
        '''
        判断页面是否有alert,有的话返回alert，没有返回False
        '''
        result = WebDriverWait(
            self.driver, timeout, 1
        ).until(EC.alert_is_present())
        return result

    def is_visibility(self, locator, timeout=10):
        '''
        元素可见，返回本身，不可见返回False
        '''
        result = WebDriverWait(
            self.driver, timeout, 1
        ).until(EC.visibility_of_element_located(locator))
        return result

    def is_invisibility(self, locator, timeout=10):
        '''
        元素可见返回本身，不可见返回Ture,没有找到元素也返回Ture
        '''
        result = WebDriverWait(
            self.driver, timeout, 1
        ).until(EC.invisibility_of_element_located(locator))
        return result

    def is_clickable(self, locator, timeout=10):
        '''
        元素可以点击is_enabled返回本身，不可点击返回False
        '''
        result = WebDriverWait(
            self.driver, timeout, 1
        ).until(EC.element_to_be_clickable(locator))
        return result

    def is_located(self, locator, timeout=10):
        '''
        判断元素有没有被定位到(并不意味着可见),定位到返回element，没有定位到返回False
        '''
        result = WebDriverWait(
            self.driver, timeout, 1
        ).until(EC.presence_of_all_elements_located(locator))
        return result

    def move_to_element(self, locator):
        '''
        鼠标悬停操作
        locator=('id','xxx')
        driver.move_to_element(locator)
        '''
        element = self.find_element(locator)
        ActionChains(self.driver).move_to_element(element).perform()
        logger.info('ActionChins move to %s' % locator)

    def back(self):
        self.driver.back()
        logger.info('back driver!')

    def forward(self):
        self.driver.forward()
        logger.info('forward driver!')

    def close(self):
        self.driver.close()
        logger.info('close driver!')

    def get_title(self):
        '''
        获取title
        '''
        logger.info('git dirver title.')
        return self.driver.title()

    def get_text(self, locator):
        '''
        获取文本
        '''
        element = self.find_element(locator)
        logger.info('get text in %s' % locator)
        return element.text()

    def get_attribute(self, locator, name):
        '''
        获取属性
        '''
        element = self.find_element(locator)
        logger.info('get attribute in %s' % locator)
        return element.get_attribute(name)

    def js_execute(self, js):
        '''
        执行js
        '''
        logger.info('Execute js.%s' % js)
        return self.driver.execute_script(js)

    def js_focus_element(self, locator):
        '''
        聚焦元素
        '''
        target = self.find_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", target)

    def js_scroll_top(self):
        '''
        滚动到顶部
        '''
        js = 'window.scrollTo(0,0)'
        self.driver.js_execute(js)
        logger.info('Roll to the top!')

    def js_scroll_end(self):
        '''
        滚动到底部
        '''
        js = "window.scrollTo(0,document.body.scrollHight)"
        self.js_execute(js)
        logger.info('Roll to the end!')

    def get_windows_img(self):
        '''
        在这里我们把file_path这个参数写死，直接保存到我们项目根目录的一个文件夹里，.\Screenshots下
        '''
        file_name = time.strftime('%Y%m%d.%H.%M.%S')
        file_path = os.path.abspath('..') + '\Screenshots\\' + file_name + '.png'
        try:
            self.driver.get_screenshot_as_file(file_path)
            logger.info('Had take screenshot and save to folder:/screenshots')
        except NameError as e:
            logger.info('Failed to take the screenshot!%s' % e)
            self.get_windows_img()
