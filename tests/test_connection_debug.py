import pytest
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
import time

class TestConnectionDebug:
    """Appium 연결 상태 디버깅"""
    
    def test_connection_status(self, driver_setup):
        """연결 상태 확인"""
        driver = driver_setup['driver']
        
        try:
            print("\n🔍 Appium 연결 상태 디버깅")
            
            # 1. 세션 정보 확인
            session_id = driver.session_id
            print(f"📱 세션 ID: {session_id}")
            
            # 2. 디바이스 정보 확인
            capabilities = driver.capabilities
            print(f"📱 Capabilities: {capabilities}")
            
            # 3. 현재 액티비티 확인
            try:
                current_activity = driver.current_activity
                print(f"📱 현재 액티비티: {current_activity}")
            except Exception as e:
                print(f"❌ 액티비티 가져오기 실패: {e}")
            
            # 4. 화면 크기 확인
            try:
                screen_size = driver.get_window_size()
                print(f"📱 화면 크기: {screen_size}")
            except Exception as e:
                print(f"❌ 화면 크기 가져오기 실패: {e}")
            
            # 5. 앱 상태 확인
            try:
                app_state = driver.query_app_state("com.teammapa.seniorcare.patient")
                print(f"📱 앱 상태: {app_state}")
                # 0: not installed, 1: not running, 2: running in background, 3: running in background suspended, 4: running in foreground
            except Exception as e:
                print(f"❌ 앱 상태 확인 실패: {e}")
            
            # 6. 페이지 소스 일부 확인
            try:
                page_source = driver.page_source[:500]  # 처음 500자만
                print(f"📱 페이지 소스 (일부): {page_source}")
            except Exception as e:
                print(f"❌ 페이지 소스 가져오기 실패: {e}")
            
            # 7. 강제로 앱 활성화 시도
            try:
                print("🔄 앱 활성화 시도...")
                driver.activate_app("com.teammapa.seniorcare.patient")
                time.sleep(2)
                print("✅ 앱 활성화 완료")
            except Exception as e:
                print(f"❌ 앱 활성화 실패: {e}")
            
            # 8. 디바이스 깨우기 시도
            try:
                print("🔄 디바이스 깨우기 시도...")
                if not driver.is_locked():
                    print("✅ 디바이스가 이미 깨어있음")
                else:
                    driver.unlock()
                    print("✅ 디바이스 잠금 해제")
            except Exception as e:
                print(f"❌ 디바이스 깨우기 실패: {e}")
            
            # 9. 홈 버튼 누르기 시도
            try:
                print("🔄 홈 버튼 누르기...")
                driver.press_keycode(3)  # HOME key
                time.sleep(1)
                print("✅ 홈 버튼 누르기 완료")
            except Exception as e:
                print(f"❌ 홈 버튼 누르기 실패: {e}")
            
            # 10. 다시 앱 실행
            try:
                print("🔄 앱 다시 실행...")
                driver.activate_app("com.teammapa.seniorcare.patient")
                time.sleep(2)
                print("✅ 앱 다시 실행 완료")
            except Exception as e:
                print(f"❌ 앱 다시 실행 실패: {e}")
            
        except Exception as e:
            print(f"❌ 연결 디버깅 실패: {str(e)}")
            pytest.fail(f"연결 디버깅 실패: {str(e)}")
    
    def test_force_interaction(self, driver_setup):
        """강제 상호작용 테스트"""
        driver = driver_setup['driver']
        
        try:
            print("\n💪 강제 상호작용 테스트")
            
            # 1. 앱이 포그라운드에 있는지 확인
            try:
                driver.activate_app("com.teammapa.seniorcare.patient")
                time.sleep(2)
            except:
                pass
            
            # 2. ADB 명령어로 직접 탭 시도
            try:
                print("🔄 ADB 직접 탭 시도...")
                driver.execute_script("mobile: shell", {
                    "command": "input",
                    "args": ["tap", "500", "1000"]
                })
                time.sleep(2)
                print("✅ ADB 탭 완료")
            except Exception as e:
                print(f"❌ ADB 탭 실패: {e}")
            
            # 3. 키 이벤트 시도
            try:
                print("🔄 키 이벤트 시도...")
                driver.press_keycode(4)  # BACK key
                time.sleep(1)
                driver.press_keycode(3)  # HOME key
                time.sleep(1)
                print("✅ 키 이벤트 완료")
            except Exception as e:
                print(f"❌ 키 이벤트 실패: {e}")
            
            # 4. 화면 터치 이벤트
            try:
                print("🔄 화면 터치 이벤트...")
                driver.execute_script("mobile: touchAction", {
                    "action": "tap",
                    "options": {
                        "x": 500,
                        "y": 1000
                    }
                })
                time.sleep(2)
                print("✅ 터치 이벤트 완료")
            except Exception as e:
                print(f"❌ 터치 이벤트 실패: {e}")
            
            # 5. 스크린샷으로 변화 확인
            driver.save_screenshot("screenshots/force_interaction_test.png")
            print("📸 강제 상호작용 후 스크린샷 저장")
            
        except Exception as e:
            print(f"❌ 강제 상호작용 실패: {str(e)}")
    
    def test_restart_app(self, driver_setup):
        """앱 재시작 테스트"""
        driver = driver_setup['driver']
        
        try:
            print("\n🔄 앱 재시작 테스트")
            
            # 1. 현재 상태 확인
            driver.save_screenshot("screenshots/before_restart.png")
            
            # 2. 앱 종료
            try:
                print("🛑 앱 종료 중...")
                driver.terminate_app("com.teammapa.seniorcare.patient")
                time.sleep(2)
                print("✅ 앱 종료 완료")
            except Exception as e:
                print(f"❌ 앱 종료 실패: {e}")
            
            # 3. 앱 재시작
            try:
                print("🚀 앱 재시작 중...")
                driver.activate_app("com.teammapa.seniorcare.patient")
                time.sleep(3)
                print("✅ 앱 재시작 완료")
            except Exception as e:
                print(f"❌ 앱 재시작 실패: {e}")
            
            # 4. 재시작 후 상태 확인
            driver.save_screenshot("screenshots/after_restart.png")
            
            # 5. 간단한 동작 테스트
            screen_size = driver.get_window_size()
            center_x = screen_size['width'] // 2
            center_y = screen_size['height'] // 2
            
            print(f"👆 재시작 후 중앙 탭: ({center_x}, {center_y})")
            driver.tap([(center_x, center_y)])
            time.sleep(2)
            
            driver.save_screenshot("screenshots/after_restart_tap.png")
            print("📸 재시작 후 탭 스크린샷 저장")
            
        except Exception as e:
            print(f"❌ 앱 재시작 테스트 실패: {str(e)}")
            pytest.fail(f"앱 재시작 테스트 실패: {str(e)}")