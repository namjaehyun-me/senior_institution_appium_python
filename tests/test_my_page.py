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
                'pay_ment_first_notice_item': (AppiumBy.XPATH, '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup'),
                'error_first_notice_item': (AppiumBy.XPATH, '//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[1]'),
                'event_first_notice_item': (AppiumBy.XPATH, '//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[1]'),
                'fnq_first_notice_item': (AppiumBy.XPATH, '//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[1]'),
                'fnq_first_notice_item2': (AppiumBy.XPATH, '//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[1]'),
                'faq_btn': (AppiumBy.XPATH, '//android.widget.TextView[@text="자주 묻는 질문"]'),
                'faq_search_input': (AppiumBy.XPATH, '//android.widget.EditText[@text="궁금한 내용을 검색하세요"]'),
                'search_btn': (AppiumBy.XPATH, '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup[4]/android.view.ViewGroup/com.horcrux.svg.SvgView/com.horcrux.svg.GroupView'),
                'event_btn': (AppiumBy.XPATH, '//android.widget.TextView[@text="이벤트"]'),
                'customer_center_btn': (AppiumBy.XPATH, '//android.widget.TextView[@text="고객센터"]'),
                'kakao_btn': (AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="카카오톡으로 상담하기, 카카오톡 오픈"]/android.view.ViewGroup'),
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
                'reCAPTCHA': (AppiumBy.XPATH, '//android.view.View[@text="reCAPTCHA"]'),
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
                'category_button1': (AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="채널명테스트!"]/android.view.ViewGroup'),
                'category_button2': (AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="시작하기"]/android.view.ViewGroup'),
                'list_item': (AppiumBy.XPATH, '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup'),
                'list_item_youtube': (AppiumBy.XPATH, '//android.widget.Button[@text="Play video"]'),
                # 새로운 시나리오 로케이터들
                'my_resume_btn': (AppiumBy.XPATH, '//android.widget.TextView[@text="내 이력서"]'),
                'first_resume_item': (AppiumBy.XPATH, '//android.widget.TextView[@text="사회복지사/요양보호사"]'),
                'second_resume_item': (AppiumBy.XPATH, '//android.widget.TextView[@text="간병/가사/동행"]'),
                'detail_address_input_4floor1': (AppiumBy.XPATH, '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup[11]'),
                'detail_address_input_4floor2': (AppiumBy.XPATH, '//android.widget.EditText[@text="4층"]'),
                'detail_address_input_2floor': (AppiumBy.XPATH, '//android.widget.EditText[@text="상세주소"]'),
                'detail_address_input_3floor': (AppiumBy.XPATH, '//android.widget.EditText[@text="상세 주소"]'),
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
                'list_items_locator':(AppiumBy.XPATH, '//android.widget.TextView[@text="데이터를 찾을 수 없습니다"]'),
                'first_item_receipt_btn':(AppiumBy.XPATH, '(//android.view.ViewGroup[@content-desc="영수증출력"])[1]'),
                'first_item':(AppiumBy.XPATH, '//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[1]'),
                'bottom_menu_proposal_locator':(AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="입소제안"]'),
                'search_input_locator':(AppiumBy.XPATH, '//android.widget.EditText[@text="이름 또는 휴대전화번호"]'),
                'admission_inquiry_btn':(AppiumBy.XPATH, '//android.widget.TextView[@text="입소문의"]'),
                'list_not_have_text': (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("데이터를 찾을 수 없습니다")'),
                'bottom_menu_proposal_locator':(AppiumBy.XPATH, '//android.widget.TextView[@text="입소제안"]'),
                'position_search_input':(AppiumBy.XPATH, '//android.widget.EditText[@text="이름 또는 휴대전화번호"]'),
                'list_items_locator':(AppiumBy.XPATH, '//android.widget.TextView[@text="데이터를 찾을 수 없습니다"]'),
                'bottom_position_proposal_btn': (AppiumBy.XPATH, '(//android.widget.TextView[@text="포지션제안"])[1]'),
                'position_list_items': (AppiumBy.XPATH, "//android.widget.ListView//android.widget.LinearLayout"),
                # 새로운 시나리오 로케이터들
                'member_info_management_btn': (AppiumBy.XPATH, '//android.widget.TextView[@text="회원정보관리"]'),
                'detail_address_input_3floor': (AppiumBy.XPATH, '//android.widget.EditText[@text="상세주소"]'),
                'institution_info_management_btn': (AppiumBy.XPATH, '//android.widget.TextView[@text="기관 정보 관리"]'),
                'greeting_description_input': (AppiumBy.XPATH, '//android.widget.EditText[@text="기관 개요"]'),
                'grade_5_btn': (AppiumBy.XPATH, '//android.widget.TextView[@text="5등급"]'),
                'grade_2_btn': (AppiumBy.XPATH, '//android.widget.TextView[@text="2등급"]'),
                'nature_friendly_btn': (AppiumBy.XPATH, '//android.widget.TextView[@text="자연친화"]'),
                'urban_type_btn': (AppiumBy.XPATH, '//android.widget.TextView[@text="도심형"]'),
                'garden_btn': (AppiumBy.XPATH, '//android.widget.TextView[@text="텍밭"]'),
                'multi_room_btn': (AppiumBy.XPATH, '//android.widget.TextView[@text="다인실"]'),
                'swimming_pool_btn': (AppiumBy.XPATH, '//android.widget.TextView[@text="수영장"]'),
                'gym_btn': (AppiumBy.XPATH, '//android.widget.TextView[@text="헬스장"]'),
                'parking_lot_btn': (AppiumBy.XPATH, '//android.widget.TextView[@text="주차장"]'),
                'monthly_stay_btn': (AppiumBy.XPATH, '//android.widget.TextView[@text="한달살기"]'),
                'nutrition_diet_btn': (AppiumBy.XPATH, '//android.widget.TextView[@text="영양식단"]'),
                'pet_btn': (AppiumBy.XPATH, '//android.widget.TextView[@text="반려동물"]'),
                'input_complete_btn': (AppiumBy.XPATH, '//android.widget.TextView[@text="입력완료"]'),
                'job_management_btn': (AppiumBy.XPATH, '//android.widget.TextView[@text="공고관리"]'),
                'all_btn': (AppiumBy.XPATH, '//android.widget.TextView[@text="전체"]'),
                'progress_btn': (AppiumBy.XPATH, '(//android.widget.TextView[@text="진행"])[1]'),
                'first_job_item': (AppiumBy.XPATH, '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup'),
                'applicant_management_btn': (AppiumBy.XPATH, '//android.widget.TextView[@text="지원지관리"]'),
                'applicant_management_modal': (AppiumBy.XPATH, '//android.widget.TextView[@text="지원자 관리를 위한 2차인증 담당자가 등록되어있지 않습니다. 등록페이지로 이동합니다."]'),
                'closed_btn': (AppiumBy.XPATH, '//android.widget.TextView[@text="마감"]'),
                'copy_btn': (AppiumBy.XPATH, '//android.widget.TextView[@text="복사하기"]'),
                'next_step_btn': (AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="다음 단계"]'),
                'one_month_btn': (AppiumBy.XPATH, '//android.widget.TextView[@text="1개월"]'),
                'job_title_input': (AppiumBy.XPATH, '//android.widget.EditText'),
                'job_registration_complete_btn': (AppiumBy.XPATH, '//android.widget.TextView[@text="공고 등록 완료"]'),
                'all_agree_checkbox': (AppiumBy.XPATH, '//android.widget.TextView[@text="전체 동의"]'),
                'confirm_btn': (AppiumBy.XPATH, '//android.widget.TextView[@text="확인"]'),
                'second_job_item': (AppiumBy.XPATH, '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup'),
                'delete_btn': (AppiumBy.XPATH, '//android.widget.TextView[@text="삭제하기"]'),
                'job_registration_btn': (AppiumBy.XPATH, '//android.widget.TextView[@text="공고등록"]'),
                'care_worker_checkbox': (AppiumBy.XPATH, '//android.widget.TextView[@text="요양보호사"]'),
                'female_checkbox': (AppiumBy.XPATH, '//android.widget.TextView[@text="여성"]'),
                'homeless_checkbox': (AppiumBy.XPATH, '//android.widget.TextView[@text="노숙인"]'),
                'mental_health_checkbox': (AppiumBy.XPATH, '//android.widget.TextView[@text="정신건강"]'),
                'recruitment_count_input': (AppiumBy.XPATH, '//android.widget.EditText[@text="모집인원"]'),
                'experience_irrelevant_checkbox': (AppiumBy.XPATH, '//android.widget.TextView[@text="경력 무관"]'),
                'main_task_input': (AppiumBy.XPATH, '//android.widget.EditText[@text="예) 주요 업무를 입력해주세요."]'),
                'certificate_input': (AppiumBy.XPATH, '//android.widget.EditText[@text="예) 2종보통운전면허"]'),
                'full_time_checkbox': (AppiumBy.XPATH, '//android.widget.TextView[@text="정규직"]'),
                'daily_work_hours_input': (AppiumBy.XPATH, '//android.widget.EditText'),
                'weekly_work_days_dropdown': (AppiumBy.XPATH, '(//android.view.ViewGroup[@content-desc="선택"])[1]'),
                'four_days_btn': (AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="4"]'),
                'salary_dropdown': (AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="선택"]'),
                'monthly_salary_btn': (AppiumBy.XPATH, '//android.widget.TextView[@text="월급"]'),
                'salary_input': (AppiumBy.XPATH, '//android.widget.HorizontalScrollView/android.view.ViewGroup/android.view.ViewGroup[7]/android.widget.EditText'),
                'fifteen_days_btn': (AppiumBy.XPATH, '//android.widget.TextView[@text="15일"]'),
                'job_title_input_urgent': (AppiumBy.XPATH, '//android.widget.EditText[@text="채용제목"]'),
                'more_btn': (AppiumBy.XPATH, '(//android.view.ViewGroup[@content-desc="더보기"])[1]'),
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
                'search_btn': (AppiumBy.XPATH, "//XCUIElementTypeTextField[@name='검색']"),
                'event_btn': (AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='이벤트']"),
                'customer_center_btn': (AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='고객센터']"),
                'kakao_btn': (AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='고객센터']"),
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
                'reCAPTCHA': (AppiumBy.XPATH, "//XCUIElementTypeTextField"),
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
                'list_items_locator': (AppiumBy.XPATH, "(//XCUIElementTypeButton[@name='하트'])[1]"),
                'first_item_receipt_btn': (AppiumBy.XPATH, "(//XCUIElementTypeButton[@name='하트'])[1]"),
                'first_item': (AppiumBy.XPATH, "(//XCUIElementTypeButton[@name='하트'])[1]"),
                'bottom_menu_proposal_locator': (AppiumBy.XPATH, "(//XCUIElementTypeButton[@name='하트'])[1]"),
                'search_input_locator': (AppiumBy.XPATH, "(//XCUIElementTypeButton[@name='하트'])[1]"),
                'admission_inquiry_btn': (AppiumBy.XPATH, "(//XCUIElementTypeButton[@name='하트'])[1]"),
                'list_not_have_text': (AppiumBy.XPATH, "(//XCUIElementTypeButton[@name='하트'])[1]"),
                'bottom_menu_proposal_locator':(AppiumBy.XPATH, "//XCUIElementTypeStaticText[@text='입소제안']"),
                'position_search_input':(AppiumBy.XPATH, "//XCUIElementTypeTextField"),
                'list_items_locator':(AppiumBy.XPATH, "//XCUIElementTypeTable//XCUIElementTypeCell"),
                'bottom_position_proposal_btn': (AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='포지션제안']"),
                'position_search_input': (AppiumBy.XPATH, "//XCUIElementTypeTextField"),
                'position_list_items': (AppiumBy.XPATH, "//XCUIElementTypeTable//XCUIElementTypeCell"),
                # 새로운 시나리오 로케이터들
                'member_info_management_btn': (AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='회원정보관리']"),
                'detail_address_input_3floor': (AppiumBy.XPATH, "//XCUIElementTypeTextField[@name='상세주소']"),
                'institution_info_management_btn': (AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='기관 정보 관리']"),
                'greeting_description_input': (AppiumBy.XPATH, "//XCUIElementTypeTextField[@name='인사-설명']"),
                'grade_5_btn': (AppiumBy.XPATH, "//XCUIElementTypeButton[@name='5등급']"),
                'grade_2_btn': (AppiumBy.XPATH, "//XCUIElementTypeButton[@name='2등급']"),
                'nature_friendly_btn': (AppiumBy.XPATH, "//XCUIElementTypeButton[@name='자연친화']"),
                'urban_type_btn': (AppiumBy.XPATH, "//XCUIElementTypeButton[@name='도심형']"),
                'garden_btn': (AppiumBy.XPATH, "//XCUIElementTypeButton[@name='텍밭']"),
                'multi_room_btn': (AppiumBy.XPATH, "//XCUIElementTypeButton[@name='다인실']"),
                'swimming_pool_btn': (AppiumBy.XPATH, "//XCUIElementTypeButton[@name='수영장']"),
                'gym_btn': (AppiumBy.XPATH, "//XCUIElementTypeButton[@name='헬스장']"),
                'parking_lot_btn': (AppiumBy.XPATH, "//XCUIElementTypeButton[@name='주차장']"),
                'monthly_stay_btn': (AppiumBy.XPATH, "//XCUIElementTypeButton[@name='한달살기']"),
                'nutrition_diet_btn': (AppiumBy.XPATH, "//XCUIElementTypeButton[@name='영양식단']"),
                'pet_btn': (AppiumBy.XPATH, "//XCUIElementTypeButton[@name='반려동물']"),
                'input_complete_btn': (AppiumBy.XPATH, "//XCUIElementTypeButton[@name='입력완료']"),
                'job_management_btn': (AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='공고관리']"),
                'all_btn': (AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='전체']"),
                'progress_btn': (AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='진행']"),
                'first_job_item': (AppiumBy.XPATH, "(//XCUIElementTypeCell)[1]"),
                'applicant_management_btn': (AppiumBy.XPATH, "//XCUIElementTypeButton[@name='지원지관리']"),
                'applicant_management_modal': (AppiumBy.XPATH, "//XCUIElementTypeButton[@name='지원지관리']"),
                'closed_btn': (AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='마감']"),
                'copy_btn': (AppiumBy.XPATH, "//XCUIElementTypeButton[@name='복사하기']"),
                'next_step_btn': (AppiumBy.XPATH, "//XCUIElementTypeButton[@name='다음 단계']"),
                'one_month_btn': (AppiumBy.XPATH, "//XCUIElementTypeButton[@name='1개월']"),
                'job_title_input': (AppiumBy.XPATH, "//XCUIElementTypeTextField"),
                'job_registration_complete_btn': (AppiumBy.XPATH, "//XCUIElementTypeButton[@name='공고 등록 완료']"),
                'all_agree_checkbox': (AppiumBy.XPATH, "//XCUIElementTypeButton[@name='전체동의']"),
                'confirm_btn': (AppiumBy.XPATH, "//XCUIElementTypeButton[@name='확인']"),
                'second_job_item': (AppiumBy.XPATH, "(//XCUIElementTypeCell)[2]"),
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
            }
        }
        
        return locators[platform][element_name]

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
            
            driver.find_element(
                AppiumBy.ANDROID_UIAUTOMATOR,
                'new UiScrollable(new UiSelector().scrollable(true).instance(0))'
                '.scrollIntoView(new UiSelector().textContains("학습자료실").instance(0));'
            )

            # 공지사항 버튼 클릭
            # notice_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'notice_btn')))
            notice_btn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, '공지사항')
            notice_btn.click()
            
            # 목록에 항목이 0개인지 확인
            list_items = driver.find_elements(*self._get_locator(driver, 'list_items_locator'))
            print(f"공지사항 목록 항목 확인 {len(list_items)}")
            if len(list_items) == 0:
                print("목록에 항목 없음")
            else:
                print("목록에 항목 있음")
                # 첫번째 항목 클릭
                # first_notice_item = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'first_notice_item')))
                first_notice_item = driver.find_element(*self._get_locator(driver, 'first_notice_item'))
                first_notice_item.click()
                time.sleep(2)
                
                # 뒤로가기 버튼 클릭
                driver.back()
                
            
            # 뒤로가기 버튼 클릭
            driver.back()
            
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
            # time.sleep(2)
            
            # 바텀 메뉴에서 마이 페이지 클릭
            bottom_my_page_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'bottom_my_page_btn')))
            bottom_my_page_btn.click()

            driver.find_element(
                AppiumBy.ANDROID_UIAUTOMATOR,
                'new UiScrollable(new UiSelector().scrollable(true).instance(0))'
                '.scrollIntoView(new UiSelector().textContains("학습자료실").instance(0));'
            )
            
            # 자주 묻는 질문 버튼 클릭
            # faq_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'faq_btn')))
            faq_btn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, '자주 묻는 질문')
            faq_btn.click()

            # 목록에 항목이 0개인지 확인
            list_items = driver.find_elements(*self._get_locator(driver, 'list_items_locator'))
            print("목록 항목 확인")
            if len(list_items) == 0:
                print("목록에 항목 없음")
            else:
                print("목록에 항목 있음")            
                # 첫번째 항목 클릭
                first_notice_item = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'fnq_first_notice_item')))
                first_notice_item.click()
                time.sleep(2)
            
            # 검색 인풋에 하반기 넣기
            search_input = wait.until(EC.presence_of_element_located(self._get_locator(driver, 'faq_search_input')))
            search_input.clear()
            search_input.send_keys("두번째")

            search_btn = wait.until(EC.presence_of_element_located(self._get_locator(driver, 'search_btn')))
            search_btn.clear()
            
            # 목록에 항목이 0개인지 확인
            list_items = driver.find_elements(*self._get_locator(driver, 'list_items_locator'))
            print("목록 항목 확인")
            if len(list_items) == 0:
                print("목록에 항목 없음")
            else:
                print("목록에 항목 있음")
                # 첫번째 항목 클릭
                first_notice_item = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'fnq_first_notice_item2')))
                first_notice_item.click()
                time.sleep(2)

                # 뒤로가기 버튼 클릭
                driver.back()
            
            # 뒤로가기 버튼 클릭
            driver.back()
            
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
            # time.sleep(2)
            
            # 바텀 메뉴에서 마이 페이지 클릭
            bottom_my_page_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'bottom_my_page_btn')))
            bottom_my_page_btn.click()

            driver.find_element(
                AppiumBy.ANDROID_UIAUTOMATOR,
                'new UiScrollable(new UiSelector().scrollable(true).instance(0))'
                '.scrollIntoView(new UiSelector().textContains("학습자료실").instance(0));'
            )
            
            # 이벤트 버튼 클릭
            # event_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'event_btn')))
            event_btn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, '이벤트')
            event_btn.click()
            
            # 목록에 항목이 0개인지 확인
            list_items = driver.find_elements(*self._get_locator(driver, 'list_items_locator'))
            print("목록 항목 확인")
            if len(list_items) == 0:
                print("목록에 항목 없음")
            else:
                print("목록에 항목 있음")
                # 첫번째 항목 클릭
                first_notice_item = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'event_first_notice_item')))
                first_notice_item.click()
                time.sleep(2)
                
                # 뒤로가기 버튼 클릭
                driver.back()
            
            # 뒤로가기 버튼 클릭
            driver.back()
            
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
            # time.sleep(2)
            
            # 바텀 메뉴에서 마이 페이지 클릭
            bottom_my_page_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'bottom_my_page_btn')))
            bottom_my_page_btn.click()
            
            driver.find_element(
                AppiumBy.ANDROID_UIAUTOMATOR,
                'new UiScrollable(new UiSelector().scrollable(true).instance(0))'
                '.scrollIntoView(new UiSelector().textContains("학습자료실").instance(0));'
            )

            # 고객센터 버튼 클릭
            # customer_center_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'customer_center_btn')))
            customer_center_btn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, '고객센터')
            customer_center_btn.click()

            kakao_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'kakao_btn')))
            # kakao_btn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, '카카오톡 오픈')
            kakao_btn.click()
            time.sleep(1)
            
            # 뒤로가기 버튼 클릭
            driver.back()
            # 뒤로가기 버튼 클릭
            driver.back()
            
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
            # time.sleep(2)
            
            # 바텀 메뉴에서 마이 페이지 클릭
            bottom_my_page_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'bottom_my_page_btn')))
            bottom_my_page_btn.click()
            
            driver.find_element(
                AppiumBy.ANDROID_UIAUTOMATOR,
                'new UiScrollable(new UiSelector().scrollable(true).instance(0))'
                '.scrollIntoView(new UiSelector().textContains("학습자료실").instance(0));'
            )

            # 오류신고센터 버튼 클릭
            # error_report_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'error_report_btn')))
            error_report_btn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, '오류신고센터')
            error_report_btn.click()
            
            # 분류 드롭다운 클릭
            # category_dropdown = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'category_dropdown')))
            category_dropdown = driver.find_element(AppiumBy.ACCESSIBILITY_ID, '분류를 선택해 주세요')
            category_dropdown.click()
            
            # 서비스신청오류 클릭
            # service_error_option = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'service_error_option')))
            service_error_option = wait.until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, '서비스신청오류')))
            service_error_option.click()
            
            driver.find_element(
                AppiumBy.ANDROID_UIAUTOMATOR,
                'new UiScrollable(new UiSelector().scrollable(true).instance(0))'
                '.scrollIntoView(new UiSelector().textContains("사용자님의 의견").instance(0));'
            )

            # 제목 인풋에 오류 테스트중입니다 넣기
            title_input = wait.until(EC.presence_of_element_located(self._get_locator(driver, 'title_input')))
            title_input.clear()
            title_input.send_keys("오류 테스트중입니다")
            
            # 사용자님의 의견 인풋에 오류 테스트중입니다 내용 테스트중입니다 넣기
            opinion_input = wait.until(EC.presence_of_element_located(self._get_locator(driver, 'opinion_input')))
            opinion_input.clear()
            opinion_input.send_keys("오류 테스트중입니다 내용 테스트중입니다")
            
            driver.find_element(
                AppiumBy.ANDROID_UIAUTOMATOR,
                'new UiScrollable(new UiSelector().scrollable(true).instance(0))'
                '.scrollIntoView(new UiSelector().textContains("신고하기").instance(0));'
            )

            # 신고하기 버튼 클릭
            # report_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'report_btn')))
            report_btn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, '신고하기')
            report_btn.click()
            
            # 토스트메세지 분석
            try:
                toast_message = wait.until(EC.presence_of_element_located(self._get_locator(driver, 'toast_message2')))
                msg = toast_message.get_attribute("text")
                assert toast_message.is_displayed(), "완료!"
                print(f"앱 기능 건의함 신고하기 버튼 토스트 메세지: {msg}")
            except:
                pytest.fail("앱 기능 건의함 신고하기 버튼 토스트 메세지가 정상적이지 않음")
                print("앱 기능 건의함 신고하기 버튼 토스트 메세지를 찾을 수 없습니다")
            
            # 목록에 항목이 0개인지 확인
            list_items = driver.find_elements(*self._get_locator(driver, 'list_items_locator'))
            print("목록 항목 확인")
            if len(list_items) == 0:
                print("목록에 항목 없음")
            else:
                print("목록에 항목 있음")
                # 첫번째 항목 클릭
                first_notice_item = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'error_first_notice_item')))
                first_notice_item.click()
                
                # 목록 버튼 클릭
                # list_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'list_btn')))
                list_btn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, '목록')
                list_btn.click()
                
                # 첫번째 항목 클릭
                first_notice_item = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'error_first_notice_item')))
                first_notice_item.click()
                
                # 삭제하기 버튼 클릭
                # delete_report_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'delete_report_btn')))
                delete_report_btn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, '삭제하기')
                delete_report_btn.click()
                
                # 진행 버튼 클릭
                # proceed_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'proceed_btn')))
                proceed_btn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, '진행')
                proceed_btn.click()
                
                # 토스트메세지 분석
                try:
                    toast_message = wait.until(EC.presence_of_element_located(self._get_locator(driver, 'toast_message2')))
                    msg = toast_message.get_attribute("text")
                    assert toast_message.is_displayed(), "완료!"
                    print(f"앱 기능 건의함 삭제하기 버튼 토스트 메세지: {msg}")
                except:
                    pytest.fail("앱 기능 건의함 삭제하기 버튼 토스트 메세지가 정상적이지 않음")
                    print("앱 기능 건의함 삭제하기 버튼 토스트 메세지를 찾을 수 없습니다")
                
            # 오류신고하기 버튼 클릭
            # error_report_create_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'error_report_create_btn')))
            error_report_create_btn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, '오류신고하기')
            error_report_create_btn.click()
            
            # 고객센터 문의하기 버튼 클릭
            # customer_inquiry_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'customer_inquiry_btn')))
            customer_inquiry_btn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, '고객센터 문의하기')
            customer_inquiry_btn.click()
            
            # 뒤로가기 버튼 클릭
            driver.back()
            
            driver.find_element(
                AppiumBy.ANDROID_UIAUTOMATOR,
                'new UiScrollable(new UiSelector().scrollable(true).instance(0))'
                '.scrollIntoView(new UiSelector().textContains("내 신고내역").instance(0));'
            )

            # 내 신고내역 버튼 클릭
            # my_report_history_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'my_report_history_btn')))
            my_report_history_btn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, '내 신고내역')
            my_report_history_btn.click()
            
            # 뒤로가기 버튼 클릭
            driver.back()
            
            # 뒤로가기 버튼 클릭
            driver.back()
            
        except Exception as e:
            pytest.fail(f"오류신고센터 테스트 실패: {str(e)}")
    
    def test_learning_materials(self, driver_setup):
        """학습자료실 테스트"""
        if isinstance(driver_setup, dict):
            driver = driver_setup['driver']
        else:
            driver = driver_setup
        wait = WebDriverWait(driver, 10)
        
        try:
            # time.sleep(2)
            
            # 바텀 메뉴에서 마이 페이지 클릭
            bottom_my_page_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'bottom_my_page_btn')))
            bottom_my_page_btn.click()
            
            driver.find_element(
                AppiumBy.ANDROID_UIAUTOMATOR,
                'new UiScrollable(new UiSelector().scrollable(true).instance(0))'
                '.scrollIntoView(new UiSelector().textContains("학습자료실").instance(0));'
            )

            # 학습자료실 버튼 클릭
            # learning_materials_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'learning_materials_btn')))
            learning_materials_btn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, '학습자료실')
            learning_materials_btn.click()

            # 목록에 항목이 0개인지 확인
            list_items = driver.find_elements(*self._get_locator(driver, 'list_items_locator'))
            print("목록 항목 확인")
            if len(list_items) == 0:
                print("목록에 항목 없음")
            else:
                print("목록에 항목 있음")

                # 2. 카테고리 클릭
                category_button1 = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'category_button1')))
                category_button1.click()

                category_button2 = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'category_button2')))
                category_button2.click()

                # 3-1. 목록 아이템 클릭
                list_item = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'list_item')))
                list_item.click()
                # print("여기까지 왔음1")
                time.sleep(2)

                # 뒤로가기 버튼 클릭
                driver.back()

            # 뒤로가기 버튼 클릭
            driver.back()
            
        except Exception as e:
            pytest.fail(f"학습자료실 테스트 실패: {str(e)}")
    
    def test_product_purchase(self, driver_setup):
        """기업 상품 구매 테스트"""
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
                '.scrollIntoView(new UiSelector().textContains("인증관리").instance(0));'
            )
            time.sleep(0.5)

            # 기업 상품 안내 버튼 클릭
            # product_purchase_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'product_purchase_btn')))
            product_purchase_btn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, '기업 상품 안내')
            product_purchase_btn.click()
            time.sleep(0.5)

            # 채용 열람권 카테고리 클릭
            # product_purchase_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'product_purchase_btn')))
            recruitment_ticket_btn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, '채용열람권')
            recruitment_ticket_btn.click()
            time.sleep(0.5)
            
            # 첫번째 항목 클릭
            first_notice_item = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'pay_ment_first_notice_item')))
            first_notice_item.click()
            time.sleep(0.5)
            
            # 구매하기 버튼 클릭
            # purchase_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'purchase_btn')))
            # purchase_btn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, '구매하기')
            # purchase_btn.click()
            # time.sleep(0.5)
            
            # 결제수단 드롭다운 클릭
            # payment_method_dropdown = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'payment_method_dropdown')))
            payment_method_dropdown = wait.until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, '선택')))
            payment_method_dropdown.click()
            
            # 실시간 계좌이체 클릭
            # bank_transfer_option = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'bank_transfer_option')))
            bank_transfer_option = wait.until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, '실시간 계좌이체')))
            bank_transfer_option.click()
            
            # 전체동의 체크박스 클릭
            # agree_all_checkbox = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'agree_all_checkbox')))
            agree_all_checkbox = wait.until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, '전체동의')))
            agree_all_checkbox.click()

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
            
            # 인풋을 클릭후 92205162 넣기
            phone_input = wait.until(EC.presence_of_element_located(self._get_locator(driver, 'phone_input')))
            phone_input.click()
            phone_input.send_keys("01092205162")

            # 다음 버튼 클릭
            next_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'pay_ment_next_btn')))
            next_btn.click()
            
            reCAPTCHA = wait.until(EC.presence_of_element_located(self._get_locator(driver, 'reCAPTCHA')))

            print(f"{reCAPTCHA} reCAPTCHA  유무")
            if reCAPTCHA == False:
                print("reCAPTCHA 없음")

                
                # 5클릭
                number_5 = wait.until(EC.presence_of_element_located(self._get_locator(driver, 'number_5')))
                # number_5 = driver.find_element(AppiumBy.ACCESSIBILITY_ID, '5')
                number_5.click()
                
                # 2클릭
                number_2 = wait.until(EC.presence_of_element_located(self._get_locator(driver, 'number_2')))
                # number_2 = driver.find_element(AppiumBy.ACCESSIBILITY_ID, '2')
                number_2.click()
                
                # 2클릭
                number_2.click()
                
                # 8클릭
                number_8 = wait.until(EC.presence_of_element_located(self._get_locator(driver, 'number_8')))
                # number_8 = driver.find_element(AppiumBy.ACCESSIBILITY_ID, '8')
                number_8.click()
                
                # 9클릭
                number_9 = wait.until(EC.presence_of_element_located(self._get_locator(driver, 'number_9')))
                # number_9 = driver.find_element(AppiumBy.ACCESSIBILITY_ID, '9')
                number_9.click()
                
                # 7클릭
                number_7 = wait.until(EC.presence_of_element_located(self._get_locator(driver, 'number_7')))
                # number_7 = driver.find_element(AppiumBy.ACCESSIBILITY_ID, '7')
                number_7.click()
                
                # 동의하고 결제하기 버튼 클릭
                agree_payment_btn = wait.until(EC.presence_of_element_located(self._get_locator(driver, 'agree_payment_btn')))
                agree_payment_btn.click()
                
                # 확인 버튼 클릭
                # confirm_btn = wait.until(EC.presence_of_element_located(self._get_locator(driver, 'pay_ment_confirm_btn')))
                # confirm_btn.click()
                # time.sleep(0.5)
                
                # 5클릭
                number_5 = wait.until(EC.presence_of_element_located(self._get_locator(driver, 'number_5')))
                number_5.click()
                
                # 2클릭
                number_2 = wait.until(EC.presence_of_element_located(self._get_locator(driver, 'number_2')))
                number_2.click()
                
                # 2클릭
                number_2.click()
                
                # 8클릭
                number_8 = wait.until(EC.presence_of_element_located(self._get_locator(driver, 'number_8')))
                number_8.click()
                
                # 9클릭
                number_9 = wait.until(EC.presence_of_element_located(self._get_locator(driver, 'number_9')))
                number_9.click()
                
                # 7클릭
                number_7 = wait.until(EC.presence_of_element_located(self._get_locator(driver, 'number_7')))
                number_7.click()

                time.sleep(0.5)
                
                # 뒤로가기 버튼 클릭
                driver.back()
                
                # 뒤로가기 버튼 클릭
                driver.back()
            else:
                print("reCAPTCHA 있음")

                # 뒤로가기 버튼 클릭
                driver.back()

            
        except Exception as e:
            pytest.fail(f"상품구매 테스트 실패: {str(e)}")

    def test_payment_details_scenario(self, driver_setup):
        """마이페이지 -> 서비스 결제내역 시나리오 테스트"""
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
            
            # 서비스 결제내역 버튼 클릭
            # payment_details_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'bottom_payment_details_btn')))
            payment_details_btn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, '서비스 결제내역')
            payment_details_btn.click()
            time.sleep(2)
             
            # 목록에 항목이 0개인지 확인
            list_items = driver.find_elements(*self._get_locator(driver, 'list_items_locator'))
            print("목록 항목 확인")
            if len(list_items) > 0:
                print("목록에 항목 없음")
            else:
                print("목록에 항목 있음")
                # 첫번째 항목의 영수증출력 버튼 클릭
                first_receipt_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'first_item_receipt_btn')))
                first_receipt_btn.click()
                time.sleep(2)
                
                # 다시 앱으로 돌아오기
                driver.back()
                
                # 첫번째 항목 클릭
                first_item = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'first_item')))
                first_item.click()
                time.sleep(2)
                
                # 영수증출력 버튼 클릭
                # receipt_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'receipt_print_btn')))
                receipt_btn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, '영수증출력')
                receipt_btn.click()
                time.sleep(2)
                
                # 다시 앱으로 돌아오기
                driver.back()
                
                # 환불하기 버튼 클릭
                # refund_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'refund_btn')))
                refund_btn = wait.until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, '환불하기')))
                if refund_btn == False:
                    print("환불하기 버튼 없음")
                    driver.back()
                else:
                    print("환불하기 버튼 있음")
                    refund_btn.click()
                
                    # 확인 버튼 클릭
                    # confirm_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'confirm_btn')))
                    confirm_btn = wait.until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, '확인')))
                    confirm_btn.click()
                    
                    # 뒤로가기 버튼 클릭
                    driver.back()
                
                # 첫번째 항목의 재구매 버튼 클릭
                # repurchase_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'repurchase_btn')))
                repurchase_btn = wait.until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, '재구매')))
                repurchase_btn.click()
            
                # 결제수단 드롭다운 클릭
                # payment_method_dropdown = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'payment_method_dropdown')))
                payment_method_dropdown = wait.until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, '선택')))
                payment_method_dropdown.click()
                
                # 실시간 계좌이체 클릭
                # bank_transfer_option = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'bank_transfer_option')))
                bank_transfer_option = wait.until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, '실시간 계좌이체')))
                bank_transfer_option.click()
                
                # 전체동의 체크박스 클릭
                # agree_all_checkbox = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'agree_all_checkbox')))
                agree_all_checkbox = wait.until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, '전체동의')))
                agree_all_checkbox.click()

                driver.find_element(
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    'new UiScrollable(new UiSelector().scrollable(true).instance(0))'
                    '.scrollIntoView(new UiSelector().textContains("다음").instance(0));'
                )
                
                # 다음 버튼 클릭
                # next_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'next_btn')))
                next_btn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, '다음')
                next_btn.click()
                
                # 인풋을 클릭후 92205162 넣기
                phone_input = wait.until(EC.presence_of_element_located(self._get_locator(driver, 'phone_input')))
                phone_input.click()
                phone_input.send_keys("01092205162")
                
                # 다음 버튼 클릭
                next_btn = wait.until(EC.presence_of_element_located(self._get_locator(driver, 'pay_ment_next_btn')))
                next_btn.click()
                
                reCAPTCHA = wait.until(EC.presence_of_element_located(self._get_locator(driver, 'reCAPTCHA')))

                print(f"{reCAPTCHA} reCAPTCHA  유무")
                if reCAPTCHA == False:
                    print("reCAPTCHA 없음")

                    # 5클릭
                    number_5 = wait.until(EC.presence_of_element_located(self._get_locator(driver, 'number_5')))
                    number_5.click()
                    
                    # 2클릭
                    number_2 = wait.until(EC.presence_of_element_located(self._get_locator(driver, 'number_2')))
                    number_2.click()
                    
                    # 2클릭
                    number_2.click()

                    # 8클릭
                    number_8 = wait.until(EC.presence_of_element_located(self._get_locator(driver, 'number_8')))
                    number_8.click()
                    
                    # 9클릭
                    number_9 = wait.until(EC.presence_of_element_located(self._get_locator(driver, 'number_9')))
                    number_9.click()
                    
                    # 7클릭
                    number_7 = wait.until(EC.presence_of_element_located(self._get_locator(driver, 'number_7')))
                    number_7.click()
                    
                    # 동의하고 결제하기 버튼 클릭
                    agree_payment_btn = wait.until(EC.presence_of_element_located(self._get_locator(driver, 'agree_payment_btn')))
                    agree_payment_btn.click()
                    
                    # 확인 버튼 클릭
                    # confirm_btn = wait.until(EC.presence_of_element_located(self._get_locator(driver, 'pay_ment_confirm_btn')))
                    # confirm_btn.click()
                    # time.sleep(0.5)
                    
                    # 5클릭
                    number_5 = wait.until(EC.presence_of_element_located(self._get_locator(driver, 'number_5')))
                    number_5.click()
                    
                    # 2클릭
                    number_2 = wait.until(EC.presence_of_element_located(self._get_locator(driver, 'number_2')))
                    number_2.click()
                    
                    # 2클릭
                    number_2.click()
                    
                    # 8클릭
                    number_8 = wait.until(EC.presence_of_element_located(self._get_locator(driver, 'number_8')))
                    number_8.click()
                    
                    # 9클릭
                    number_9 = wait.until(EC.presence_of_element_located(self._get_locator(driver, 'number_9')))
                    number_9.click()
                    
                    # 7클릭
                    number_7 = wait.until(EC.presence_of_element_located(self._get_locator(driver, 'number_7')))
                    number_7.click()
                    
                    # 뒤로가기 버튼 클릭
                    driver.back()
                    
                    # 토스트메세지 분석
                    try:
                        toast_message = wait.until(EC.presence_of_element_located(self._get_locator(driver, 'toast_message2')))
                        msg = toast_message.get_attribute("text")
                        assert toast_message.is_displayed(), "완료!"
                        print(f"토스트 메세지: {msg}")
                    except:
                        pytest.fail("결제 토스트 메세지가 정상적이지 않음")
                        print("결제 토스트 메세지를 찾을 수 없습니다")
                    time.sleep(2)
                else:
                    print("reCAPTCHA 있음")

                    # 뒤로가기 버튼 클릭
                    driver.back()

                    # 뒤로가기 버튼 클릭
                    driver.back()
                
                # 검색 인풋에 A 넣기
                # search_input = wait.until(EC.presence_of_element_located(self._get_locator(driver, 'search_input')))
                # search_input.click()
                # search_input.send_keys("베")
                # time.sleep(2)
                
                # # 목록에 A가 들어간 항목들이 나오는지 확인
                # list_items = driver.find_elements(*self._get_locator(driver, 'list_items_locator'))
                # print("목록 항목 확인")
                # if len(list_items) > 0:
                #     print("목록에 항목 없음")
                # else:
                #     print("목록에 항목 있음")
            
            # 구인이용권사용내역 버튼 클릭
            # job_history_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'job_usage_history_btn')))
            job_history_btn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, '구인 이용권사용내역')
            job_history_btn.click()
            
            list_items = driver.find_elements(*self._get_locator(driver, 'list_items_locator'))
            print("목록 항목 확인")
            if len(list_items) > 0:
                print("목록에 항목 없음")
            else:
                print("목록에 항목 있음")
                # 첫번째 항목 클릭
                first_item = wait.until(EC.presence_of_element_located(self._get_locator(driver, 'first_item')))
                first_item.click()
                time.sleep(2)

                driver.back()
            
            
            # 입소 이용권사용내역 클릭
            # admission_history_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'admission_usage_history_btn')))
            admission_history_btn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, '입소 이용권사용내역')
            admission_history_btn.click()
            
            list_items = driver.find_elements(*self._get_locator(driver, 'list_items_locator'))
            print("목록 항목 확인")
            if len(list_items) > 0:
                print("목록에 항목 없음")
            else:
                print("목록에 항목 있음")
                # 첫번째 항목 클릭
                first_item = wait.until(EC.presence_of_element_located(self._get_locator(driver, 'first_item')))
                first_item.click()
                time.sleep(2)

                driver.back()

            
            # 뒤로가기 버튼 클릭
            # driver.back()
            
            print("결제내역 시나리오 테스트 완료")
            
        except Exception as e:
            pytest.fail(f"결제내역 시나리오 테스트 실패: {str(e)}")
    
    def test_proposal_search_scenario(self, driver_setup):
        """마이페이지 -> 입소제안 검색 시나리오 테스트"""
        if isinstance(driver_setup, dict):
            driver = driver_setup['driver']
        else:
            driver = driver_setup
        wait = WebDriverWait(driver, 10)

        try:   

            # 바텀 메뉴에서 마이 페이지 클릭
            bottom_my_page_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'bottom_my_page_btn')))
            bottom_my_page_btn.click()
            
            # 입소제안 버튼 클릭
            proposal_menu = wait.until(EC.element_to_be_clickable(self._get_locator(driver,'bottom_menu_proposal_locator')))
            proposal_menu.click()
            
            # 인풋에 "김" 넣기
            search_input = wait.until(EC.presence_of_element_located(self._get_locator(driver, 'search_input_locator')))
            search_input.clear()
            search_input.send_keys("남")
            
            # 목록에 항목이 0개인지 확인
            list_items = driver.find_elements(*self._get_locator(driver, 'list_items_locator'))
            print("목록 항목 확인")
            if len(list_items) > 0:
                print("목록에 항목 없음")
            else:
                print("목록에 항목 있음")

            # 인풋에 "남" 넣기
            # search_input.clear()
            # search_input.send_keys("남")
            # time.sleep(2)
            
            # # 목록에 항목이 1개인지 확인
            # list_items = self.driver.find_elements(*self._get_locator(driver, 'list_items_locator'))
            # print("목록 항목 확인")
            # if len(list_items) > 0:
            #     print("목록에 항목 없음")
            # else:
            #     print("목록에 항목 있음")
            # time.sleep(1)
            
            print("입소제안 검색 시나리오 테스트 완료")
        except Exception as e:
            pytest.fail(f"입소제안 검색 기능 시나리오 테스트 실패: {str(e)}")

    def test_recruitment_mode_admission_inquiry(self, driver_setup):
        """마이페이지 → 입소문의 → SMS 발송 및 신청서 관리 테스트"""
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
            # progress_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'progress_btn')))
            # progress_btn.click()
            # time.sleep(0.5)
            
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

    def test_position_proposal_scenario(self, driver_setup):
        """포지션제안 검색 시나리오 테스트"""
        if isinstance(driver_setup, dict):
            driver = driver_setup['driver']
        else:
            driver = driver_setup
        wait = WebDriverWait(driver, 10)
        
        try:

            # 바텀 메뉴에서 마이 페이지 클릭
            bottom_my_page_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'bottom_my_page_btn')))
            bottom_my_page_btn.click()
            
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
    
    def test_member_info_management(self, driver_setup):
        """바텀 메뉴에서 마이 페이지 클릭 → 회원정보관리 버튼 클릭 → 상세주소 인풋에 3층 넣기 → 저장 버튼 클릭 → 토스트 메세지 분석"""
        if isinstance(driver_setup, dict):
            driver = driver_setup['driver']
        else:
            driver = driver_setup
        wait = WebDriverWait(driver, 10)
        
        try:
            # time.sleep(1)
            
            # 바텀 메뉴에서 마이 페이지 클릭
            bottom_my_page_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'bottom_my_page_btn')))
            bottom_my_page_btn.click()
            # time.sleep(0.5)
            
            # 회원정보관리 버튼 클릭
            # member_info_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'member_info_management_btn')))
            member_info_btn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "회원정보관리")
            member_info_btn.click()
            # time.sleep(0.5)

            driver.find_element(
                AppiumBy.ANDROID_UIAUTOMATOR,
                'new UiScrollable(new UiSelector().scrollable(true).instance(0))'
                '.scrollIntoView(new UiSelector().textContains("저장").instance(0));'
            )

            # 상세주소 인풋에 3층 넣기
            detail_address_input = wait.until(EC.presence_of_element_located(self._get_locator(driver, 'detail_address_input_3floor')))
            detail_address_input.clear()
            detail_address_input.send_keys("3층")
            # time.sleep(0.5)
            
            # 저장 버튼 클릭
            # save_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'save_btn')))
            save_btn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "저장")
            save_btn.click()
            # time.sleep(1)
            
            # 토스트 메세지 분석
            try:
                toast_message = wait.until(EC.presence_of_element_located(self._get_locator(driver, 'toast_message2')))
                msg = toast_message.get_attribute("text")
                assert toast_message.is_displayed(), "수정이 완료되었습니다!"
                print(f"회원정보관리 저장 토스트 메세지: {msg}")
            except:
                pytest.fail("회원정보관리 저장 토스트 메세지가 정상적이지 않음")
                print("회원정보관리 저장 토스트 메세지를 찾을 수 없습니다")
            print("회원정보관리 테스트 완료")
            
        except Exception as e:
            pytest.fail(f"회원정보관리 테스트 실패: {str(e)}")
    
    def test_institution_info_management(self, driver_setup):
        """바텀 메뉴에서 마이 페이지 클릭 → 기관 정보 관리 버튼 클릭 → 인사-설명 인풋에 한마음요양원 세련된 시설과 깨끗한 인테리어로 .. 넣기 → 5등급 버튼 클릭 → 2등급 버튼 클릭 → 자연친화 버튼 클릭 → 도심형 버튼 클릭 → 텃밭 버튼 클릭 → 다인실 버튼 클릭 → 수영장 버튼 클릭 → 헬스장 버튼 클릭 → 주차장 버튼 클릭 → 한달살기 버튼 클릭 → 영양식단 버튼 클릭 → 반려동물 버튼 클릭 → 입력완료 버튼 클릭 → 토스트 메세지 분석"""
        if isinstance(driver_setup, dict):
            driver = driver_setup['driver']
        else:
            driver = driver_setup
        wait = WebDriverWait(driver, 10)
        
        try:
            # time.sleep(1)
            
            # 바텀 메뉴에서 마이 페이지 클릭
            bottom_my_page_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'bottom_my_page_btn')))
            bottom_my_page_btn.click()
            # time.sleep(0.5)
            
            # 기관 정보 관리 버튼 클릭
            # institution_info_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'institution_info_management_btn')))
            institution_info_btn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "기관 정보 관리")
            institution_info_btn.click()
            # time.sleep(0.5)
            
            # 인사-설명 인풋에 한마음요양원 세련된 시설과 깨끗한 인테리어로 .. 넣기
            greeting_input = wait.until(EC.presence_of_element_located(self._get_locator(driver, 'greeting_description_input')))
            greeting_input.clear()
            greeting_input.send_keys("한마음요양원 세련된 시설과 깨끗한 인테리어로 어르신들께 최고의 서비스를 제공합니다")
            # time.sleep(0.5)
            
            # 5등급 버튼 클릭
            grade_5_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'grade_5_btn')))
            grade_5_btn.click()
            # time.sleep(0.5)
            
            # 2등급 버튼 클릭
            grade_2_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'grade_2_btn')))
            grade_2_btn.click()
            # time.sleep(0.5)
            
            driver.find_element(
                AppiumBy.ANDROID_UIAUTOMATOR,
                'new UiScrollable(new UiSelector().scrollable(true).instance(0))'
                '.scrollIntoView(new UiSelector().textContains("환경 시설").instance(0));'
            )

            # 자연친화 버튼 클릭
            # nature_friendly_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'nature_friendly_btn')))
            nature_friendly_btn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "자연친화")
            nature_friendly_btn.click()
            # time.sleep(0.5)
            
            # 도심형 버튼 클릭
            # urban_type_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'urban_type_btn')))
            urban_type_btn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "도심형")
            urban_type_btn.click()
            # time.sleep(0.5)
            
            # 텃밭 버튼 클릭
            # garden_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'garden_btn')))
            garden_btn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "텃밭")
            garden_btn.click()
            # time.sleep(0.5)
            
            # 다인실 버튼 클릭
            # multi_room_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'multi_room_btn')))
            multi_room_btn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "다인실")
            multi_room_btn.click()
            # time.sleep(0.5)
            
            driver.find_element(
                AppiumBy.ANDROID_UIAUTOMATOR,
                'new UiScrollable(new UiSelector().scrollable(true).instance(0))'
                '.scrollIntoView(new UiSelector().textContains("주요 시설").instance(0));'
            )

            # 수영장 버튼 클릭
            # swimming_pool_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'swimming_pool_btn')))
            swimming_pool_btn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "수영장")
            swimming_pool_btn.click()
            # time.sleep(0.5)
            
            # 헬스장 버튼 클릭
            # gym_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'gym_btn')))
            gym_btn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "헬스장")
            gym_btn.click()
            # time.sleep(0.5)
            
            # 주차장 버튼 클릭
            # parking_lot_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'parking_lot_btn')))
            parking_lot_btn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "주차장")
            parking_lot_btn.click()
            # time.sleep(0.5)
            
            # 한달살기 버튼 클릭
            # monthly_stay_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'monthly_stay_btn')))
            monthly_stay_btn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "한달살기")
            monthly_stay_btn.click()
            # time.sleep(0.5)
            
            # 영양식단 버튼 클릭
            # nutrition_diet_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'nutrition_diet_btn')))
            nutrition_diet_btn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "영양식단")
            nutrition_diet_btn.click()
            # time.sleep(0.5)
            
            # 반려동물 버튼 클릭
            # pet_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'pet_btn')))
            pet_btn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "반려동물")
            pet_btn.click()
            # time.sleep(0.5)
            
            driver.find_element(
                AppiumBy.ANDROID_UIAUTOMATOR,
                'new UiScrollable(new UiSelector().scrollable(true).instance(0))'
                '.scrollIntoView(new UiSelector().textContains("입력완료").instance(0));'
            )

            # 입력완료 버튼 클릭
            # input_complete_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'input_complete_btn')))
            input_complete_btn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "입력완료")
            input_complete_btn.click()
            # time.sleep(1)
            
            # 토스트 메세지 분석
            try:
                toast_message = wait.until(EC.presence_of_element_located(self._get_locator(driver, 'toast_message2')))
                msg = toast_message.get_attribute("text")
                assert toast_message.is_displayed(), "수정이 완료되었습니다!"
                print(f"기관정보관리 저장 토스트 메세지: {msg}")
            except:
                pytest.fail("기관정보관리 저장 토스트 메세지가 정상적이지 않음")
                print("기관정보관리 저장 토스트 메세지를 찾을 수 없습니다")
            print("기관정보관리 테스트 완료")

        except Exception as e:
            pytest.fail(f"기관정보관리 테스트 실패: {str(e)}")
    
    def test_job_posting_management_comprehensive(self, driver_setup):
        """바텀 메뉴에서 마이 페이지 클릭 → 공고관리 버튼 클릭 → 전체 버튼 클릭 → 진행 버튼 클릭 → 첫번째 항목 클릭 → 지원지관리 버튼 클릭 → 뒤로가기 버튼 클릭  → 마감버튼 클릭 → 첫번째 항목 클릭 → 복사하기 버튼 클릭 → 스크롤 내려서 다음 단계 버튼 클릭 → 스크롤 내려서 다음 단계 버튼 클릭 → 스크롤 내려서 다음 단계 버튼 클릭 → 1개월 버튼 클릭 → 체용제목 인풋에있던 텍스트 뒤에 오늘 날짜 넣기 → 다음 단계 버튼 클릭 → 공고 등록 완료 버튼 클릭 → 전체동의 체크박스 클릭 → 확인 버튼 클릭 → 마감 버튼 클릭 → 두번째 항목 클릭 → 삭제하기 버튼 클릭 → 공고등록 버튼 클릭 → 스크롤 내려서 다음 단계 버튼 클릭 → 요양보호사 체크박스 클릭 → 여성 체크박스 클릭 → 노숙인 체크박스 클릭 → 정신건강 체크박스 클릭 → 모집인원 인풋에 3 넣기 → 경력 무관 체크박스 클릭 → 주요 업무 인풋에 총괄 업무 분담 넣기 → 자격증 인풋에 2종보통 넣기 → 다음 단계 버튼 클릭 → 정규직 체크박스 클릭 → 매일 근무시간 인풋에 5 넣기 → 주당 근무일수 드롭다운 클릭 → 4 클릭 → 급여 드롭다운 클릭 → 월급 클릭 → 급여인풋에 2000000 넣기 → 다음 단계 버튼 클릭 → 15일 클릭 → 채용제목 인풋에 [긴급] 총괄 정규직 채용 넣기 → 다음 단계 버튼 클릭 → 공고 등록 완료 버튼 클릭 → 전체동의 체크박스 클릭 → 확인 버튼 클릭 → 토스트 메세지 분석 → 첫번째 항목으 더보기 버튼 클릭 → 뒤로가기 버튼 클릭"""
        if isinstance(driver_setup, dict):
            driver = driver_setup['driver']
        else:
            driver = driver_setup
        wait = WebDriverWait(driver, 10)
        
        try:
            # time.sleep(1)
            
            # 바텀 메뉴에서 마이 페이지 클릭
            bottom_my_page_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'bottom_my_page_btn')))
            bottom_my_page_btn.click()
            # time.sleep(0.5)
            
            # 공고관리 버튼 클릭
            # job_management_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'job_management_btn')))
            job_management_btn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "공고관리")
            job_management_btn.click()
            # time.sleep(0.5)
            
            # 전체 버튼 클릭
            all_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'all_btn')))
            all_btn.click()
            # time.sleep(0.5)
            
            # 진행 버튼 클릭
            progress_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'progress_btn')))
            progress_btn.click()
            # time.sleep(0.5)
            
            # 첫번째 항목 클릭
            first_job_item = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'first_job_item')))
            first_job_item.click()
            # time.sleep(0.5)
            
            # 지원지관리 버튼 클릭
            # applicant_management_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'applicant_management_btn')))
            applicant_management_btn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "지원지 관리")
            applicant_management_btn.click()
            # time.sleep(0.5)
            
            applicant_management_modal = wait.until(EC.presence_of_element_located(self._get_locator(driver, 'applicant_management_modal')))
            if applicant_management_modal != False:
                comfrim = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "확인")
                comfrim.click()
                # 뒤로가기 버튼 클릭
                driver.back()
            else:
                # 뒤로가기 버튼 클릭
                driver.back()

            # 뒤로가기 버튼 클릭
            driver.back()
            # time.sleep(0.5)
            
            # 마감버튼 클릭
            closed_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'closed_btn')))
            closed_btn.click()
            # time.sleep(0.5)

            # 목록에 항목이 0개인지 확인
            list_items = driver.find_elements(*self._get_locator(driver, 'list_items_locator'))
            print("목록 항목 확인")
            if len(list_items) == 0:
                print("목록에 항목 없음")
            else:
                print("목록에 항목 있음")
                # 첫번째 항목 클릭
                first_job_item = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'first_job_item')))
                first_job_item.click()
                # time.sleep(0.5)
                
                # 복사하기 버튼 클릭
                # copy_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'copy_btn')))
                copy_btn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "복사하기")
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
                # one_month_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'one_month_btn')))
                one_month_btn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "1개월")
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
                
                driver.find_element(
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    'new UiScrollable(new UiSelector().scrollable(true).instance(0))'
                    '.scrollIntoView(new UiSelector().textContains("공고 등록 완료").instance(0));'
                )

                # 공고 등록 완료 버튼 클릭
                # job_registration_complete_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'job_registration_complete_btn')))
                job_registration_complete_btn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "공고 등록 완료")
                job_registration_complete_btn.click()
                # time.sleep(0.5)
                
                # 전체동의 체크박스 클릭
                all_agree_checkbox = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'all_agree_checkbox')))
                all_agree_checkbox.click()
                # time.sleep(0.5)
                
                # 확인 버튼 클릭
                # confirm_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'confirm_btn')))
                confirm_btn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "확인")
                confirm_btn.click()
                # time.sleep(0.5)
                
                # 마감 버튼 클릭
                closed_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'closed_btn')))
                closed_btn.click()
                # time.sleep(0.5)
                
                # 두번째 항목 클릭
                second_job_item = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'second_job_item')))
                second_job_item.click()
                # time.sleep(0.5)
                
                # 삭제하기 버튼 클릭
                delete_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'delete_btn')))
                delete_btn.click()
                # time.sleep(0.5)
            
            # 공고등록 버튼 클릭
            # job_registration_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'job_registration_btn')))
            job_registration_btn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "공고등록")
            job_registration_btn.click()
            # time.sleep(0.5)
            
            # 스크롤 내려서 다음 단계 버튼 클릭
            driver.find_element(
                AppiumBy.ANDROID_UIAUTOMATOR,
                'new UiScrollable(new UiSelector().scrollable(true)).scrollIntoView(new UiSelector().textContains("다음 단계"));'
            )
            next_step_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'next_step_btn')))
            next_step_btn.click()
            # time.sleep(0.5)

            # 요양보호사 체크박스 클릭
            # care_worker_checkbox = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'care_worker_checkbox')))
            care_worker_checkbox = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "요양보호사")
            care_worker_checkbox.click()
            # time.sleep(0.5)
            
            driver.find_element(
                AppiumBy.ANDROID_UIAUTOMATOR,
                'new UiScrollable(new UiSelector().scrollable(true).instance(0))'
                '.scrollIntoView(new UiSelector().textContains("모집인원").instance(0));'
            )
            
            # 여성 체크박스 클릭
            # female_checkbox = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'female_checkbox')))
            female_checkbox = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "여성")
            female_checkbox.click()
            # time.sleep(0.5)
            
            # 노숙인 체크박스 클릭
            # homeless_checkbox = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'homeless_checkbox')))
            homeless_checkbox = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "노숙인")
            homeless_checkbox.click()
            # time.sleep(0.5)
            
            # 정신건강 체크박스 클릭
            # mental_health_checkbox = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'mental_health_checkbox')))
            mental_health_checkbox = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "정신 건강")
            mental_health_checkbox.click()
            # time.sleep(0.5)
            
            driver.find_element(
                AppiumBy.ANDROID_UIAUTOMATOR,
                'new UiScrollable(new UiSelector().scrollable(true).instance(0))'
                '.scrollIntoView(new UiSelector().textContains("신입").instance(0));'
            )

            # 모집인원 인풋에 3 넣기
            recruitment_count_input = wait.until(EC.presence_of_element_located(self._get_locator(driver, 'recruitment_count_input')))
            recruitment_count_input.clear()
            recruitment_count_input.send_keys("3")
            # time.sleep(0.5)
            
            # 경력 무관 체크박스 클릭
            # experience_irrelevant_checkbox = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'experience_irrelevant_checkbox')))
            experience_irrelevant_checkbox = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "경력 무관")
            experience_irrelevant_checkbox.click()
            # time.sleep(0.5)
            
            driver.find_element(
                AppiumBy.ANDROID_UIAUTOMATOR,
                'new UiScrollable(new UiSelector().scrollable(true).instance(0))'
                '.scrollIntoView(new UiSelector().textContains("자격증").instance(0));'
            )

            # 주요 업무 인풋에 총괄 업무 분담 넣기
            main_task_input = wait.until(EC.presence_of_element_located(self._get_locator(driver, 'main_task_input')))
            main_task_input.clear()
            main_task_input.send_keys("총괄 업무 분담")
            # time.sleep(0.5)
            
            # 자격증 인풋에 2종보통 넣기
            certificate_input = wait.until(EC.presence_of_element_located(self._get_locator(driver, 'certificate_input')))
            certificate_input.clear()
            certificate_input.send_keys("2종보통")
            # time.sleep(0.5)
            
            # 다음 단계 버튼 클릭
            next_step_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'next_step_btn')))
            next_step_btn.click()
            # time.sleep(0.5)
            
            # 정규직 체크박스 클릭
            # full_time_checkbox = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'full_time_checkbox')))
            full_time_checkbox = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "정규직")
            full_time_checkbox.click()
            # time.sleep(0.5)
            
            # 매일 근무시간 인풋에 5 넣기
            daily_work_hours_input = wait.until(EC.presence_of_element_located(self._get_locator(driver, 'daily_work_hours_input')))
            daily_work_hours_input.clear()
            daily_work_hours_input.send_keys("5")
            # time.sleep(0.5)
            
            driver.find_element(
                AppiumBy.ANDROID_UIAUTOMATOR,
                'new UiScrollable(new UiSelector().scrollable(true).instance(0))'
                '.scrollIntoView(new UiSelector().textContains("급여").instance(0));'
            )

            # 주당 근무일수 드롭다운 클릭
            weekly_work_days_dropdown = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'weekly_work_days_dropdown')))
            weekly_work_days_dropdown.click()
            # time.sleep(0.5)
            
            # 4 클릭
            four_days_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'four_days_btn')))
            four_days_btn.click()
            # time.sleep(0.5)
            
            # 급여 드롭다운 클릭
            salary_dropdown = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'salary_dropdown')))
            salary_dropdown.click()
            # time.sleep(0.5)
            
            # 월급 클릭
            # monthly_salary_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'monthly_salary_btn')))
            monthly_salary_btn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "월급")
            monthly_salary_btn.click()
            # time.sleep(0.5)
            
            # 급여인풋에 2000000 넣기
            salary_input = wait.until(EC.presence_of_element_located(self._get_locator(driver, 'salary_input')))
            salary_input.clear()
            salary_input.send_keys("2000000")
            # time.sleep(0.5)
            
            # 다음 단계 버튼 클릭
            next_step_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'next_step_btn')))
            next_step_btn.click()
            # time.sleep(0.5)
            
            # 15일 클릭
            # fifteen_days_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'fifteen_days_btn')))
            fifteen_days_btn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "15일")
            fifteen_days_btn.click()
            # time.sleep(0.5)
            
            driver.find_element(
                AppiumBy.ANDROID_UIAUTOMATOR,
                'new UiScrollable(new UiSelector().scrollable(true).instance(0))'
                '.scrollIntoView(new UiSelector().textContains("채용제목").instance(0));'
            )

            # 채용제목 인풋에 [긴급] 총괄 정규직 채용 넣기
            job_title_input_urgent = wait.until(EC.presence_of_element_located(self._get_locator(driver, 'job_title_input_urgent')))
            job_title_input_urgent.clear()
            job_title_input_urgent.send_keys("[긴급] 총괄 정규직 채용")
            # time.sleep(0.5)
            
            # 다음 단계 버튼 클릭
            next_step_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'next_step_btn')))
            next_step_btn.click()
            # time.sleep(0.5)
            
            driver.find_element(
                AppiumBy.ANDROID_UIAUTOMATOR,
                'new UiScrollable(new UiSelector().scrollable(true).instance(0))'
                '.scrollIntoView(new UiSelector().textContains("공고 등록 완료").instance(0));'
            )

            # 공고 등록 완료 버튼 클릭
            # job_registration_complete_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'job_registration_complete_btn')))
            job_registration_complete_btn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "공고 등록 완료")
            job_registration_complete_btn.click()
            # time.sleep(0.5)
            
            # 전체동의 체크박스 클릭
            all_agree_checkbox = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'all_agree_checkbox')))
            all_agree_checkbox.click()
            # time.sleep(0.5)
            
            # 확인 버튼 클릭
            # confirm_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'confirm_btn')))
            confirm_btn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "확인")
            confirm_btn.click()
            # time.sleep(1)
            
            # 토스트 메세지 분석
            try:
                toast_message = wait.until(EC.presence_of_element_located(self._get_locator(driver, 'toast_message2')))
                msg = toast_message.get_attribute("text")
                assert toast_message.is_displayed(), "완료!"
                print(f"공고 등록 완료 토스트 메세지: {msg}")
            except:
                pytest.fail("공고 등록 완료 토스트 메세지가 정상적이지 않음")
                print("공고 등록 완료 토스트 메세지를 찾을 수 없습니다")
            

            # 목록에 항목이 0개인지 확인
            list_items = driver.find_elements(*self._get_locator(driver, 'list_items_locator'))
            print("목록 항목 확인")
            if len(list_items) == 0:
                print("목록에 항목 없음")
            else:
                print("목록에 항목 있음")
                # 첫번째 항목의 더보기 버튼 클릭
                more_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'more_btn')))
                more_btn.click()
                # time.sleep(0.5)
            
            # 뒤로가기 버튼 클릭
            driver.back()
            # time.sleep(0.5)
            
            print("공고관리 종합 테스트 완료")
            
        except Exception as e:
            pytest.fail(f"공고관리 종합 테스트 실패: {str(e)}")