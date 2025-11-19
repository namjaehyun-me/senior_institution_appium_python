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
                'bottom_payment_details_btn': (AppiumBy.XPATH, "//android.widget.TextView[@text='결제내역']"),
                'first_item_receipt_btn': (AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="영수증출력"]'),
                'first_item': (AppiumBy.XPATH, "//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[1]"),
                'receipt_print_btn': (AppiumBy.XPATH, "//android.widget.Button[@text='영수증출력']"),
                'refund_btn': (AppiumBy.XPATH, "//android.widget.Button[@text='환불하기']"),
                'confirm_btn': (AppiumBy.XPATH, "//android.widget.Button[@text='확인']"),
                'back_btn': (AppiumBy.XPATH, "//android.widget.Button[@text='뒤로가기']"),
                'repurchase_btn': (AppiumBy.XPATH, "(//android.widget.Button[contains(@text, '재구매')])[1]"),
                'payment_method_dropdown': (AppiumBy.XPATH, "//android.widget.Spinner"),
                'bank_transfer_option': (AppiumBy.XPATH, "//android.widget.TextView[@text='실시간 계좌이체']"),
                'agree_all_checkbox': (AppiumBy.XPATH, "//android.widget.CheckBox[@text='전체동의']"),
                'next_btn': (AppiumBy.XPATH, "//android.widget.Button[@text='다음']"),
                'input_field': (AppiumBy.XPATH, "//android.widget.EditText"),
                'number_5': (AppiumBy.XPATH, "//android.widget.Button[@text='5']"),
                'number_2': (AppiumBy.XPATH, "//android.widget.Button[@text='2']"),
                'number_8': (AppiumBy.XPATH, "//android.widget.Button[@text='8']"),
                'number_9': (AppiumBy.XPATH, "//android.widget.Button[@text='9']"),
                'number_7': (AppiumBy.XPATH, "//android.widget.Button[@text='7']"),
                'agree_and_pay_btn': (AppiumBy.XPATH, "//android.widget.Button[@text='동의하고 결제하기']"),
                'search_input': (AppiumBy.XPATH, '//android.widget.EditText[@text="검색"]'),
                'list_items': (AppiumBy.XPATH, "//android.widget.ListView//android.widget.LinearLayout"),
                'job_usage_history_btn': (AppiumBy.XPATH, "//android.widget.Button[@text='구인이용권사용내역']"),
                'admission_usage_history_btn': (AppiumBy.XPATH, "//android.widget.Button[@text='입소 이용권사용내역']"),
                'toast_message': (AppiumBy.XPATH, '//android.widget.TextView[@text="완료!"]'),
                'list_items_locator':(AppiumBy.XPATH, '//android.widget.TextView[@text="데이터를 찾을 수 없습니다"]'),
                'phone_input': (AppiumBy.XPATH, '//android.widget.EditText[@text="010"]'),
                'pay_ment_next_btn': (AppiumBy.XPATH, '//android.widget.Button[@text="다음"]'),
                'number_5': (AppiumBy.XPATH, '//android.widget.Button[@content-desc="5"]'),
                'number_2': (AppiumBy.XPATH, '//android.widget.Button[@content-desc="2"]'),
                'number_8': (AppiumBy.XPATH, '//android.widget.Button[@content-desc="8"]'),
                'number_9': (AppiumBy.XPATH, '//android.widget.Button[@content-desc="9"]'),
                'number_7': (AppiumBy.XPATH, '//android.widget.Button[@content-desc="7"]'),
                'agree_payment_btn': (AppiumBy.XPATH, '//android.widget.Button[@text="동의하고 결제하기"]'),
                'pay_ment_confirm_btn': (AppiumBy.XPATH, '//android.widget.Button[@text="확인"]'),
            },
            'ios': {
                'bottom_payment_details_btn': (AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='결제내역']"),
                'first_item_receipt_btn': (AppiumBy.XPATH, "(//XCUIElementTypeButton[contains(@name, '영수증출력')])[1]"),
                'first_item': (AppiumBy.XPATH, "(//XCUIElementTypeCell)[1]"),
                'receipt_print_btn': (AppiumBy.XPATH, "//XCUIElementTypeButton[@name='영수증출력']"),
                'refund_btn': (AppiumBy.XPATH, "//XCUIElementTypeButton[@name='환불하기']"),
                'confirm_btn': (AppiumBy.XPATH, "//XCUIElementTypeButton[@name='확인']"),
                'back_btn': (AppiumBy.XPATH, "//XCUIElementTypeButton[@name='뒤로가기']"),
                'repurchase_btn': (AppiumBy.XPATH, "(//XCUIElementTypeButton[contains(@name, '재구매')])[1]"),
                'payment_method_dropdown': (AppiumBy.XPATH, "//XCUIElementTypePicker"),
                'bank_transfer_option': (AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='실시간 계좌이체']"),
                'agree_all_checkbox': (AppiumBy.XPATH, "//XCUIElementTypeSwitch[@name='전체동의']"),
                'next_btn': (AppiumBy.XPATH, "//XCUIElementTypeButton[@name='다음']"),
                'input_field': (AppiumBy.XPATH, "//XCUIElementTypeTextField"),
                'number_5': (AppiumBy.XPATH, "//XCUIElementTypeButton[@name='5']"),
                'number_2': (AppiumBy.XPATH, "//XCUIElementTypeButton[@name='2']"),
                'number_8': (AppiumBy.XPATH, "//XCUIElementTypeButton[@name='8']"),
                'number_9': (AppiumBy.XPATH, "//XCUIElementTypeButton[@name='9']"),
                'number_7': (AppiumBy.XPATH, "//XCUIElementTypeButton[@name='7']"),
                'agree_and_pay_btn': (AppiumBy.XPATH, "//XCUIElementTypeButton[@name='동의하고 결제하기']"),
                'search_input': (AppiumBy.XPATH, "//XCUIElementTypeTextField"),
                'list_items': (AppiumBy.XPATH, "//XCUIElementTypeTable//XCUIElementTypeCell"),
                'job_usage_history_btn': (AppiumBy.XPATH, "//XCUIElementTypeButton[@name='구인이용권사용내역']"),
                'admission_usage_history_btn': (AppiumBy.XPATH, "//XCUIElementTypeButton[@name='입소 이용권사용내역']"),
                'toast_message': (AppiumBy.XPATH, "//XCUIElementTypeAlert"),
                'list_items_locator': (AppiumBy.XPATH, "//XCUIElementTypeAlert"),
                'phone_input': (AppiumBy.XPATH, "//XCUIElementTypeAlert"),
                'pay_ment_next_btn': (AppiumBy.XPATH, "//XCUIElementTypeAlert"),
                'number_5': (AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='5']"),
                'number_2': (AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='2']"),
                'number_8': (AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='8']"),
                'number_9': (AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='9']"),
                'number_7': (AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='7']"),
                'agree_payment_btn': (AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='동의하고 결제하기']"),
                'pay_ment_confirm_btn': (AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='동의하고 결제하기']"),
            }
        }
        
        return locators[platform][element_name]

    def test_payment_details_scenario(self, driver_setup):
        """결제내역 시나리오 테스트"""
        if isinstance(driver_setup, dict):
            driver = driver_setup['driver']
        else:
            driver = driver_setup
        wait = WebDriverWait(driver, 10)
        
        try:
            time.sleep(2)
            
            # 바텀 메뉴에서 결제내역 클릭
            payment_details_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'bottom_payment_details_btn')))
            payment_details_btn.click()
            time.sleep(2)
             
            # 목록에 항목이 0개인지 확인
            list_items = driver.find_elements(*self._get_locator(driver, 'list_items_locator'))
            print("목록 항목 확인")
            if len(list_items) > 0:
                print("목록에 항목 없음")
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
                refund_btn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, '환불하기')
                refund_btn.click()
                time.sleep(1)
                
                # 확인 버튼 클릭
                # confirm_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'confirm_btn')))
                confirm_btn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, '확인')
                confirm_btn.click()
                time.sleep(1)
                
                # 뒤로가기 버튼 클릭
                driver.back()
                
                # 첫번째 항목의 재구매 버튼 클릭
                # repurchase_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'repurchase_btn')))
                repurchase_btn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, '재구매')
                repurchase_btn.click()
                time.sleep(2)
            
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
                
                # # 결제수단 드롭다운 클릭
                # payment_dropdown = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'payment_method_dropdown')))
                # payment_dropdown.click()
                # time.sleep(1)
                
                # # 실시간 계좌이체 클릭
                # bank_transfer = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'bank_transfer_option')))
                # bank_transfer.click()
                # time.sleep(1)
                
                # # 전체동의 체크박스 클릭
                # agree_checkbox = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'agree_all_checkbox')))
                # agree_checkbox.click()
                # time.sleep(1)
                
                # # 다음 버튼 클릭
                # next_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'next_btn')))
                # next_btn.click()
                # time.sleep(2)
                
                # # 인풋을 클릭후 92205162 넣기
                # input_field = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'input_field')))
                # input_field.click()
                # input_field.send_keys("92205162")
                # time.sleep(1)
                
                # # 다음 버튼 클릭
                # next_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'next_btn')))
                # next_btn.click()
                # time.sleep(2)
                
                # # 숫자 입력: 5, 2, 2, 8, 9, 7
                # numbers = ['number_5', 'number_2', 'number_2', 'number_8', 'number_9', 'number_7']
                # for num in numbers:
                #     num_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, num)))
                #     num_btn.click()
                #     time.sleep(0.5)
                
                # # 동의하고 결제하기 버튼 클릭
                # pay_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'agree_and_pay_btn')))
                # pay_btn.click()
                # time.sleep(2)
                
                # # 확인 버튼 클릭
                # confirm_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'confirm_btn')))
                # confirm_btn.click()
                # time.sleep(2)
                
                # # 숫자 재입력: 5, 2, 2, 8, 9, 7
                # for num in numbers:
                #     num_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, num)))
                #     num_btn.click()
                #     time.sleep(0.5)
                
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
                
                # 검색 인풋에 A 넣기
                search_input = wait.until(EC.presence_of_element_located(self._get_locator(driver, 'search_input')))
                search_input.click()
                search_input.send_keys("베")
                time.sleep(2)
                
                # 목록에 A가 들어간 항목들이 나오는지 확인
                list_items = driver.find_elements(*self._get_locator(driver, 'list_items_locator'))
                print("목록 항목 확인")
                if len(list_items) > 0:
                    print("목록에 항목 없음")
                else:
                    print("목록에 항목 있음")
                time.sleep(1)
            else:
                print("목록에 항목 있음")
            time.sleep(1)
            
            # 구인이용권사용내역 버튼 클릭
            # job_history_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'job_usage_history_btn')))
            job_history_btn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, '구인 이용권사용내역')
            job_history_btn.click()
            time.sleep(2)
            
            list_items = driver.find_elements(*self._get_locator(driver, 'list_items_locator'))
            print("목록 항목 확인")
            if len(list_items) > 0:
                print("목록에 항목 없음")
            else:
                print("목록에 항목 있음")
                # 첫번째 항목 클릭
                first_item = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'first_item')))
                first_item.click()
                time.sleep(2)

                driver.back()
            time.sleep(1)
            
            
            # 입소 이용권사용내역 클릭
            # admission_history_btn = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'admission_usage_history_btn')))
            admission_history_btn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, '입소 이용권사용내역')
            admission_history_btn.click()
            time.sleep(2)
            
            list_items = driver.find_elements(*self._get_locator(driver, 'list_items_locator'))
            print("목록 항목 확인")
            if len(list_items) > 0:
                print("목록에 항목 없음")
            else:
                print("목록에 항목 있음")
                # 첫번째 항목 클릭
                first_item = wait.until(EC.element_to_be_clickable(self._get_locator(driver, 'first_item')))
                first_item.click()
                time.sleep(2)

                driver.back()
            time.sleep(1)

            
            # 뒤로가기 버튼 클릭
            # driver.back()
            
            print("결제내역 시나리오 테스트 완료")
            
        except Exception as e:
            pytest.fail(f"결제내역 시나리오 테스트 실패: {str(e)}")
    