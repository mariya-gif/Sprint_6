# pages/main_page.py
import allure
from selenium.webdriver.support.wait import WebDriverWait

from pages.base_page import BasePage
from locators.main_locators import MainPageLocators
from url import MAIN_URL


class MainPage(BasePage):
    def open_main(self):
        self.open(MAIN_URL)

    # --- Аккордеон ---
    def get_accordion_items_count(self):
        items = self.driver.find_elements(*MainPageLocators.ACCORDION_ITEMS)
        return len(items)

    def open_accordion_item(self, index):
        locator = MainPageLocators.accordion_heading(index)
        element = self.driver.find_element(*locator)
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});", element
        )
        self.driver.execute_script("arguments[0].click();", element)

    def is_accordion_panel_expanded(self, index):
        heading = self.driver.find_element(*MainPageLocators.accordion_heading(index))
        return heading.get_attribute("aria-expanded") == "true"

    def get_accordion_panel_text(self, index):
        locator = MainPageLocators.accordion_panel(index)
        panel = self.driver.find_element(*locator)
        return self.driver.execute_script("return arguments[0].textContent;", panel)

    # --- Кнопки заказа ---
    def click_order_button_top(self):
        self._js_click(MainPageLocators.ORDER_BUTTON_TOP)

    def click_order_button_bottom(self):
        self._js_click(MainPageLocators.ORDER_BUTTON_BOTTOM)

    # --- Логотипы ---
    @allure.step("Клик по лого самоката должен вернуть на главную страницу")
    def click_scooter_logo(self):
        self._js_click(MainPageLocators.SCOOTER_LOGO)

    @allure.step("Клик по лого Яндекса должен открыть Дзен в новой вкладке через редирект")
    def click_yandex_logo_and_get_new_tab_url(self):
        original_handles = self.driver.window_handles
        self._js_click(MainPageLocators.YANDEX_LOGO)

        WebDriverWait(self.driver, 10).until(
            lambda d: len(d.window_handles) > len(original_handles)
        )
        new_handle = [h for h in self.driver.window_handles if h not in original_handles][0]
        self.driver.switch_to.window(new_handle)

        WebDriverWait(self.driver, 10).until(lambda d: "dzen" in d.current_url)
        redirected_url = self.driver.current_url

        self.driver.close()
        self.driver.switch_to.window(original_handles[0])
        return redirected_url

    # --- Вспомогательное ---
    def _js_click(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});", element
        )
        self.driver.execute_script("arguments[0].click();", element)