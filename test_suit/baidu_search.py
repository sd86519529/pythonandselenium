import unittest
from Framework.browser_engine import BrowserEngine
import time
from Framework.base_page import BasePage

class BaiduSearch(unittest.TestCase):
    def setUp(self):
        self.browser = BrowserEngine(self)
        self.driver = self.browser.open_browser(self)

    def tearDown(self):
        #self.browser.quit_browser(self.driver)
        pass
    def test_search(self):
        base = BasePage(self.driver)
        locator=('id','kw')
        locator2 = ('link text','地图')
        base.click(locator2)
        base.back()
        base.send_keys(locator,'selenium')
        base.get_windows_img()
        time.sleep(2)
        try:
            assert 'selenium' in self.driver.title
            print('pass')
        except:
            print('Fail')

if __name__ == '__main__':
    unittest.main()