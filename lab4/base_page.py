from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class BasePage:
    def __init__(self, driver, url, timeout=10):
        self.driver = driver
        self.url = url
        self.default_wait = WebDriverWait(driver, timeout)
    
    def open(self):
        self.driver.get(self.url)
    
    def _get_wait(self, timeout=None):
        return WebDriverWait(self.driver, timeout) if timeout else self.default_wait
    
    def find_element(self, locator, timeout=None):
        try:
            wait = self._get_wait(timeout)
            return wait.until(EC.presence_of_element_located(locator))
        except TimeoutException:
            return None
    
    def find_clickable_element(self, locator, timeout=None):
        try:
            wait = self._get_wait(timeout)
            return wait.until(EC.element_to_be_clickable(locator))
        except TimeoutException:
            return None
    
    def is_element_visible(self, locator, timeout=5):
        element = self.find_element(locator, timeout)
        return element is not None and element.is_displayed()
    
    def get_element_text(self, locator):
        element = self.find_element(locator)
        return element.text.strip() if element else ""