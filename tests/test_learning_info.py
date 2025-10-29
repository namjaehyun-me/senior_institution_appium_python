import pytest
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.appiumby import AppiumBy
import time

class TestLearningInfo:
    def setup_method(self, method):
        """테스트 메소드 시작 전 기본 설정"""
        print("\n📱 테스트 준비 중...")
    
    def test_learning_info_navigation(self, driver_setup, ensure_login):
        """학습정보 네비게이션 테스트: 메인 -> 학습정보 -> 카테곣리 -> 목록 -> 아이템 상세"""
        # 드라이버 설정 및 로그인 상태 확인
        self.driver = driver_setup['driver']
        self.base_driver = driver_setup['base_driver']
        self.login_page = driver_setup['login_page']
        self.wait = driver_setup['wait']
        self.platform = driver_setup['platform']
        
        print(f"\n📱 테스트 시작 - 플랫폼: {self.platform}")
        print("✅ 자동 로그인 완료 상태로 테스트 진행")
        
        # 필요시 로그인 상태 재확인 (일반적으로는 이미 로그인된 상태)
        # ensure_login()  # 필요한 경우에만 주석 해제
        
        print("\n=== 학습정보 네비게이션 테스트 시작 ===")
        
        # 1. 메인페이지에서 바텀 네비게이션의 학습정보 버튼 클릭
        print("\n1. 바텀 네비게이션의 학습정보 버튼 클릭")
        try:
            # TODO: 여기에 학습정보 버튼의 locator를 넣으세요
            # 예시: learning_info_button = self.wait.until(EC.element_to_be_clickable((AppiumBy.ID, "학습정보_버튼_ID")))
            # 또는: learning_info_button = self.wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, "//android.widget.TextView[@text='학습정보']")))
            learning_info_button = self.wait.until(
                EC.element_to_be_clickable((AppiumBy.XPATH, '//android.view.View[@content-desc="학습 정보"]'))
            )
            learning_info_button.click()
            time.sleep(2)
            print("✓ 학습정보 버튼 클릭 완료")
        except Exception as e:
            print(f"✗ 학습정보 버튼 클릭 실패: {e}")
            raise
        
        # 2. 카테고리 클릭
        print("\n2. 카테고리 클릭")
        try:
            # TODO: 여기에 카테고리 버튼의 locator를 넣으세요
            # 예시: category_button = self.wait.until(EC.element_to_be_clickable((AppiumBy.ID, "카테고리_ID")))
            # 또는: category_button = self.wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, "//android.widget.TextView[@text='건강관리']")))
            category_button1 = self.wait.until(
                EC.element_to_be_clickable((AppiumBy.XPATH, "//android.widget.ImageView"))
            )
            category_button1.click()
            time.sleep(2)
            category_button2 = self.wait.until(
                EC.element_to_be_clickable((AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="시작하기"]/android.view.ViewGroup'))
            )
            category_button2.click()
            time.sleep(2)
            print("✓ 카테고리 클릭 완료")
        except Exception as e:
            print(f"✗ 카테고리 클릭 실패: {e}")
            raise
        
        # 3. 목록 아이템 클릭
        print("\n3. 목록 아이템 클릭")
        try:
            # TODO: 여기에 목록 아이템의 locator를 넣으세요
            # 예시: list_item = self.wait.until(EC.element_to_be_clickable((AppiumBy.ID, "목록_아이템_ID")))
            # 또는: list_item = self.wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, "//android.widget.TextView[@text='첫번째 학습자료']")))
            list_item = self.wait.until(
                EC.element_to_be_clickable((AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="시작하기, 테스트 김지후"]'))
            )
            list_item.click()
            time.sleep(3)
            print("✓ 목록 아이템 클릭 완료")
        except Exception as e:
            print(f"✗ 목록 아이템 클릭 실패: {e}")
            raise

        # 3. 아이템 상세의 유튜브 재생 버튼 클릭
        print("\n4. 아이템 상세의 유튜브 재생 버튼 클릭")
        try:
            # TODO: 여기에 목록 아이템의 locator를 넣으세요
            # 예시: list_item = self.wait.until(EC.element_to_be_clickable((AppiumBy.ID, "목록_아이템_ID")))
            # 또는: list_item = self.wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, "//android.widget.TextView[@text='첫번째 학습자료']")))
            list_item_youtube = self.wait.until(
                EC.element_to_be_clickable((AppiumBy.XPATH, '//android.widget.Button[@text="Play video"]'))
            )
            list_item_youtube.click()
            time.sleep(3)
            print("✓ 아이템 상세의 유튜브 재생 버튼 완료")
        except Exception as e:
            print(f"✗ 아이템 상세의 유튜브 재생 버튼 실패: {e}")
            raise

        # 5. 뒤로가기 버튼 클릭
        print("\n5. 뒤로가기 버튼 클릭")
        try:
            # TODO: 여기에 뒤로가기 버튼의 locator를 넣으세요
            # 예시: back_button = self.wait.until(EC.element_to_be_clickable((AppiumBy.ID, "뒤로가기_버튼_ID")))
            # 또는: back_button = self.wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, "//android.widget.ImageButton[@content-desc='Navigate up']")))
            back_button = self.wait.until(
                EC.element_to_be_clickable((AppiumBy.XPATH, '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/com.horcrux.svg.SvgView/com.horcrux.svg.GroupView/com.horcrux.svg.PathView'))
            )
            back_button.click()
            time.sleep(2)
            print("✓ 뒤로가기 버튼 클릭 완료")
        except Exception as e:
            print(f"✗ 뒤로가기 버튼 클릭 실패: {e}")
            # 뒤로가기 버튼이 없으면 시스템 뒤로가기 사용
            self.driver.back()
            time.sleep(2)
            print("✓ 시스템 뒤로가기 사용")

        print("\n=== 학습정보 네비게이션 테스트 완료 ===")
        assert True, "학습정보 네비게이션 테스트 성공"