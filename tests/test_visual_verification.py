import pytest
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput
import time

class TestVisualVerification:
    
    def test_visual_verification_scenario(self, driver):
        """시각적 검증 시나리오 테스트"""
        # driver가 딕셔너리인 경우 실제 driver 객체 추출
        if isinstance(driver, dict):
            actual_driver = driver['driver']
        else:
            actual_driver = driver
        
        try:
            time.sleep(2)
            
            # 탭 동작들
            self._perform_tap(actual_driver, 616, 517)
            print('1')
            time.sleep(1)
            self._perform_tap(actual_driver, 697, 2856)
            print('2')
            time.sleep(1)
            self._perform_tap(actual_driver, 479, 1206)
            print('3')
            time.sleep(1)
            self._perform_tap(actual_driver, 701, 2863)
            print('4')
            time.sleep(1)
            self._perform_tap(actual_driver, 704, 1830)
            print('5')
            time.sleep(1)
            self._perform_tap(actual_driver, 425, 375)
            print('6')
            time.sleep(1)
            self._send_text(actual_driver, "s")
            time.sleep(1)
            self._perform_tap(actual_driver, 1359, 375)
            print('7')
            time.sleep(1)
            self._perform_tap(actual_driver, 417, 635)
            print('8')
            time.sleep(1)
            self._perform_tap(actual_driver, 976, 2247)
            print('9')
            time.sleep(1)
            self._perform_tap(actual_driver, 915, 2171)
            print('10')
            time.sleep(1)
            self._perform_tap(actual_driver, 946, 2818)
            print('11')
            time.sleep(1)
            self._perform_tap(actual_driver, 1256, 1145)
            print('12')
            time.sleep(1)
            self._perform_tap(actual_driver, 371, 2098)
            print('13')
            time.sleep(1)
            
            # 스와이프 동작들
            self._perform_swipe(actual_driver, 731, 2630, 892, 1570)
            print('14')
            time.sleep(1)
            
            # 탭 동작
            self._perform_tap(actual_driver, 413, 2063)
            print('15')
            time.sleep(1)
            
            # 스와이프 동작들
            self._perform_swipe(actual_driver, 651, 1390, 624, 2573)
            print('16')
            time.sleep(1)
            self._perform_swipe(actual_driver, 815, 1428, 812, 1711)
            print('17')
            time.sleep(1)
            
            # 탭 동작들
            self._perform_tap(actual_driver, 1202, 2048)
            print('18')
            time.sleep(1)
            self._perform_tap(actual_driver, 1072, 2075)
            print('19')
            time.sleep(1)
            self._perform_tap(actual_driver, 992, 2312)
            print('20')
            time.sleep(1)
            
            # 스와이프 동작
            self._perform_swipe(actual_driver, 1045, 2810, 1152, 1424)
            print('21')
            time.sleep(1)
            
            # 탭 동작
            self._perform_tap(actual_driver, 1045, 2860)
            print('22')
            time.sleep(1)
            
            # 추가 동작들
            self._perform_tap(actual_driver, 682, 1574)
            print('23')
            time.sleep(1)
            self._perform_tap(actual_driver, 817, 1830)
            print('24')
            time.sleep(1)
            self._perform_swipe(actual_driver, 867, 2800, 1013, 1318)
            print('25')
            time.sleep(1)
            self._perform_tap(actual_driver, 1080, 2875)
            print('26')
            time.sleep(1)
            self._perform_tap(actual_driver, 686, 1656)
            print('27')
            time.sleep(1)
            self._perform_tap(actual_driver, 206, 2065)
            print('28')
            time.sleep(1)
            self._perform_tap(actual_driver, 362, 2814)
            print('29')
            time.sleep(1)
            self._perform_swipe(actual_driver, 991, 2658, 1144, 1123)
            print('30')
            time.sleep(1)
            self._perform_tap(actual_driver, 1094, 2853)
            print('31')
            time.sleep(1)
            self._perform_swipe(actual_driver, 640, 2445, 839, 384)
            print('32')
            time.sleep(1)
            self._perform_swipe(actual_driver, 771, 2672, 768, 679)
            print('33')
            time.sleep(1)
            self._perform_tap(actual_driver, 981, 2821)
            print('34')
            time.sleep(1)
            self._perform_tap(actual_driver, 423, 1059)
            print('35')
            time.sleep(1)
            self._perform_tap(actual_driver, 956, 2875)
            print('36')
            time.sleep(1)
            self._perform_swipe(actual_driver, 679, 2786, 746, 657)
            print('37')
            time.sleep(1)
            self._perform_tap(actual_driver, 981, 2857)
            print('38')
            time.sleep(1)
            self._perform_tap(actual_driver, 981, 2857)
            print('39')
            time.sleep(1)
            self._perform_tap(actual_driver, 114, 256)
            print('40')
            time.sleep(1)
            
        except Exception as e:
            pytest.fail(f"시각적 검증 시나리오 테스트 실패: {str(e)}")
    
    def _perform_swipe(self, driver, start_x, start_y, end_x, end_y):
        """스와이프 동작 수행"""
        actions = ActionChains(driver)
        actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
        actions.w3c_actions.pointer_action.move_to_location(start_x, start_y)
        actions.w3c_actions.pointer_action.pointer_down()
        actions.w3c_actions.pointer_action.move_to_location(end_x, end_y)
        actions.w3c_actions.pointer_action.release()
        actions.perform()
    
    def _perform_tap(self, driver, x, y):
        """탭 동작 수행"""
        actions = ActionChains(driver)
        actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
        actions.w3c_actions.pointer_action.move_to_location(x, y)
        actions.w3c_actions.pointer_action.pointer_down()
        actions.w3c_actions.pointer_action.pause(0.1)
        actions.w3c_actions.pointer_action.release()
        actions.perform()
    
    def _send_text(self, driver, text):
        """텍스트 입력"""
        from selenium.webdriver.common.keys import Keys
        actions = ActionChains(driver)
        actions.send_keys(text)
        actions.perform()