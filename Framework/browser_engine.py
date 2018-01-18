import configparser
from selenium import webdriver
import os
from selenium.common.exceptions import TimeoutException
from Framework.logger import Logger
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

'''
browser_engine(浏览器引擎类) 此类通过读取配置文件来打开设置的浏览器以及规定的url
后续添加日志打印类优化  优化后增加调用日志类，接受日志初始化格式后的logger
'''
logger = Logger('BrowserEngine').getlog()


class BrowserEngine(object):
    '''
    获取配置文件的路径
    '''
    Config_path = os.path.abspath('..') + '\Config\config.ini'  # 使用os.path.abspath可以获得上层目录
    Chrome_driver_path = os.path.abspath('..') + '\\tools\chromedriver.exe'  # 获得chromedriver所在路径
    IE_driver_path = os.path.abspath('..') + '\\tools\Ie.exe'  # 获得IEdriver.exe所在路径

    def __init__(self, driver):
        '''
        初始化 driver  此初始化可以省略
        :param driver:
        :return:
        '''
        self.driver = driver

    def open_browser(self, driver):
        '''
        读取配置文件获得其设置的url和browser
        '''
        config = configparser.ConfigParser()  # 实例化读取ini配置文件的类
        config.read(self.Config_path, encoding='utf-8')  # 读取ini文件
        browser = config.get('browserType', 'browserKey')
        logger.info('you select browser is %s' % browser)
        url = config.get('ServerType', 'URL')
        logger.info('you select URL is %s' % url)
        title = config.get('urltitle', 'title')
        '''
        判断配置文件设置浏览器的类型决定打开某浏览器
        '''
        if browser == 'Firefox':
            logger.info('Starting firefox browser')
            driver = webdriver.Firefox()
        elif browser == 'Chrome':
            logger.info('Starting chrome browser')
            driver = webdriver.Chrome(self.Chrome_driver_path)
        elif browser == 'IE':
            logger.info('Starting IE browser')
            driver = webdriver.Ie(self.IE_driver_path)

        '''
        打开句柄后根据配置文件设置sever的内容决定打开某URL
        '''
        driver.get(url)
        logger.info('open url is %s' % url)
        driver.maximize_window()
        logger.info('maximize the current windows.')
        try:
            WebDriverWait(driver, timeout=10).until(EC.title_contains(title))
            logger.info('oppen %s title success' % url)
        except TimeoutException:
            logger.info('oppen %s title error' % url)
        except Exception as msg:
            logger.info('Error:%s' % msg)
        return driver

    def quit_browser(self, driver):
        logger.info('Now , Close the browser')
        driver.quit()
