from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def open(self, url):
        self.driver.get(url)

    def find(self, locator):
        return self.driver.find_element(*locator)

    def find_all(self, locator):
        return self.driver.find_elements(*locator)

    def click(self, locator):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(locator)
        ).click()

    def js_click(self, locator):
        element = self.find(locator)
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});", element
        )
        self.driver.execute_script("arguments[0].click();", element)

    def get_text_content(self, locator):
        element = self.find(locator)
        return self.driver.execute_script("return arguments[0].textContent;", element)

    def get_attribute(self, locator, attribute):
        return self.find(locator).get_attribute(attribute)

    def is_element_visible(self, locator, timeout=10):
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)
            )
            return True
        except Exception:
            return False

    def wait_until_visible(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )

    def get_current_url(self):
        return self.driver.current_url

    def get_window_handles(self):
        return self.driver.window_handles

    def wait_for_new_window(self, original_handles, timeout=10):
        WebDriverWait(self.driver, timeout).until(
            lambda d: len(d.window_handles) > len(original_handles)
        )
        return [h for h in self.driver.window_handles if h not in original_handles][0]

    def switch_to_window(self, handle):
        self.driver.switch_to.window(handle)

    def close_current_window_and_switch_to(self, handle):
        self.driver.close()
        self.driver.switch_to.window(handle)

    def wait_until_url_contains(self, substring, timeout=10):
        WebDriverWait(self.driver, timeout).until(lambda d: substring in d.current_url)