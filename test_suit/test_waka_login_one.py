import unittest
from Framework.browser_engine import BrowserEngine
from pageobjects.waka_loginpage import WakaLoginPage
from Framework.logger import Logger

log = Logger('WkLoginone').getlog()


class WkLoginone(unittest.TestCase):
    def setUp(self):
        self.browser = BrowserEngine(self)
        self.dirver = self.browser.open_browser(self)
        self.login = WakaLoginPage(self.dirver)

    def tearDown(self):
        self.browser.quit_browser(self.dirver)

    def test_loginone_01(self):
        try:
            self.login.Login('555555', '777777')
            result = self.login.is_text_in_element(self.login.locator_text, '退出')
            self.assertEqual(result, True)
        except Exception as e:
            print('异常原因%s' % e)
            log.info('%%%%%%%%异常原因：%s%%%%%%%%%%' % e)
            self.login.get_windows_img()
            raise

    def test_logintwo_02(self):
        try:
            self.login.Login('SDFG', 'ERTYUIOJHGF')
            result = self.login.is_text_in_element(self.login.locator_text, '退出')
            self.assertEqual(result, True)
        except Exception as e:
            print('异常原因%s' % e)
            log.info('%%%%%%%%异常原因：%s%%%%%%%%%%' % e)
            self.login.get_windows_img()
            raise
