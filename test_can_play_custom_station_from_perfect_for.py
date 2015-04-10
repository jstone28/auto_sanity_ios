import unittest
from appium import webdriver
from hamcrest import *
import time
from selenium.webdriver.support.wait import WebDriverWait


class PlayCustomStationFromPerfect(unittest.TestCase):
    global driver

    def setUp(self):
        app = '/Users/1111096/Library/Developer/Xcode/DerivedData/iPhone-bqtvqfsqefxseodnwdaoieqdxavv/Build/Products/Debug-iphonesimulator/iHeartRadio.app'

        self.driver = webdriver.Remote(
            command_executor='http://localhost:4723/wd/hub',
            desired_capabilities={
                'app': app,
                'platformName': 'iOS',
                'deviceName': 'iPhone 6',
            })

    def tearDown(self):
        self.driver.quit()

    def test_login_with_existing_user(self):
        self.driver.find_element_by_name('Have an account? Log In').click()

        # input email address
        self.driver.find_element_by_xpath(
            "//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell[1]/UIATextField[1]").send_keys(
            'iheartmediatester@gmail.com')

        # input password
        # TODO super dumb workaround
        self.driver.execute_script("mobile: tap", {"tapCount": 1, "touchCount": 1, "duration": 0.6, "x": 150, "y": 153})
        self.driver.find_element_by_xpath(
            "//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell[2]/UIASecureTextField[1]").send_keys(
            'things')

        # submit the form
        self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIAButton[1]").click()

        self.driver.find_element_by_name("No Thanks").click()

        self.driver.find_element_by_name('Country').click()

        self.driver.find_element_by_name('Done').click()

        self.driver.find_element_by_name('Perfect For').click()

        # precise click the first station (possibly dynamic ordering)
        self.driver.execute_script("mobile: tap",
                                   {
                                       "tapCount": 1,
                                       "touchCount": 1,
                                       "duration": 0.6,
                                       "x": 134,
                                       "y": 223
                                   })
        # another precise click first station (dynamic ordering)
        self.driver.execute_script("mobile: tap",
                                   {
                                       "tapCount": 1,
                                       "touchCount": 1,
                                       "duration": 0.59,
                                       "x": 108,
                                       "y": 133
                                   })
        # time.sleep(10)
        # need to figure out how to interact with the player



if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(PlayCustomStationFromPerfect)
    unittest.TextTestRunner(verbosity=2).run(suite)