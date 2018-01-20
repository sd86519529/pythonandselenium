import unittest
from Framework.browser_engine import BrowserEngine
from pageobjects.waka_loginpage import WakaLoginPage
from Framework.logger import Logger

log = Logger('WkLogin').getlog()


class WkLogin(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.browser = BrowserEngine(cls)
        cls.driver = cls.browser.open_browser(cls)

    def login_case(self, username, password):
        self.login = WakaLoginPage(self.driver)
        self.login.Login(username, password)
        result = self.login.is_text_in_element(self.login.locator_text, '退出')
        self.assertEqual(result, True)

    def test_login01(self):
        # 输入正确的账号密码
        try:
            self.login_case('13968141450', '1111111')
            self.login.back()
        except Exception as e:
            print('异常原因%s' % e)
            log.info('%%%%%%%%异常原因：%s%%%%%%%%%%' % e)
            self.login.get_windows_img()
            raise

    def test_login_02(self):
        # 输入错误的账号密码
        try:
            self.login_case('111111', '111111')
        except Exception as e:
            print('异常原因%s' % e)
            log.info('%%%%%%%%异常原因：%s%%%%%%%%%%' % e)
            self.login.get_windows_img()
            raise

    @classmethod
    def tearDownClass(cls):
        cls.browser.quit_browser(cls.driver)
