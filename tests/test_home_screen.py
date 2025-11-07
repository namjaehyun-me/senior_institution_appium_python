import pytest
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
import time
from conftest import * 

class TestHomeScreen:
    
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
                # 기존 로케이터들
                'visit_care_btn': (AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="방문요양 찾기, 찾기"]'),
                'apply_btn': (AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="방문요양서비스 신청하기"]'),
                'not_family_checkbox': (AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="아니오, 가족이 아닙니다."]'),
                'register_btn': (AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="등록하기"]'),
                'location_btn': (AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="장소 선택"]'),
                'address_input': (AppiumBy.XPATH, '//android.widget.EditText[@resource-id="region_name"]'),
                'search_btn': (AppiumBy.XPATH, '//android.widget.Button[@text="검색"]'),
                'first_result': (AppiumBy.XPATH, '//android.widget.Button[@text="경기 가평군 가평읍 가화로 225-3 (S타운)"]'),
                'confirm_btn': (AppiumBy.XPATH, '//android.widget.TextView[@text="확인"]'),
                'confirm_btn2': (AppiumBy.XPATH, '//android.widget.Button[@resource-id="android:id/button1"]'),
                'next_btn': (AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="다음"]'),
                'next_btn1': (AppiumBy.XPATH, '//android.widget.TextView[@text="다음"]'),
                'next_btn2': (AppiumBy.XPATH, '//android.widget.TextView[@text="다음"]'),
                'calendar_next': (AppiumBy.XPATH, '//android.widget.HorizontalScrollView/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup[2]/android.view.ViewGroup'),
                'calendar_date': (AppiumBy.XPATH, '//android.widget.TextView[@text="18"]'),
                'start_time_dropdown': (AppiumBy.XPATH, '//android.widget.HorizontalScrollView/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup[1]'),
                'duration_dropdown': (AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="선택"]'),
                'three_hours': (AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="3시간"]'),
                'load_info_btn': (AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="정보 불러오기"]'),
                'kim_younghee': (AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="김영희, 1등급, 여성, 41세, 자가거동자가보행"]'),
                'gender_any': (AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="성별무관"]'),
                'no_proceed': (AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="진행안함"]'),
                'kind_btn': (AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="친절함"]'),
                'agree_btn': (AppiumBy.XPATH, '//android.widget.TextView[@text="네, 동의합니다."]'),
                'main_btn': (AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="메인이동"]'),
                'back_btn1': (AppiumBy.XPATH, '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup[1]'),
                'back_btn4': (AppiumBy.XPATH, '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]'),
                'hope_mony_input': (AppiumBy.XPATH, '//android.widget.HorizontalScrollView/android.view.ViewGroup/android.view.ViewGroup[6]'),
                'meeting_place_add_btn': (AppiumBy.XPATH, '//android.widget.HorizontalScrollView/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup[1]'),
                'visit_place_add_btn': (AppiumBy.XPATH, '//android.widget.HorizontalScrollView/android.view.ViewGroup/android.view.ViewGroup[5]/android.view.ViewGroup[1]'),
                'confirm_btn6': (AppiumBy.XPATH, '(//android.view.ViewGroup[@content-desc="확인"])[1]'),
                'confirm_btn7': (AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="확인"]'),
                'same_return_checkbox': (AppiumBy.XPATH, '//android.widget.TextView[@text="복귀장소가 만남장소와 동일합니다."]'),
                'patient_location_input': (AppiumBy.XPATH, '//android.widget.EditText[@text="예시) 서울시 강남구"]'),
                'pass_keyboard_btn': (AppiumBy.XPATH, '//android.widget.HorizontalScrollView/android.view.ViewGroup'),
                # 새로운 시나리오 로케이터들
                'my_resume_btn': (AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="내 이력서"]'),
                'first_resume_item': (AppiumBy.XPATH, '//android.widget.TextView[@text="사회복지사/요양보호사"]'),
                'second_resume_item': (AppiumBy.XPATH, '//android.widget.TextView[@text="간병/가사/동행"]'),
                'detail_address_input': (AppiumBy.XPATH, '//android.widget.EditText[@text="상세주소"]'),
                'agree_btn1': (AppiumBy.XPATH, '//android.widget.HorizontalScrollView/android.view.ViewGroup/android.view.ViewGroup[5]'),
                'preview_btn': (AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="미리보기"]'),
                'registration_complete_btn': (AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="등록완료"]'),
                'specialty_input': (AppiumBy.XPATH, '//android.widget.HorizontalScrollView/android.view.ViewGroup/android.view.ViewGroup[8]'),
                'back_btn_general': (AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="뒤로가기"]'),
                'toast_message': (AppiumBy.XPATH, '//android.view.ViewGroup[@resource-id="toastAnimatedContainer"]/android.view.ViewGroup'),
                'job_application_btn': (AppiumBy.XPATH, '//android.widget.TextView[@text="지원공고"]'),
                'employment_certificate_btn': (AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="취업활동 증명서 발급하기"]/android.view.View'),
                'first_application_item': (AppiumBy.XPATH, '//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[1]'),
                'email_send_btn': (AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="이메일 전송하기"]'),
                'position_proposal_btn': (AppiumBy.XPATH, '//android.widget.TextView[@text="포지션제안"]'),
                'resume_update_btn': (AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="이력서 업데이트"]'),
                'edit_btn': (AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="수정하기"]'),
                'complete_btn': (AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="완료"]'),
                'position_proposal_setting_btn': (AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="포지션 제안 설정"]'),
                'future_position_checkbox': (AppiumBy.XPATH, '//android.widget.TextView[@text="후순 포지션이 있다면 제안 받을래요"]'),
                'setting_complete_btn': (AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="설정완료"]'),
                'care_worker_btn': (AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="요양보호사"]'),
                'care_housekeeping_companion_btn': (AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="간병/가사/동행"]'),
                'caregiver_btn': (AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="간병"]'),
                'housekeeping_btn': (AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="가사돌봄"]'),
                'companion_btn': (AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="동행"]'),
                'social_worker_btn': (AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="사회복지사"]'),
                'home_btn': (AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="홈"]'),
                'location_permission_while_using': (AppiumBy.XPATH, '//android.widget.Button[@resource-id="com.android.permissioncontroller:id/permission_allow_foreground_only_button"]'),
                'bottom_home_btn': (AppiumBy.XPATH, '//android.view.View[@content-desc="홈"]/android.view.ViewGroup'),
                'modal': (AppiumBy.XPATH, '//android.widget.TextView[@text="경고 !"]'),
            },
            'ios': {
                # 기존 로케이터들
                'visit_care_btn': (AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='방문요양찾기']"),
                'apply_btn': (AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='방문요양서비스 신청하기']"),
                'not_family_checkbox': (AppiumBy.XPATH, "//XCUIElementTypeButton[contains(@name,'아니오')]"),
                'register_btn': (AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='등록하기']"),
                'location_btn': (AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='장소 선택']"),
                'address_input': (AppiumBy.XPATH, "//XCUIElementTypeTextField"),
                'search_btn': (AppiumBy.XPATH, "//XCUIElementTypeButton[@name='검색']"),
                'first_result': (AppiumBy.XPATH, "(//XCUIElementTypeStaticText)[1]"),
                'confirm_btn': (AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='확인']"),
                'next_btn': (AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='다음']"),
                'calendar_next': (AppiumBy.XPATH, "//XCUIElementTypeButton[@name='다음']"),
                'start_time_dropdown': (AppiumBy.XPATH, "//XCUIElementTypePicker"),
                'duration_dropdown': (AppiumBy.XPATH, "//XCUIElementTypePicker"),
                'three_hours': (AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='3시간']"),
                'load_info_btn': (AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='정보불러오기']"),
                'kim_younghee': (AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='김영희']"),
                'gender_any': (AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='성별무관']"),
                'no_proceed': (AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='진행안함']"),
                'kind_btn': (AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='친절함']"),
                'agree_btn': (AppiumBy.XPATH, "//XCUIElementTypeStaticText[contains(@name,'동의합니다')]"),
                'main_btn': (AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='메인이동']"),
                'hope_mony_input': (AppiumBy.XPATH, "//XCUIElementTypeTextField[@name='희망 시급']"),
                'meeting_place_add_btn': (AppiumBy.XPATH, "//XCUIElementTypeButton[@name='추가']"),
                'visit_place_add_btn': (AppiumBy.XPATH, "//XCUIElementTypeButton[@name='추가']"),
                'confirm_btn6': (AppiumBy.XPATH, "(//XCUIElementTypeStaticText[@name='확인'])[1]"),
                'confirm_btn7': (AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='확인']"),
                'same_return_checkbox': (AppiumBy.XPATH, "//XCUIElementTypeButton[contains(@name,'동일합니다')]"),
                # 새로운 시나리오 로케이터들
                'my_resume_btn': (AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='내 이력서']"),
                'first_resume_item': (AppiumBy.XPATH, "(//XCUIElementTypeCell)[1]"),
                'second_resume_item': (AppiumBy.XPATH, "(//XCUIElementTypeCell)[2]"),
                'detail_address_input': (AppiumBy.XPATH, "//XCUIElementTypeTextField[@name='상세주소']"),
                'agree_btn1': (AppiumBy.XPATH, "//XCUIElementTypeButton[@name='미리보기']"),
                'preview_btn': (AppiumBy.XPATH, "//XCUIElementTypeButton[@name='미리보기']"),
                'registration_complete_btn': (AppiumBy.XPATH, "//XCUIElementTypeButton[@name='등록완료']"),
                'specialty_input': (AppiumBy.XPATH, "//XCUIElementTypeTextField[@name='전문분야']"),
                'back_btn_general': (AppiumBy.XPATH, "//XCUIElementTypeButton[@name='뒤로가기']"),
                'toast_message': (AppiumBy.XPATH, "//XCUIElementTypeStaticText"),
                'job_application_btn': (AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='지원공고']"),
                'employment_certificate_btn': (AppiumBy.XPATH, "//XCUIElementTypeButton[@name='취업활동 증명서 발급하기']"),
                'first_application_item': (AppiumBy.XPATH, "(//XCUIElementTypeCell)[1]"),
                'email_send_btn': (AppiumBy.XPATH, "//XCUIElementTypeButton[@name='이메일 전송하기']"),
                'position_proposal_btn': (AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='포지션제안']"),
                'resume_update_btn': (AppiumBy.XPATH, "//XCUIElementTypeButton[@name='이력서 업데이트']"),
                'edit_btn': (AppiumBy.XPATH, "//XCUIElementTypeButton[@name='수정하기']"),
                'complete_btn': (AppiumBy.XPATH, "//XCUIElementTypeButton[@name='완료']"),
                'position_proposal_setting_btn': (AppiumBy.XPATH, "//XCUIElementTypeButton[@name='포지션 제안 설정']"),
                'future_position_checkbox': (AppiumBy.XPATH, "//XCUIElementTypeButton[@name='후순 포지션이 있다면 제안 받을래요']"),
                'setting_complete_btn': (AppiumBy.XPATH, "//XCUIElementTypeButton[@name='설정완료']"),
                'care_worker_btn': (AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='요양보호사']"),
                'care_housekeeping_companion_btn': (AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='간병/가사/동행']"),
                'caregiver_btn': (AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='간병']"),
                'housekeeping_btn': (AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='가사돌봄']"),
                'companion_btn': (AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='동행']"),
                'social_worker_btn': (AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='사회복지사']"),
                'home_btn': (AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='홈']"),
                'location_permission_while_using': (AppiumBy.XPATH, "//XCUIElementTypeButton[@name='While using the app']"),
                'bottom_home_btn': (AppiumBy.XPATH, "//XCUIElementTypeButton[@name='홈']"),
                'modal': (AppiumBy.XPATH, "//XCUIElementTypeButton[@name='홈']"),
            }
        }
        
        return locators[platform][element_name]
    
    def _get_date_locator(self, driver, day):
        """날짜별 로케이터 반환"""
        platform = self._get_platform(driver)
        if platform == 'android':
            return (AppiumBy.XPATH, f"//android.widget.TextView[@text='{day}']") 
        else:
            return (AppiumBy.XPATH, f"//XCUIElementTypeStaticText[@name='{day}']")
    
    def _get_checkbox_locator(self, driver, index):
        """체크박스 인덱스별 로케이터 반환"""
        platform = self._get_platform(driver)
        if platform == 'android':
            return (AppiumBy.XPATH, f"(//android.widget.CheckBox)[{index}]")
        else:
            return (AppiumBy.XPATH, f"(//XCUIElementTypeButton[@name='체크박스'])[{index}]")
    
    def _show_second_match(driver, text="선택하세요", max_swipes=8):
        size = driver.get_window_size()
        for _ in range(max_swipes):
            els = driver.find_elements(AppiumBy.ANDROID_UIAUTOMATOR, f'new UiSelector().textContains("{text}")')
            # 화면 안에 최소 2개가 보이면 종료
            if len(els) >= 2:
                return driver.swipe(size['width']//2, int(size['height']*0.8), size['width']//2, int(size['height']*0.2), 400)

    def test_resume_management(self, driver_setup):
        """홈화면 → 내 이력서 → 이력서 등록 및 수정 테스트"""
        if isinstance(driver_setup, dict):
            driver = driver_setup['driver']
        else:
            driver = driver_setup
        wait = WebDriverWait(driver, 10)
        
        try:
            time.sleep(0.5)
            
            # 내 이력서 버튼 클릭
            # my_resume_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'my_resume_btn')))
            my_resume_btn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "내 이력서")
            my_resume_btn.click()
            time.sleep(0.5)
            
            # 첫번째 항목 클릭
            first_resume_item = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'first_resume_item')))
            first_resume_item.click()
            time.sleep(0.5)

            modal_element = driver.find_elements(*self._get_locator(driver, 'modal'))
            if len(modal_element) == 1:
                # 모달이 나타난 경우 닫기 버튼 클릭
                modal_close_btn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "확인")
                modal_close_btn.click()
                time.sleep(0.5)
            else:
                pass

            
            # # 확인 버튼 클릭
            # confirm_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'confirm_btn')))
            # confirm_btn.click()
            # time.sleep(0.5)

            # 스크롤해서 아래로 내려가서 다음 버튼 클릭
            driver.find_element(
                AppiumBy.ANDROID_UIAUTOMATOR,
                'new UiScrollable(new UiSelector().scrollable(true).instance(0))'
                '.scrollIntoView(new UiSelector().textContains("다음").instance(0));'
            )
            time.sleep(0.5)

            # 다음 버튼 클릭
            # next_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'next_btn')))
            next_btn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "다음")
            next_btn.click()
            time.sleep(0.5)
            
            # 스크롤해서 아래로 내려가서 미리보기 버튼 클릭
            driver.find_element(
                AppiumBy.ANDROID_UIAUTOMATOR,
                'new UiScrollable(new UiSelector().scrollable(true).instance(0))'
                '.scrollIntoView(new UiSelector().textContains("미리보기").instance(0));'
            )
            time.sleep(0.5)
            
            # agree_btn1 = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'agree_btn1')))
            # agree_btn1.click()
            # time.sleep(0.5)
            
            # preview_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'preview_btn')))
            preview_btn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "미리보기")
            preview_btn.click()
            time.sleep(0.5)
            
            # 스크롤해서 아래로 내려가서 미리보기 버튼 클릭
            driver.find_element(
                AppiumBy.ANDROID_UIAUTOMATOR,
                'new UiScrollable(new UiSelector().scrollable(true).instance(0))'
                '.scrollIntoView(new UiSelector().textContains("등록완료").instance(0));'
            )
            time.sleep(0.5)
            
            # 등록완료 버튼 클릭
            # registration_complete_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'registration_complete_btn')))
            registration_complete_btn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "등록완료")
            registration_complete_btn.click()
            time.sleep(0.5)
            
            # 토스트 메세지 분석
            # try:
            #     toast_message = wait.until(EC.presence_of_element_located(self._get_locator(driver, 'toast_message')))
            #     print(f"첫번째 이력서 등록 토스트 메세지: {toast_message.text}")
            # except:
            #     print("첫번째 이력서 등록 토스트 메세지를 찾을 수 없습니다")
            
            # 두번째 항목 클릭
            second_resume_item = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'second_resume_item')))
            second_resume_item.click()
            time.sleep(0.5)

            modal_element = driver.find_elements(*self._get_locator(driver, 'modal'))
            if len(modal_element) == 1:
                # 모달이 나타난 경우 닫기 버튼 클릭
                modal_close_btn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "확인")
                modal_close_btn.click()
                time.sleep(0.5)
            else:
                pass

            # 확인 버튼 클릭
            # confirm_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'confirm_btn')))
            # confirm_btn.click()
            # time.sleep(0.5)
            
            # 상세주소 인풋 클릭해서 2층 넣기
            # detail_address_input = wait.until(EC.presence_of_element_located(self._get_locator(driver, 'detail_address_input')))
            # detail_address_input.clear()
            # detail_address_input.send_keys("2층")
            # time.sleep(0.5)

            # 스크롤해서 아래로 내려가서 다음 버튼 클릭
            driver.find_element(
                AppiumBy.ANDROID_UIAUTOMATOR,
                'new UiScrollable(new UiSelector().scrollable(true).instance(0))'
                '.scrollIntoView(new UiSelector().textContains("다음").instance(0));'
            )
            time.sleep(0.5)
            
            # 다음 버튼 클릭
            # next_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'next_btn')))
            next_btn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "다음")
            next_btn.click()
            time.sleep(0.5)
            
            # 전문분야 인풋에 간병요양 테스트중입니다 넣기
            # specialty_input = wait.until(EC.presence_of_element_located(self._get_locator(driver, 'specialty_input')))
            # specialty_input.clear()
            # specialty_input.send_keys("간병요양 테스트중입니다")
            # time.sleep(0.5)
            
            # 스크롤해서 아래로 내려가서 미리보기 버튼 클릭
            driver.find_element(
                AppiumBy.ANDROID_UIAUTOMATOR,
                'new UiScrollable(new UiSelector().scrollable(true).instance(0))'
                '.scrollIntoView(new UiSelector().textContains("미리보기").instance(0));'
            )
            time.sleep(0.5)
            
            # agree_btn1 = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'agree_btn1')))
            # agree_btn1.click()
            # time.sleep(0.5)
            
            # preview_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'preview_btn')))
            preview_btn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "미리보기")
            preview_btn.click()
            time.sleep(0.5)
            
            # 스크롤해서 아래로 내려가서 등록완료 버튼 클릭
            driver.find_element(
                AppiumBy.ANDROID_UIAUTOMATOR,
                'new UiScrollable(new UiSelector().scrollable(true).instance(0))'
                '.scrollIntoView(new UiSelector().textContains("등록완료").instance(0));'
            )
            time.sleep(0.5)

            # 등록완료 버튼 클릭
            # registration_complete_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'registration_complete_btn')))
            registration_complete_btn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "등록완료")
            registration_complete_btn.click()
            time.sleep(0.5)
            
            # 토스트 메세지 분석
            # try:
            #     toast_message = wait.until(EC.presence_of_element_located(self._get_locator(driver, 'toast_message')))
            #     print(f"두번째 이력서 등록 토스트 메세지: {toast_message.text}")
            # except:
            #     print("두번째 이력서 등록 토스트 메세지를 찾을 수 없습니다")
            
            # 뒤로가기 버튼 클릭
            # back_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'back_btn_general')))
            # back_btn.click()
            # time.sleep(0.5)
            driver.back()
            
        except Exception as e:
            pytest.fail(f"이력서 관리 테스트 실패: {str(e)}")
    
    def test_employment_certificate(self, driver_setup):
        """홈화면 → 지원공고 → 취업활동 증명서 발급 테스트"""
        if isinstance(driver_setup, dict):
            driver = driver_setup['driver']
        else:
            driver = driver_setup
        wait = WebDriverWait(driver, 10)
        
        try:
            time.sleep(2)
            
            # 지원공고 버튼 클릭
            job_application_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'job_application_btn')))
            job_application_btn.click()
            time.sleep(0.5)
            
            # 취업활동 증명서 발급하기 버튼 클릭
            employment_certificate_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'employment_certificate_btn')))
            employment_certificate_btn.click()
            time.sleep(0.5)
            
            # 첫번째 항목 클릭
            first_application_item = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'first_application_item')))
            first_application_item.click()
            time.sleep(0.5)
            
            # 이메일 전송하기 버튼 클릭
            # email_send_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'email_send_btn')))
            email_send_btn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "이메일 전송하기")
            email_send_btn.click()
            time.sleep(0.5)
            
            # 토스트 메세지 분석
            # try:
            #     toast_message = wait.until(EC.presence_of_element_located(self._get_locator(driver, 'toast_message')))
            #     print(f"이메일 전송 토스트 메세지: {toast_message.text}")
            # except:
            #     print("이메일 전송 토스트 메세지를 찾을 수 없습니다")
            
            # 뒤로가기 버튼 클릭 (3번)
            for i in range(3):
                # back_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'back_btn_general')))
                # back_btn.click()
                # time.sleep(0.5)
                driver.back()
            
        except Exception as e:
            pytest.fail(f"취업활동 증명서 발급 테스트 실패: {str(e)}")
    
    def test_position_proposal_management(self, driver_setup):
        """홈화면 → 포지션제안 → 이력서 업데이트 및 설정 테스트"""
        if isinstance(driver_setup, dict):
            driver = driver_setup['driver']
        else:
            driver = driver_setup
        wait = WebDriverWait(driver, 10)
        
        try:
            time.sleep(0.5)
            
            # 포지션제안 버튼 클릭
            position_proposal_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'position_proposal_btn')))
            position_proposal_btn.click()
            time.sleep(0.5)
            
            # 이력서 업데이트 버튼 클릭
            # resume_update_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'resume_update_btn')))
            resume_update_btn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "이력서 업데이트")
            resume_update_btn.click()
            time.sleep(0.5)
            
            # 스크롤 내려서 수정하기 버튼 클릭
            driver.find_element(
                AppiumBy.ANDROID_UIAUTOMATOR,
                'new UiScrollable(new UiSelector().scrollable(true).instance(0))'
                '.scrollIntoView(new UiSelector().textContains("수정하기").instance(0));'
            )
            time.sleep(0.5)
            
            # edit_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'edit_btn')))
            edit_btn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "수정하기")
            edit_btn.click()
            time.sleep(0.5)
            
            # 스크롤 내려서 수정하기 버튼 클릭
            driver.find_element(
                AppiumBy.ANDROID_UIAUTOMATOR,
                'new UiScrollable(new UiSelector().scrollable(true).instance(0))'
                '.scrollIntoView(new UiSelector().textContains("완료").instance(0));'
            )
            time.sleep(0.5)
            
            # 완료 버튼 클릭
            # complete_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'complete_btn')))
            complete_btn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "완료")
            complete_btn.click()
            time.sleep(0.5)
            
            # 토스트 메세지 분석
            # try:
            #     toast_message = wait.until(EC.presence_of_element_located(self._get_locator(driver, 'toast_message')))
            #     print(f"이력서 수정 토스트 메세지: {toast_message.text}")
            # except:
            #     print("이력서 수정 토스트 메세지를 찾을 수 없습니다")
            
            # 포지션 제안 설정 버튼 클릭
            # position_proposal_setting_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'position_proposal_setting_btn')))
            position_proposal_setting_btn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "포지션 제안 설정")
            position_proposal_setting_btn.click()
            time.sleep(0.5)
            
            # 후순 포지션이 있다면 제안 받을래요 체크박스 클릭
            # future_position_checkbox = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'future_position_checkbox')))
            # future_position_checkbox.click()
            # time.sleep(0.5)
            
            # 설정완료 버튼 클릭
            # setting_complete_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'setting_complete_btn')))
            setting_complete_btn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "설정완료")
            setting_complete_btn.click()
            time.sleep(0.5)
            
            # 토스트 메세지 분석
            # try:
            #     toast_message = wait.until(EC.presence_of_element_located(self._get_locator(driver, 'toast_message')))
            #     print(f"포지션 제안 설정 토스트 메세지: {toast_message.text}")
            # except:
            #     print("포지션 제안 설정 토스트 메세지를 찾을 수 없습니다")
            
            # 뒤로가기 버튼 클릭
            # back_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'back_btn_general')))
            # back_btn.click()
            # time.sleep(0.5)
            driver.back()
            
        except Exception as e:
            pytest.fail(f"포지션제안 관리 테스트 실패: {str(e)}")
    
    def test_service_category_navigation(self, driver_setup):
        """홈화면 → 요양보호사 → 간병/가사/동행 → 각 서비스 → 사회복지사 → 홈 네비게이션 테스트"""
        if isinstance(driver_setup, dict):
            driver = driver_setup['driver']
        else:
            driver = driver_setup
        wait = WebDriverWait(driver, 10)
        
        try:
            time.sleep(0.5)
            
            # 요양보호사 버튼 클릭
            # care_worker_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'care_worker_btn')))
            care_worker_btn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "요양보호사")
            care_worker_btn.click()
            time.sleep(1)
            
            # 간병/가사/동행 버튼 클릭
            # care_housekeeping_companion_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'care_housekeeping_companion_btn')))
            care_housekeeping_companion_btn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "간병/가사/동행")
            care_housekeeping_companion_btn.click()
            time.sleep(1)
            
            # 간병 버튼 클릭
            # caregiver_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'caregiver_btn')))
            caregiver_btn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "간병")
            caregiver_btn.click()
            time.sleep(1)
            
            # 가사돌봄 버튼 클릭
            # housekeeping_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'housekeeping_btn')))
            housekeeping_btn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "가사돌봄")
            housekeeping_btn.click()
            time.sleep(1)
            
            # 동행 버튼 클릭
            # companion_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'companion_btn')))
            companion_btn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "동행")
            companion_btn.click()
            time.sleep(1)
            
            # 사회복지사 버튼 클릭
            # social_worker_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'social_worker_btn')))
            social_worker_btn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "사회복지사")
            social_worker_btn.click()
            time.sleep(1)
            
            # 홈 버튼 클릭
            home_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'home_btn')))
            home_btn.click()
            time.sleep(1)
            
            # 위치 권한 모달이 있을 경우 While using the app 버튼 클릭
            try:
                location_permission_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'location_permission_while_using')))
                location_permission_btn.click()
                time.sleep(1)
            except:
                print("위치 권한 모달이 표시되지 않았습니다")
            
            # 바텀 메뉴에서 홈 버튼 클릭
            bottom_home_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'bottom_home_btn')))
            bottom_home_btn.click()
            time.sleep(0.5)
            
        except Exception as e:
            pytest.fail(f"서비스 카테고리 네비게이션 테스트 실패: {str(e)}")