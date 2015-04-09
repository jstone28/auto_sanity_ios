
import unittest
from appium import webdriver
from hamcrest import *
import thread


class SimpleAndroidTests(unittest.TestCase):
    def setUp(self):
        app = '/Users/1111096/Library/Developer/Xcode/DerivedData/iPhone-bqtvqfsqefxseodnwdaoieqdxavv/Build/Products/Debug-iphonesimulator/iHeartRadio.app'

        self.driver = webdriver.Remote(
            command_executor='http://localhost:4723/wd/hub',
            desired_capabilities={
                'app': 'Safari',
                'platformName': 'iOS',
                'deviceName': 'iPhone 6',
                'broswerName': 'Safari',
            }).get('http://www.google.com/')


    def tearDown(self):
        self.driver.quit()

    def test_find_skip_button(self):
        # el = self.driver.find_element_by_name('Maybe Later')
        # assert_that(el.text, equal_to("Maybe Later"))
        # el.click()
        self.driver.get('http://www.google.com/')
        pass



if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(SimpleAndroidTests)
    unittest.TextTestRunner(verbosity=2).run(suite)