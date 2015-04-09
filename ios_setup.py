from appium.webdriver import webdriver


class IosSetup():
    def __init__(self):
        app = '/Users/1111096/Library/Developer/Xcode/DerivedData/iPhone-bqtvqfsqefxseodnwdaoieqdxavv/Build/Products/Debug-iphonesimulator/iHeartRadio.app'
        self.driver = webdriver.Remote(
            command_executor='http://localhost:4723/wd/hub',
            desired_capabilities={
                'app': app,
                'platformName': 'iOS',
                'deviceName': 'iPhone 6',
            })
