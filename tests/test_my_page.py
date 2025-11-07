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
                'address': (AppiumBy.XPATH, '//android.widget.TextView[@text="주소"]'),
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
                'toast_message2': (AppiumBy.XPATH, '//android.widget.TextView[@text="완료!"]'),
                'favorite_toast_message': (AppiumBy.XPATH, '//android.widget.TextView[@text="이 시설을 즐겨찾기 목록에서 제거했습니다!"]'),
                'scraped_toast_message': (AppiumBy.XPATH, '//android.widget.TextView[@text="이 공고를 즐겨찾기 목록에서 제거했습니다!"]'),
                'position_proposal_toast_message': (AppiumBy.XPATH, '//android.widget.TextView[@text="수정이 완료되었습니다!"]'),
                'hanmaeum_nursing_home_name': (AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="재가복지센터, 숲데이케어센터, 서울 동작구 상도로68길 1-20"]/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup'),
                'search_input': (AppiumBy.XPATH, '//android.widget.EditText[@text="검색"]'),
                'search_icon_btn': (AppiumBy.XPATH, '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]'),
                'loction_access_modal': (AppiumBy.XPATH, '//android.widget.Button[@resource-id="com.android.permissioncontroller:id/permission_allow_foreground_only_button"]'),
                'category_button1': (AppiumBy.XPATH, '//android.widget.ImageView'),
                'category_button2': (AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="시작하기"]/android.view.ViewGroup'),
                'list_item': (AppiumBy.XPATH, '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[1]'),
                'list_item_youtube': (AppiumBy.XPATH, '//android.widget.Button[@text="Play video"]'),
                # 새로운 시나리오 로케이터들
                'my_resume_btn': (AppiumBy.XPATH, '//android.widget.TextView[@text="내 이력서"]'),
                'first_resume_item': (AppiumBy.XPATH, '//android.widget.TextView[@text="사회복지사/요양보호사"]'),
                'second_resume_item': (AppiumBy.XPATH, '//android.widget.TextView[@text="간병/가사/동행"]'),
                'detail_address_input_4floor1': (AppiumBy.XPATH, '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup[11]'),
                'detail_address_input_4floor2': (AppiumBy.XPATH, '//android.widget.EditText[@text="4층"]'),
                'detail_address_input_2floor': (AppiumBy.XPATH, '//android.widget.EditText[@text="상세주소"]'),
                'detail_address_input_3floor': (AppiumBy.XPATH, '//android.widget.EditText[@text="상세주소"]'),
                'specialty_input': (AppiumBy.CLASS_NAME, 'android.widget.EditText'),
                'preview_btn': (AppiumBy.XPATH, '//android.widget.HorizontalScrollView/android.view.ViewGroup/android.view.ViewGroup[6]/android.view.ViewGroup'),
                'registration_complete_btn': (AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="등록완료 "]'),
                'deposit_withdrawal_history_btn': (AppiumBy.XPATH, '//android.widget.TextView[@text="입출금내역"]'),
                'account_management_btn': (AppiumBy.XPATH, '//android.widget.TextView[@text="계좌관리"]'),
                'account_registration_btn': (AppiumBy.XPATH, '//android.widget.TextView[@text="계좌등록"]'),
                'account_nickname_input': (AppiumBy.XPATH, '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup[1]/android.widget.EditText'),
                'bank_selection_dropdown': (AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="은행선택"]'),
                # 'bank_selection_dropdown': (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().description("은행선택")'),
                'ibk_bank_option': (AppiumBy.XPATH, '//android.widget.TextView[@text="기업은행"]'),
                'account_number_input': (AppiumBy.XPATH, '//android.widget.EditText[@text="계좌번호를 입력해 주세요"]'),
                'register_account_btn': (AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="등록하기"]'),
                'transfer_btn': (AppiumBy.XPATH, '//android.widget.TextView[@text="이체하기"]'),
                'modal_content': (AppiumBy.XPATH, '//android.widget.TextView'),
                'modal_confirm_btn': (AppiumBy.XPATH, '//android.widget.Button[@text="확인"]'),
                'back_btn_general': (AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="뒤로가기"]'),
                # 추가 시나리오 로케이터들
                'general_matching_info_btn': (AppiumBy.XPATH, '//android.widget.TextView[@text="일반\n매칭정보 관리"]'),
                'caregiver_job_matching_btn': (AppiumBy.XPATH, '//android.widget.TextView[@text="간병 일자리\n맞춤매칭 관리"]'),
                'first_edit_icon': (AppiumBy.XPATH, '//android.widget.HorizontalScrollView/android.view.ViewGroup/android.view.ViewGroup[1]'),
                'second_edit_icon': (AppiumBy.XPATH, '//android.widget.HorizontalScrollView/android.view.ViewGroup/android.view.ViewGroup[3]'),
                'third_edit_icon': (AppiumBy.XPATH, '//android.widget.HorizontalScrollView/android.view.ViewGroup/android.view.ViewGroup[2]'),
                # 'fourth_edit_icon': (AppiumBy.XPATH, '//android.widget.HorizontalScrollView/android.view.ViewGroup/android.view.ViewGroup[4]'),
                # 'fourth_edit_icon': (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.view.ViewGroup").instance(82)'),
                # 'fourth_edit_icon': (AppiumBy.XPATH, '//android.widget.HorizontalScrollView/android.view.ViewGroup/android.view.ViewGroup[4]/com.horcrux.svg.SvgView'),
                'fourth_edit_icon': (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("com.horcrux.svg.SvgView").instance(2)'),
                'jongro_gu_checkbox': (AppiumBy.XPATH, '//android.widget.TextView[@text="종로구"]'),
                'yongsan_gu_checkbox': (AppiumBy.XPATH, '//android.widget.TextView[@text="용산구"]'),
                'seongdong_gu_checkbox': (AppiumBy.XPATH, '//android.widget.TextView[@text="성동구"]'),
                'gwangjin_gu_checkbox': (AppiumBy.XPATH, '//android.widget.TextView[@text="광진구"]'),
                'schedule_reset_btn': (AppiumBy.XPATH, '//android.widget.TextView[@text="일정초기화"]'),
                'monday_btn': (AppiumBy.XPATH, '//android.widget.TextView[@text="월"]'),
                'tuesday_btn': (AppiumBy.XPATH, '//android.widget.TextView[@text="화"]'),
                'wednesday_btn': (AppiumBy.XPATH, '//android.widget.TextView[@text="수"]'),
                'thursday_btn': (AppiumBy.XPATH, '//android.widget.TextView[@text="목"]'),
                'friday_btn': (AppiumBy.XPATH, '//android.widget.TextView[@text="금"]'),
                'feeding_btn': (AppiumBy.XPATH, '//android.widget.TextView[@text="피딩"]'),
                'paralysis_btn': (AppiumBy.XPATH, '//android.widget.TextView[@text="마비"]'),
                'bedsore_btn': (AppiumBy.XPATH, '//android.widget.TextView[@text="욕창"]'),
                'diaper_care_btn': (AppiumBy.XPATH, '//android.widget.TextView[@text="기저귀 케어"]'),
                'communication_difficulty_btn': (AppiumBy.XPATH, '//android.widget.TextView[@text="의사소통어려움"]'),
                'no_proceed_btn': (AppiumBy.XPATH, '//android.widget.TextView[@text="진행안함"]'),
                'pcr_btn': (AppiumBy.XPATH, '//android.widget.TextView[@text="PCR"]'),
                'application_status_btn': (AppiumBy.XPATH, '//android.widget.TextView[@text="지원현황"]'),
                'first_cancel_btn': (AppiumBy.XPATH, '(//android.view.ViewGroup[@content-desc="취소하기"])[1]'),
                'cancel_btn': (AppiumBy.XPATH, '(//android.view.ViewGroup[@content-desc="취소하기"])[1]'),
                'first_delete_btn': (AppiumBy.XPATH, '(//android.view.ViewGroup[@content-desc="지원내역 삭제"])[1]'),
                'proceed_btn': (AppiumBy.XPATH, '//android.widget.TextView[@text="진행"]'),
                # 새로운 시나리오 로케이터들
                'position_proposal_btn': (AppiumBy.XPATH, '//android.widget.TextView[@text="포지션제안"]'),
                'resume_update_btn': (AppiumBy.XPATH, '//android.widget.TextView[@text="이력서 업데이트"]'),
                'edit_btn': (AppiumBy.XPATH, '//android.widget.TextView[@text="수정하기"]'),
                'complete_btn': (AppiumBy.XPATH, '//android.widget.TextView[@text="완료"]'),
                'position_proposal_setting_btn': (AppiumBy.XPATH, '//android.widget.TextView[@text="포지션 제안 설정"]'),
                'receive_proposal_checkbox': (AppiumBy.XPATH, '//android.widget.TextView[@text="후순 포지션이 있다면 제안 받을래요"]'),
                'scraped_jobs_btn': (AppiumBy.XPATH, '//android.widget.TextView[@text="스크랩 공고"]'),
                'first_star_btn': (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("com.horcrux.svg.GroupView").instance(2)'),
                'favorite_companies_btn': (AppiumBy.XPATH, '//android.widget.TextView[@text="관심기업"]'),
                'first_company_heart_btn': (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("com.horcrux.svg.GroupView").instance(2)'),
            },
            'ios': {
                # 마이페이지 관련 로케이터
                'bottom_my_page_btn': (AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='마이페이지']"),
                'my_info_management_btn': (AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='내 정보관리']"),
                'detail_address_input': (AppiumBy.XPATH, "//XCUIElementTypeTextField[@name='상세주소']"),
                'keyborad_hied': (AppiumBy.XPATH, "//XCUIElementTypeTextField[@name='상세주소']"),
                'save_btn': (AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='저장']"),
                'address': (AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='저장']"),
                'toast_message': (AppiumBy.XPATH, "//XCUIElementTypeStaticText"),
                'toast_message2': (AppiumBy.XPATH, "//XCUIElementTypeStaticText"),
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
                'toast_message2': (AppiumBy.XPATH, "//XCUIElementTypeStaticText"),
                'scraped_toast_message': (AppiumBy.XPATH, "//XCUIElementTypeStaticText"),
                'position_proposal_toast_message': (AppiumBy.XPATH, "//XCUIElementTypeStaticText"),
                'hanmaeum_nursing_home_name': (AppiumBy.XPATH, "//XCUIElementTypeStaticText"),
                'search_input': (AppiumBy.XPATH, "//XCUIElementTypeTextField[@name='검색']"),
                'search_icon_btn': (AppiumBy.XPATH, "//XCUIElementTypeButton[@name='검색']"),
                'loction_access_modal': (AppiumBy.XPATH, "//XCUIElementTypeButton[@name='허용']"),
                'category_button1': (AppiumBy.XPATH, "//XCUIElementTypeButton[@name='허용']"),
                'category_button2': (AppiumBy.XPATH, "//XCUIElementTypeButton[@name='허용']"),
                'list_item': (AppiumBy.XPATH, "//XCUIElementTypeButton[@name='허용']"),
                'list_item_youtube': (AppiumBy.XPATH, "//XCUIElementTypeButton[@name='허용']"),
                # 새로운 시나리오 로케이터들
                'my_resume_btn': (AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='내 이력서']"),
                'first_resume_item': (AppiumBy.XPATH, "(//XCUIElementTypeCell)[1]"),
                'second_resume_item': (AppiumBy.XPATH, "(//XCUIElementTypeCell)[2]"),
                'detail_address_input_4floor1': (AppiumBy.XPATH, "//XCUIElementTypeTextField[@name='상세주소']"),
                'detail_address_input_4floor2': (AppiumBy.XPATH, "//XCUIElementTypeTextField[@name='상세주소']"),
                'detail_address_input_2floor': (AppiumBy.XPATH, "//XCUIElementTypeTextField[@name='상세주소']"),
                'detail_address_input_3floor': (AppiumBy.XPATH, "//XCUIElementTypeTextField[@name='상세주소']"),
                'specialty_input': (AppiumBy.XPATH, "//XCUIElementTypeTextField[@name='전문분야']"),
                'preview_btn': (AppiumBy.XPATH, "//XCUIElementTypeButton[@name='미리보기']"),
                'registration_complete_btn': (AppiumBy.XPATH, "//XCUIElementTypeButton[@name='등록완료']"),
                'deposit_withdrawal_history_btn': (AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='입출금내역']"),
                'account_management_btn': (AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='계좌관리']"),
                'account_registration_btn': (AppiumBy.XPATH, "//XCUIElementTypeButton[@name='계좌등록']"),
                'account_nickname_input': (AppiumBy.XPATH, "//XCUIElementTypeTextField[@name='통장별명']"),
                'bank_selection_dropdown': (AppiumBy.XPATH, "//XCUIElementTypePicker"),
                'ibk_bank_option': (AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='기업은행']"),
                'account_number_input': (AppiumBy.XPATH, "//XCUIElementTypeTextField[@name='등록 계좌번호']"),
                'register_account_btn': (AppiumBy.XPATH, "//XCUIElementTypeButton[@name='등록하기']"),
                'transfer_btn': (AppiumBy.XPATH, "//XCUIElementTypeButton[@name='이체하기']"),
                'modal_content': (AppiumBy.XPATH, "//XCUIElementTypeStaticText"),
                'modal_confirm_btn': (AppiumBy.XPATH, "//XCUIElementTypeButton[@name='확인']"),
                'back_btn_general': (AppiumBy.XPATH, "//XCUIElementTypeButton[@name='뒤로가기']"),
                # 추가 시나리오 로케이터들
                'general_matching_info_btn': (AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='일반 매칭정보 관리']"),
                'caregiver_job_matching_btn': (AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='간병 일자리 맞춤매칭 관리']"),
                'first_edit_icon': (AppiumBy.XPATH, "(//XCUIElementTypeButton[@name='편집'])[1]"),
                'second_edit_icon': (AppiumBy.XPATH, "(//XCUIElementTypeButton[@name='편집'])[2]"),
                'third_edit_icon': (AppiumBy.XPATH, "(//XCUIElementTypeButton[@name='편집'])[3]"),
                'fourth_edit_icon': (AppiumBy.XPATH, "(//XCUIElementTypeButton[@name='편집'])[4]"),
                'jongro_gu_checkbox': (AppiumBy.XPATH, "//XCUIElementTypeButton[@name='종로구']"),
                'yongsan_gu_checkbox': (AppiumBy.XPATH, "//XCUIElementTypeButton[@name='용산구']"),
                'seongdong_gu_checkbox': (AppiumBy.XPATH, "//XCUIElementTypeButton[@name='성동구']"),
                'gwangjin_gu_checkbox': (AppiumBy.XPATH, "//XCUIElementTypeButton[@name='광진구']"),
                'schedule_reset_btn': (AppiumBy.XPATH, "//XCUIElementTypeButton[@name='일정초기화']"),
                'monday_btn': (AppiumBy.XPATH, "//XCUIElementTypeButton[@name='월']"),
                'tuesday_btn': (AppiumBy.XPATH, "//XCUIElementTypeButton[@name='화']"),
                'wednesday_btn': (AppiumBy.XPATH, "//XCUIElementTypeButton[@name='수']"),
                'thursday_btn': (AppiumBy.XPATH, "//XCUIElementTypeButton[@name='목']"),
                'friday_btn': (AppiumBy.XPATH, "//XCUIElementTypeButton[@name='금']"),
                'feeding_btn': (AppiumBy.XPATH, "//XCUIElementTypeButton[@name='피딩']"),
                'paralysis_btn': (AppiumBy.XPATH, "//XCUIElementTypeButton[@name='마비']"),
                'bedsore_btn': (AppiumBy.XPATH, "//XCUIElementTypeButton[@name='욕창']"),
                'diaper_care_btn': (AppiumBy.XPATH, "//XCUIElementTypeButton[@name='기저귀 케어']"),
                'communication_difficulty_btn': (AppiumBy.XPATH, "//XCUIElementTypeButton[@name='의사소통어려움']"),
                'no_proceed_btn': (AppiumBy.XPATH, "//XCUIElementTypeButton[@name='진행안함']"),
                'pcr_btn': (AppiumBy.XPATH, "//XCUIElementTypeButton[@name='PCR']"),
                'application_status_btn': (AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='지원현황']"),
                'first_cancel_btn': (AppiumBy.XPATH, "(//XCUIElementTypeButton[@name='취소하기'])[1]"),
                'cancel_btn': (AppiumBy.XPATH, "//XCUIElementTypeButton[@name='취소하기']"),
                'first_delete_btn': (AppiumBy.XPATH, "(//XCUIElementTypeButton[@name='지원내역 삭제'])[1]"),
                'proceed_btn': (AppiumBy.XPATH, "//XCUIElementTypeButton[@name='진행']"),
                # 새로운 시나리오 로케이터들
                'position_proposal_btn': (AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='포지션제안']"),
                'resume_update_btn': (AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='이력서 업데이트']"),
                'edit_btn': (AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='수정하기']"),
                'complete_btn': (AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='완료']"),
                'position_proposal_setting_btn': (AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='포지션 제안 설정']"),
                'receive_proposal_checkbox': (AppiumBy.XPATH, "//XCUIElementTypeButton[@name='후순 포지션이 있다면 제안 받을래요']"),
                'scraped_jobs_btn': (AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='스크랩 공고']"),
                'first_star_btn': (AppiumBy.XPATH, "(//XCUIElementTypeButton[@name='별'])[1]"),
                'favorite_companies_btn': (AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='관심기업']"),
                'first_company_heart_btn': (AppiumBy.XPATH, "(//XCUIElementTypeButton[@name='하트'])[1]"),
            }
        }
        
        return locators[platform][element_name]
    
    def test_favorite_institutions_from_mypage(self, driver_setup):
        """마이페이지 관심기관 테스트"""
        if isinstance(driver_setup, dict):
            driver = driver_setup['driver']
        else:
            driver = driver_setup
        wait = WebDriverWait(driver, 10)
        
        try:
            time.sleep(2)
            
            # 바텀 메뉴에서 마이 페이지 클릭
            bottom_my_page_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'bottom_my_page_btn')))
            bottom_my_page_btn.click()
            time.sleep(0.5)
            
            # 관심기관 버튼 클릭
            favorite_institutions_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'favorite_institutions_btn')))
            favorite_institutions_btn.click()
            time.sleep(0.5)

            # 첫번째 항목의 하트 클릭
            first_favorite_heart_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'first_favorite_heart_btn')))
            first_favorite_heart_btn.click()
            time.sleep(0.5)
            
            # 관심기업 해제 토스트메세지가 잘 뜨는지 확인
            toast_message = wait.until(EC.presence_of_element_located(self._get_locator(driver, 'toast_message2')))
            assert toast_message.is_displayed(), "이 시설을 즐겨찾기 목록에서 제거했습니다!"
            time.sleep(0.5)

            driver.back()
            driver.back()

            # 숲데이케어센터 검색
            # 돋보기 버튼 클릭
            search_icon_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'search_icon_btn')))
            search_icon_btn.click()
            time.sleep(0.5)
            
            # 위치 권한 모달
            loction_access_modal = wait.until(EC.presence_of_element_located(self._get_locator(driver, 'loction_access_modal')))
            loction_access_modal.click()
            time.sleep(0.5)
            
            # 검색 인풋에 숲데이케어센터 넣기
            search_input = wait.until(EC.presence_of_element_located(self._get_locator(driver, 'search_input')))
            search_input.clear()
            search_input.send_keys("숲데이케어센터")
            time.sleep(0.5)
            
            # 숲데이케어센터 클릭
            hanmaeum_nursing_home_name = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'hanmaeum_nursing_home_name')))
            hanmaeum_nursing_home_name.click()
            time.sleep(0.5)
            driver.back()
            
        except Exception as e:
            pytest.fail(f"마이페이지 관심기관 테스트 실패: {str(e)}")
    
    def test_notice(self, driver_setup):
        """공지사항 테스트"""
        if isinstance(driver_setup, dict):
            driver = driver_setup['driver']
        else:
            driver = driver_setup
        wait = WebDriverWait(driver, 10)
        
        try:
            time.sleep(2)
            
            # 바텀 메뉴에서 마이 페이지 클릭
            bottom_my_page_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'bottom_my_page_btn')))
            bottom_my_page_btn.click()
            time.sleep(0.5)
            
            driver.find_element(
                AppiumBy.ANDROID_UIAUTOMATOR,
                'new UiScrollable(new UiSelector().scrollable(true).instance(0))'
                '.scrollIntoView(new UiSelector().textContains("학습자료실").instance(0));'
            )
            time.sleep(0.5)

            # 공지사항 버튼 클릭
            # notice_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'notice_btn')))
            notice_btn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, '공지사항')
            notice_btn.click()
            time.sleep(0.5)
            
            # 첫번째 항목 클릭
            # first_notice_item = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'first_notice_item')))
            first_notice_item = driver.find_element(*self._get_locator(driver, 'first_notice_item'))
            first_notice_item.click()
            time.sleep(2)
            
            # 뒤로가기 버튼 클릭
            driver.back()
            time.sleep(0.5)
            
            # 뒤로가기 버튼 클릭
            driver.back()
            time.sleep(0.5)
            
        except Exception as e:
            pytest.fail(f"공지사항 테스트 실패: {str(e)}")
    
    def test_faq(self, driver_setup):
        """자주 묻는 질문 테스트"""
        if isinstance(driver_setup, dict):
            driver = driver_setup['driver']
        else:
            driver = driver_setup
        wait = WebDriverWait(driver, 10)
        
        try:
            time.sleep(2)
            
            # 바텀 메뉴에서 마이 페이지 클릭
            bottom_my_page_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'bottom_my_page_btn')))
            bottom_my_page_btn.click()
            time.sleep(0.5)

            driver.find_element(
                AppiumBy.ANDROID_UIAUTOMATOR,
                'new UiScrollable(new UiSelector().scrollable(true).instance(0))'
                '.scrollIntoView(new UiSelector().textContains("학습자료실").instance(0));'
            )
            time.sleep(0.5)
            
            # 자주 묻는 질문 버튼 클릭
            # faq_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'faq_btn')))
            faq_btn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, '자주 묻는 질문')
            faq_btn.click()
            time.sleep(0.5)
            
            # 첫번째 항목 클릭
            first_notice_item = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'fnq_first_notice_item')))
            first_notice_item.click()
            time.sleep(2)
            
            # 검색 인풋에 하반기 넣기
            search_input = wait.until(EC.presence_of_element_located(self._get_locator(driver, 'faq_search_input')))
            search_input.clear()
            # 여기 수정 필요 - 251104
            search_input.send_keys("하반기")
            time.sleep(0.5)
            
            # 여기 수정 필요 - 251104
            # 첫번째 항목 클릭
            first_notice_item = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'fnq_first_notice_item2')))
            first_notice_item.click()
            time.sleep(2)
            
            # 뒤로가기 버튼 클릭
            driver.back()
            time.sleep(0.5)
            
        except Exception as e:
            pytest.fail(f"자주 묻는 질문 테스트 실패: {str(e)}")
    
    def test_event(self, driver_setup):
        """이벤트 테스트"""
        if isinstance(driver_setup, dict):
            driver = driver_setup['driver']
        else:
            driver = driver_setup
        wait = WebDriverWait(driver, 10)
        
        try:
            time.sleep(2)
            
            # 바텀 메뉴에서 마이 페이지 클릭
            bottom_my_page_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'bottom_my_page_btn')))
            bottom_my_page_btn.click()
            time.sleep(0.5)

            driver.find_element(
                AppiumBy.ANDROID_UIAUTOMATOR,
                'new UiScrollable(new UiSelector().scrollable(true).instance(0))'
                '.scrollIntoView(new UiSelector().textContains("학습자료실").instance(0));'
            )
            time.sleep(0.5)
            
            # 이벤트 버튼 클릭
            # event_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'event_btn')))
            event_btn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, '이벤트')
            event_btn.click()
            time.sleep(0.5)
            
            # 첫번째 항목 클릭
            first_notice_item = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'event_first_notice_item')))
            first_notice_item.click()
            time.sleep(2)
            
            # 뒤로가기 버튼 클릭
            driver.back()
            time.sleep(0.5)
            
            # 뒤로가기 버튼 클릭
            driver.back()
            time.sleep(0.5)
            
        except Exception as e:
            pytest.fail(f"이벤트 테스트 실패: {str(e)}")
    
    def test_customer_center(self, driver_setup):
        """고객센터 테스트"""
        if isinstance(driver_setup, dict):
            driver = driver_setup['driver']
        else:
            driver = driver_setup
        wait = WebDriverWait(driver, 10)
        
        try:
            time.sleep(2)
            
            # 바텀 메뉴에서 마이 페이지 클릭
            bottom_my_page_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'bottom_my_page_btn')))
            bottom_my_page_btn.click()
            time.sleep(0.5)
            
            driver.find_element(
                AppiumBy.ANDROID_UIAUTOMATOR,
                'new UiScrollable(new UiSelector().scrollable(true).instance(0))'
                '.scrollIntoView(new UiSelector().textContains("학습자료실").instance(0));'
            )
            time.sleep(0.5)

            # 고객센터 버튼 클릭
            # customer_center_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'customer_center_btn')))
            customer_center_btn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, '고객센터')
            customer_center_btn.click()
            time.sleep(0.5)
            
            # 뒤로가기 버튼 클릭
            driver.back()
            time.sleep(0.5)
            
        except Exception as e:
            pytest.fail(f"고객센터 테스트 실패: {str(e)}")
    
    def test_error_report_center(self, driver_setup):
        """오류신고센터 테스트"""
        if isinstance(driver_setup, dict):
            driver = driver_setup['driver']
        else:
            driver = driver_setup
        wait = WebDriverWait(driver, 10)
        
        try:
            time.sleep(2)
            
            # 바텀 메뉴에서 마이 페이지 클릭
            bottom_my_page_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'bottom_my_page_btn')))
            bottom_my_page_btn.click()
            time.sleep(0.5)
            
            driver.find_element(
                AppiumBy.ANDROID_UIAUTOMATOR,
                'new UiScrollable(new UiSelector().scrollable(true).instance(0))'
                '.scrollIntoView(new UiSelector().textContains("학습자료실").instance(0));'
            )
            time.sleep(0.5)

            # 여기 수정 필요 - 251104
            # 오류신고센터 버튼 클릭
            # error_report_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'error_report_btn')))
            error_report_btn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, '앱기능 건의함')
            error_report_btn.click()
            time.sleep(0.5)
            
            # 분류 드롭다운 클릭
            # category_dropdown = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'category_dropdown')))
            category_dropdown = driver.find_element(AppiumBy.ACCESSIBILITY_ID, '분류를 선택해 주세요')
            category_dropdown.click()
            time.sleep(0.5)
            
            # 서비스신청오류 클릭
            # service_error_option = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'service_error_option')))
            service_error_option = driver.find_element(AppiumBy.ACCESSIBILITY_ID, '매칭오류')
            service_error_option.click()
            time.sleep(0.5)
            
            driver.find_element(
                AppiumBy.ANDROID_UIAUTOMATOR,
                'new UiScrollable(new UiSelector().scrollable(true).instance(0))'
                '.scrollIntoView(new UiSelector().textContains("사용자님의 의견").instance(0));'
            )
            time.sleep(0.5)

            # 제목 인풋에 오류 테스트중입니다 넣기
            title_input = wait.until(EC.presence_of_element_located(self._get_locator(driver, 'title_input')))
            title_input.clear()
            title_input.send_keys("오류 테스트중입니다")
            time.sleep(0.5)
            
            # 사용자님의 의견 인풋에 오류 테스트중입니다 내용 테스트중입니다 넣기
            opinion_input = wait.until(EC.presence_of_element_located(self._get_locator(driver, 'opinion_input')))
            opinion_input.clear()
            opinion_input.send_keys("오류 테스트중입니다 내용 테스트중입니다")
            time.sleep(0.5)
            
            driver.find_element(
                AppiumBy.ANDROID_UIAUTOMATOR,
                'new UiScrollable(new UiSelector().scrollable(true).instance(0))'
                '.scrollIntoView(new UiSelector().textContains("신고하기").instance(0));'
            )
            time.sleep(0.5)

            # 신고하기 버튼 클릭
            # report_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'report_btn')))
            report_btn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, '신고하기')
            report_btn.click()
            time.sleep(0.5)
            
            # 토스트메세지 분석
            toast_message = wait.until(EC.presence_of_element_located(self._get_locator(driver, 'toast_message2')))
            assert toast_message.is_displayed(), "완료!"
            time.sleep(2)
            
            # 첫번째 항목 클릭
            first_notice_item = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'error_first_notice_item')))
            first_notice_item.click()
            time.sleep(0.5)
            
            # 목록 버튼 클릭
            # list_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'list_btn')))
            list_btn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, '목록')
            list_btn.click()
            time.sleep(0.5)
            
            # 첫번째 항목 클릭
            first_notice_item = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'error_first_notice_item')))
            first_notice_item.click()
            time.sleep(0.5)
            
            # 삭제하기 버튼 클릭
            # delete_report_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'delete_report_btn')))
            delete_report_btn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, '삭제하기')
            delete_report_btn.click()
            time.sleep(0.5)
            
            # 진행 버튼 클릭
            # proceed_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'proceed_btn')))
            proceed_btn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, '진행')
            proceed_btn.click()
            time.sleep(0.5)
            
            # 토스트메세지 분석
            toast_message = wait.until(EC.presence_of_element_located(self._get_locator(driver, 'toast_message2')))
            assert toast_message.is_displayed(), "완료!"
            time.sleep(2)
            
            # 오류신고하기 버튼 클릭
            # error_report_create_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'error_report_create_btn')))
            error_report_create_btn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, '오류신고하기')
            error_report_create_btn.click()
            time.sleep(0.5)
            
            # 고객센터 문의하기 버튼 클릭
            # customer_inquiry_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'customer_inquiry_btn')))
            customer_inquiry_btn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, '고객센터 문의하기')
            customer_inquiry_btn.click()
            time.sleep(0.5)
            
            # 뒤로가기 버튼 클릭
            driver.back()
            time.sleep(0.5)
            
            driver.find_element(
                AppiumBy.ANDROID_UIAUTOMATOR,
                'new UiScrollable(new UiSelector().scrollable(true).instance(0))'
                '.scrollIntoView(new UiSelector().textContains("내 신고내역").instance(0));'
            )
            time.sleep(0.5)

            # 내 신고내역 버튼 클릭
            # my_report_history_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'my_report_history_btn')))
            my_report_history_btn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, '내 신고내역')
            my_report_history_btn.click()
            time.sleep(0.5)
            
            # 뒤로가기 버튼 클릭
            driver.back()
            time.sleep(0.5)
            
            # 뒤로가기 버튼 클릭
            driver.back()
            time.sleep(0.5)
            
        except Exception as e:
            pytest.fail(f"오류신고센터 테스트 실패: {str(e)}")
    
    # def test_learning_materials(self, driver_setup):
    #     """학습자료실 테스트"""
    #     if isinstance(driver_setup, dict):
    #         driver = driver_setup['driver']
    #     else:
    #         driver = driver_setup
    #     wait = WebDriverWait(driver, 10)
        
    #     try:
    #         time.sleep(2)
            
    #         # 바텀 메뉴에서 마이 페이지 클릭
    #         bottom_my_page_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'bottom_my_page_btn')))
    #         bottom_my_page_btn.click()
    #         time.sleep(0.5)
            
    #         driver.find_element(
    #             AppiumBy.ANDROID_UIAUTOMATOR,
    #             'new UiScrollable(new UiSelector().scrollable(true).instance(0))'
    #             '.scrollIntoView(new UiSelector().textContains("학습자료실").instance(0));'
    #         )
    #         time.sleep(0.5)

    #         # 학습자료실 버튼 클릭
    #         # learning_materials_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'learning_materials_btn')))
    #         learning_materials_btn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, '학습자료실')
    #         learning_materials_btn.click()
    #         time.sleep(0.5)

    #         # 2. 카테고리 클릭
    #         category_button1 = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'category_button1')))
    #         category_button1.click()
    #         time.sleep(0.5)

    #         category_button2 = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'category_button2')))
    #         category_button2.click()
    #         time.sleep(0.5)

    #         # 3-1. 목록 아이템 클릭
    #         list_item = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'list_item')))
    #         list_item.click()
    #         # print("여기까지 왔음1")
    #         time.sleep(2)

    #         # 뒤로가기 버튼 클릭
    #         driver.back()
    #         driver.back()
            
    #     except Exception as e:
    #         pytest.fail(f"학습자료실 테스트 실패: {str(e)}")
    
    # def test_product_purchase(self, driver_setup):
        """상품구매 테스트"""
        if isinstance(driver_setup, dict):
            driver = driver_setup['driver']
        else:
            driver = driver_setup
        wait = WebDriverWait(driver, 10)
        
        try:
            time.sleep(2)
            
            # 바텀 메뉴에서 마이 페이지 클릭
            bottom_my_page_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'bottom_my_page_btn')))
            bottom_my_page_btn.click()
            time.sleep(0.5)
            
            driver.find_element(
                AppiumBy.ANDROID_UIAUTOMATOR,
                'new UiScrollable(new UiSelector().scrollable(true).instance(0))'
                '.scrollIntoView(new UiSelector().textContains("상품구매").instance(0));'
            )
            time.sleep(0.5)

            # 상품구매 버튼 클릭
            # product_purchase_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'product_purchase_btn')))
            product_purchase_btn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, '상품구매')
            product_purchase_btn.click()
            time.sleep(0.5)
            
            # 첫번째 항목 클릭
            first_notice_item = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'pay_ment_first_notice_item')))
            first_notice_item.click()
            time.sleep(0.5)
            
            # 구매하기 버튼 클릭
            # purchase_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'purchase_btn')))
            purchase_btn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, '구매하기')
            purchase_btn.click()
            time.sleep(0.5)
            
            # 결제수단 드롭다운 클릭
            # payment_method_dropdown = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'payment_method_dropdown')))
            payment_method_dropdown = driver.find_element(AppiumBy.ACCESSIBILITY_ID, '선택')
            payment_method_dropdown.click()
            time.sleep(0.5)
            
            # 실시간 계좌이체 클릭
            # bank_transfer_option = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'bank_transfer_option')))
            bank_transfer_option = driver.find_element(AppiumBy.ACCESSIBILITY_ID, '실시간 계좌이체')
            bank_transfer_option.click()
            time.sleep(0.5)
            
            # 전체동의 체크박스 클릭
            # agree_all_checkbox = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'agree_all_checkbox')))
            agree_all_checkbox = driver.find_element(AppiumBy.ACCESSIBILITY_ID, '전체동의')
            agree_all_checkbox.click()
            time.sleep(0.5)

            driver.find_element(
                AppiumBy.ANDROID_UIAUTOMATOR,
                'new UiScrollable(new UiSelector().scrollable(true).instance(0))'
                '.scrollIntoView(new UiSelector().textContains("다음").instance(0));'
            )
            time.sleep(0.5)
            
            # 다음 버튼 클릭
            # next_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'next_btn')))
            next_btn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, '다음')
            next_btn.click()
            time.sleep(0.5)
            
            # 인풋을 클릭후 92205162 넣기
            phone_input = wait.until(EC.presence_of_element_located(self._get_locator(driver, 'phone_input')))
            phone_input.click()
            phone_input.send_keys("01092205162")
            time.sleep(0.5)
            
            # 다음 버튼 클릭
            next_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'pay_ment_next_btn')))
            next_btn.click()
            time.sleep(0.5)
            
            # 5클릭
            number_5 = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'number_5')))
            # number_5 = driver.find_element(AppiumBy.ACCESSIBILITY_ID, '5')
            number_5.click()
            time.sleep(0.5)
            
            # 2클릭
            number_2 = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'number_2')))
            # number_2 = driver.find_element(AppiumBy.ACCESSIBILITY_ID, '2')
            number_2.click()
            time.sleep(0.5)
            
            # 2클릭
            number_2.click()
            time.sleep(0.5)
            
            # 8클릭
            number_8 = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'number_8')))
            # number_8 = driver.find_element(AppiumBy.ACCESSIBILITY_ID, '8')
            number_8.click()
            time.sleep(0.5)
            
            # 9클릭
            number_9 = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'number_9')))
            # number_9 = driver.find_element(AppiumBy.ACCESSIBILITY_ID, '9')
            number_9.click()
            time.sleep(0.5)
            
            # 7클릭
            number_7 = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'number_7')))
            # number_7 = driver.find_element(AppiumBy.ACCESSIBILITY_ID, '7')
            number_7.click()
            time.sleep(0.5)
            
            # 동의하고 결제하기 버튼 클릭
            agree_payment_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'agree_payment_btn')))
            agree_payment_btn.click()
            time.sleep(0.5)
            
            # 확인 버튼 클릭
            confirm_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'pay_ment_confirm_btn')))
            confirm_btn.click()
            time.sleep(0.5)
            
            # 5클릭
            number_5 = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'number_5')))
            number_5.click()
            time.sleep(0.5)
            
            # 2클릭
            number_2 = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'number_2')))
            number_2.click()
            time.sleep(0.5)
            
            # 2클릭
            number_2.click()
            time.sleep(0.5)
            
            # 8클릭
            number_8 = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'number_8')))
            number_8.click()
            time.sleep(0.5)
            
            # 9클릭
            number_9 = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'number_9')))
            number_9.click()
            time.sleep(0.5)
            
            # 7클릭
            number_7 = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'number_7')))
            number_7.click()
            time.sleep(0.5)
            
            # 뒤로가기 버튼 클릭
            driver.back()
            
            # 뒤로가기 버튼 클릭
            driver.back()
            time.sleep(0.5)
            
        except Exception as e:
            pytest.fail(f"상품구매 테스트 실패: {str(e)}")
    
    def test_my_info_and_resume_management(self, driver_setup):
        """홈화면 → 바텀 메뉴에서 마이 페이지 클릭 → 내 정보관리 → 내 이력서 관리 테스트"""
        if isinstance(driver_setup, dict):
            driver = driver_setup['driver']
        else:
            driver = driver_setup
        wait = WebDriverWait(driver, 10)
        
        try:
            time.sleep(2)
            
            # 바텀 메뉴에서 마이 페이지 클릭
            bottom_my_page_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'bottom_my_page_btn')))
            bottom_my_page_btn.click()
            time.sleep(1)
            
            # 내 정보관리 버튼 클릭
            # my_info_management_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'my_info_management_btn')))
            my_info_management_btn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, '내 정보관리')
            my_info_management_btn.click()
            time.sleep(1)
            
            # 스크롤해서 아래로 내려가서 저장 버튼 클릭
            driver.find_element(
                AppiumBy.ANDROID_UIAUTOMATOR,
                'new UiScrollable(new UiSelector().scrollable(true).instance(0))'
                '.scrollIntoView(new UiSelector().textContains("저장").instance(0));'
            )
            time.sleep(1)
            
            # 상세주소 인풋에 4층 넣기
            detail_address_input1 = wait.until(EC.presence_of_element_located(self._get_locator(driver, 'detail_address_input_4floor1')))
            detail_address_input1.click()
            time.sleep(0.5)

            detail_address_input2 = wait.until(EC.presence_of_element_located(self._get_locator(driver, 'detail_address_input_4floor2')))
            # detail_address_input2.click()
            detail_address_input2.clear()
            detail_address_input2.send_keys("4층")
            time.sleep(1)

            # 주소 텍스트 클릭해서 키보드 포커싱 끄기
            address = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'address')))
            address.click()
            time.sleep(1)

            # 저장 버튼 클릭
            # save_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'save_btn')))
            save_btn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, '저장')   
            save_btn.click()
            time.sleep(1)
            
            # 토스트 메세지 분석
            try:
                toast_message = wait.until(EC.presence_of_element_located(self._get_locator(driver, 'toast_message2')))
                assert toast_message.is_displayed(), "수정이 완료되었습니다!"
                print(f"내 정보관리 저장 토스트 메세지: {toast_message.text}")
            except:
                print("내 정보관리 저장 토스트 메세지를 찾을 수 없습니다")
            
            # 내 이력서 버튼 클릭
            # my_resume_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'my_resume_btn')))
            my_resume_btn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, '내 이력서')
            my_resume_btn.click()
            time.sleep(1)
            
            # 첫번째 항목 클릭
            first_resume_item = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'first_resume_item')))
            first_resume_item.click()
            time.sleep(1)
            
            # 확인 버튼 클릭
            # confirm_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'confirm_btn')))
            confirm_btn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, '확인')
            confirm_btn.click()
            time.sleep(1)

            # 스크롤해서 아래로 내려가서 다음 버튼 클릭
            driver.find_element(
                AppiumBy.ANDROID_UIAUTOMATOR,
                'new UiScrollable(new UiSelector().scrollable(true).instance(0))'
                '.scrollIntoView(new UiSelector().textContains("다음").instance(0));'
            )
            time.sleep(1)
            
            # 상세주소 인풋에 2층 넣기
            # detail_address_input = wait.until(EC.presence_of_element_located(self._get_locator(driver, 'detail_address_input_2floor')))
            # detail_address_input.clear()
            # detail_address_input.send_keys("2층")
            # time.sleep(1)
            
            # 다음 버튼 클릭
            # next_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'next_btn')))
            next_btn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, '다음')
            next_btn.click()
            time.sleep(1)
            
            # 스크롤해서 아래로 내려가서 친절함 버튼 클릭
            driver.find_element(
                AppiumBy.ANDROID_UIAUTOMATOR,
                'new UiScrollable(new UiSelector().scrollable(true).instance(0))'
                '.scrollIntoView(new UiSelector().textContains("친절함").instance(0));'
            )
            time.sleep(1)

            # 전문분야 인풋에 인사과 테스트중입니다 브잉 넣기
            specialty_input = wait.until(EC.presence_of_element_located(self._get_locator(driver, 'specialty_input')))
            specialty_input.clear()
            specialty_input.send_keys("인사과 테스트중입니다 브잉")
            time.sleep(1)
            
            # 스크롤해서 아래로 내려가서 미리보기 버튼 클릭
            driver.find_element(
                AppiumBy.ANDROID_UIAUTOMATOR,
                'new UiScrollable(new UiSelector().scrollable(true).instance(0))'
                '.scrollIntoView(new UiSelector().textContains("미리보기").instance(0));'
            )
            time.sleep(1)
            
            # 전체동의 체크박스 클릭
            # preview_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'preview_btn')))
            # preview_btn.click()
            # time.sleep(1)
            
            # 등록완료 버튼 클릭
            # registration_complete_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'registration_complete_btn')))
            registration_complete_btn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, '완료')
            registration_complete_btn.click()
            time.sleep(1)

            # 토스트 메세지 분석
            try:
                toast_message = wait.until(EC.presence_of_element_located(self._get_locator(driver, 'toast_message2')))
                msg = toast_message.get_attribute("text")
                assert msg == "완료!"
                print(f"첫번째 이력서 등록완료 토스트 메세지: {msg}, {toast_message.is_displayed()}")
            except:
                print("첫번째 이력서 완료 토스트 메세지를 찾을 수 없습니다")
                pytest.fail("사회복지사/요양보호사 이력서 등록완료시 뜨는 토스트 메세지가 정상적이지 않음")
            
            # 두번째 항목 클릭
            second_resume_item = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'second_resume_item')))
            second_resume_item.click()
            time.sleep(1)
            
            # 확인 버튼 클릭
            # confirm_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'confirm_btn')))
            confirm_btn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, '확인')
            confirm_btn.click()
            time.sleep(1)
            
            # 상세주소 인풋 클릭해서 3층 넣기
            # detail_address_input = wait.until(EC.presence_of_element_located(self._get_locator(driver, 'detail_address_input_3floor')))
            # detail_address_input.clear()
            # detail_address_input.send_keys("3층")
            # time.sleep(1)
            
            # 스크롤해서 아래로 내려가서 다음 버튼 클릭
            driver.find_element(
                AppiumBy.ANDROID_UIAUTOMATOR,
                'new UiScrollable(new UiSelector().scrollable(true).instance(0))'
                '.scrollIntoView(new UiSelector().textContains("다음").instance(0));'
            )
            time.sleep(1)
            
            # 다음 버튼 클릭
            # next_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'next_btn')))
            next_btn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, '다음')
            next_btn.click()
            time.sleep(1)
            
            # 전문분야 인풋에 간병요양 테스트중입니다 브잉 넣기
            # specialty_input = wait.until(EC.presence_of_element_located(self._get_locator(driver, 'specialty_input')))
            specialty_input = driver.find_element(*self._get_locator(driver, 'specialty_input'))
            specialty_input.clear()
            specialty_input.send_keys("간병요양 테스트중입니다 브잉")
            time.sleep(1)
            
            # 스크롤해서 아래로 내려가서 미리보기 버튼 클릭
            driver.find_element(
                AppiumBy.ANDROID_UIAUTOMATOR,
                'new UiScrollable(new UiSelector().scrollable(true).instance(0))'
                '.scrollIntoView(new UiSelector().textContains("미리보기").instance(0));'
            )
            time.sleep(1)
            
            # 전체동의 체크박스 클릭
            # preview_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'preview_btn')))
            # preview_btn.click()
            # time.sleep(1)
            
            # 등록완료 버튼 클릭
            # registration_complete_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'registration_complete_btn')))
            registration_complete_btn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, '등록완료')
            registration_complete_btn.click()
            time.sleep(1)
            
            # 토스트 메세지 분석
            try:
                toast_message = wait.until(EC.presence_of_element_located(self._get_locator(driver, 'toast_message2')))
                msg = toast_message.get_attribute("text")
                assert msg == "완료!"
                print(f"두번째 이력서 등록완료 토스트 메세지: {msg}, {toast_message.is_displayed()}")
            except:
                print("두번째 이력서 등록완료 토스트 메세지를 찾을 수 없습니다")
                pytest.fail("간병가사동행 이력서 등록완료시 뜨는 토스트 메세지가 정상적이지 않음")
            
        except Exception as e:
            pytest.fail(f"내 정보관리 및 이력서 관리 테스트 실패: {str(e)}")
    
    def test_deposit_withdrawal_and_account_management(self, driver_setup):
        """홈화면 → 바텀 메뉴에서 마이 페이지 클릭 → 입출금내역 → 계좌관리 → 계좌등록 → 이체하기 테스트"""
        if isinstance(driver_setup, dict):
            driver = driver_setup['driver']
        else:
            driver = driver_setup
        wait = WebDriverWait(driver, 10)
        
        try:
            time.sleep(2)
            
            # 바텀 메뉴에서 마이 페이지 클릭
            bottom_my_page_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'bottom_my_page_btn')))
            bottom_my_page_btn.click()
            time.sleep(1)
            
            # 입출금내역 버튼 클릭
            # deposit_withdrawal_history_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'deposit_withdrawal_history_btn')))
            deposit_withdrawal_history_btn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, '입출금내역')
            deposit_withdrawal_history_btn.click()
            time.sleep(1)
            
            # 계좌관리 버튼 클릭
            # account_management_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'account_management_btn')))
            account_management_btn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, '계좌관리')
            account_management_btn.click()
            time.sleep(1)
            
            # 계좌등록 버튼 클릭
            # account_registration_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'account_registration_btn')))
            account_registration_btn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, '계좌 등록')
            account_registration_btn.click()
            time.sleep(1)
            
            # 통장별명 인풋에 입금 통장 넣기
            account_nickname_input = wait.until(EC.presence_of_element_located(self._get_locator(driver, 'account_nickname_input')))
            account_nickname_input.clear()
            account_nickname_input.send_keys("입금 통장")
            time.sleep(1)
            
            # 은행선택 드롭다운 클릭
            bank_selection_dropdown = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'bank_selection_dropdown')))
            bank_selection_dropdown.click()
            time.sleep(1)
            
            # 기업은행 클릭
            # ibk_bank_option = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'ibk_bank_option')))
            ibk_bank_option = driver.find_element(AppiumBy.ACCESSIBILITY_ID, '기업은행')
            ibk_bank_option.click()
            time.sleep(1)
            
            # 등록 계좌번호 인풋에 01092205162 넣기
            account_number_input = wait.until(EC.presence_of_element_located(self._get_locator(driver, 'account_number_input')))
            account_number_input.clear()
            account_number_input.send_keys("01092205162")
            time.sleep(1)
            
            # 등록하기 버튼 클릭 (화면에 그대로 남아있는지 확인 그대로 남아있을경우 테스트 실패로 간주)
            # register_account_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'register_account_btn')))
            register_account_btn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, '등록하기')
            register_account_btn.click()
            time.sleep(2)
            
            # 화면에 그대로 남아있는지 확인
            try:
                still_on_screen = driver.find_elements(*self._get_locator(driver, 'register_account_btn'))
                if len(still_on_screen) > 0:
                    pytest.fail("등록하기 버튼 클릭 후 화면이 변경되지 않았습니다 - 테스트 실패")
            except:
                pass  # 화면이 변경되었으므로 정상
            
            # 토스트메세지 분석
            try:
                toast_message = wait.until(EC.presence_of_element_located(self._get_locator(driver, 'toast_message2')))
                print(f"계좌등록 토스트 메세지: {toast_message.text}")
            except:
                print("계좌등록 토스트 메세지를 찾을 수 없습니다")
            
            # 뒤로 가기 버튼 클릭
            # back_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'back_btn_general')))
            # back_btn.click()
            # time.sleep(1)
            driver.back()
            driver.back()
            
            # 이체하기 버튼 클릭
            # transfer_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'transfer_btn')))
            transfer_btn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, '이체하기')
            transfer_btn.click()
            time.sleep(1)
            
            # 모달이 있을 경우 모달 내용 분석
            try:
                modal_content = wait.until(EC.presence_of_element_located(self._get_locator(driver, 'modal_content')))
                print(f"이체하기 모달 내용: {modal_content.text}")
                
                # 확인 버튼 클릭
                modal_confirm_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'modal_confirm_btn')))
                modal_confirm_btn.click()
                time.sleep(1)
            except:
                print("모달이 표시되지 않았습니다")
                # 모달이없을경우 뒤로가기 버튼 클릭
                # back_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'back_btn_general')))
                # back_btn.click()
                # time.sleep(1)
                driver.back()
            
            # 뒤로가기 버튼 클릭
            # back_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'back_btn_general')))
            # back_btn.click()
            # time.sleep(1)
            driver.back()
            
        except Exception as e:
            pytest.fail(f"입출금내역 및 계좌관리 테스트 실패: {str(e)}")
    
    def test_account_management_only(self, driver_setup):
        """홈화면 → 바텀 메뉴에서 마이 페이지 클릭 → 계좌관리 → 계좌등록 테스트"""
        if isinstance(driver_setup, dict):
            driver = driver_setup['driver']
        else:
            driver = driver_setup
        wait = WebDriverWait(driver, 10)
        
        try:
            time.sleep(2)
            
            # 바텀 메뉴에서 마이 페이지 클릭
            bottom_my_page_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'bottom_my_page_btn')))
            bottom_my_page_btn.click()
            time.sleep(1)
            
            # 계좌관리 버튼 클릭
            # account_management_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'account_management_btn')))
            account_management_btn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, '계좌관리')
            account_management_btn.click()
            time.sleep(1)
            
            # 계좌등록 버튼 클릭
            # account_registration_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'account_registration_btn')))
            account_registration_btn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, '계좌 등록')
            account_registration_btn.click()
            time.sleep(1)
            
            # 통장별명 인풋에 입금 통장 넣기
            account_nickname_input = wait.until(EC.presence_of_element_located(self._get_locator(driver, 'account_nickname_input')))
            account_nickname_input.clear()
            account_nickname_input.send_keys("입금 통장")
            time.sleep(1)
            
            # 은행선택 드롭다운 클릭
            bank_selection_dropdown = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'bank_selection_dropdown')))
            # bank_selection_dropdown = driver.find_element(AppiumBy.ACCESSIBILITY_ID, '은행선택')
            bank_selection_dropdown.click()
            time.sleep(1)
            
            # 기업은행 클릭
            # ibk_bank_option = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'ibk_bank_option')))
            ibk_bank_option = driver.find_element(AppiumBy.ACCESSIBILITY_ID, '기업은행')
            ibk_bank_option.click()
            time.sleep(1)
            
            # 등록 계좌번호 인풋에 01092205162 넣기
            account_number_input = wait.until(EC.presence_of_element_located(self._get_locator(driver, 'account_number_input')))
            account_number_input.clear()
            account_number_input.send_keys("01092205162")
            time.sleep(1)
            
            # 등록하기 버튼 클릭 (화면에 그대로 남아있는지 확인 그대로 남아있을경우 테스트 실패로 간주)
            # register_account_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'register_account_btn')))
            register_account_btn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, '등록하기')
            register_account_btn.click()
            time.sleep(2)
            
            # 화면에 그대로 남아있는지 확인
            try:
                still_on_screen = driver.find_elements(*self._get_locator(driver, 'register_account_btn'))
                if len(still_on_screen) > 0:
                    pytest.fail("등록하기 버튼 클릭 후 화면이 변경되지 않았습니다 - 테스트 실패")
            except:
                pass  # 화면이 변경되었으므로 정상
            
            # 토스트메세지 분석
            try:
                toast_message = wait.until(EC.presence_of_element_located(self._get_locator(driver, 'toast_message2')))
                print(f"계좌등록 토스트 메세지: {toast_message.text} {toast_message.is_displayed()}")
            except:
                print("계좌등록 토스트 메세지를 찾을 수 없습니다")
            
            # 뒤로 가기 버튼 클릭
            driver.back()
            
        except Exception as e:
            pytest.fail(f"계좌관리 테스트 실패: {str(e)}")
    
    def test_transfer_and_account_registration(self, driver_setup):
        """홈화면 → 바텀 메뉴에서 마이 페이지 클릭 → 이체하기 → 계좌등록 테스트"""
        if isinstance(driver_setup, dict):
            driver = driver_setup['driver']
        else:
            driver = driver_setup
        wait = WebDriverWait(driver, 10)
        
        try:
            time.sleep(2)
            
            # 바텀 메뉴에서 마이 페이지 클릭
            bottom_my_page_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'bottom_my_page_btn')))
            bottom_my_page_btn.click()
            time.sleep(1)
            
            # 이체하기 버튼 클릭
            # transfer_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'transfer_btn')))
            transfer_btn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, '이체하기')
            transfer_btn.click()
            time.sleep(1)
            
            # 계좌등록 버튼 클릭
            # account_registration_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'account_registration_btn')))
            account_registration_btn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, '계좌 등록')
            account_registration_btn.click()
            time.sleep(1)
            
            # 통장별명 인풋에 입금 통장 넣기
            account_nickname_input = wait.until(EC.presence_of_element_located(self._get_locator(driver, 'account_nickname_input')))
            account_nickname_input.clear()
            account_nickname_input.send_keys("입금 통장")
            time.sleep(1)
            
            # 은행선택 드롭다운 클릭
            bank_selection_dropdown = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'bank_selection_dropdown')))
            bank_selection_dropdown.click()
            time.sleep(1)
            
            # 기업은행 클릭
            # ibk_bank_option = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'ibk_bank_option')))
            ibk_bank_option = driver.find_element(AppiumBy.ACCESSIBILITY_ID, '기업은행')
            ibk_bank_option.click()
            time.sleep(1)
            
            # 등록 계좌번호 인풋에 01092205162 넣기
            account_number_input = wait.until(EC.presence_of_element_located(self._get_locator(driver, 'account_number_input')))
            account_number_input.clear()
            account_number_input.send_keys("01092205162")
            time.sleep(1)
            
            # 등록하기 버튼 클릭 (화면에 그대로 남아있는지 확인 그대로 남아있을경우 테스트 실패로 간주)
            # register_account_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'register_account_btn')))
            register_account_btn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, '등록하기')
            register_account_btn.click()
            time.sleep(2)
            
            # 화면에 그대로 남아있는지 확인
            try:
                still_on_screen = driver.find_elements(*self._get_locator(driver, 'register_account_btn'))
                if len(still_on_screen) > 0:
                    pytest.fail("등록하기 버튼 클릭 후 화면이 변경되지 않았습니다 - 테스트 실패")
            except:
                pass  # 화면이 변경되었으므로 정상
            
            # 토스트메세지 분석
            try:
                toast_message = wait.until(EC.presence_of_element_located(self._get_locator(driver, 'toast_message2')))
                print(f"계좌등록 토스트 메세지: {toast_message.text}")
            except:
                print("계좌등록 토스트 메세지를 찾을 수 없습니다")
            
            # 뒤로 가기 버튼 클릭
            # back_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'back_btn_general')))
            # back_btn.click()
            # time.sleep(1)
            driver.back()
            driver.back()
            
        except Exception as e:
            pytest.fail(f"이체하기 및 계좌등록 테스트 실패: {str(e)}")
    
    def test_general_matching_info_management(self, driver_setup):
        """홈화면 → 바텀 메뉴에서 마이 페이지 클릭 → 일반 매칭정보 관리 테스트"""
        if isinstance(driver_setup, dict):
            driver = driver_setup['driver']
        else:
            driver = driver_setup
        wait = WebDriverWait(driver, 10)
        
        try:
            time.sleep(2)
            
            # 바텀 메뉴에서 마이 페이지 클릭
            bottom_my_page_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'bottom_my_page_btn')))
            bottom_my_page_btn.click()
            time.sleep(1)
            
            # 일반 매칭정보 관리 버튼 클릭
            general_matching_info_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'general_matching_info_btn')))
            general_matching_info_btn.click()
            time.sleep(1)
            
            # 선택완료 버튼 클릭
            # selection_complete_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'selection_complete_btn')))
            selection_complete_btn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, '선택완료')
            selection_complete_btn.click()
            time.sleep(1)

            # 토스트 메세지 분석
            try:
                toast_message = wait.until(EC.presence_of_element_located(self._get_locator(driver, 'toast_message2')))
                msg = toast_message.get_attribute("text")
                assert msg == "완료!"
                print(f"일반 매칭정보 관리 설정 메세지: {msg}, {toast_message.is_displayed()}")
            except:
                print("일반 매칭정보 관리 설정 토스트 메세지를 찾을 수 없습니다")
                pytest.fail("일반 매칭정보 관리 설정 완료시 뜨는 토스트 메세지가 정상적이지 않음")
            
        except Exception as e:
            pytest.fail(f"일반 매칭정보 관리 테스트 실패: {str(e)}")
    
    def test_caregiver_job_matching_management(self, driver_setup):
        """홈화면 → 바텀 메뉴에서 마이 페이지 클릭 → 간병 일자리 맞춤매칭 관리 테스트"""
        if isinstance(driver_setup, dict):
            driver = driver_setup['driver']
        else:
            driver = driver_setup
        wait = WebDriverWait(driver, 10)
        
        try:
            time.sleep(2)
            
            # 바텀 메뉴에서 마이 페이지 클릭
            bottom_my_page_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'bottom_my_page_btn')))
            bottom_my_page_btn.click()
            time.sleep(1)
            
            # 간병 일자리 맞춤매칭 관리 버튼 클릭
            caregiver_job_matching_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'caregiver_job_matching_btn')))
            caregiver_job_matching_btn.click()
            time.sleep(1)
            
            # 첫번째 항목의 편집 아이콘 클릭
            first_edit_icon = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'first_edit_icon')))
            first_edit_icon.click()
            time.sleep(1)
            
            # 종로구 체크박스 클릭
            # jongro_gu_checkbox = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'jongro_gu_checkbox')))
            jongro_gu_checkbox = driver.find_element(AppiumBy.ACCESSIBILITY_ID, '종로구')
            jongro_gu_checkbox.click()
            time.sleep(0.5)
            
            # 용산구 체크박스 클릭
            # yongsan_gu_checkbox = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'yongsan_gu_checkbox')))
            yongsan_gu_checkbox = driver.find_element(AppiumBy.ACCESSIBILITY_ID, '용산구')
            yongsan_gu_checkbox.click()
            time.sleep(0.5)
            
            # 성동구 체크박스 클릭
            # seongdong_gu_checkbox = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'seongdong_gu_checkbox')))
            seongdong_gu_checkbox = driver.find_element(AppiumBy.ACCESSIBILITY_ID, '성동구')
            seongdong_gu_checkbox.click()
            time.sleep(0.5)
            
            # 광진구 체크박스 클릭
            # gwangjin_gu_checkbox = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'gwangjin_gu_checkbox')))
            gwangjin_gu_checkbox = driver.find_element(AppiumBy.ACCESSIBILITY_ID, '광진구')
            gwangjin_gu_checkbox.click()
            time.sleep(0.5)
            
            # 등록완료 버튼 클릭
            # registration_complete_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'registration_complete_btn')))
            registration_complete_btn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, '등록완료')
            registration_complete_btn.click()
            time.sleep(1)
            
            # 두번째 항목의 편집 아이콘 클릭
            second_edit_icon = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'second_edit_icon')))
            second_edit_icon.click()
            time.sleep(1)
            
            # 일정초기화 버튼 클릭
            # schedule_reset_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'schedule_reset_btn')))
            schedule_reset_btn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, '일정초기화')
            schedule_reset_btn.click()
            time.sleep(0.5)
            
            # 월 버튼 클릭
            # monday_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'monday_btn')))
            monday_btn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, '월')
            monday_btn.click()
            time.sleep(0.5)
            
            # 화 버튼 클릭
            # tuesday_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'tuesday_btn')))
            tuesday_btn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, '화')
            tuesday_btn.click()
            time.sleep(0.5)
            
            # 수 버튼 클릭
            # wednesday_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'wednesday_btn')))
            wednesday_btn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, '수')
            wednesday_btn.click()
            time.sleep(0.5)
            
            # 목 버튼 클릭
            # thursday_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'thursday_btn')))
            thursday_btn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, '목')
            thursday_btn.click()
            time.sleep(0.5)
            
            # 금 버튼 클릭
            # friday_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'friday_btn')))
            friday_btn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, '금')
            friday_btn.click()
            time.sleep(0.5)
                        
            # 스크롤해서 아래로 내려가서 이전 버튼 클릭
            driver.find_element(
                AppiumBy.ANDROID_UIAUTOMATOR,
                'new UiScrollable(new UiSelector().scrollable(true).instance(0))'
                '.scrollIntoView(new UiSelector().textContains("이전").instance(0));'
            )
            time.sleep(1)

            # 등록완료 버튼 클릭
            # registration_complete_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'registration_complete_btn')))
            registration_complete_btn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, '등록완료')
            registration_complete_btn.click()
            time.sleep(1)
                        
            # 스크롤해서 아래로 내려가서 등록완료 버튼 클릭
            driver.find_element(
                AppiumBy.ANDROID_UIAUTOMATOR,
                'new UiScrollable(new UiSelector().scrollable(true).instance(0))'
                '.scrollIntoView(new UiSelector().textContains("등록완료").instance(0));'
            )
            time.sleep(1)
            
            # 세번째 항목의 편집 아이콘 클릭
            third_edit_icon = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'third_edit_icon')))
            third_edit_icon.click()
            time.sleep(1)
            
            # 피딩 버튼 클릭
            # feeding_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'feeding_btn')))
            feeding_btn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, '피딩')
            feeding_btn.click()
            time.sleep(0.5)
            
            # 마비 버튼 클릭
            # paralysis_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'paralysis_btn')))
            paralysis_btn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, '마비')
            paralysis_btn.click()
            time.sleep(0.5)
            
            # 욕창 버튼 클릭
            # bedsore_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'bedsore_btn')))
            bedsore_btn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, '욕창')
            bedsore_btn.click()
            time.sleep(0.5)
            
            # 기저귀 케어 버튼 클릭
            # diaper_care_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'diaper_care_btn')))
            diaper_care_btn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, '기저귀 케어')
            diaper_care_btn.click()
            time.sleep(0.5)
            
            # 의사소통어려움 버튼 클릭
            # communication_difficulty_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'communication_difficulty_btn')))
            communication_difficulty_btn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, '의사소통어려움')
            communication_difficulty_btn.click()
            time.sleep(0.5)
            
            # 등록완료 버튼 클릭
            # registration_complete_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'registration_complete_btn')))
            registration_complete_btn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, '등록완료')
            registration_complete_btn.click()
            time.sleep(1)
                      
            # 스크롤해서 아래로 내려가서 등록완료 버튼 클릭
            driver.find_element(
                AppiumBy.ANDROID_UIAUTOMATOR,
                'new UiScrollable(new UiSelector().scrollable(true).instance(0))'
                '.scrollIntoView(new UiSelector().textContains("등록완료").instance(0));'
            )
            time.sleep(1)
            
            # 네번째 항목의 편집 아이콘 클릭
            # fourth_edit_icon = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'fourth_edit_icon')))
            fourth_edit_icon = driver.find_element(*self._get_locator(driver, 'fourth_edit_icon'))
            fourth_edit_icon.click()
            time.sleep(1)
            
            # 진행안함 버튼 클릭
            # no_proceed_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'no_proceed_btn')))
            no_proceed_btn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, '진행안함')
            no_proceed_btn.click()
            time.sleep(0.5)
            
            # PCR 버튼 클릭
            # pcr_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'pcr_btn')))
            pcr_btn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'PCR')
            pcr_btn.click()
            time.sleep(0.5)
            
            # 등록완료 버튼 클릭
            # registration_complete_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'registration_complete_btn')))
            registration_complete_btn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, '등록완료')
            registration_complete_btn.click()
            time.sleep(1)
                  
            # 스크롤해서 아래로 내려가서 등록완료 버튼 클릭
            driver.find_element(
                AppiumBy.ANDROID_UIAUTOMATOR,
                'new UiScrollable(new UiSelector().scrollable(true).instance(0))'
                '.scrollIntoView(new UiSelector().textContains("등록완료").instance(0));'
            )
            time.sleep(1)
            
            # 등록완료 버튼 클릭 (최종)
            registration_complete_btn2 = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'registration_complete_btn')))
            # registration_complete_btn2 = driver.find_element(AppiumBy.ACCESSIBILITY_ID, '등록완료')
            registration_complete_btn2.click()
            time.sleep(1)
            
            # 토스트 메세지 분석
            try:
                toast_message = wait.until(EC.presence_of_element_located(self._get_locator(driver, 'toast_message2')))
                msg = toast_message.get_attribute("text")
                assert msg == "완료!"
                print(f"간병 일자리 맞춤매칭 관리 토스트 메세지: {msg}")
            except:
                print("간병 일자리 맞춤매칭 관리 토스트 메세지를 찾을 수 없습니다")
                pytest.fail("간병 일자리 맞춤매칭 관리 설정 완료시 뜨는 토스트 메세지가 정상적이지 않음")
            
        except Exception as e:
            pytest.fail(f"간병 일자리 맞춤매칭 관리 테스트 실패: {str(e)}")
    
    def test_application_status_management(self, driver_setup):
        """홈화면 → 바텀 메뉴에서 마이 페이지 클릭 → 지원현황 → 취소하기 → 지원내역 삭제 테스트"""
        if isinstance(driver_setup, dict):
            driver = driver_setup['driver']
        else:
            driver = driver_setup
        wait = WebDriverWait(driver, 10)
        
        try:
            time.sleep(2)
            
            # 바텀 메뉴에서 마이 페이지 클릭
            bottom_my_page_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'bottom_my_page_btn')))
            bottom_my_page_btn.click()
            time.sleep(1)
            
            # 지원현황 버튼 클릭
            application_status_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'application_status_btn')))
            application_status_btn.click()
            time.sleep(1)
            
            # 첫번째 항목의 취소하기 버튼 클릭
            first_cancel_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'first_cancel_btn')))
            first_cancel_btn.click()
            time.sleep(1)
                      
            # 스크롤해서 아래로 내려가서 등록완료 버튼 클릭
            driver.find_element(
                AppiumBy.ANDROID_UIAUTOMATOR,
                'new UiScrollable(new UiSelector().scrollable(true).instance(0))'
                '.scrollIntoView(new UiSelector().textContains("돌아가기").instance(0));'
            )
            time.sleep(1)
            
            # 취소하기 버튼 클릭
            cancel_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'cancel_btn')))
            cancel_btn.click()
            time.sleep(1)
            
            # 첫번째 항목의 지원내역 삭제 버튼 클릭
            first_delete_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'first_delete_btn')))
            first_delete_btn.click()
            time.sleep(1)
            
            # 진행 버튼 클릭
            # proceed_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'proceed_btn')))
            # proceed_btn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, '진행')
            proceed_btn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, '확인')
            proceed_btn.click()
            time.sleep(1)
            
            # 뒤로가기 버튼 클릭
            # back_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'back_btn_general')))
            # back_btn.click()
            # time.sleep(1)
            driver.back()

        except Exception as e:
            pytest.fail(f"지원현황 관리 테스트 실패: {str(e)}")
    
    def test_position_proposal_and_resume_update(self, driver_setup):
        """홈화면 → 바텀 메뉴에서 마이 페이지 클릭 → 포지션제안 버튼 클릭 → 이력서 업데이트 버튼 클릭 → 스크롤 내려서 수정하기 버튼 클릭 → 전문분야 인풋에 인사과 자동화 테스트중22 넣기 → 완료 버튼 클릭 → 토스트 메세지 분석 → 포지션 제안 설정 버튼 클릭 → 후순 포지션이 있다면 제안 받을래요 체크박스 클릭 → 설정완료 버튼 클릭 → 토스트 메세지 분석 → 뒤로가기 버튼 클릭"""
        if isinstance(driver_setup, dict):
            driver = driver_setup['driver']
        else:
            driver = driver_setup
        wait = WebDriverWait(driver, 10)
        
        try:
            time.sleep(2)
            
            # 바텀 메뉴에서 마이 페이지 클릭
            bottom_my_page_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'bottom_my_page_btn')))
            bottom_my_page_btn.click()
            time.sleep(1)
            
            # 스크롤 내려서 학습자료실 버튼 클릭
            driver.find_element(
                AppiumBy.ANDROID_UIAUTOMATOR,
                'new UiScrollable(new UiSelector().scrollable(true).instance(0))'
                '.scrollIntoView(new UiSelector().textContains("학습자료실").instance(0));'
            )
            time.sleep(1)
            
            # 포지션제안 버튼 클릭
            position_proposal_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'position_proposal_btn')))
            position_proposal_btn.click()
            time.sleep(1)
            
            # 이력서 업데이트 버튼 클릭
            # resume_update_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'resume_update_btn')))
            resume_update_btn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, '이력서 업데이트')
            resume_update_btn.click()
            time.sleep(1)
            
            # 스크롤 내려서 수정하기 버튼 클릭
            driver.find_element(
                AppiumBy.ANDROID_UIAUTOMATOR,
                'new UiScrollable(new UiSelector().scrollable(true).instance(0))'
                '.scrollIntoView(new UiSelector().textContains("수정하기").instance(0));'
            )
            time.sleep(1)
            
            # 수정하기 버튼 클릭
            # edit_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'edit_btn')))
            edit_btn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, '수정하기')
            edit_btn.click()
            time.sleep(1)
            
            # 스크롤 내려서 수정하기 버튼 클릭
            driver.find_element(
                AppiumBy.ANDROID_UIAUTOMATOR,
                'new UiScrollable(new UiSelector().scrollable(true).instance(0))'
                '.scrollIntoView(new UiSelector().textContains("친절함").instance(0));'
            )
            time.sleep(1)
            
            # 전문분야 인풋에 인사과 자동화 테스트중22 넣기
            specialty_input = wait.until(EC.presence_of_element_located(self._get_locator(driver, 'specialty_input')))
            specialty_input.clear()
            specialty_input.send_keys("인사과 자동화 테스트중22")
            time.sleep(1)
            
            # 스크롤 내려서 수정하기 버튼 클릭
            driver.find_element(
                AppiumBy.ANDROID_UIAUTOMATOR,
                'new UiScrollable(new UiSelector().scrollable(true).instance(0))'
                '.scrollIntoView(new UiSelector().textContains("완료").instance(0));'
            )
            time.sleep(1)
            
            # 완료 버튼 클릭
            # complete_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'complete_btn')))
            complete_btn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, '완료')
            complete_btn.click()
            time.sleep(1)
            
            # 토스트 메세지 분석
            try:
                toast_message = wait.until(EC.presence_of_element_located(self._get_locator(driver, 'toast_message2')))
                msg = toast_message.get_attribute("text")
                assert msg == "완료!"
                print(f"이력서 업데이트 토스트 메세지: {msg}")
            except:
                pytest.fail("이력서 업데이트 토스트 메세지가 정상적이지 않음")
                print("이력서 업데이트 토스트 메세지를 찾을 수 없습니다")
            
            # 포지션 제안 설정 버튼 클릭
            # position_proposal_setting_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'position_proposal_setting_btn')))
            position_proposal_setting_btn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, '포지션 제안 설정')
            position_proposal_setting_btn.click()
            time.sleep(1)
            
            # 후순 포지션이 있다면 제안 받을래요 체크박스 클릭
            receive_proposal_checkbox = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'receive_proposal_checkbox')))
            receive_proposal_checkbox.click()
            time.sleep(1)
            
            # 설정완료 버튼 클릭
            # setting_complete_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'setting_complete_btn')))
            setting_complete_btn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, '설정완료')
            setting_complete_btn.click()
            # time.sleep(1)
            
            # 토스트 메세지 분석
            try:
                toast_message = wait.until(EC.presence_of_element_located(self._get_locator(driver, 'position_proposal_toast_message')))
                msg = toast_message.get_attribute("text")
                assert msg == "수정이 완료되었습니다!"
                print(f"포지션 제안 설정 토스트 메세지: {msg}")
            except:
                pytest.fail("포지션 제안 설정 토스트 메세지가 정상적이지 않음")
                print("포지션 제안 설정 토스트 메세지를 찾을 수 없습니다")
            
            # 뒤로가기 버튼 클릭
            driver.back()
            # time.sleep(1)
            
        except Exception as e:
            pytest.fail(f"포지션제안 및 이력서 업데이트 테스트 실패: {str(e)}")
    
    def test_scraped_jobs_management(self, driver_setup):
        """홈화면 → 바텀 메뉴에서 마이 페이지 클릭 → 스크랩 공고 버튼 클릭 → 첫번째 항목의 별 버튼 클릭 → 토스트 메세지 분석 → 뒤로가기 버튼 클릭"""
        if isinstance(driver_setup, dict):
            driver = driver_setup['driver']
        else:
            driver = driver_setup
        wait = WebDriverWait(driver, 10)
        
        try:
            time.sleep(2)
            
            # 바텀 메뉴에서 마이 페이지 클릭
            bottom_my_page_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'bottom_my_page_btn')))
            bottom_my_page_btn.click()
            time.sleep(1)
            
            # 스크롤 내려서 학습자료실 버튼 클릭
            driver.find_element(
                AppiumBy.ANDROID_UIAUTOMATOR,
                'new UiScrollable(new UiSelector().scrollable(true).instance(0))'
                '.scrollIntoView(new UiSelector().textContains("학습자료실").instance(0));'
            )
            time.sleep(1)
            
            # 스크랩 공고 버튼 클릭
            scraped_jobs_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'scraped_jobs_btn')))
            scraped_jobs_btn.click()
            time.sleep(1)
            
            # 첫번째 항목의 별 버튼 클릭
            # first_star_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'first_star_btn')))
            first_star_btn = driver.find_element(*self._get_locator(driver, 'first_star_btn'))
            first_star_btn.click()
            time.sleep(1)
            
            # 토스트 메세지 분석
            try:
                toast_message = wait.until(EC.presence_of_element_located(self._get_locator(driver, 'scraped_toast_message')))
                msg = toast_message.get_attribute("text")
                assert msg == "이 공고를 즐겨찾기 목록에서 제거했습니다!"
                print(f"스크랩 공고 별 버튼 토스트 메세지: {msg}")
            except:
                pytest.fail("스크랩 공고 별 버튼 토스트 메세지가 정상적이지 않음")
                print("스크랩 공고 별 버튼 토스트 메세지를 찾을 수 없습니다")
            
            # 뒤로가기 버튼 클릭
            driver.back()
            # time.sleep(1)
            
        except Exception as e:
            pytest.fail(f"스크랩 공고 관리 테스트 실패: {str(e)}")
    
    def test_favorite_companies_management(self, driver_setup):
        """홈화면 → 바텀 메뉴에서 마이 페이지 클릭 → 관심기업 버튼 클릭 → 첫번째 항목의 하트 버튼 클릭 → 토스트 메세지 분석 → 뒤로가기 버튼 클릭"""
        if isinstance(driver_setup, dict):
            driver = driver_setup['driver']
        else:
            driver = driver_setup
        wait = WebDriverWait(driver, 10)
        
        try:
            time.sleep(2)
            
            # 바텀 메뉴에서 마이 페이지 클릭
            bottom_my_page_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'bottom_my_page_btn')))
            bottom_my_page_btn.click()
            time.sleep(1)
            
            # 스크롤 내려서 학습자료실 버튼 클릭
            driver.find_element(
                AppiumBy.ANDROID_UIAUTOMATOR,
                'new UiScrollable(new UiSelector().scrollable(true).instance(0))'
                '.scrollIntoView(new UiSelector().textContains("학습자료실").instance(0));'
            )
            time.sleep(1)
            
            # 관심기업 버튼 클릭
            favorite_companies_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'favorite_companies_btn')))
            favorite_companies_btn.click()
            time.sleep(1)
            
            # 첫번째 항목의 하트 버튼 클릭
            # first_company_heart_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'first_company_heart_btn')))
            first_company_heart_btn = driver.find_element(*self._get_locator(driver, 'first_company_heart_btn'))
            first_company_heart_btn.click()
            time.sleep(1)
            
            # 토스트 메세지 분석
            try:
                toast_message = wait.until(EC.presence_of_element_located(self._get_locator(driver, 'favorite_toast_message')))
                msg = toast_message.get_attribute("text")
                assert msg == "이 시설을 즐겨찾기 목록에서 제거했습니다!"
                print(f"관심기업 하트 버튼 토스트 메세지: {msg}")
            except:
                pytest.fail("관심기업 하트 버튼 토스트 메세지가 정상적이지 않음")
                print("관심기업 하트 버튼 토스트 메세지를 찾을 수 없습니다")
            
            # 뒤로가기 버튼 클릭
            driver.back()
            # time.sleep(1)
            
        except Exception as e:
            pytest.fail(f"관심기업 관리 테스트 실패: {str(e)}")