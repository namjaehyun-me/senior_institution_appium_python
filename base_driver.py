from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.options.ios import XCUITestOptions
from config import ANDROID_CAPS, IOS_CAPS, APPIUM_SERVER_URL

class BaseDriver:
    def __init__(self, platform="android"):
        self.driver = None
        self.platform = platform.lower()
    
    def start_driver(self):
        if self.platform == "android":
            options = UiAutomator2Options().load_capabilities(ANDROID_CAPS)
        else:
            options = XCUITestOptions().load_capabilities(IOS_CAPS)
        
        self.driver = webdriver.Remote(APPIUM_SERVER_URL, options=options)
        return self.driver
    
    def quit_driver(self):
        if self.driver:
            self.driver.quit()
