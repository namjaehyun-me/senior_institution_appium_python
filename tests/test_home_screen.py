import pytest
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from scroll_helper import ScrollHelper
import time
import random

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
                # TODO: Android 요소들 - 실제 요소 확인 후 수정 필요
                'visit_care_btn': (AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="방문요양 찾기, 찾기"]'),
                # 'visit_care_btn': (AppiumBy.XPATH, '//android.widget.TextView[@text="방문요양 찾기"]'),
                'intro_btn': (AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="소개보기"]'),
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
                # 'start_time_dropdown': (AppiumBy.XPATH, '//android.widget.EditText[@text="선택"]'),
                'start_time_dropdown': (AppiumBy.XPATH, '//android.widget.HorizontalScrollView/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup[1]'),
                # 'time_11': (AppiumBy.XPATH, "//android.widget.TextView[@text='11:00']"),
                'duration_dropdown': (AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="선택"]'),
                'three_hours': (AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="3시간"]'),
                'load_info_btn': (AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="정보 불러오기"]'),
                'kim_younghee': (AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="김영희, 1등급, 여성, 41세, 자가거동자가보행"]'),
                'gender_any': (AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="성별무관"]'),
                'no_proceed': (AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="진행안함"]'),
                'kind_btn': (AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="친절함"]'),
                'agree_btn': (AppiumBy.XPATH, '//android.widget.TextView[@text="네, 동의합니다."]'),
                'auto_match_checkbox': (AppiumBy.XPATH, '//android.widget.TextView[@text="자동매칭"]'),
                'main_btn': (AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="메인이동"]'),
                'back_btn1': (AppiumBy.XPATH, '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup[1]'),
                'ltc_facility_btn': (AppiumBy.XPATH, "//android.widget.TextView[@text='장기요양기관 찾기']"),
                'location_access': (AppiumBy.ID, "com.android.permissioncontroller:id/permission_allow_foreground_only_button"),
                'region_dropdown': (AppiumBy.XPATH, "//android.widget.Spinner"),
                'nationwide': (AppiumBy.XPATH, "//android.widget.TextView[@text='전국']"),
                'find_facility_btn': (AppiumBy.XPATH, "//android.widget.TextView[@text='시설 찾기']"),
                'second_heart_btn': (AppiumBy.XPATH, "(//android.widget.ImageView[@content-desc='하트'])[2]"),
                'toast_message': (AppiumBy.XPATH, "//android.widget.Toast"),
                'second_item': (AppiumBy.XPATH, "(//android.widget.LinearLayout)[2]"),
                'consult_btn': (AppiumBy.XPATH, "//android.widget.TextView[@text='상담신청']"),
                'name_input': (AppiumBy.XPATH, "//android.widget.EditText[@hint='이름']"),
                'grade_dropdown': (AppiumBy.XPATH, "//android.widget.Spinner"),
                'dementia_checkbox': (AppiumBy.XPATH, "//android.widget.CheckBox[@text='치매']"),
                'female_checkbox': (AppiumBy.XPATH, "//android.widget.CheckBox[@text='여성']"),
                'sms_checkbox': (AppiumBy.XPATH, "//android.widget.CheckBox[@text='문자']"),
                'birth_year_dropdown': (AppiumBy.XPATH, "//android.widget.Spinner"),
                'year_2024': (AppiumBy.XPATH, "//android.widget.TextView[@text='2024']"),
                'phone_input': (AppiumBy.XPATH, "//android.widget.EditText[@hint='전화번호']"),
                'consult_time_dropdown': (AppiumBy.XPATH, "//android.widget.Spinner"),
                'send_btn': (AppiumBy.XPATH, "//android.widget.TextView[@text='보내기']"),
                'admission_support_btn': (AppiumBy.XPATH, "//android.widget.TextView[@text='입소지원']"),
                'hong_gildong_checkbox': (AppiumBy.XPATH, "//android.widget.CheckBox[@text='홍길동']"),
                'home_btn': (AppiumBy.XPATH, "//android.widget.TextView[@text='홈으로']"),
                'housekeeping_btn': (AppiumBy.XPATH, "//android.widget.TextView[@text='가사돌봄']"),
                'apply_housekeeping_btn': (AppiumBy.XPATH, "//android.widget.TextView[@text='가사돌봄서비스 신청하기']"),
                'under_18_checkbox': (AppiumBy.XPATH, "//android.widget.CheckBox[@text='18평 미만']"),
                'under_1_checkbox': (AppiumBy.XPATH, "//android.widget.CheckBox[@text='1개 이하']"),
                'alone_checkbox': (AppiumBy.XPATH, "//android.widget.CheckBox[@text='독거']"),
                'yes_checkbox_1': (AppiumBy.XPATH, "(//android.widget.CheckBox[@text='예'])[1]"),
                'yes_checkbox_2': (AppiumBy.XPATH, "(//android.widget.CheckBox[@text='예'])[2]"),
                'housekeeping_start_time_dropdown': (AppiumBy.XPATH, "//android.widget.Spinner"),
                'duration_dropdown_housekeeping': (AppiumBy.XPATH, "//android.widget.Spinner"),
                'one_hour': (AppiumBy.XPATH, "//android.widget.TextView[@text='1시간']")
            },
            'ios': {
                # TODO: iOS 요소들 - 실제 요소 확인 후 수정 필요
                'visit_care_btn': (AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='방문요양찾기']"),
                'intro_btn': (AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='소개보기']"),
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
                'time_11': (AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='11:00']"),
                'duration_dropdown': (AppiumBy.XPATH, "//XCUIElementTypePicker"),
                'three_hours': (AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='3시간']"),
                'load_info_btn': (AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='정보불러오기']"),
                'kim_younghee': (AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='김영희']"),
                'gender_any': (AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='성별무관']"),
                'no_proceed': (AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='진행안함']"),
                'kind_btn': (AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='친절함']"),
                'agree_btn': (AppiumBy.XPATH, "//XCUIElementTypeStaticText[contains(@name,'동의합니다')]"),
                'auto_match_checkbox': (AppiumBy.XPATH, "//XCUIElementTypeButton[contains(@name,'자동매칭')]"),
                'main_btn': (AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='메인이동']"),
                'ltc_facility_btn': (AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='장기요양기관 찾기']"),
                'region_dropdown': (AppiumBy.XPATH, "//XCUIElementTypePicker"),
                'nationwide': (AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='전국']"),
                'find_facility_btn': (AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='시설 찾기']"),
                'second_heart_btn': (AppiumBy.XPATH, "(//XCUIElementTypeButton[@name='하트'])[2]"),
                'toast_message': (AppiumBy.XPATH, "//XCUIElementTypeStaticText"),
                'second_item': (AppiumBy.XPATH, "(//XCUIElementTypeCell)[2]"),
                'consult_btn': (AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='상담신청']"),
                'name_input': (AppiumBy.XPATH, "//XCUIElementTypeTextField[@name='이름']"),
                'grade_dropdown': (AppiumBy.XPATH, "//XCUIElementTypePicker"),
                'dementia_checkbox': (AppiumBy.XPATH, "//XCUIElementTypeButton[@name='치매']"),
                'female_checkbox': (AppiumBy.XPATH, "//XCUIElementTypeButton[@name='여성']"),
                'sms_checkbox': (AppiumBy.XPATH, "//XCUIElementTypeButton[@name='문자']"),
                'birth_year_dropdown': (AppiumBy.XPATH, "//XCUIElementTypePicker"),
                'year_2024': (AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='2024']"),
                'phone_input': (AppiumBy.XPATH, "//XCUIElementTypeTextField[@name='전화번호']"),
                'consult_time_dropdown': (AppiumBy.XPATH, "//XCUIElementTypePicker"),
                'send_btn': (AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='보내기']"),
                'admission_support_btn': (AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='입소지원']"),
                'hong_gildong_checkbox': (AppiumBy.XPATH, "//XCUIElementTypeButton[@name='홍길동']"),
                'home_btn': (AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='홈으로']"),
                'housekeeping_btn': (AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='가사돌봄']"),
                'apply_housekeeping_btn': (AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='가사돌봄서비스 신청하기']"),
                'under_18_checkbox': (AppiumBy.XPATH, "//XCUIElementTypeButton[@name='18평 미만']"),
                'under_1_checkbox': (AppiumBy.XPATH, "//XCUIElementTypeButton[@name='1개 이하']"),
                'alone_checkbox': (AppiumBy.XPATH, "//XCUIElementTypeButton[@name='독거']"),
                'yes_checkbox_1': (AppiumBy.XPATH, "(//XCUIElementTypeButton[@name='예'])[1]"),
                'yes_checkbox_2': (AppiumBy.XPATH, "(//XCUIElementTypeButton[@name='예'])[2]"),
                'housekeeping_start_time_dropdown': (AppiumBy.XPATH, "//XCUIElementTypePicker"),
                'duration_dropdown_housekeeping': (AppiumBy.XPATH, "//XCUIElementTypePicker"),
                'one_hour': (AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='1시간']")
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
    
    def test_visit_care_service_registration(self, driver):
        """방문요양찾기 서비스 신청 테스트"""
        # driver가 딕셔너리인 경우 실제 driver 객체 추출
        sh = ScrollHelper(driver)
        if isinstance(driver, dict):
            actual_driver = driver['driver']
        else:
            actual_driver = driver
        wait = WebDriverWait(actual_driver, 10)
        
        try:
            # 홈 화면 진입 확인
            time.sleep(2)
            
            # 방문요양찾기 버튼 클릭
            visit_care_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'visit_care_btn')))
            visit_care_btn.click()
            time.sleep(1)
            
            # 소개보기 버튼 클릭
            # intro_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'intro_btn')))
            # intro_btn.click()
            # time.sleep(2)
            
            # # 다시 앱으로 돌아오기 (뒤로가기)
            # driver.back()
            # time.sleep(1)
            
            # 방문요양서비스 신청하기 클릭
            apply_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'apply_btn')))
            apply_btn.click()
            time.sleep(1)
            
            # "아니오, 가족이 아닙니다." 체크박스 클릭
            not_family_checkbox = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'not_family_checkbox')))
            not_family_checkbox.click()
            time.sleep(1)
            
            # 등록하기 버튼 클릭
            register_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'register_btn')))
            register_btn.click()
            time.sleep(1)
            
            # 장소 선택 버튼 클릭
            location_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'location_btn')))
            location_btn.click()
            time.sleep(1)
            
            # 인풋에 "다산순환로20" 입력
            address_input = wait.until(EC.presence_of_element_located(self._get_locator(driver, 'address_input')))
            address_input.clear()
            address_input.send_keys("s")
            time.sleep(1)
            
            # 돋보기 버튼 클릭
            search_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'search_btn')))
            search_btn.click()
            time.sleep(2)
            
            # 첫번째 항목 클릭
            first_result = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'first_result')))
            first_result.click()
            time.sleep(1)
            
            # 확인 버튼 클릭
            confirm_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'confirm_btn')))
            confirm_btn.click()
            time.sleep(1)
            
            # 다음 버튼 클릭
            next_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'next_btn')))
            next_btn.click()
            time.sleep(1)
            
            # 캘린더에서 > 버튼 클릭
            calendar_next = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'calendar_next')))
            calendar_next.click()
            time.sleep(1)
            
            # 1~30까지 랜덤한 날짜 클릭
            # //android.view.ViewGroup[@content-desc="28"]
            random_day = random.randint(1, 30)
            date_btn = wait.until(EC.element_to_be_clickable(self._get_date_locator(driver, random_day)))
            date_btn.click()
            time.sleep(1)
            # driver.swipe(driver, 708, 2433, 666, 792)
            actual_driver.swipe(708, 2433, 666, 792, 1000)
            # target = self._get_locator(driver, 'start_time_dropdown')
            # sh.into_view(target, direction='down')
            # sh.into_view(self._get_locator(driver, 'start_time_dropdown'))
            # 방문 시작시간 드롭다운 클릭
            start_time_dropdown = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'start_time_dropdown')))
            start_time_dropdown.click()
            time.sleep(1)
            
            # 11:00로 시간 설정
            # time_11 = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'time_11')))
            # time_11.click()
            # time.sleep(1)
            
            # 확인 버튼 클릭
            # //android.widget.Button[@resource-id="android:id/button1"]
            confirm_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'confirm_btn2')))
            confirm_btn.click()
            time.sleep(1)
            
            # 방문시간 드롭다운 클릭
            duration_dropdown = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'duration_dropdown')))
            duration_dropdown.click()
            time.sleep(1)
            
            # 3시간 클릭
            three_hours = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'three_hours')))
            three_hours.click()
            time.sleep(1)


            actual_driver.swipe(650, 2535, 842, 403, 1000)
            time.sleep(1)
            
            # 다음 버튼 클릭
            # //android.view.ViewGroup[@content-desc="다음"]
            # next_btn1 = wait.until(EC.element_to_be_clickable(AppiumBy.XPATH, '//android.widget.TextView[@text="다음"]'))
            # next_btn1 = wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="다음"]')))
            # next_btn_element = actual_driver.find_element(*self._get_locator(driver, 'next_btn1'))
            # TouchAction(actual_driver).tap(next_btn_element).perform()
            # next_btn1 = wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, '//android.widget.TextView[@text="다음"]')))
            next_btn_element = actual_driver.find_element(*self._get_locator(driver, 'next_btn1'))

            # mobile: clickGesture로 클릭
            actual_driver.execute_script('mobile: clickGesture', {
                'elementId': next_btn_element.id
            })
            print("다음버튼 클릭")
            # next_btn1.click()
            time.sleep(1)
            
            # 정보불러오기 버튼 클릭
            load_info_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'load_info_btn')))
            load_info_btn.click()
            time.sleep(1)
            
            # 김영희 항목 클릭
            kim_younghee = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'kim_younghee')))
            kim_younghee.click()
            time.sleep(1)

            actual_driver.swipe(646, 2635, 668, 221, 1000)
            
            time.sleep(1)
            # 다음 버튼 클릭
            element = actual_driver.find_element(AppiumBy.ACCESSIBILITY_ID, "다음")
            element.click()
            # next_btn_element2 = actual_driver.find_element(*self._get_locator(driver, 'next_btn2'))
            # print("다음버튼 클릭", next_btn_element2)
            # # mobile: clickGesture로 클릭
            # actual_driver.execute_script('mobile: clickGesture', {
            #     'elementId': next_btn_element2.id
            # })
            time.sleep(1)
            
            # 성별무관 버튼 클릭
            gender_any = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'gender_any')))
            gender_any.click()
            time.sleep(1)
            
            # 진행안함 버튼 클릭
            no_proceed = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'no_proceed')))
            no_proceed.click()
            time.sleep(1)
            
            # 친절함 버튼 클릭
            kind_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'kind_btn')))
            kind_btn.click()
            time.sleep(1)

            actual_driver.swipe(571, 2577, 603, 411, 1000)
            time.sleep(1)
            
            # 다음 버튼 클릭
            next_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'next_btn')))
            next_btn.click()
            time.sleep(1)
            
            actual_driver.swipe(578, 2906, 478, 282, 1000)
            time.sleep(1)
            actual_driver.swipe(728, 2735, 735, 793, 1000)
            time.sleep(1)

            # 다음 버튼 클릭
            next_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'next_btn')))
            next_btn.click()
            time.sleep(1)
            
            # "네, 동의합니다." 버튼 클릭
            agree_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'agree_btn')))
            agree_btn.click()
            time.sleep(1)
            
            # 등록하기 버튼 클릭
            # //android.view.ViewGroup[@content-desc="등록하기"]
            register_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'register_btn')))
            register_btn.click()
            time.sleep(1)
            
            # 자동매칭 체크박스 클릭
            # auto_match_checkbox = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'auto_match_checkbox')))
            # auto_match_checkbox.click()
            # time.sleep(1)
            
            actual_driver.swipe(525, 2720, 425, 664, 1000)
            time.sleep(1)

            # 다음 버튼 클릭
            # //android.view.ViewGroup[@content-desc="다음"]
            next_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'next_btn')))
            next_btn.click()
            time.sleep(1)
            
            # 메인이동 버튼 클릭
            main_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'main_btn')))
            main_btn.click()
            time.sleep(1)
            
            # 뒤로가기 버튼 클릭
            back_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'back_btn1')))
            back_btn.click()
            # actual_driver.back()
            time.sleep(1)
            
        except Exception as e:
            pytest.fail(f"방문요양찾기 테스트 실패: {str(e)}")
    
    def test_long_term_care_facility_search(self, driver):
        """장기요양기관 찾기 테스트"""
        # driver가 딕셔너리인 경우 실제 driver 객체 추출
        if isinstance(driver, dict):
            actual_driver = driver['driver']
        else:
            actual_driver = driver
        wait = WebDriverWait(actual_driver, 10)
        
        try:
            # 홈 화면 진입 확인
            time.sleep(2)
            
            # 장기요양기관 찾기 버튼 클릭
            # ltc_facility_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'ltc_facility_btn')))
            # ltc_facility_btn.click()
            ltc_facility_btn = actual_driver.find_element(AppiumBy.ACCESSIBILITY_ID, "장기요양기관\n찾기, 찾기")
            ltc_facility_btn.click()
            time.sleep(1)

            location_access_btn = actual_driver.find_element(*self._get_locator(driver, 'location_access'))
            location_access_btn.click()
            
            # 시도/ 드롭다운 클릭
            region_dropdown = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'region_dropdown')))
            region_dropdown.click()
            time.sleep(1)
            
            # 전국 클릭
            nationwide = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'nationwide')))
            nationwide.click()
            time.sleep(1)
            
            # 시설 찾기 버튼 클릭
            find_facility_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'find_facility_btn')))
            find_facility_btn.click()
            time.sleep(2)
            
            # 두번째 항목의 하트 버튼 클릭
            second_heart_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'second_heart_btn')))
            second_heart_btn.click()
            time.sleep(1)
            
            # 관심기업으로 등록이 되었다는 토스트메세지 확인
            toast_message = wait.until(EC.presence_of_element_located(self._get_locator(driver, 'toast_message')))
            assert "관심기업" in toast_message.text or "등록" in toast_message.text
            time.sleep(2)
            
            # 두번째 항목 클릭
            second_item = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'second_item')))
            second_item.click()
            time.sleep(1)
            
            # 스크롤해서 아래로 내려가서 상담신청 버튼 클릭
            driver.swipe(500, 1500, 500, 500, 1000)  # 스크롤 다운
            time.sleep(1)
            consult_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'consult_btn')))
            consult_btn.click()
            time.sleep(1)
            
            # 이름 인풋에 "김동라그미" 입력
            name_input = wait.until(EC.presence_of_element_located(self._get_locator(driver, 'name_input')))
            name_input.clear()
            name_input.send_keys("김동라그미")
            time.sleep(1)
            
            # 등급 드롭다운 클릭
            grade_dropdown = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'grade_dropdown')))
            grade_dropdown.click()
            time.sleep(1)
            
            # 치매 체크박스 클릭
            dementia_checkbox = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'dementia_checkbox')))
            dementia_checkbox.click()
            time.sleep(1)
            
            # 여성 체크박스 클릭
            female_checkbox = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'female_checkbox')))
            female_checkbox.click()
            time.sleep(1)
            
            # 문자 체크박스 클릭
            sms_checkbox = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'sms_checkbox')))
            sms_checkbox.click()
            time.sleep(1)
            
            # 어르신의 출생 연도 드롭다운 클릭
            birth_year_dropdown = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'birth_year_dropdown')))
            birth_year_dropdown.click()
            time.sleep(1)
            
            # 2024 클릭
            year_2024 = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'year_2024')))
            year_2024.click()
            time.sleep(1)
            
            # 상담 받으실 전화번호 인풋에 "01092205162" 입력
            phone_input = wait.until(EC.presence_of_element_located(self._get_locator(driver, 'phone_input')))
            phone_input.clear()
            phone_input.send_keys("01092205162")
            time.sleep(1)
            
            # 상담받기 편한 시간대 드롭다운 클릭
            consult_time_dropdown = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'consult_time_dropdown')))
            consult_time_dropdown.click()
            time.sleep(1)
            
            # 11:00로 시간 설정
            time_11 = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'time_11')))
            time_11.click()
            time.sleep(1)
            
            # 확인 버튼 클릭
            confirm_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'confirm_btn')))
            confirm_btn.click()
            time.sleep(1)
            
            # 보내기 버튼 클릭
            send_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'send_btn')))
            send_btn.click()
            time.sleep(1)
            
            # 입소지원 버튼 클릭
            admission_support_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'admission_support_btn')))
            admission_support_btn.click()
            time.sleep(1)
            
            # 홍길동 항목 체크박스 클릭
            hong_gildong_checkbox = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'hong_gildong_checkbox')))
            hong_gildong_checkbox.click()
            time.sleep(1)
            
            # 확인 버튼 클릭
            confirm_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'confirm_btn')))
            confirm_btn.click()
            time.sleep(1)
            
            # 홈으로 버튼 클릭
            home_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'home_btn')))
            home_btn.click()
            time.sleep(1)
            
        except Exception as e:
            pytest.fail(f"장기요양기관 찾기 테스트 실패: {str(e)}")
    
    def test_housekeeping_service_registration(self, driver):
        """가사돌봄 서비스 신청 테스트"""
        # driver가 딕셔너리인 경우 실제 driver 객체 추출
        if isinstance(driver, dict):
            actual_driver = driver['driver']
        else:
            actual_driver = driver
        wait = WebDriverWait(actual_driver, 10)
        
        try:
            # 홈 화면 진입 확인
            time.sleep(2)
            
            # 가사돌봄 버튼 클릭
            housekeeping_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'housekeeping_btn')))
            housekeeping_btn.click()
            time.sleep(1)
            
            # 소개보기 버튼 클릭
            # intro_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'intro_btn')))
            # intro_btn.click()
            # time.sleep(2)
            
            # # 다시 앱으로 돌아오기
            # driver.back()
            # time.sleep(1)
            
            # 가사돌봄서비스 신청하기
            apply_housekeeping_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'apply_housekeeping_btn')))
            apply_housekeeping_btn.click()
            time.sleep(1)
            
            # 다음 버튼 클릭
            next_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'next_btn')))
            next_btn.click()
            time.sleep(1)
            
            # 장소선택 버튼 클릭
            location_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'location_btn')))
            location_btn.click()
            time.sleep(1)
            
            # 인풋에 "다산순환로20" 입력
            address_input = wait.until(EC.presence_of_element_located(self._get_locator(driver, 'address_input')))
            address_input.clear()
            address_input.send_keys("다산순환로20")
            time.sleep(1)
            
            # 돋보기 버튼 클릭
            search_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'search_btn')))
            search_btn.click()
            time.sleep(2)
            
            # 첫번째 항목 클릭
            first_result = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'first_result')))
            first_result.click()
            time.sleep(1)
            
            # 확인 버튼 클릭
            confirm_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'confirm_btn')))
            confirm_btn.click()
            time.sleep(1)
            
            # 다음 버튼 클릭
            next_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'next_btn')))
            next_btn.click()
            time.sleep(1)
            
            # 1-5번째 체크박스까지 클릭
            for i in range(1, 6):
                checkbox = wait.until(EC.element_to_be_clickable(self._get_checkbox_locator(driver, i)))
                checkbox.click()
                time.sleep(0.5)
            
            # 18평 미만 체크박스 클릭
            under_18_checkbox = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'under_18_checkbox')))
            under_18_checkbox.click()
            time.sleep(1)
            
            # 1개 이하 체크박스 클릭
            under_1_checkbox = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'under_1_checkbox')))
            under_1_checkbox.click()
            time.sleep(1)
            
            # 독거 체크박스 클릭
            alone_checkbox = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'alone_checkbox')))
            alone_checkbox.click()
            time.sleep(1)
            
            # 예 체크박스 클릭 (2번)
            yes_checkbox_1 = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'yes_checkbox_1')))
            yes_checkbox_1.click()
            time.sleep(1)
            
            yes_checkbox_2 = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'yes_checkbox_2')))
            yes_checkbox_2.click()
            time.sleep(1)
            
            # 다음 버튼 클릭
            next_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'next_btn')))
            next_btn.click()
            time.sleep(1)
            
            # 1-30까지 랜덤한 날짜 클릭
            random_day = random.randint(1, 30)
            date_btn = wait.until(EC.element_to_be_clickable(self._get_date_locator(driver, random_day)))
            date_btn.click()
            time.sleep(1)
            
            # 가사돌봄 시작시간 드롭다운 클릭
            start_time_dropdown = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'housekeeping_start_time_dropdown')))
            start_time_dropdown.click()
            time.sleep(1)
            
            # 11:00로 시간 설정
            time_11 = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'time_11')))
            time_11.click()
            time.sleep(1)
            
            # 확인 버튼 클릭
            confirm_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'confirm_btn')))
            confirm_btn.click()
            time.sleep(1)
            
            # 신청 시간 드롭다운 클릭
            duration_dropdown = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'duration_dropdown_housekeeping')))
            duration_dropdown.click()
            time.sleep(1)
            
            # 1시간 클릭
            one_hour = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'one_hour')))
            one_hour.click()
            time.sleep(1)
            
            # 다음 버튼 클릭
            next_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'next_btn')))
            next_btn.click()
            time.sleep(1)
            
            # 정보불러오기 버튼 클릭
            load_info_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'load_info_btn')))
            load_info_btn.click()
            time.sleep(1)
            
            # 김영희 항목 클릭
            kim_younghee = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'kim_younghee')))
            kim_younghee.click()
            time.sleep(1)
            
            # 다음 버튼 클릭
            next_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'next_btn')))
            next_btn.click()
            time.sleep(1)
            
            # "네, 동의합니다." 버튼 클릭
            agree_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'agree_btn')))
            agree_btn.click()
            time.sleep(1)
            
            # 등록하기 버튼 클릭
            register_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'register_btn')))
            register_btn.click()
            time.sleep(1)
            
            # 메인이동 버튼 클릭
            main_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'main_btn')))
            main_btn.click()
            time.sleep(1)
            
            # 뒤로가기 버튼 클릭
            actual_driver.back()
            time.sleep(1)
            
        except Exception as e:
            pytest.fail(f"가사돌봄 서비스 테스트 실패: {str(e)}")