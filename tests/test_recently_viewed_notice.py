import pytest
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
import time
from conftest import * 

class TestMyPage:
    
    def _get_platform(self, driver):
        """플랫폼 확인"""
        # driver가 딕셔너리인 경우 실제 driver 객체 추출
        if isinstance(driver, dict):
            actual_driver = driver['driver']
            platform = driver.get('platform', 'android')
            return platform
        else:
            capabilities = driver.capabilities
            platform_name = capabilities.get('platformName', '').lower()
            return 'ios' if platform_name == 'ios' else 'android'
    
    def _get_locator(self, driver, element_name):
        """플랫폼별 로케이터 반환"""
        platform = self._get_platform(driver)
        
        locators = {
            'android': {
                # 최근 본 공고 관련 로케이터들
                'bottom_recently_viewed_btn': (AppiumBy.XPATH, '//android.widget.TextView[@text="최근 본 공고"]'),
                'first_recently_viewed_item': (AppiumBy.XPATH, '//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[1]'),
                'back_btn_general': (AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="뒤로가기"]'),
            },
            'ios': {
                # 최근 본 공고 관련 로케이터들
                'bottom_recently_viewed_btn': (AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='최근 본 공고']"),
                'first_recently_viewed_item': (AppiumBy.XPATH, "(//XCUIElementTypeCell)[1]"),
                'back_btn_general': (AppiumBy.XPATH, "//XCUIElementTypeButton[@name='뒤로가기']"),
            }
        }
        
        return locators[platform][element_name]

    def test_recently_viewed_notice(self, driver_setup):
        """바텀 메뉴에서 최근 본 공고 클릭 → 첫번째 항목 클릭 → 뒤로가기 버튼 클릭 테스트"""
        if isinstance(driver_setup, dict):
            driver = driver_setup['driver']
        else:
            driver = driver_setup
        wait = WebDriverWait(driver, 10)
        
        try:
            time.sleep(2)
            
            # 바텀 메뉴에서 최근 본 공고 클릭
            bottom_recently_viewed_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'bottom_recently_viewed_btn')))
            bottom_recently_viewed_btn.click()
            time.sleep(1)
            
            # 첫번째 항목 클릭
            first_recently_viewed_item = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'first_recently_viewed_item')))
            first_recently_viewed_item.click()
            time.sleep(1)
            
            # 뒤로가기 버튼 클릭
            driver.back()
            
        except Exception as e:
            pytest.fail(f"최근 본 공고 테스트 실패: {str(e)}")