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
                # 새로운 시나리오 로케이터들
                'admission_mode_btn': (AppiumBy.XPATH, '//android.widget.TextView[@text="입소모드"]'),
                'ltc_facility_search_btn': (AppiumBy.XPATH, '//android.widget.TextView[@text="장기요양기관찾기"]'),
                'region_btn': (AppiumBy.XPATH, '//android.widget.TextView[@text="지역:"]'),
                'seoul_btn': (AppiumBy.XPATH, '//android.widget.TextView[@text="서울"]'),
                'seoul_all_btn': (AppiumBy.XPATH, '//android.widget.TextView[@text="서울전체"]'),
                'selection_complete_btn': (AppiumBy.XPATH, '//android.widget.TextView[@text="선택완료"]'),
                'first_facility_item': (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.view.ViewGroup").instance(23)'),
                'first_item': (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.view.ViewGroup").instance(32)'),
                'nationwide_btn': (AppiumBy.XPATH, '//android.widget.TextView[@text="전국"]'),
                # 'search_input_caring': (AppiumBy.CLASS_NAME, 'android.widget.EditText'),
                'search_input_caring': (AppiumBy.XPATH, '//android.widget.EditText[@text="검색"]'),
                'search_magnifier_btn': (AppiumBy.XPATH, '//android.widget.Button[@text="검색"]'),
                'facility_name_text': (AppiumBy.XPATH, '(//android.widget.TextView[@text="국민건강보험공단 서울요양원 재가복지센터"])[1]'),
                'recruitment_mode_btn': (AppiumBy.XPATH, '//android.widget.TextView[@text="채용모드"]'),
                'admission_inquiry_btn': (AppiumBy.XPATH, '//android.widget.TextView[@text="입소문의"]'),
                'sms_send_btn': (AppiumBy.XPATH, '//android.widget.TextView[@text="SMS 발송"]'),
                'application_form_btn': (AppiumBy.XPATH, '//android.widget.TextView[@text="입소신청서"]'),
                'approve_btn': (AppiumBy.XPATH, '//android.widget.TextView[@text="신청서 승인"]'),
                'reject_btn': (AppiumBy.XPATH, '//android.widget.TextView[@text="신청서 거절"]'),
                'progress_btn': (AppiumBy.XPATH, '(//android.view.ViewGroup[@content-desc="진행"])[1]'),
                'list_not_have_text': (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("데이터를 찾을 수 없습니다")'),
                'job_posting_progress_btn': (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("진행").instance(0)'),
                'job_posting_progress_btn2': (AppiumBy.XPATH, '(//android.widget.TextView[@text="진행"])[1]'),
                'closed_btn': (AppiumBy.XPATH, '//android.widget.TextView[@text="마감"]'),
                'completed_btn': (AppiumBy.XPATH, '//android.widget.TextView[@text="완료"]'),
                'job_posting_btn': (AppiumBy.XPATH, '//android.widget.TextView[@text="채용공고"]'),
                'all_btn': (AppiumBy.XPATH, '//android.widget.TextView[@text="전체"]'),
                'applicant_management_btn': (AppiumBy.XPATH, '//android.widget.TextView[@text="지원지관리"]'),
                'copy_btn': (AppiumBy.XPATH, '//android.widget.TextView[@text="복사하기"]'),
                'next_step_btn': (AppiumBy.XPATH, '//android.widget.TextView[@text="다음 단계"]'),
                'one_month_btn': (AppiumBy.XPATH, '//android.widget.TextView[@text="1개월"]'),
                'job_title_input': (AppiumBy.XPATH, '//android.widget.EditText'),
                'job_registration_complete_btn': (AppiumBy.XPATH, '//android.widget.TextView[@text="공고 등록 완료"]'),
                'all_agree_checkbox': (AppiumBy.XPATH, '//android.widget.TextView[@text="전체동의"]'),
                'delete_btn': (AppiumBy.XPATH, '//android.widget.TextView[@text="삭제하기"]'),
                'job_registration_btn': (AppiumBy.XPATH, '//android.widget.TextView[@text="공고등록"]'),
                'care_worker_checkbox': (AppiumBy.XPATH, '//android.widget.TextView[@text="요양보호사"]'),
                'female_checkbox': (AppiumBy.XPATH, '//android.widget.TextView[@text="여성"]'),
                'homeless_checkbox': (AppiumBy.XPATH, '//android.widget.TextView[@text="노숙인"]'),
                'mental_health_checkbox': (AppiumBy.XPATH, '//android.widget.TextView[@text="정신건강"]'),
                'recruitment_count_input': (AppiumBy.XPATH, '//android.widget.EditText[@text="모집인원"]'),
                'experience_irrelevant_checkbox': (AppiumBy.XPATH, '//android.widget.TextView[@text="경력 무관"]'),
                'main_task_input': (AppiumBy.XPATH, '//android.widget.EditText[@text="주요 업무"]'),
                'certificate_input': (AppiumBy.XPATH, '//android.widget.EditText[@text="자격증"]'),
                'full_time_checkbox': (AppiumBy.XPATH, '//android.widget.TextView[@text="정규직"]'),
                'daily_work_hours_input': (AppiumBy.XPATH, '//android.widget.EditText[@text="매일 근무시간"]'),
                'weekly_work_days_dropdown': (AppiumBy.XPATH, '//android.widget.Spinner[@text="주당 근무일수"]'),
                'four_days_btn': (AppiumBy.XPATH, '//android.widget.TextView[@text="4"]'),
                'salary_dropdown': (AppiumBy.XPATH, '//android.widget.Spinner[@text="급여"]'),
                'monthly_salary_btn': (AppiumBy.XPATH, '//android.widget.TextView[@text="월급"]'),
                'salary_input': (AppiumBy.XPATH, '//android.widget.EditText[@text="급여"]'),
                'fifteen_days_btn': (AppiumBy.XPATH, '//android.widget.TextView[@text="15일"]'),
                'job_title_input_urgent': (AppiumBy.XPATH, '//android.widget.EditText[@text="채용제목"]'),
                'more_btn': (AppiumBy.XPATH, '//android.widget.TextView[@text="더보기"]'),
                'befor_more_btn': (AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="나와 가까운 채용정보, 마이 플레이스"]/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup'),
                'refresh_btn': (AppiumBy.XPATH, '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]'),
                'intro_btn': (AppiumBy.XPATH, '//android.widget.TextView[@text="소개보기"]'),
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
                # 새로운 시나리오 로케이터들
                'admission_mode_btn': (AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='입소모드']"),
                'ltc_facility_search_btn': (AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='장기요양기관찾기']"),
                'region_btn': (AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='지역:']"),
                'seoul_btn': (AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='서울']"),
                'seoul_all_btn': (AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='서울전체']"),
                'selection_complete_btn': (AppiumBy.XPATH, "//XCUIElementTypeButton[@name='선택완료']"),
                'first_facility_item': (AppiumBy.XPATH, "(//XCUIElementTypeCell)[1]"),
                'first_item': (AppiumBy.XPATH, "(//XCUIElementTypeCell)[1]"),
                'nationwide_btn': (AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='전국']"),
                'search_input_caring': (AppiumBy.XPATH, "//XCUIElementTypeTextField[@name='검색']"),
                'search_magnifier_btn': (AppiumBy.XPATH, "//XCUIElementTypeButton[@name='검색']"),
                'facility_name_text': (AppiumBy.XPATH, "//XCUIElementTypeStaticText"),
                'recruitment_mode_btn': (AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='채용모드']"),
                'admission_inquiry_btn': (AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='입소문의']"),
                'sms_send_btn': (AppiumBy.XPATH, "//XCUIElementTypeButton[@name='SMS 발송']"),
                'application_form_btn': (AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='입소신청서']"),
                'approve_btn': (AppiumBy.XPATH, "//XCUIElementTypeButton[@name='신청서 승인']"),
                'reject_btn': (AppiumBy.XPATH, "//XCUIElementTypeButton[@name='신청서 거절']"),
                'progress_btn': (AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='진행']"),
                'job_posting_progress_btn': (AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='진행']"),
                'job_posting_progress_btn2': (AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='진행']"),
                'closed_btn': (AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='마감']"),
                'completed_btn': (AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='완료']"),
                'job_posting_btn': (AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='채용공고']"),
                'all_btn': (AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='전체']"),
                'applicant_management_btn': (AppiumBy.XPATH, "//XCUIElementTypeButton[@name='지원지관리']"),
                'copy_btn': (AppiumBy.XPATH, "//XCUIElementTypeButton[@name='복사하기']"),
                'next_step_btn': (AppiumBy.XPATH, "//XCUIElementTypeButton[@name='다음 단계']"),
                'one_month_btn': (AppiumBy.XPATH, "//XCUIElementTypeButton[@name='1개월']"),
                'job_title_input': (AppiumBy.XPATH, "//XCUIElementTypeTextField"),
                'job_registration_complete_btn': (AppiumBy.XPATH, "//XCUIElementTypeButton[@name='공고 등록 완료']"),
                'all_agree_checkbox': (AppiumBy.XPATH, "//XCUIElementTypeButton[@name='전체동의']"),
                'delete_btn': (AppiumBy.XPATH, "//XCUIElementTypeButton[@name='삭제하기']"),
                'job_registration_btn': (AppiumBy.XPATH, "//XCUIElementTypeButton[@name='공고등록']"),
                'care_worker_checkbox': (AppiumBy.XPATH, "//XCUIElementTypeButton[@name='요양보호사']"),
                'female_checkbox': (AppiumBy.XPATH, "//XCUIElementTypeButton[@name='여성']"),
                'homeless_checkbox': (AppiumBy.XPATH, "//XCUIElementTypeButton[@name='노숙인']"),
                'mental_health_checkbox': (AppiumBy.XPATH, "//XCUIElementTypeButton[@name='정신건강']"),
                'recruitment_count_input': (AppiumBy.XPATH, "//XCUIElementTypeTextField[@name='모집인원']"),
                'experience_irrelevant_checkbox': (AppiumBy.XPATH, "//XCUIElementTypeButton[@name='경력 무관']"),
                'main_task_input': (AppiumBy.XPATH, "//XCUIElementTypeTextField[@name='주요 업무']"),
                'certificate_input': (AppiumBy.XPATH, "//XCUIElementTypeTextField[@name='자격증']"),
                'full_time_checkbox': (AppiumBy.XPATH, "//XCUIElementTypeButton[@name='정규직']"),
                'daily_work_hours_input': (AppiumBy.XPATH, "//XCUIElementTypeTextField[@name='매일 근무시간']"),
                'weekly_work_days_dropdown': (AppiumBy.XPATH, "//XCUIElementTypePicker[@name='주당 근무일수']"),
                'four_days_btn': (AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='4']"),
                'salary_dropdown': (AppiumBy.XPATH, "//XCUIElementTypePicker[@name='급여']"),
                'monthly_salary_btn': (AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='월급']"),
                'salary_input': (AppiumBy.XPATH, "//XCUIElementTypeTextField[@name='급여']"),
                'fifteen_days_btn': (AppiumBy.XPATH, "//XCUIElementTypeButton[@name='15일']"),
                'job_title_input_urgent': (AppiumBy.XPATH, "//XCUIElementTypeTextField[@name='채용제목']"),
                'more_btn': (AppiumBy.XPATH, "//XCUIElementTypeButton[@name='더보기']"),
                'befor_more_btn': (AppiumBy.XPATH, "//XCUIElementTypeButton[@name='더보기']"),
                'refresh_btn': (AppiumBy.XPATH, "//XCUIElementTypeButton[@name='새로고침']"),
                'intro_btn': (AppiumBy.XPATH, "//XCUIElementTypeButton[@name='소개보기']"),
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

    """홈화면 → 입소모드 → 장기요양기관찾기 → 지역 선택 및 검색 테스트"""
    def test_admission_mode_ltc_facility_search(self, driver_setup): 
        # 지역: 전국 버튼 클릭시 나오는 이슈 수정되면 이후 플로우 작성가능
        if isinstance(driver_setup, dict):
            driver = driver_setup['driver']
        else:
            driver = driver_setup
        wait = WebDriverWait(driver, 10)
        
        try:
            time.sleep(0.5)
            
            # 입소모드 버튼 클릭
            # admission_mode_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'admission_mode_btn')))
            admission_mode_btn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "입소모드")
            admission_mode_btn.click()
            time.sleep(0.5)
            
            # 장기요양기관찾기 버튼 클릭
            # ltc_facility_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'ltc_facility_search_btn')))
            ltc_facility_btn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "장기요양기관찾기, 찾기")
            ltc_facility_btn.click()
            time.sleep(0.5)
            
            # 지역: 버튼 클릭
            # region_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'region_btn')))
            region_btn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "지역: 전국")
            region_btn.click()
            time.sleep(0.5)
            
            # 서울 버튼 클릭
            # seoul_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'seoul_btn')))
            seoul_btn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "서울")
            seoul_btn.click()
            time.sleep(0.5)
            
            # 서울전체 버튼 클릭
            # seoul_all_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'seoul_all_btn')))
            seoul_all_btn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "서울전체")
            seoul_all_btn.click()
            time.sleep(0.5)
            
            # 선택완료 버튼 클릭
            # selection_complete_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'selection_complete_btn')))
            selection_complete_btn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "선택완료")
            selection_complete_btn.click()
            time.sleep(2)
            
            # 첫번째 항목 클릭
            # first_facility_item = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'first_facility_item')))
            first_facility_item = driver.find_element(*self._get_locator(driver, 'first_facility_item'))
            first_facility_item.click()
            time.sleep(2)
            
            # 스크롤해서 아래까지 갔다가 다시 위로 올라오기
            driver.find_element(
                AppiumBy.ANDROID_UIAUTOMATOR,
                'new UiScrollable(new UiSelector().scrollable(true)).scrollToEnd(10)'
            )
            time.sleep(0.5)
            driver.find_element(
                AppiumBy.ANDROID_UIAUTOMATOR,
                'new UiScrollable(new UiSelector().scrollable(true)).scrollToBeginning(10)'
            )
            time.sleep(0.5)
            
            # 뒤로가기 버튼 클릭
            driver.back()
            # time.sleep(0.5)
            
            # 지역: 서울/서울전체 버튼 클릭
            # region_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'region_btn')))
            region_btn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "지역: 서울/서울전체")
            region_btn.click()
            time.sleep(0.5)
            
            # 전국 버튼 클릭
            # nationwide_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'nationwide_btn')))
            nationwide_btn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "전국")
            nationwide_btn.click()
            time.sleep(0.5)
            
            # 선택완료 버튼 클릭
            # selection_complete_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'selection_complete_btn')))
            selection_complete_btn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "선택완료")
            selection_complete_btn.click()
            time.sleep(2)
            
            # 첫번째 항목 클릭
            # first_facility_item = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'first_facility_item')))
            first_facility_item = driver.find_element(*self._get_locator(driver, 'first_facility_item'))
            first_facility_item.click()
            time.sleep(2)
            
            # 스크롤해서 아래까지 갔다가 다시 위로 올라오기
            driver.find_element(
                AppiumBy.ANDROID_UIAUTOMATOR,
                'new UiScrollable(new UiSelector().scrollable(true)).scrollToEnd(10)'
            )
            time.sleep(0.5)
            driver.find_element(
                AppiumBy.ANDROID_UIAUTOMATOR,
                'new UiScrollable(new UiSelector().scrollable(true)).scrollToBeginning(10)'
            )
            time.sleep(0.5)
            
            # 뒤로가기 버튼 클릭
            driver.back()
            # time.sleep(0.5)
            
            # 검색 인풋에 케어링 넣기
            # search_input = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'search_input_caring')))
            search_input = driver.find_element(*self._get_locator(driver, 'search_input_caring'))
            # search_input.click()
            search_input.clear()
            search_input.send_keys("국민건강보험")
            time.sleep(0.5)
            
            # 돋보기 버튼 클릭
            # search_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'search_magnifier_btn')))
            # search_btn.click()
            # time.sleep(2)
            
            # 첫번째항목 클릭
            # first_facility_item = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'first_facility_item')))
            first_facility_item = driver.find_element(*self._get_locator(driver, 'first_facility_item'))
            first_facility_item.click()
            time.sleep(2)
            
            # 요양원 이름에 검색 키워드가 들어가있는지 확인
            try:
                facility_name = wait.until(EC.presence_of_element_located(self._get_locator(driver, 'facility_name_text')))
                text = facility_name.get_attribute("text")
                assert text == "국민건강보험공단 서울요양원 재가복지센터" 
                print("검색 키워드과 첫번째 항목 일치")
            except:
                pytest.fail("검색 키워드과 첫번째 항목 불일치")

            # 뒤로가기 버튼 클릭
            driver.back()
            
            # 뒤로가기 버튼 클릭
            driver.back()
            
            print("입소모드 장기요양기관찾기 테스트 완료")
            
        except Exception as e:
            pytest.fail(f"입소모드 장기요양기관찾기 테스트 실패: {str(e)}")
    
    """홈화면 → 채용모드 → 입소문의 → SMS 발송 및 신청서 관리 테스트"""
    def test_recruitment_mode_admission_inquiry(self, driver_setup):
        if isinstance(driver_setup, dict):
            driver = driver_setup['driver']
        else:
            driver = driver_setup
        wait = WebDriverWait(driver, 10)
        
        try:
            time.sleep(0.5)
            
            # 채용모드 버튼 클릭
            # recruitment_mode_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'recruitment_mode_btn')))
            recruitment_mode_btn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "채용모드")
            recruitment_mode_btn.click()
            time.sleep(0.5)
            
            # 입소문의 버튼 클릭
            admission_inquiry_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'admission_inquiry_btn')))
            admission_inquiry_btn.click()
            time.sleep(0.5)
            
            # 첫번째 항목의 SMS 발송 버튼 클릭
            # sms_send_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'sms_send_btn')))
            sms_send_btn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "SMS 발송")
            sms_send_btn.click()
            time.sleep(0.5)

            driver.back()
            driver.back()

            # 첫번째 항목의 SMS 발송 버튼 클릭
            # sms_send_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'sms_send_btn')))
            sms_send_btn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "전화 걸기")
            sms_send_btn.click()
            time.sleep(1)

            driver.back()
            driver.back()
            
            # 입소신청서 버튼 클릭
            # application_form_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'application_form_btn')))
            application_form_btn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "입소신청서")
            application_form_btn.click()
            time.sleep(0.5)
            
            # 첫번째 항목의 신청서 승인 버튼 클릭
            # approve_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'approve_btn')))
            approve_btn = driver.find_elements(AppiumBy.ACCESSIBILITY_ID, "신청서 승인")
            if len(approve_btn) > 0:
                approve_btn[0].click()
                time.sleep(0.5)
            else:
                print("신청서 승인 버튼 없음")
                pass
            
            # 두번째 항목의 신청서 거절 버튼 클릭
            # reject_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'reject_btn')))
            reject_btn = driver.find_elements(AppiumBy.ACCESSIBILITY_ID, "신청서 거절")
            if len(reject_btn) > 0:
                reject_btn[0].click()
                time.sleep(0.5)
            else:
                print("신청서 거절 버튼 없음")
                pass

            
            # 진행 버튼 클릭
            progress_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'progress_btn')))
            progress_btn.click()
            time.sleep(0.5)
            
            # (실제 구현에서는 목록 항목들을 확인하는 로직 추가)
            # progress_category_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'closed_btn')))
            progress_category_btn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "진행")
            progress_category_btn.click()
            time.sleep(0.5)

            # 목록에 상태가 진행인 건들만있는지 확인
            list_not_have_text = driver.find_elements(*self._get_locator(driver, 'list_not_have_text'))
            print("진행 상태 목록 확인")
            if len(list_not_have_text) > 0:
                print("진행 상태 목록에 항목 없음")
            else:
                print("진행 상태 목록에 항목 있음")
            
            # 마감 버튼 클릭
            # closed_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'closed_btn')))
            closed_btn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "마감")
            closed_btn.click()
            time.sleep(0.5)

            # 목록에 상태가 마감인 건들만있는지 확인
            list_not_have_text = driver.find_elements(*self._get_locator(driver, 'list_not_have_text'))
            print("마감 상태 목록 확인")
            if len(list_not_have_text) > 0:
                print("마감 상태 목록에 항목 없음")
            else:
                print("마감 상태 목록에 항목 있음")
            
            # 완료 버튼 클릭
            # completed_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'completed_btn')))
            completed_btn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "완료")
            completed_btn.click()
            time.sleep(0.5)
            # 목록에 상태가 완료인 건들만있는지 확인
            list_not_have_text = driver.find_elements(*self._get_locator(driver, 'list_not_have_text'))
            print("완료 상태 목록 확인")
            if len(list_not_have_text) > 0:
                print("완료 상태 목록에 항목 없음")
            else:
                print("완료 상태 목록에 항목 있음")
            
            
            # 뒤로가기 버튼 클릭
            driver.back()
            # time.sleep(0.5)
            
            print("채용모드 입소문의 테스트 완료")
            
        except Exception as e:
            pytest.fail(f"채용모드 입소문의 테스트 실패: {str(e)}")

    """홈화면 → 채용모드 → 채용공고 → 공고 관리 및 등록 테스트"""
    def test_recruitment_mode_job_posting_management(self, driver_setup):
        if isinstance(driver_setup, dict):
            driver = driver_setup['driver']
        else:
            driver = driver_setup
        wait = WebDriverWait(driver, 10)
        
        try:
            # time.sleep(0.5)
            
            # 채용모드 버튼 클릭
            # recruitment_mode_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'recruitment_mode_btn')))
            recruitment_mode_btn = wait.until(EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, "채용모드")))
            # recruitment_mode_btn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "채용모드")
            recruitment_mode_btn.click()
            # time.sleep(0.5)
            
            # 채용공고 버튼 클릭
            job_posting_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'job_posting_btn')))
            job_posting_btn.click()
            # time.sleep(0.5)
            
            # 전체 버튼 클릭
            all_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'all_btn')))
            all_btn.click()
            # time.sleep(0.5)
            
            # 진행 버튼 클릭
            # job_posting_progress_btn1 = wait.until(EC.presence_of_element_located(self._get_locator(driver, 'job_posting_progress_btn1')))

            # print(f"진행버튼이있어서 진행 단일 버튼일 경우 :{job_posting_progress_btn1}")
            # if job_posting_progress_btn1 != False:
            #     job_posting_progress_btn1.click()
            # else:
            job_posting_progress_btn = driver.find_element(*self._get_locator(driver, 'job_posting_progress_btn'))
            job_posting_progress_btn.click()
            print(f"진행버튼이있어서 진행 단일 버튼일 경우 :{job_posting_progress_btn}")
            # time.sleep(0.5)


            list_not_have_text = driver.find_elements(*self._get_locator(driver, 'list_not_have_text'))
            print("진행 상태 목록 확인")
            if len(list_not_have_text) > 0:
                print("진행 상태 목록에 항목 있음")
                # 첫번째 항목 클릭
                # first_item = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'first_facility_item')))
                first_item = driver.find_element(*self._get_locator(driver, 'first_item'))
                first_item.click()
                # time.sleep(0.5)
                # 지원지관리 버튼 클릭
                applicant_management_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'applicant_management_btn')))
                applicant_management_btn.click()
                # time.sleep(0.5)
                
                # 뒤로가기 버튼 클릭
                driver.back()
            else:
                print("진행 상태 목록에 항목 없음")
            
            # 마감버튼 클릭
            closed_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'closed_btn')))
            closed_btn.click()
            # time.sleep(0.5)
            

            list_not_have_text = driver.find_elements(*self._get_locator(driver, 'list_not_have_text'))
            print("마감 상태 목록 확인")
            if len(list_not_have_text) > 0:
                print("마감 상태 목록에 항목 있음")
                # 첫번째 항목 클릭
                # first_item = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'first_facility_item')))
                first_item = driver.find_element(*self._get_locator(driver, 'first_item'))
                first_item.click()
                # time.sleep(0.5)
                
                # 복사하기 버튼 클릭
                copy_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'copy_btn')))
                copy_btn.click()
                # time.sleep(0.5)
                
                # 스크롤 내려서 다음 단계 버튼 클릭 (3번)
                for i in range(3):
                    driver.find_element(
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiScrollable(new UiSelector().scrollable(true)).scrollIntoView(new UiSelector().textContains("다음 단계"));'
                    )
                    next_step_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'next_step_btn')))
                    next_step_btn.click()
                    # time.sleep(0.5)
                
                # 1개월 버튼 클릭
                one_month_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'one_month_btn')))
                one_month_btn.click()
                # time.sleep(0.5)
                
                # 채용제목 인풋에있던 텍스트 뒤에 오늘 날짜 넣기
                from datetime import datetime
                today = datetime.now().strftime("%Y%m%d")
                job_title_input = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'job_title_input')))
                current_text = job_title_input.text
                job_title_input.clear()
                job_title_input.send_keys(f"{current_text} {today}")
                # time.sleep(0.5)
                
                # 다음 단계 버튼 클릭
                next_step_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'next_step_btn')))
                next_step_btn.click()
                # time.sleep(0.5)
                
                # 공고 등록 완료 버튼 클릭
                job_registration_complete_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'job_registration_complete_btn')))
                job_registration_complete_btn.click()
                # time.sleep(0.5)
                
                # 전체동의 체크박스 클릭
                all_agree_checkbox = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'all_agree_checkbox')))
                all_agree_checkbox.click()
                # time.sleep(0.5)
                
                # 확인 버튼 클릭
                confirm_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'confirm_btn')))
                confirm_btn.click()
                # time.sleep(0.5)
            else:
                print("마감 상태 목록에 항목 없음")
            
            driver.back()

            print("채용공고 관리 테스트 완료")
            
        except Exception as e:
            pytest.fail(f"채용공고 관리 테스트 실패: {str(e)}")
    
    """홈화면 → 채용모드 → 사회복지사/요양보호사 새로고침 → 더보기 → 소개보기 테스트"""
    def test_service_category_refresh_and_intro(self, driver_setup):
        if isinstance(driver_setup, dict):
            driver = driver_setup['driver']
        else:
            driver = driver_setup
        wait = WebDriverWait(driver, 10)
        
        try:
            # time.sleep(0.5)
            
            # 채용모드 버튼 클릭
            # recruitment_mode_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'recruitment_mode_btn')))
            recruitment_mode_btn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "채용모드")
            recruitment_mode_btn.click()
            
            driver.find_element(
                AppiumBy.ANDROID_UIAUTOMATOR,
                'new UiScrollable(new UiSelector().scrollable(true).instance(0))'
                '.scrollIntoView(new UiSelector().textContains("사회복지사").instance(0));'
            )
            
            # 사회복지사 버튼 클릭
            # social_worker_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'social_worker_btn')))
            social_worker_btn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "사회복지사")
            social_worker_btn.click()
            
            # 새로고침 버튼 클릭
            refresh_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'refresh_btn')))
            refresh_btn.click()
            # 목록에 항목이 나오는지 확인
            list_not_have_text = driver.find_elements(*self._get_locator(driver, 'list_not_have_text'))
            print("목록 항목 확인")
            if len(list_not_have_text) > 0:
                print("목록에 항목 없음")
            else:
                print("목록에 항목 있음")
            
            # 요양보호사 버튼 클릭
            # care_worker_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'care_worker_btn')))
            care_worker_btn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "요양보호사")
            care_worker_btn.click()
            
            # 새로고침 버튼 클릭
            refresh_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'refresh_btn')))
            refresh_btn.click()
            # 목록에 항목이 나오는지 확인
            list_not_have_text = driver.find_elements(*self._get_locator(driver, 'list_not_have_text'))
            print("목록 항목 확인")
            if len(list_not_have_text) > 0:
                print("목록에 항목 없음")
            else:
                print("목록에 항목 있음")
            
            # 홈 버튼 클릭
            # home_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'home_btn')))
            home_btn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "홈")
            home_btn.click()
            
            befor_more_btn = wait.until(EC.presence_of_element_located(self._get_locator(driver, 'befor_more_btn')))
            print(f"더보기 버튼 클릭전 {befor_more_btn}")
            # 더보기 버튼 클릭
            # more_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'more_btn')))
            if befor_more_btn != False:
                more_btn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "더보기")
                more_btn.click()

                # 목록에 항목이 나오는지 확인
                list_not_have_text = driver.find_elements(*self._get_locator(driver, 'list_not_have_text'))
                print("목록 항목 확인")
                if len(list_not_have_text) > 0:
                    print("목록에 항목 없음")
                else:
                    print("목록에 항목 있음")
                
                # 뒤로가기 버튼 클릭
                driver.back()
            
            
            # 소개보기 버튼 클릭
            # intro_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'intro_btn')))
            intro_btn = driver.find_elements(AppiumBy.ACCESSIBILITY_ID, '소개보기')
            intro_btn[0].click()
            
            if len(intro_btn) == 0:
                # 다시 앱으로 돌아오기
                driver.back()

            # 뒤로가기 버튼 클릭
            driver.back()
            
            print("서비스 카테고리 새로고침 및 소개보기 테스트 완료")
            
        except Exception as e:
            pytest.fail(f"서비스 카테고리 새로고침 및 소개보기 테스트 실패: {str(e)}")