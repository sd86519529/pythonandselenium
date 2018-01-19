import unittest
from Framework.browser_engine import BrowserEngine
from pageobjects.waka_loginpage import WakaLoginPage


class WkLogin(unittest.TestCase):
    def setUp(self):
        self.browser = BrowserEngine(self)
        self.driver = self.browser.open_browser(self)
        self.login = WakaLoginPage(self.driver)

    def tearDown(self):
        self.browser.quit_browser(self.driver)

    def login_case(self, username, password):
        self.login.Login(username, password)
        result = self.login.is_text_in_element(self.login.locator_text, '退出')
        self.assertEqual(result, True)

    def test_login01(self):
        # 输入正确的账号密码

        self.login_case('13968141450', '1111111')

    def test_login_02(self):
        # 输入错误的账号密码

        self.login_case('111111', '111111')


if __name__ == '__main__':
    unittest.main()
