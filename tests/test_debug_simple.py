import pytest
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
import time

class TestDebugSimple:
    """간단한 디버깅 테스트"""
    
    def test_simple_tap_and_swipe(self, driver_setup):
        """기본 탭과 스와이프 테스트"""
        driver = driver_setup['driver']
        
        try:
            print("\n🔍 현재 화면 정보 확인 중...")
            
            # 현재 액티비티 확인
            current_activity = driver.current_activity
            print(f"현재 액티비티: {current_activity}")
            
            # 화면 크기 확인
            screen_size = driver.get_window_size()
            print(f"화면 크기: {screen_size}")
            
            # 현재 화면의 모든 요소 확인
            all_elements = driver.find_elements(AppiumBy.XPATH, "//*[@clickable='true']")
            print(f"클릭 가능한 요소 개수: {len(all_elements)}")
            
            # 처음 5개 요소 정보 출력
            for i, element in enumerate(all_elements[:5]):
                try:
                    text = element.get_attribute('text') or ''
                    content_desc = element.get_attribute('content-desc') or ''
                    resource_id = element.get_attribute('resource-id') or ''
                    print(f"  요소 {i+1}: text='{text}', desc='{content_desc}', id='{resource_id}'")
                except:
                    print(f"  요소 {i+1}: 정보 읽기 실패")
            
            print("\n📱 기본 동작 테스트 시작...")
            
            # 1. 화면 중앙 탭
            center_x = screen_size['width'] // 2
            center_y = screen_size['height'] // 2
            print(f"화면 중앙 ({center_x}, {center_y}) 탭")
            driver.tap([(center_x, center_y)])
            time.sleep(2)
            
            # 2. 위로 스와이프 (스크롤 다운)
            start_x = center_x
            start_y = int(screen_size['height'] * 0.8)
            end_x = center_x
            end_y = int(screen_size['height'] * 0.2)
            print(f"스와이프: ({start_x}, {start_y}) -> ({end_x}, {end_y})")
            driver.swipe(start_x, start_y, end_x, end_y, 1000)
            time.sleep(2)
            
            # 3. 아래로 스와이프 (스크롤 업)
            print(f"스와이프: ({end_x}, {end_y}) -> ({start_x}, {start_y})")
            driver.swipe(end_x, end_y, start_x, start_y, 1000)
            time.sleep(2)
            
            # 4. 뒤로가기
            print("뒤로가기 실행")
            driver.back()
            time.sleep(2)
            
            print("✅ 기본 동작 테스트 완료")
            
        except Exception as e:
            print(f"❌ 테스트 실패: {str(e)}")
            pytest.fail(f"디버깅 테스트 실패: {str(e)}")
    
    def test_find_common_elements(self, driver_setup):
        """일반적인 요소들 찾기 테스트"""
        driver = driver_setup['driver']
        wait = WebDriverWait(driver, 5)
        
        try:
            print("\n🔍 일반적인 요소들 찾기 테스트...")
            
            # 일반적인 버튼들 찾기
            common_selectors = [
                ("다음 버튼", AppiumBy.ACCESSIBILITY_ID, "다음"),
                ("확인 버튼", AppiumBy.ACCESSIBILITY_ID, "확인"),
                ("등록하기 버튼", AppiumBy.ACCESSIBILITY_ID, "등록하기"),
                ("메인이동 버튼", AppiumBy.ACCESSIBILITY_ID, "메인이동"),
                ("뒤로가기 버튼", AppiumBy.ACCESSIBILITY_ID, "뒤로가기"),
                ("다음 텍스트", AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("다음")'),
                ("확인 텍스트", AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("확인")'),
                ("등록하기 텍스트", AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("등록하기")'),
            ]
            
            found_elements = []
            
            for name, by, value in common_selectors:
                try:
                    element = driver.find_element(by, value)
                    if element.is_displayed():
                        found_elements.append((name, element))
                        print(f"✅ {name} 발견")
                    else:
                        print(f"⚠️ {name} 존재하지만 보이지 않음")
                except:
                    print(f"❌ {name} 찾을 수 없음")
            
            # 발견된 요소들 중 하나 클릭해보기
            if found_elements:
                name, element = found_elements[0]
                print(f"\n👆 {name} 클릭 테스트")
                element.click()
                time.sleep(2)
                print(f"✅ {name} 클릭 완료")
            else:
                print("❌ 클릭할 수 있는 요소를 찾지 못했습니다")
            
        except Exception as e:
            print(f"❌ 요소 찾기 테스트 실패: {str(e)}")
    
    def test_coordinate_actions(self, driver_setup):
        """좌표 기반 동작 테스트"""
        driver = driver_setup['driver']
        
        try:
            print("\n📍 좌표 기반 동작 테스트...")
            
            screen_size = driver.get_window_size()
            width = screen_size['width']
            height = screen_size['height']
            
            # 화면의 여러 지점 탭해보기
            test_points = [
                ("좌상단", int(width * 0.1), int(height * 0.1)),
                ("우상단", int(width * 0.9), int(height * 0.1)),
                ("중앙", int(width * 0.5), int(height * 0.5)),
                ("좌하단", int(width * 0.1), int(height * 0.9)),
                ("우하단", int(width * 0.9), int(height * 0.9)),
            ]
            
            for name, x, y in test_points:
                print(f"📍 {name} ({x}, {y}) 탭")
                driver.tap([(x, y)])
                time.sleep(1)
            
            # 다양한 방향 스와이프
            swipe_tests = [
                ("위로", width//2, int(height*0.8), width//2, int(height*0.2)),
                ("아래로", width//2, int(height*0.2), width//2, int(height*0.8)),
                ("왼쪽으로", int(width*0.8), height//2, int(width*0.2), height//2),
                ("오른쪽으로", int(width*0.2), height//2, int(width*0.8), height//2),
            ]
            
            for name, sx, sy, ex, ey in swipe_tests:
                print(f"👆 {name} 스와이프: ({sx},{sy}) -> ({ex},{ey})")
                driver.swipe(sx, sy, ex, ey, 800)
                time.sleep(1)
            
            print("✅ 좌표 기반 동작 테스트 완료")
            
        except Exception as e:
            print(f"❌ 좌표 동작 테스트 실패: {str(e)}")
            pytest.fail(f"좌표 동작 테스트 실패: {str(e)}")