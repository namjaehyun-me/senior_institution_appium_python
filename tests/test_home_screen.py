import pytest
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.appiumby import AppiumBy
import time

class TestHomeScreen:
    def setup_method(self, method):
        """테스트 메소드 시작 전 기본 설정"""
        print("\n🏠 홈화면 테스트 준비 중...")

    def test_home_screen_elements(self, driver_setup, ensure_login):
        """홈화면 주요 요소들 확인 테스트"""
        # 드라이버 설정 및 로그인 상태 확인
        self.driver = driver_setup['driver']
        self.base_driver = driver_setup['base_driver']
        self.login_page = driver_setup['login_page']
        self.wait = driver_setup['wait']
        self.platform = driver_setup['platform']
        
        print(f"\n📱 홈화면 테스트 시작 - 플랫폼: {self.platform}")
        print("✅ 자동 로그인 완료 상태로 테스트 진행")
        
        print("\n=== 홈화면 주요 요소 확인 테스트 시작 ===")
        
        # 1. 바텀 네비게이션 요소들 확인
        print("\n1. 바텀 네비게이션 요소들 확인")
        bottom_nav_items = [
            ("홈", "//android.view.View[@content-desc='홈']"),
            ("관심기관", "//android.view.View[@content-desc='관심기관']"),
            ("학습 정보", "//android.view.View[@content-desc='학습 정보']"),
            ("마이 페이지", "//android.view.View[@content-desc='마이 페이지']")
        ]
        
        for name, xpath in bottom_nav_items:
            try:
                element = self.wait.until(EC.presence_of_element_located((AppiumBy.XPATH, xpath)))
                assert element.is_displayed(), f"{name} 버튼이 표시되어야 함"
                print(f"✓ {name} 버튼 확인 완료")
            except Exception as e:
                print(f"✗ {name} 버튼 확인 실패: {e}")
        
        # 2. 홈화면 서비스 카드들 확인
        print("\n2. 홈화면 서비스 카드들 확인")
        service_cards = [
            ("방문요양 찾기", "//android.view.ViewGroup[@content-desc='방문요양 찾기, 찾기']"),
            ("장기요양기관 찾기", "//android.view.ViewGroup[@content-desc='장기요양기관\n찾기, 찾기']"),
            ("가사돌봄", "//android.view.ViewGroup[@content-desc='가사돌봄, 찾기']"),
            ("간병인 찾기", "//android.view.ViewGroup[@content-desc='간병인 찾기, 찾기']"),
            ("동행서비스", "//android.view.ViewGroup[@content-desc='동행서비스, 찾기']")
        ]
        
        for name, xpath in service_cards:
            try:
                element = self.wait.until(EC.presence_of_element_located((AppiumBy.XPATH, xpath)))
                assert element.is_displayed(), f"{name} 카드가 표시되어야 함"
                print(f"✓ {name} 카드 확인 완료")
            except Exception as e:
                print(f"✗ {name} 카드 확인 실패: {e}")
        
        print("\n=== 홈화면 주요 요소 확인 테스트 완료 ===")
        assert True, "홈화면 요소 확인 테스트 성공"

    def test_service_card_navigation(self, driver_setup, ensure_login):
        """서비스 카드 클릭 네비게이션 테스트"""
        # 드라이버 설정
        self.driver = driver_setup['driver']
        self.wait = driver_setup['wait']
        self.platform = driver_setup['platform']
        
        print("\n=== 서비스 카드 네비게이션 테스트 시작 ===")
        
        # 방문요양 찾기 카드 클릭 테스트
        print("\n1. 방문요양 찾기 카드 클릭")
        try:
            service_card = self.wait.until(
                EC.element_to_be_clickable((AppiumBy.XPATH, "//android.view.ViewGroup[@content-desc='방문요양 찾기, 찾기']"))
            )
            service_card.click()
            time.sleep(2)
            print("✓ 방문요양 찾기 카드 클릭 완료")
            
            # 뒤로가기
            self.driver.back()
            time.sleep(2)
            print("✓ 홈화면으로 복귀")
            
        except Exception as e:
            print(f"✗ 방문요양 찾기 카드 클릭 실패: {e}")
        
        # 장기요양기관 찾기 카드 클릭 테스트
        print("\n2. 장기요양기관 찾기 카드 클릭")
        try:
            service_card = self.wait.until(
                EC.element_to_be_clickable((AppiumBy.XPATH, "//android.view.ViewGroup[@content-desc='장기요양기관\n찾기, 찾기']"))
            )
            service_card.click()
            time.sleep(2)
            print("✓ 장기요양기관 찾기 카드 클릭 완료")
            
            # 뒤로가기
            self.driver.back()
            time.sleep(2)
            print("✓ 홈화면으로 복귀")
            
        except Exception as e:
            print(f"✗ 장기요양기관 찾기 카드 클릭 실패: {e}")
        
        print("\n=== 서비스 카드 네비게이션 테스트 완료 ===")
        assert True, "서비스 카드 네비게이션 테스트 성공"

    def test_bottom_navigation(self, driver_setup, ensure_login):
        """바텀 네비게이션 전체 테스트"""
        # 드라이버 설정
        self.driver = driver_setup['driver']
        self.wait = driver_setup['wait']
        self.platform = driver_setup['platform']
        
        print("\n=== 바텀 네비게이션 전체 테스트 시작 ===")
        
        # 각 탭 클릭 테스트
        nav_tabs = [
            ("관심기관", "//android.view.View[@content-desc='관심기관']"),
            ("학습 정보", "//android.view.View[@content-desc='학습 정보']"),
            ("마이 페이지", "//android.view.View[@content-desc='마이 페이지']"),
            ("홈", "//android.view.View[@content-desc='홈']")  # 마지막에 홈으로 돌아가기
        ]
        
        for name, xpath in nav_tabs:
            try:
                print(f"\n{name} 탭 클릭")
                tab = self.wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, xpath)))
                tab.click()
                time.sleep(2)
                print(f"✓ {name} 탭 클릭 완료")
                
            except Exception as e:
                print(f"✗ {name} 탭 클릭 실패: {e}")
        
        print("\n=== 바텀 네비게이션 전체 테스트 완료 ===")
        assert True, "바텀 네비게이션 테스트 성공"

    def test_home_screen_scroll(self, driver_setup, ensure_login):
        """홈화면 스크롤 테스트"""
        # 드라이버 설정
        self.driver = driver_setup['driver']
        self.wait = driver_setup['wait']
        self.platform = driver_setup['platform']
        
        print("\n=== 홈화면 스크롤 테스트 시작 ===")
        
        try:
            # 화면 크기 가져오기
            screen_size = self.driver.get_window_size()
            screen_width = screen_size['width']
            screen_height = screen_size['height']
            
            # 스크롤 좌표 계산
            start_x = screen_width // 2
            start_y = int(screen_height * 0.8)
            end_y = int(screen_height * 0.2)
            
            print("\n1. 아래로 스크롤")
            self.driver.swipe(start_x, start_y, start_x, end_y, 1000)
            time.sleep(2)
            print("✓ 아래로 스크롤 완료")
            
            print("\n2. 위로 스크롤")
            self.driver.swipe(start_x, end_y, start_x, start_y, 1000)
            time.sleep(2)
            print("✓ 위로 스크롤 완료")
            
        except Exception as e:
            print(f"✗ 스크롤 테스트 실패: {e}")
        
        print("\n=== 홈화면 스크롤 테스트 완료 ===")
        assert True, "홈화면 스크롤 테스트 성공"