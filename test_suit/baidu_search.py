import unittest
from Framework.browser_engine import BrowserEngine
import time


class BaiduSearch(unittest.TestCase):
    def setUp(self):
        self.browser = BrowserEngine(self)
        self.driver = self.browser.open_browser(self)

    def tearDown(self):
        self.browser.quit_browser(self.driver)

    def test_search(self):
        self.driver.find_element_by_id('kw').send_keys('selenium')
        time.sleep(1)
        try:
            assert 'selenium' in self.driver.title
            print('pass')
        except:
            print('Fail')

if __name__ == '__main__':
    unittest.main()