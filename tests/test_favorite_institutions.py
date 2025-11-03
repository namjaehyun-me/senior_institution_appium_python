import pytest
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
import time
from conftest import *

class TestFavoriteInstitutions:
    
    def _get_platform(self, driver):
        """플랫폼 확인"""
        if isinstance(driver, dict):
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
                'hamburger_menu_btn': (AppiumBy.XPATH, '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[3]'),
                'favorite_institutions_btn': (AppiumBy.XPATH, '//android.widget.TextView[@text="관심기관"]'),
                'first_institution_item': (AppiumBy.XPATH, '(//android.view.ViewGroup[@clickable="true"])[1]'),
                'institution_heart_btn': (AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="하트"]'),
                'back_btn': (AppiumBy.XPATH, '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]'),
                # 바텀 메뉴 관심기관 관련 로케이터
                'bottom_favorite_institutions_btn': (AppiumBy.XPATH, '//android.widget.TextView[@text="관심기관"]'),
                'first_favorite_heart_btn': (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.view.ViewGroup").instance(21)'),
                'toast_message': (AppiumBy.XPATH, '//android.view.ViewGroup[@resource-id="toastAnimatedContainer"]'),
                # 'toast_message': (AppiumBy.ID, 'toastAnimatedContainer'),
                # 'toast_message': (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("toastAnimatedContainer")'),
            },
            'ios': {
                'hamburger_menu_btn': (AppiumBy.XPATH, "//XCUIElementTypeButton[@name='메뉴']"),
                'favorite_institutions_btn': (AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='관심기관']"),
                'first_institution_item': (AppiumBy.XPATH, "(//XCUIElementTypeCell)[1]"),
                'institution_heart_btn': (AppiumBy.XPATH, "//XCUIElementTypeButton[@name='하트']"),
                'back_btn': (AppiumBy.XPATH, "//XCUIElementTypeButton[@name='뒤로가기']"),
                # 바텀 메뉴 관심기관 관련 로케이터
                'bottom_favorite_institutions_btn': (AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='관심기관']"),
                'first_favorite_heart_btn': (AppiumBy.XPATH, "(//XCUIElementTypeButton[@name='하트'])[1]"),
                'toast_message': (AppiumBy.XPATH, "//XCUIElementTypeStaticText"),
            }
        }
        
        return locators[platform][element_name]
    
    def test_favorite_institutions_management(self, driver_setup):
        """바텀 메뉴 관심기관 테스트"""
        if isinstance(driver_setup, dict):
            driver = driver_setup['driver']
        else:
            driver = driver_setup
        wait = WebDriverWait(driver, 10)
        
        try:
            time.sleep(0.5)
            
            # 바텀 메뉴에서 관심기관 클릭
            bottom_favorite_institutions_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'bottom_favorite_institutions_btn')))
            bottom_favorite_institutions_btn.click()
            time.sleep(1)
            
            # 첫번째 항목의 하트 클릭
            first_favorite_heart_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'first_favorite_heart_btn')))
            first_favorite_heart_btn.click()
            time.sleep(1)
            
            # 관심기업 해제 토스트메세지가 잘 뜨는지 확인
            toast_message = wait.until(EC.presence_of_element_located(self._get_locator(driver, 'toast_message')))
            assert toast_message.is_displayed(), "이 시설을 즐겨찾기 목록에서 제거했습니다!"
            time.sleep(1)
            
        except Exception as e:
            pytest.fail(f"바텀 메뉴 관심기관 테스트 실패: {str(e)}")