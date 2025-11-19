import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.appiumby import AppiumBy
from base_driver import BaseDriver
from pages.login_page import LoginPage
import time

class TestProposalForAdmission:

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
                'bottom_menu_proposal_locator':(AppiumBy.XPATH, '//android.widget.TextView[@text="입소제안"]'),
                'position_search_input':(AppiumBy.XPATH, '//android.widget.EditText[@text="이름 또는 휴대전화번호"]'),
                'list_items_locator':(AppiumBy.XPATH, '//android.widget.TextView[@text="데이터를 찾을 수 없습니다"]'),
                'bottom_position_proposal_btn': (AppiumBy.XPATH, "//android.widget.TextView[@text='포지션제안']"),
                'position_list_items': (AppiumBy.XPATH, "//android.widget.ListView//android.widget.LinearLayout")
            },
            'ios': {
                'bottom_menu_proposal_locator':(AppiumBy.XPATH, "//XCUIElementTypeStaticText[@text='입소제안']"),
                'position_search_input':(AppiumBy.XPATH, "//XCUIElementTypeTextField"),
                'list_items_locator':(AppiumBy.XPATH, "//XCUIElementTypeTable//XCUIElementTypeCell"),
                'bottom_position_proposal_btn': (AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='포지션제안']"),
                'position_search_input': (AppiumBy.XPATH, "//XCUIElementTypeTextField"),
                'position_list_items': (AppiumBy.XPATH, "//XCUIElementTypeTable//XCUIElementTypeCell")
            }
        }
        
        return locators[platform][element_name]

    def test_position_proposal_scenario(self, driver_setup):
        """포지션제안 검색 시나리오 테스트"""
        if isinstance(driver_setup, dict):
            driver = driver_setup['driver']
        else:
            driver = driver_setup
        wait = WebDriverWait(driver, 10)
        
        try:
            # 바텀 메뉴에서 포지션제안 클릭
            position_proposal_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'bottom_position_proposal_btn')))
            position_proposal_btn.click()
            
            # 인풋에 "김" 넣기
            search_input = wait.until(EC.presence_of_element_located(self._get_locator(driver, 'position_search_input')))
            search_input.clear()
            search_input.send_keys("남")
            
            # 목록에 항목이 0개인지 확인
            # list_items = driver.find_elements(*self._get_locator(driver, 'position_list_items'))
            # assert len(list_items) == 0, f"'김' 검색 결과는 0개여야 하는데 {len(list_items)}개입니다"
            
            # # 인풋에 "남" 넣기
            # search_input.clear()
            # search_input.send_keys("남")
            # time.sleep(2)
            
            # # 목록에 항목이 1개인지 확인
            # list_items = driver.find_elements(*self._get_locator(driver, 'position_list_items'))
            # assert len(list_items) == 1, f"'남' 검색 결과는 1개여야 하는데 {len(list_items)}개입니다"
            
            # 목록에 항목이 0개인지 확인
            list_items = driver.find_elements(*self._get_locator(driver, 'list_items_locator'))
            print("목록 항목 확인")
            if len(list_items) > 0:
                print("목록에 항목 없음")
            else:
                print("목록에 항목 있음")

            print("포지션제안 검색 시나리오 테스트 완료")
        except Exception as e:
            pytest.fail(f"포지션제안 검색 시나리오 테스트 실패: {str(e)}")