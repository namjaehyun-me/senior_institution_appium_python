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
                # 마이페이지 관련 로케이터
                'bottom_my_page_btn': (AppiumBy.XPATH, '//android.widget.TextView[@text="마이 페이지"]'),
                'my_info_management_btn': (AppiumBy.XPATH, '//android.widget.TextView[@text="내 정보관리"]'),
                'detail_address_input': (AppiumBy.XPATH, '//android.widget.EditText[@text="2층"]'),
                'keyborad_hied': (AppiumBy.XPATH, '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup'),
                'save_btn': (AppiumBy.XPATH, '//android.widget.TextView[@text="저장"]'),
                'toast_message': (AppiumBy.XPATH, '//android.view.ViewGroup[@resource-id="toastAnimatedContainer"]/android.view.ViewGroup'),
                # 'toast_message': (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.view.ViewGroup").instance(54)'),
                'family_info_management_btn': (AppiumBy.XPATH, '//android.widget.TextView[@text="내 가족 정보 관리"]'),
                'register_btn': (AppiumBy.XPATH, '//android.widget.TextView[@text="등록하기"]'),
                'name_input': (AppiumBy.XPATH, '//android.widget.EditText[@text="대상자의 이름을 입력하세요"]'),
                # 'birth_date_btn': (AppiumBy.XPATH, '//android.widget.EditText[@text="날짜 선택"]'),
                # 'birth_date_btn': (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("날짜 선택")'),
                'birth_date_btn': (AppiumBy.XPATH, '//android.widget.HorizontalScrollView/android.view.ViewGroup/android.view.ViewGroup[3]'),
                # 'birth_date_btn': (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.view.ViewGroup").instance(19)'),
                'year_1992': (AppiumBy.XPATH, '//android.widget.TextView[@text="1992"]'),
                'month_1': (AppiumBy.XPATH, '//android.widget.TextView[@text="1월"]'),
                'day_21': (AppiumBy.XPATH, '//android.widget.TextView[@text="21"]'),
                'confirm_btn': (AppiumBy.XPATH, '//android.widget.Button[@resource-id="android:id/button1"]'),
                'pay_ment_confirm_btn': (AppiumBy.XPATH, '//android.widget.Button[@text="확인"]'),
                'relationship_dropdown': (AppiumBy.XPATH, '(//android.view.ViewGroup[@content-desc="선택"])[1]'),
                'other_option': (AppiumBy.XPATH, '//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[3]'),
                'grade_dropdown': (AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="선택"]'),
                'grade_4': (AppiumBy.XPATH, '//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[3]'),
                'male_checkbox': (AppiumBy.XPATH, '//android.widget.TextView[@text="남성"]'),
                'height_input': (AppiumBy.XPATH, '//android.widget.EditText[@text="키"]'),
                'weight_input': (AppiumBy.XPATH, '//android.widget.EditText[@text="진단명을 입력하세요"]'),
                'no_diagnosis_btn': (AppiumBy.XPATH, '//android.widget.TextView[@text="해당없음"]'),
                'symptom_input': (AppiumBy.XPATH, '//android.widget.EditText[@text="대상자의 증상을 입력해 주세요"]'),
                'self_walking_checkbox': (AppiumBy.XPATH, '//android.widget.TextView[@text="자가보행"]'),
                'admission_support_btn': (AppiumBy.XPATH, '//android.widget.TextView[@text="입소지원서 작성"]'),
                'plus_btn': (AppiumBy.XPATH, '//android.widget.HorizontalScrollView/android.view.ViewGroup/android.view.ViewGroup[2]'),
                'jongro_checkbox': (AppiumBy.XPATH, '//android.widget.TextView[@text="종로구"]'),
                'jung_checkbox': (AppiumBy.XPATH, '//android.widget.TextView[@text="중구"]'),
                'yongsan_checkbox': (AppiumBy.XPATH, '//android.widget.TextView[@text="용산구"]'),
                'selection_complete_btn': (AppiumBy.XPATH, '//android.widget.TextView[@text="선택완료"]'),
                'size_10_59_btn': (AppiumBy.XPATH, '//android.widget.TextView[@text="10~59인"]'),
                'nature_friendly_btn': (AppiumBy.XPATH, '//android.widget.TextView[@text="자연친화"]'),
                'urban_type_btn': (AppiumBy.XPATH, '//android.widget.TextView[@text="도심형"]'),
                'physical_therapy_btn': (AppiumBy.XPATH, '//android.widget.TextView[@text="물리치료실"]'),
                'gym_btn': (AppiumBy.XPATH, '//android.widget.TextView[@text="헬스장"]'),
                'monthly_stay_btn': (AppiumBy.XPATH, '//android.widget.TextView[@text="한달살기"]'),
                'accept_checkbox': (AppiumBy.XPATH, '//android.widget.TextView[@text="수락"]'),
                'privacy_consent_checkbox': (AppiumBy.XPATH, '//android.widget.HorizontalScrollView/android.view.ViewGroup/android.view.ViewGroup[15]/android.view.ViewGroup[1]'),
                'complete_btn': (AppiumBy.XPATH, '//android.widget.TextView[@text="작성완료"]'),
                'first_item_checkbox': (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.view.ViewGroup").instance(21)'),
                'delete_btn': (AppiumBy.XPATH, '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup[4]'),
                'proceed_btn': (AppiumBy.XPATH, '//android.widget.TextView[@text="진행"]'),
                'back_btn': (AppiumBy.XPATH, '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]'),
                'payment_history_btn': (AppiumBy.XPATH, '//android.widget.TextView[@text="결제내역"]'),
                'first_payment_item': (AppiumBy.XPATH, '//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[1]'),
                'service_detail_btn': (AppiumBy.XPATH, '//android.widget.TextView[@text="서비스내용 상세보기"]'),
                'no_problem_btn': (AppiumBy.XPATH, '//android.widget.TextView[@text="이상없음"]'),
                # 추가 마이페이지 로케이터
                'admission_proposal_btn': (AppiumBy.XPATH, '//android.widget.TextView[@text="입소제안"]'),
                'first_proposal_item': (AppiumBy.XPATH, '(//android.view.ViewGroup[@clickable="true"])[1]'),
                'come_first_proposal_item': (AppiumBy.XPATH, '//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[2]'),
                'admission_support_update_btn': (AppiumBy.XPATH, '//android.widget.TextView[@text="입소지원서 업데이트"]'),
                'proposal_setting_btn': (AppiumBy.XPATH, '//android.widget.TextView[@text="입소 제안 설정"]'),
                'third_checkbox': (AppiumBy.XPATH, '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup[3]'),
                'setting_complete_btn': (AppiumBy.XPATH, '//android.widget.TextView[@text="설정완료"]'),
                'favorite_institutions_btn': (AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="관심기관"]'),
                'first_heart_btn': (AppiumBy.XPATH, '(//android.view.ViewGroup[@content-desc="하트"])[1]'),
                'certificate_btn': (AppiumBy.XPATH, '//android.widget.TextView[@text="증명서 발급"]'),
                'download_btn': (AppiumBy.XPATH, '//android.widget.TextView[@text="다운받기"]'),
                'notice_btn': (AppiumBy.XPATH, '//android.widget.TextView[@text="공지사항"]'),
                'first_notice_item': (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.view.ViewGroup").instance(19)'),
                'pay_ment_first_notice_item': (AppiumBy.XPATH, '//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[1]'),
                'error_first_notice_item': (AppiumBy.XPATH, '//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[1]'),
                'event_first_notice_item': (AppiumBy.XPATH, '//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[1]'),
                'fnq_first_notice_item': (AppiumBy.XPATH, '//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[1]'),
                'fnq_first_notice_item2': (AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="2025년 하반기 시스템 통합 업데이트 사전 안내"]'),
                'faq_btn': (AppiumBy.XPATH, '//android.widget.TextView[@text="자주 묻는 질문"]'),
                'faq_search_input': (AppiumBy.XPATH, '//android.widget.EditText[@text="궁금한 내용을 검색하세요"]'),
                'event_btn': (AppiumBy.XPATH, '//android.widget.TextView[@text="이벤트"]'),
                'customer_center_btn': (AppiumBy.XPATH, '//android.widget.TextView[@text="고객센터"]'),
                'error_report_btn': (AppiumBy.XPATH, '//android.widget.TextView[@text="오류신고센터"]'),
                'category_dropdown': (AppiumBy.XPATH, '//android.widget.Spinner'),
                'service_error_option': (AppiumBy.XPATH, '//android.widget.TextView[@text="서비스신청오류"]'),
                'title_input': (AppiumBy.XPATH, '//android.widget.EditText[@text="제목을 기재해 주세요"]'),
                'opinion_input': (AppiumBy.XPATH, '//android.widget.EditText[@text="의견을 자유롭게 기재해주세요."]'),
                'report_btn': (AppiumBy.XPATH, '//android.widget.TextView[@text="신고하기"]'),
                'list_btn': (AppiumBy.XPATH, '//android.widget.TextView[@text="목록"]'),
                'delete_report_btn': (AppiumBy.XPATH, '//android.widget.TextView[@text="삭제하기"]'),
                'error_report_create_btn': (AppiumBy.XPATH, '//android.widget.TextView[@text="오류신고하기"]'),
                'customer_inquiry_btn': (AppiumBy.XPATH, '//android.widget.TextView[@text="고객센터 문의하기"]'),
                'my_report_history_btn': (AppiumBy.XPATH, '//android.widget.TextView[@text="내 신고내역"]'),
                'learning_materials_btn': (AppiumBy.XPATH, '//android.widget.TextView[@text="학습자료실"]'),
                'product_purchase_btn': (AppiumBy.XPATH, '//android.widget.TextView[@text="상품구매"]'),
                'purchase_btn': (AppiumBy.XPATH, '//android.widget.TextView[@text="구매하기"]'),
                'payment_method_dropdown': (AppiumBy.XPATH, '//android.widget.Spinner'),
                'bank_transfer_option': (AppiumBy.XPATH, '//android.widget.TextView[@text="실시간 계좌이체"]'),
                'agree_all_checkbox': (AppiumBy.XPATH, '//android.widget.TextView[@text="전체동의"]'),
                'next_btn': (AppiumBy.XPATH, '//android.widget.TextView[@text="다음"]'),
                'pay_ment_next_btn': (AppiumBy.XPATH, '//android.widget.Button[@text="다음"]'),
                'phone_input': (AppiumBy.XPATH, '//android.widget.EditText[@text="010"]'),
                'number_5': (AppiumBy.XPATH, '//android.widget.Button[@content-desc="5"]'),
                'number_2': (AppiumBy.XPATH, '//android.widget.Button[@content-desc="2"]'),
                'number_8': (AppiumBy.XPATH, '//android.widget.Button[@content-desc="8"]'),
                'number_9': (AppiumBy.XPATH, '//android.widget.Button[@content-desc="9"]'),
                'number_7': (AppiumBy.XPATH, '//android.widget.Button[@content-desc="7"]'),
                'agree_payment_btn': (AppiumBy.XPATH, '//android.widget.Button[@text="동의하고 결제하기"]'),
                'bottom_favorite_institutions_btn': (AppiumBy.XPATH, '//android.widget.TextView[@text="관심기관"]'),
                'first_favorite_heart_btn': (AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="숲데이케어센터, 2018.04.19, 60 명 정원, 서울 동작구 상도로68길 1-20"]/android.view.ViewGroup[2]/android.view.ViewGroup'),
                'toast_message': (AppiumBy.XPATH, '//android.view.ViewGroup[@resource-id="toastAnimatedContainer"]'),
                'hanmaeum_nursing_home_name': (AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="재가복지센터, 숲데이케어센터, 서울 동작구 상도로68길 1-20"]/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup'),
                'search_input': (AppiumBy.XPATH, '//android.widget.EditText[@text="검색"]'),
                'search_icon_btn': (AppiumBy.XPATH, '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]'),
                'loction_access_modal': (AppiumBy.XPATH, '//android.widget.Button[@resource-id="com.android.permissioncontroller:id/permission_allow_foreground_only_button"]'),
                'category_button1': (AppiumBy.XPATH, '//android.widget.ImageView'),
                'category_button2': (AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="시작하기"]/android.view.ViewGroup'),
                'list_item': (AppiumBy.XPATH, '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[1]'),
                'list_item_youtube': (AppiumBy.XPATH, '//android.widget.Button[@text="Play video"]'),
                # 새로운 시나리오 로케이터들
                'bottom_matching_management_btn': (AppiumBy.XPATH, '//android.widget.TextView[@text="채용 공고"]'),
                'region_btn': (AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="지역"]'),
                'jung_gu_checkbox': (AppiumBy.XPATH, '//android.widget.TextView[@text="중구"]'),
                'jongro_gu_checkbox': (AppiumBy.XPATH, '//android.widget.TextView[@text="종로구"]'),
                'yongsan_gu_checkbox': (AppiumBy.XPATH, '//android.widget.TextView[@text="용산구"]'),
                'gwangjin_gu_checkbox': (AppiumBy.XPATH, '//android.widget.TextView[@text="광진구"]'),
                'selection_complete_btn_final': (AppiumBy.XPATH, '//android.widget.TextView[@text="선택완료"]'),
                # 채용공고 관련 로케이터들
                'bottom_job_notice_btn': (AppiumBy.XPATH, '//android.widget.TextView[@text="채용 공고"]'),
                'home_btn': (AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="홈"]'),
                'intro_btn': (AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="소개보기"]'),
                # 'more_btn': (AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="더보기"]'),
                'more_btn': (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().description("더보기")'),
                'first_job_item': (AppiumBy.XPATH, '//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[1]'),
                # 'first_job_item': (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.view.ViewGroup").instance(31)'),
                'first_job_item_not_found': (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("데이터를 찾을 수 없습니다")'),
                'home_first_job_item': (AppiumBy.XPATH, '//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[1]'),
                'socialworker_first_job_item': (AppiumBy.XPATH, '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[4]/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[2]'),
                'nursingcareworker_first_job_item': (AppiumBy.XPATH, '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[4]/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[2]'),
                'apply_btn': (AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="지원하기"]'),
                'modal_apply_btn': (AppiumBy.XPATH, '(//android.view.ViewGroup[@content-desc="지원하기"])[1]'),
                'modal_applys': (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("이미 지원한 공고입니다!")'),
                'send_msg_modal_applys': (AppiumBy.XPATH, '(//android.view.ViewGroup[@content-desc="지원하기"])[1]'),
                'send_msg_modal_comfirm_input': (AppiumBy.XPATH, '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup[3]/android.view.ViewGroup[1]'),
                'send_msg_modal_comfirm_input2': (AppiumBy.CLASS_NAME, 'android.widget.EditText'),
                'send_msg_modal_comfirm_btn': (AppiumBy.XPATH, '//android.widget.TextView[@text="보호자님께 전하고\n싶은 한마디를 작성해 주세요"]'),
                'desired_hourly_wage_btn': (AppiumBy.XPATH, '//android.widget.TextView[@text="희망하는 시급을 보호자에게 제안하세요"]'),
                'send_desired_hourly_wage': (AppiumBy.XPATH, '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup[3]/android.view.ViewGroup[1]'),
                'send_desired_hourly_wage2': (AppiumBy.XPATH, '//android.widget.EditText'),
                # 'send_desired_hourly_wage2': (AppiumBy.CLASS_NAME, 'android.widget.EditText'),
                'resume_view_btn': (AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="이력서 보기"]'),
                'back_btn_general': (AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="뒤로가기"]'),
                'social_worker_btn': (AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="사회복지사"]'),
                'care_housekeeping_companion_btn': (AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="간병/가사/동행"]'),
                'caregiver_btn': (AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="간병"]'),
                'housekeeping_btn': (AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="가사돌봄"]'),
                'companion_btn': (AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="동행"]'),
                'modal_content': (AppiumBy.XPATH, '//android.widget.TextView'),
                'modal_confirm_btn': (AppiumBy.XPATH, '//android.widget.Button[@text="확인"]'),
                'salary_input': (AppiumBy.XPATH, '//android.widget.EditText[@text="희망 시급을 입력하세요"]'),
                'background_click': (AppiumBy.XPATH, '//android.view.ViewGroup[@resource-id="android:id/content"]'),
                'loction_access_modal': (AppiumBy.XPATH, '//android.widget.Button[@resource-id="com.android.permissioncontroller:id/permission_allow_foreground_only_button"]'),
            },
            'ios': {
                # 마이페이지 관련 로케이터
                'bottom_my_page_btn': (AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='마이페이지']"),
                'my_info_management_btn': (AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='내 정보관리']"),
                'detail_address_input': (AppiumBy.XPATH, "//XCUIElementTypeTextField[@name='상세주소']"),
                'keyborad_hied': (AppiumBy.XPATH, "//XCUIElementTypeTextField[@name='상세주소']"),
                'save_btn': (AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='저장']"),
                'toast_message': (AppiumBy.XPATH, "//XCUIElementTypeStaticText"),
                'family_info_management_btn': (AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='내 가족 정보 관리']"),
                'register_btn': (AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='등록하기']"),
                'name_input': (AppiumBy.XPATH, "//XCUIElementTypeTextField[@name='이름을 입력하세요']"),
                'birth_date_btn': (AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='생년월일']"),
                'year_1992': (AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='1992']"),
                'month_1': (AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='1월']"),
                'day_21': (AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='21']"),
                'confirm_btn': (AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='확인']"),
                'pay_ment_confirm_btn': (AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='확인']"),
                'relationship_dropdown': (AppiumBy.XPATH, "//XCUIElementTypePicker"),
                'other_option': (AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='기타']"),
                'grade_dropdown': (AppiumBy.XPATH, "//XCUIElementTypePicker"),
                'grade_4': (AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='4등급']"),
                'male_checkbox': (AppiumBy.XPATH, "//XCUIElementTypeButton[@name='남성']"),
                'height_input': (AppiumBy.XPATH, "//XCUIElementTypeTextField[@name='키']"),
                'weight_input': (AppiumBy.XPATH, "//XCUIElementTypeTextField[@name='몸무게']"),
                'no_diagnosis_btn': (AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='해당없음']"),
                'symptom_input': (AppiumBy.XPATH, "//XCUIElementTypeTextField[@name='상세 증상 기재']"),
                'self_walking_checkbox': (AppiumBy.XPATH, "//XCUIElementTypeButton[@name='자가보행']"),
                'admission_support_btn': (AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='입소지원서 작성']"),
                'plus_btn': (AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='+']"),
                'jongro_checkbox': (AppiumBy.XPATH, "//XCUIElementTypeButton[@name='종로구']"),
                'jung_checkbox': (AppiumBy.XPATH, "//XCUIElementTypeButton[@name='중구']"),
                'yongsan_checkbox': (AppiumBy.XPATH, "//XCUIElementTypeButton[@name='용산구']"),
                'selection_complete_btn': (AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='선택완료']"),
                'size_10_59_btn': (AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='10~59인']"),
                'nature_friendly_btn': (AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='자연친화']"),
                'urban_type_btn': (AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='도심형']"),
                'physical_therapy_btn': (AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='물리치료실']"),
                'gym_btn': (AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='헬스장']"),
                'monthly_stay_btn': (AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='한달살기']"),
                'accept_checkbox': (AppiumBy.XPATH, "//XCUIElementTypeButton[@name='수락']"),
                'privacy_consent_checkbox': (AppiumBy.XPATH, "//XCUIElementTypeButton[@name='필수 항목에 대한 개인정보 수집 및 이용 동의']"),
                'complete_btn': (AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='작성완료']"),
                'first_item_checkbox': (AppiumBy.XPATH, "(//XCUIElementTypeButton[@name='체크박스'])[1]"),
                'delete_btn': (AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='삭제']"),
                'proceed_btn': (AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='진행']"),
                'back_btn': (AppiumBy.XPATH, "//XCUIElementTypeButton[@name='뒤로가기']"),
                'payment_history_btn': (AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='결제내역']"),
                'first_payment_item': (AppiumBy.XPATH, "(//XCUIElementTypeCell)[1]"),
                'service_detail_btn': (AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='서비스내용 상세보기']"),
                'no_problem_btn': (AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='이상없음']"),
                # 추가 마이페이지 로케이터
                'admission_proposal_btn': (AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='입소제안']"),
                'first_proposal_item': (AppiumBy.XPATH, "(//XCUIElementTypeCell)[1]"),
                'admission_support_update_btn': (AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='입소지원서 업데이트']"),
                'proposal_setting_btn': (AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='입소 제안 설정']"),
                'third_checkbox': (AppiumBy.XPATH, "(//XCUIElementTypeButton[@name='체크박스'])[3]"),
                'setting_complete_btn': (AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='설정완료']"),
                'favorite_institutions_btn': (AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='관심기관']"),
                'first_heart_btn': (AppiumBy.XPATH, "(//XCUIElementTypeButton[@name='하트'])[1]"),
                'certificate_btn': (AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='증명서 발급']"),
                'download_btn': (AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='다운받기']"),
                'notice_btn': (AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='공지사항']"),
                'first_notice_item': (AppiumBy.XPATH, "(//XCUIElementTypeCell)[1]"),
                'pay_ment_first_notice_item': (AppiumBy.XPATH, "(//XCUIElementTypeCell)[1]"),
                'error_first_notice_item': (AppiumBy.XPATH, "(//XCUIElementTypeCell)[1]"),
                'event_first_notice_item': (AppiumBy.XPATH, "(//XCUIElementTypeCell)[1]"),
                'fnq_first_notice_item': (AppiumBy.XPATH, "(//XCUIElementTypeCell)[1]"),
                'faq_btn': (AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='자주 묻는 질문']"),
                'faq_search_input': (AppiumBy.XPATH, "//XCUIElementTypeTextField[@name='검색']"),
                'event_btn': (AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='이벤트']"),
                'customer_center_btn': (AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='고객센터']"),
                'error_report_btn': (AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='오류신고센터']"),
                'category_dropdown': (AppiumBy.XPATH, "//XCUIElementTypePicker"),
                'service_error_option': (AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='서비스신청오류']"),
                'title_input': (AppiumBy.XPATH, "//XCUIElementTypeTextField[@name='제목']"),
                'opinion_input': (AppiumBy.XPATH, "//XCUIElementTypeTextField[@name='사용자님의 의견']"),
                'report_btn': (AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='신고하기']"),
                'list_btn': (AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='목록']"),
                'delete_report_btn': (AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='삭제하기']"),
                'error_report_create_btn': (AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='오류신고하기']"),
                'customer_inquiry_btn': (AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='고객센터 문의하기']"),
                'my_report_history_btn': (AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='내 신고내역']"),
                'learning_materials_btn': (AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='학습자료실']"),
                'product_purchase_btn': (AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='상품구매']"),
                'purchase_btn': (AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='구매하기']"),
                'payment_method_dropdown': (AppiumBy.XPATH, "//XCUIElementTypePicker"),
                'bank_transfer_option': (AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='실시간 계좌이체']"),
                'agree_all_checkbox': (AppiumBy.XPATH, "//XCUIElementTypeButton[@name='전체동의']"),
                'next_btn': (AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='다음']"),
                'pay_ment_next_btn': (AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='다음']"),
                'phone_input': (AppiumBy.XPATH, "//XCUIElementTypeTextField"),
                'number_5': (AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='5']"),
                'number_2': (AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='2']"),
                'number_8': (AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='8']"),
                'number_9': (AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='9']"),
                'number_7': (AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='7']"),
                'agree_payment_btn': (AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='동의하고 결제하기']"),
                'bottom_favorite_institutions_btn': (AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='관심기관']"),
                'first_favorite_heart_btn': (AppiumBy.XPATH, "(//XCUIElementTypeButton[@name='하트'])[1]"),
                'toast_message': (AppiumBy.XPATH, "//XCUIElementTypeStaticText"),
                'hanmaeum_nursing_home_name': (AppiumBy.XPATH, "//XCUIElementTypeStaticText"),
                'search_input': (AppiumBy.XPATH, "//XCUIElementTypeTextField[@name='검색']"),
                'search_icon_btn': (AppiumBy.XPATH, "//XCUIElementTypeButton[@name='검색']"),
                'loction_access_modal': (AppiumBy.XPATH, "//XCUIElementTypeButton[@name='허용']"),
                'category_button1': (AppiumBy.XPATH, "//XCUIElementTypeButton[@name='허용']"),
                'category_button2': (AppiumBy.XPATH, "//XCUIElementTypeButton[@name='허용']"),
                'list_item': (AppiumBy.XPATH, "//XCUIElementTypeButton[@name='허용']"),
                'list_item_youtube': (AppiumBy.XPATH, "//XCUIElementTypeButton[@name='허용']"),
                # 새로운 시나리오 로케이터들
                'bottom_matching_management_btn': (AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='매칭 관리']"),
                'region_btn': (AppiumBy.XPATH, "//XCUIElementTypeButton[@name='지역']"),
                'jung_gu_checkbox': (AppiumBy.XPATH, "//XCUIElementTypeButton[@name='중구']"),
                'jongro_gu_checkbox': (AppiumBy.XPATH, "//XCUIElementTypeButton[@name='종로구']"),
                'yongsan_gu_checkbox': (AppiumBy.XPATH, "//XCUIElementTypeButton[@name='용산구']"),
                'gwangjin_gu_checkbox': (AppiumBy.XPATH, "//XCUIElementTypeButton[@name='광진구']"),
                'selection_complete_btn_final': (AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='선택완료']"),
                # 채용공고 관련 로케이터들
                'bottom_job_notice_btn': (AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='채용 공고']"),
                'home_btn': (AppiumBy.XPATH, "//XCUIElementTypeButton[@name='홈']"),
                'intro_btn': (AppiumBy.XPATH, "//XCUIElementTypeButton[@name='소개보기']"),
                'more_btn': (AppiumBy.XPATH, "//XCUIElementTypeButton[@name='더보기']"),
                'first_job_item': (AppiumBy.XPATH, "(//XCUIElementTypeCell)[1]"),
                'home_first_job_item': (AppiumBy.XPATH, "(//XCUIElementTypeCell)[1]"),
                'socialworker_first_job_item': (AppiumBy.XPATH, "(//XCUIElementTypeCell)[1]"),
                'nursingcareworker_first_job_item': (AppiumBy.XPATH, "(//XCUIElementTypeCell)[1]"),
                'apply_btn': (AppiumBy.XPATH, "//XCUIElementTypeButton[@name='지원하기']"),
                'modal_apply_btn': (AppiumBy.XPATH, "//XCUIElementTypeButton[@name='지원하기']"),
                'modal_applys': (AppiumBy.XPATH, "//XCUIElementTypeButton[@name='지원하기']"),
                'send_msg_modal_applys': (AppiumBy.XPATH, "//XCUIElementTypeButton[@name='지원하기']"),
                'send_msg_modal_comfirm_input': (AppiumBy.XPATH, "//XCUIElementTypeButton[@name='지원하기']"),
                'send_msg_modal_comfirm_input2': (AppiumBy.XPATH, "//XCUIElementTypeButton[@name='지원하기']"),
                'send_msg_modal_comfirm_btn': (AppiumBy.XPATH, "//XCUIElementTypeButton[@name='지원하기']"),
                'desired_hourly_wage_btn': (AppiumBy.XPATH, "//XCUIElementTypeButton[@name='지원하기']"),
                'send_desired_hourly_wage': (AppiumBy.XPATH, "//XCUIElementTypeButton[@name='지원하기']"),
                'send_desired_hourly_wage2': (AppiumBy.XPATH, "//XCUIElementTypeButton[@name='지원하기']"),
                'resume_view_btn': (AppiumBy.XPATH, "//XCUIElementTypeButton[@name='이력서 보기']"),
                'back_btn_general': (AppiumBy.XPATH, "//XCUIElementTypeButton[@name='뒤로가기']"),
                'social_worker_btn': (AppiumBy.XPATH, "//XCUIElementTypeButton[@name='사회복지사']"),
                'care_housekeeping_companion_btn': (AppiumBy.XPATH, "//XCUIElementTypeButton[@name='간병/가사/동행']"),
                'caregiver_btn': (AppiumBy.XPATH, "//XCUIElementTypeButton[@name='간병']"),
                'housekeeping_btn': (AppiumBy.XPATH, "//XCUIElementTypeButton[@name='가사돌봄']"),
                'companion_btn': (AppiumBy.XPATH, "//XCUIElementTypeButton[@name='동행']"),
                'modal_content': (AppiumBy.XPATH, "//XCUIElementTypeStaticText"),
                'modal_confirm_btn': (AppiumBy.XPATH, "//XCUIElementTypeButton[@name='확인']"),
                'salary_input': (AppiumBy.XPATH, "//XCUIElementTypeTextField[@name='희망 시급']"),
                'background_click': (AppiumBy.XPATH, "//XCUIElementTypeApplication"),
                'loction_access_modal': (AppiumBy.XPATH, "//XCUIElementTypeApplication"),
                # =============================================================
            }
        }
        
        return locators[platform][element_name]

    def test_comprehensive_job_application_flow(self, driver_setup):
        """홈화면 → 바텀 메뉴에서 채용 공고 클릭 → 홈 버튼 클릭 → 소개보기 → 더보기 → 각 카테고리별 지원하기 테스트"""
        if isinstance(driver_setup, dict):
            driver = driver_setup['driver']
        else:
            driver = driver_setup
        wait = WebDriverWait(driver, 10)
        
        try:
            time.sleep(2)
            
            # 바텀 메뉴에서 채용 공고 클릭
            bottom_job_notice_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'bottom_job_notice_btn')))
            bottom_job_notice_btn.click()
            time.sleep(0.5)
            
            loction_access_modal = driver.find_elements(*self._get_locator(driver, 'loction_access_modal'))
            print(f"채용홈 위치 권한 모달 개수: {len(loction_access_modal)}")
            # 채용홈 위치 권한 모달
            if len(loction_access_modal) == 1:
                print("채용홈 위치 권한 모달 표시됨")
                loction_access_modal[0].click()
                print("채용홈 위치 권한 모달 클릭됨")
                time.sleep(1)
            
            # 소개보기 버튼 클릭
            intro_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'intro_btn')))
            intro_btn = driver.find_elements(AppiumBy.ACCESSIBILITY_ID, '소개보기')
            intro_btn[0].click()
            time.sleep(1)
            
            if len(intro_btn) == 0:
                # 다시 앱으로 돌아오기
                driver.back()
                time.sleep(0.5)
            
            # 더보기 버튼 클릭
            time.sleep(5)
            more_btn = driver.find_element(*self._get_locator(driver, 'more_btn'))
            more_btn.click()
            time.sleep(0.5)
            
            # 첫번째 항목 클릭
            home_first_job_item = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'home_first_job_item')))
            home_first_job_item.click()
            time.sleep(0.5)
            
            # 공고의 지원하기
            # apply_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'apply_btn')))
            apply_btn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, '지원하기')
            apply_btn.click()
            time.sleep(0.5)
            
            # 이력서 보기 버튼 클릭
            # resume_view_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'resume_view_btn')))
            resume_view_btn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, '이력서 보기')
            resume_view_btn.click()
            time.sleep(0.5)
            
            # 뒤로가기 버튼 클릭
            driver.back()
            
            # 지원하기 버튼 클릭
            apply_btn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, '지원하기')
            apply_btn.click()
            time.sleep(0.5)
            
            # 이력서 있음 모달의 지원하기
            modal_apply_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'modal_apply_btn')))
            modal_apply_btn.click()
            time.sleep(0.5)
            
            # 이미 지원한 공고 모달
            print(f"이미 지원한 공고 모달 시작전{self._get_locator(driver, 'modal_applys')}")
            modal_applys = driver.find_elements(*self._get_locator(driver, 'modal_applys'))
            print(f"이미 지원한 공고 모달 개수: {len(modal_applys)}")
            if len(modal_applys) == 1:
                confirm = driver.find_element(AppiumBy.ACCESSIBILITY_ID, '확인')
                confirm.click()
                time.sleep(0.5)
            else:
                pass

            # 뒤로가기 버튼 클릭 (한 번)
            driver.back()
            
            # 사회복지사 버튼 클릭
            # social_worker_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'social_worker_btn')))
            social_worker_btn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, '사회복지사')
            social_worker_btn.click()
            time.sleep(0.5)
            
            # 첫번째 항목 클릭
            socialworker_first_job_item = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'socialworker_first_job_item')))
            socialworker_first_job_item.click()
            time.sleep(0.5)

            # 공고의 지원하기
            apply_btn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, '지원하기')
            apply_btn.click()
            time.sleep(0.5)

            # 지원하기 버튼 클릭
            apply_btn2 = driver.find_element(AppiumBy.ACCESSIBILITY_ID, '지원하기')
            apply_btn2.click()
            time.sleep(0.5)

            # 이미 지원한 공고 모달
            modal_applys = driver.find_elements(*self._get_locator(driver, 'modal_applys'))
            if len(modal_applys) == 1:
                confirm = driver.find_element(AppiumBy.ACCESSIBILITY_ID, '확인')
                confirm.click()
                time.sleep(0.5)
            else:
                pass

            # 요양보호사
            nursingcareworker_btn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, '요양보호사')
            nursingcareworker_btn.click()
            time.sleep(0.5)
            
            # 첫번째 항목 클릭
            nursingcareworker_first_job_item = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'nursingcareworker_first_job_item')))
            nursingcareworker_first_job_item.click()
            time.sleep(0.5)

            # 공고의 지원하기
            apply_btn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, '지원하기')
            apply_btn.click()
            time.sleep(0.5)

            # 지원하기 버튼 클릭
            apply_btn2 = driver.find_element(AppiumBy.ACCESSIBILITY_ID, '지원하기')
            apply_btn2.click()
            time.sleep(0.5)

            # 이미 지원한 공고 모달
            modal_applys = driver.find_elements(*self._get_locator(driver, 'modal_applys'))
            if len(modal_applys) == 1:
                confirm = driver.find_element(AppiumBy.ACCESSIBILITY_ID, '확인')
                confirm.click()
                time.sleep(0.5)
            else:
                pass
            
            # 간병/가사/동행 버튼 클릭
            # care_housekeeping_companion_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'care_housekeeping_companion_btn')))
            care_housekeeping_companion_btn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, '간병/가사/동행')
            care_housekeeping_companion_btn.click()
            time.sleep(0.5)
            
            # 간병, 가사돌봄, 동행 각각 테스트
            service_buttons = ['caregiver_btn', 'housekeeping_btn', 'companion_btn']
            
            for service_btn in service_buttons:
                # 서비스 버튼 클릭
                service_button = wait.until(EC.element_to_be_clickable(self._get_locator(driver, service_btn)))
                service_button.click()
                time.sleep(0.5)
                
                # 첫번째 항목 클릭
                first_job_item_not_found = driver.find_elements(*self._get_locator(driver, 'first_job_item_not_found'))
                print(f"첫번째 항목 개수: {len(first_job_item_not_found)}")
                if len(first_job_item_not_found) == 0:
                    # first_job_item = driver.find_elements(*self._get_locator(driver, 'first_job_item_not_found'))
                    # first_job_item[0].click()
                    first_job_item = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'first_job_item')))
                    first_job_item.click()
                    time.sleep(0.5)
                
                    # 스크롤 내려서 지원하기 버튼 클릭
                    driver.find_element(
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiScrollable(new UiSelector().scrollable(true).instance(0))'
                        '.scrollIntoView(new UiSelector().textContains("지원하기").instance(0));'
                    )
                    time.sleep(0.5)
                    
                    # 공고의 지원하기
                    # apply_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'apply_btn')))
                    apply_btn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, '지원하기')
                    apply_btn.click()
                    time.sleep(0.5)
                    
                    # 지원하기 버튼 클릭
                    apply_btn2 = driver.find_element(AppiumBy.ACCESSIBILITY_ID, '지원하기')
                    apply_btn2.click()
                    time.sleep(0.5)

                    # 이미 지원한 공고 모달
                    modal_applys = driver.find_elements(*self._get_locator(driver, 'modal_applys'))
                    if len(modal_applys) == 1:
                        confirm = driver.find_element(AppiumBy.ACCESSIBILITY_ID, '확인')
                        confirm.click()
                        time.sleep(0.5)
                    else:
                        pass
                    
                    # 희망 시급 모달
                    desired_hourly_wage_btn = driver.find_elements(*self._get_locator(driver, 'desired_hourly_wage_btn'))
                    if len(desired_hourly_wage_btn) == 1:
                        send_desired_hourly_wage = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'send_desired_hourly_wage')))
                        send_desired_hourly_wage.click()
                        time.sleep(0.5)
                        send_desired_hourly_wage2 = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'send_desired_hourly_wage2')))
                        send_desired_hourly_wage2.clear()
                        send_desired_hourly_wage2.send_keys('5000')
                        time.sleep(0.5)
                        next_btn = driver.element(AppiumBy.ACCESSIBILITY_ID, '다음')
                        next_btn.click()
                        time.sleep(0.5)
                    else:
                        pass

                    # 보호자에게 남긴는 말 모달
                    send_msg_modal_applys = driver.find_elements(*self._get_locator(driver, 'send_msg_modal_applys'))
                    if len(send_msg_modal_applys) == 1:
                        send_msg_modal_comfirm_input = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'send_msg_modal_comfirm_input')))
                        send_msg_modal_comfirm_input.click()
                        time.sleep(0.5)
                        send_msg_modal_comfirm_input2 = driver.element(*self._get_locator(driver, 'send_msg_modal_comfirm_input2'))
                        send_msg_modal_comfirm_input2.send_keys('안녕하세요')
                        time.sleep(0.5)
                        send_msg_modal_comfirm_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'send_msg_modal_comfirm_btn')))
                        send_msg_modal_comfirm_btn.click()
                        time.sleep(0.5)
                    else:
                        pass

                    # 공고 지원 완료 모달
                    application_completed_modal = driver.find_elements(AppiumBy.ACCESSIBILITY_ID, '공고리스트로 이동')
                    if len(application_completed_modal) == 1:
                        application_completed_modal[0].click()
                        time.sleep(0.5)
                    else:
                        pass

            
            driver.back()
        except Exception as e:
            pytest.fail(f"종합 채용공고 지원 플로우 테스트 실패: {str(e)}")