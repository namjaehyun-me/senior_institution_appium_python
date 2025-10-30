# scroll_helper_plus.py
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ScrollHelper:
    def __init__(self, driver, timeout=12):
        self.d = driver['driver'] if isinstance(driver, dict) else driver
        self.platform = (
            driver.get('platform','android') if isinstance(driver, dict)
            else ('ios' if self.d.capabilities.get('platformName','').lower()=='ios' else 'android')
        )
        self.wait = WebDriverWait(self.d, timeout)

    def wait_visible(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def wait_clickable(self, locator):
        return self.wait.until(EC.element_to_be_clickable(locator))

    def exists(self, locator):
        by, sel = locator
        return len(self.d.find_elements(by, sel)) > 0

    def _swipe_screen_percent(self, start_x, start_y, end_x, end_y, duration_ms=400):
        try:
            self.d.swipe(start_x, start_y, end_x, end_y, duration_ms)
        except Exception:
            # 필요시 W3C actions로 대체 가능
            pass

    def _swipe_container(self, container_el, dx_ratio, dy_ratio, duration_ms=400):
        r = container_el.rect
        start_x = int(r['x'] + r['width'] * (0.5 - dx_ratio/2))
        end_x   = int(r['x'] + r['width'] * (0.5 + dx_ratio/2))
        start_y = int(r['y'] + r['height']* (0.5 - dy_ratio/2))
        end_y   = int(r['y'] + r['height']* (0.5 + dy_ratio/2))
        self._swipe_screen_percent(start_x, start_y, end_x, end_y, duration_ms)

    def into_view(self, target_locator, *, container_locator=None, direction='down', max_swipes=8):
        """
        target_locator: (By, selector)
        container_locator: (By, selector) | None  → None이면 화면 전체 스크롤
        direction: 'down' | 'up' | 'left' | 'right'
        """
        # 먼저 보이는지
        if self.exists(target_locator):
            return self.wait_visible(target_locator)

        container_el = None
        if container_locator:
            by, sel = container_locator
            els = self.d.find_elements(by, sel)
            container_el = els[0] if els else None

        for _ in range(max_swipes):
            if self.platform == 'ios':
                # iOS: 컨테이너 지정 시 해당 엘리먼트 기준 스크롤 제스처 사용
                if container_el:
                    self.d.execute_script("mobile: scroll", {
                        "elementId": container_el.id,
                        "direction": direction
                    })
                else:
                    self.d.execute_script("mobile: scroll", {"direction": direction})
            else:
                # Android: 컨테이너가 있으면 컨테이너 내부 스와이프, 없으면 화면 스와이프
                if container_el:
                    # 세로/가로에 맞춰 스와이프 벡터 결정
                    if direction in ('down','up'):
                        dy = -0.6 if direction=='down' else 0.6
                        self._swipe_container(container_el, dx_ratio=0.0, dy_ratio=abs(dy))
                    else:
                        dx = -0.7 if direction=='left' else 0.7
                        self._swipe_container(container_el, dx_ratio=abs(dx), dy_ratio=0.0)
                else:
                    size = self.d.get_window_size()
                    w, h = size['width'], size['height']
                    if direction == 'down':
                        self._swipe_screen_percent(int(w*0.5), int(h*0.8), int(w*0.5), int(h*0.2))
                    elif direction == 'up':
                        self._swipe_screen_percent(int(w*0.5), int(h*0.2), int(w*0.5), int(h*0.8))
                    elif direction == 'left':
                        self._swipe_screen_percent(int(w*0.8), int(h*0.5), int(w*0.2), int(h*0.5))
                    else:  # right
                        self._swipe_screen_percent(int(w*0.2), int(h*0.5), int(w*0.8), int(h*0.5))

            if self.exists(target_locator):
                return self.wait_visible(target_locator)

        raise RuntimeError(f"스크롤해도 요소를 못 찾음: {target_locator} (direction={direction}, container={container_locator})")
