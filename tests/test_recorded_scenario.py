import pytest
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class TestRecordedScenario:
    
    def test_recorded_scenario(self, driver):
        """녹화된 시나리오 테스트"""
        # driver가 딕셔너리인 경우 실제 driver 객체 추출
        if isinstance(driver, dict):
            actual_driver = driver['driver']
        else:
            actual_driver = driver
        wait = WebDriverWait(actual_driver, 10)
        
        try:
            time.sleep(2)
            
            # 방문요양 찾기 버튼 클릭
            el11 = wait.until(EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, "방문요양 찾기, 찾기")))
            el11.click()
            
            # 방문요양서비스 신청하기 버튼 클릭
            el12 = wait.until(EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, "방문요양서비스 신청하기")))
            el12.click()
            
            # "아니오, 가족이 아닙니다." 클릭
            el13 = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("아니오, 가족이 아닙니다.")')))
            el13.click()
            
            # 등록하기 버튼 클릭
            el14 = wait.until(EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, "등록하기")))
            el14.click()
            
            # 장소 선택 버튼 클릭
            el15 = wait.until(EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, "장소 선택")))
            el15.click()

            # el151 = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("searchForm")')))
            # el151.click()

            # 검색 폼 클릭
            el16 = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("region_name")')))
            el16.click()
            el16.send_keys("s")
            time.sleep(1)
            
            # 버튼들 클릭
            el17 = wait.until(EC.element_to_be_clickable((AppiumBy.CLASS_NAME, "android.widget.Button")))
            el17.click()
            
            # el18 = wait.until(EC.element_to_be_clickable((AppiumBy.CLASS_NAME, "android.view.View")))
            # el18.click()
            # el14 = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().text(\"요양 장소를 검색해 주세요\")")
            # el14.click()
            
            # 요양 장소 검색 클릭
            el19 = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("경기 가평군 가평읍 가화로 225-3 (S타운)")')))
            el19.click()
            
            # 확인 버튼 클릭
            el20 = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("확인")')))
            el20.click()
            
            # 다음 버튼 클릭
            el21 = wait.until(EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, "다음")))
            el21.click()
            
            # ViewGroup 클릭
            el22 = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.view.ViewGroup").instance(23)')))
            el22.click()
            
            el23 = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.view.ViewGroup").instance(23)')))
            el23.click()
            
            # 8 클릭
            el24 = wait.until(EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, "8")))
            el24.click()
            
            # 스와이프 동작
            self._perform_swipe(actual_driver, 708, 2433, 666, 792)
            
            # ViewGroup 클릭
            # el25 = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.view.ViewGroup").instance(95)')))
            # el25 = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("선택")')))
            el25 = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.view.ViewGroup").instance(73)')))
            el25.click()
            
            # 스와이프 동작들
            self._perform_swipe(actual_driver, 625, 1328, 614, 2317)
            # self._perform_swipe(actual_driver, 656, 1325, 624, 2405)
            
            # 확인 버튼 클릭
            el26 = wait.until(EC.element_to_be_clickable((AppiumBy.ID, "android:id/button1")))
            el26.click()
            
            # 선택 버튼 클릭
            el27 = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().description("선택")')))
            el27.click()
            
            # 3시간 선택
            # el28 = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("3시간")')))
            el28 = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().description("3시간")')))
            el28.click()
            
            # 스와이프
            self._perform_swipe(actual_driver, 838, 2531, 992, 950)
            
            # 다음 버튼 클릭
            el29 = wait.until(EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, "다음")))
            el29.click()
            
            # 정보 불러오기 버튼 클릭
            el30 = wait.until(EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, "정보 불러오기")))
            el30.click()
            
            # 김영희 선택
            el31 = wait.until(EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, "김영희, 1등급, 여성, 41세, 자가거동자가보행")))
            el31.click()
            
            # 스와이프
            self._perform_swipe(actual_driver, 603, 2591, 715, 680)
            
            # 다음 버튼 클릭
            el32 = wait.until(EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, "다음")))
            el32.click()
            
            # 친절함 선택
            el33 = wait.until(EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, "친절함")))
            el33.click()
            
            # 성별무관 선택
            el34 = wait.until(EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, "성별무관")))
            el34.click()
            
            # 진행안함 선택
            el35 = wait.until(EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, "진행안함")))
            el35.click()
            
            # 스와이프 동작들
            self._perform_swipe(actual_driver, 890, 2538, 904, 659)
            
            # 다음 버튼 클릭
            el36 = wait.until(EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, "다음")))
            el36.click()
            
            # 스와이프 동작들
            self._perform_swipe(actual_driver, 705, 2920, 715, 817)
            self._perform_swipe(actual_driver, 666, 2829, 715, 512)
            
            # 다음 버튼 클릭
            el37 = wait.until(EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, "다음")))
            el37.click()
            
            # "네, 동의합니다." 클릭
            el38 = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("네, 동의합니다.")')))
            el38.click()
            
            # 등록하기 버튼 클릭
            el39 = wait.until(EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, "등록하기")))
            el39.click()
            
            # 스와이프
            self._perform_swipe(actual_driver, 785, 2745, 754, 372)
            
            # 다음 버튼 클릭
            el40 = wait.until(EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, "다음")))
            el40.click()
            
            # 메인이동 버튼 클릭
            el41 = wait.until(EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, "메인이동")))
            el41.click()
            
            # ViewGroup 클릭
            el42 = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.view.ViewGroup").instance(11)')))
            el42.click()
            
        except Exception as e:
            pytest.fail(f"녹화된 시나리오 테스트 실패: {str(e)}")
    
    def _perform_swipe(self, driver, start_x, start_y, end_x, end_y):
        """스와이프 동작 수행"""
        actions = ActionChains(driver)
        actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
        actions.w3c_actions.pointer_action.move_to_location(start_x, start_y)
        actions.w3c_actions.pointer_action.pointer_down()
        actions.w3c_actions.pointer_action.move_to_location(end_x, end_y)
        actions.w3c_actions.pointer_action.release()
        actions.perform()