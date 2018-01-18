class BasePage(object):
    '''
    在每个页面类常用的一些方法
    '''

    def __init__(self, driver):
        self.driver = driver
