import pytest
from base_driver import BaseDriver

class TestDebug:
    def setup_method(self):
        self.base_driver = BaseDriver("android")
        self.driver = self.base_driver.start_driver()
    
    def teardown_method(self):
        self.base_driver.quit_driver()
    
    def test_current_screen(self):
        """현재 화면의 요소들을 확인"""
        from appium.webdriver.common.appiumby import AppiumBy
        import time
        
        # 팝업 처리 시도
        try:
            popup_btn = self.driver.find_element(AppiumBy.ID, "android:id/button1")
            popup_btn.click()
            print("팝업을 닫었습니다.")
            time.sleep(2)
        except:
            print("팝업이 없거나 이미 닫혔습니다.")
        
        print("\n=== 현재 화면 정보 ===")
        print(f"현재 액티비티: {self.driver.current_activity}")
        print(f"현재 패키지: {self.driver.current_package}")
        
        # 모든 클릭 가능한 요소들 찾기
        try:
            clickable_elements = self.driver.find_elements(AppiumBy.XPATH, "//*[@clickable='true']")
            print(f"\n클릭 가능한 요소 개수: {len(clickable_elements)}")
            for i, element in enumerate(clickable_elements[:10]):  # 처음 10개만
                resource_id = element.get_attribute('resource-id')
                text = element.get_attribute('text')
                class_name = element.get_attribute('class')
                print(f"{i+1}. Class: {class_name}, ID: {resource_id}, Text: {text}")
        except Exception as e:
            print(f"클릭 가능한 요소를 찾을 수 없습니다: {e}")
        
        # EditText 요소들 찾기
        try:
            edit_texts = self.driver.find_elements(AppiumBy.CLASS_NAME, "android.widget.EditText")
            print(f"\n찾은 EditText 요소 개수: {len(edit_texts)}")
            for i, element in enumerate(edit_texts):
                resource_id = element.get_attribute('resource-id')
                hint = element.get_attribute('hint')
                print(f"EditText {i+1}: ID={resource_id}, Hint={hint}")
        except Exception as e:
            print(f"EditText 요소를 찾을 수 없습니다: {e}")