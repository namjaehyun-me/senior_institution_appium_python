from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.action_chains import ActionChains
import time

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.platform = self._get_platform()
    
    def _get_platform(self):
        try:
            return self.driver.capabilities['platformName'].lower()
        except:
            return 'android'
    
    def find_element(self, locator):
        return self.wait.until(EC.element_to_be_clickable(locator))
    
    def click_element(self, locator):
        element = self.find_element(locator)
        try:
            element.click()
        except:
            # 일반 클릭 실패시 좌표 클릭 시도
            self.driver.tap([(element.location['x'] + element.size['width']//2, 
                            element.location['y'] + element.size['height']//2)])
    
    def send_keys(self, locator, text):
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)
    
    def hide_keyboard(self):
        """키보드 숨기기 - 플랫폼별 처리"""
        try:
            if self.platform == 'android':
                self.driver.hide_keyboard()
            else:  # iOS
                done_button = self.driver.find_element(AppiumBy.XPATH, "//XCUIElementTypeButton[@name='Done']")
                done_button.click()
        except:
            pass
    
    def get_current_screen(self):
        """현재 화면 정보 - 플랫폼별 처리"""
        if self.platform == 'android':
            return self.driver.current_activity
        else:  # iOS
            return self.driver.execute_script("mobile: activeAppInfo")
