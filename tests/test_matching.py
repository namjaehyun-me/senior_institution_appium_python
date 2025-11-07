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
                # 새로운 시나리오 로케이터들
                'bottom_matching_management_btn': (AppiumBy.XPATH, '//android.widget.TextView[@text="매칭 관리"]'),
                'region_btn': (AppiumBy.XPATH, '//android.widget.TextView[@text="지역"]'),
                'jung_gu_checkbox': (AppiumBy.XPATH, '//android.widget.TextView[@text="중구"]'),
                'jongro_gu_checkbox': (AppiumBy.XPATH, '//android.widget.TextView[@text="종로구"]'),
                'yongsan_gu_checkbox': (AppiumBy.XPATH, '//android.widget.TextView[@text="용산구"]'),
                'gwangjin_gu_checkbox': (AppiumBy.XPATH, '//android.widget.TextView[@text="광진구"]'),
                'selection_complete_btn_final': (AppiumBy.XPATH, '(//android.view.ViewGroup[@content-desc="선택완료"])[2]'),
            },
            'ios': {
                # 새로운 시나리오 로케이터들
                'bottom_matching_management_btn': (AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='매칭 관리']"),
                'region_btn': (AppiumBy.XPATH, "//XCUIElementTypeButton[@name='지역']"),
                'jung_gu_checkbox': (AppiumBy.XPATH, "//XCUIElementTypeButton[@name='중구']"),
                'jongro_gu_checkbox': (AppiumBy.XPATH, "//XCUIElementTypeButton[@name='종로구']"),
                'yongsan_gu_checkbox': (AppiumBy.XPATH, "//XCUIElementTypeButton[@name='용산구']"),
                'gwangjin_gu_checkbox': (AppiumBy.XPATH, "//XCUIElementTypeButton[@name='광진구']"),
                'selection_complete_btn_final': (AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='선택완료']"),
            }
        }
        
        return locators[platform][element_name]

    def test_matching_region_selection(self, driver_setup):
        """홈화면 → 바텀 메뉴에서 매칭 관리 클릭 → 지역 버튼 클릭 → 중구/종로구/용산구/광진구 체크박스 클릭 → 선택완료 버튼 클릭 테스트"""
        if isinstance(driver_setup, dict):
            driver = driver_setup['driver']
        else:
            driver = driver_setup
        wait = WebDriverWait(driver, 10)
        
        try:
            time.sleep(2)
            
            # 바텀 메뉴에서 매칭 관리 클릭
            bottom_matching_management_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'bottom_matching_management_btn')))
            bottom_matching_management_btn.click()
            time.sleep(1)
            
            # 지역 버튼 클릭
            region_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'region_btn')))
            region_btn.click()
            time.sleep(1)
            
            # 중구 체크박스 클릭
            # jung_gu_checkbox = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'jung_gu_checkbox')))
            jung_gu_checkbox = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "중구")
            jung_gu_checkbox.click()
            time.sleep(0.5)
            
            # 종로구 체크박스 클릭
            # jongro_gu_checkbox = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'jongro_gu_checkbox')))
            jung_gu_checkbox = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "종로구")
            jung_gu_checkbox.click()
            time.sleep(0.5)
            
            # 용산구 체크박스 클릭
            # yongsan_gu_checkbox = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'yongsan_gu_checkbox')))
            yongsan_gu_checkbox = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "용산구")
            yongsan_gu_checkbox.click()
            time.sleep(0.5)
            
            # 광진구 체크박스 클릭
            # gwangjin_gu_checkbox = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'gwangjin_gu_checkbox')))
            gwangjin_gu_checkbox = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "광진구")
            gwangjin_gu_checkbox.click()
            time.sleep(0.5)
            
            # 선택완료 버튼 클릭
            selection_complete_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'selection_complete_btn_final')))
            selection_complete_btn.click()
            time.sleep(1)
            
            # 선택완료 버튼 클릭 (두 번째)
            # selection_complete_btn2 = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'selection_complete_btn_final')))
            selection_complete_btn2 = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "선택완료")
            selection_complete_btn2.click()
            time.sleep(1)
            
        except Exception as e:
            pytest.fail(f"매칭 지역 선택 테스트 실패: {str(e)}")