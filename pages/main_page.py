import allure

from pages.base_page import BasePage
from locators.main_locators import MainPageLocators
from url import MAIN_URL


class MainPage(BasePage):
    def open_main(self):
        self.open(MAIN_URL)

    # --- Аккордеон ---
    def get_accordion_items_count(self):
        return len(self.find_all(MainPageLocators.ACCORDION_ITEMS))

    def open_accordion_item(self, index):
        self.js_click(MainPageLocators.accordion_heading(index))

    def is_accordion_panel_expanded(self, index):
        return self.get_attribute(
            MainPageLocators.accordion_heading(index), "aria-expanded"
        ) == "true"

    def get_accordion_panel_text(self, index):
        return self.get_text_content(MainPageLocators.accordion_panel(index))

    # --- Кнопки заказа ---
    def click_order_button_top(self):
        self.js_click(MainPageLocators.ORDER_BUTTON_TOP)

    def click_order_button_bottom(self):
        self.js_click(MainPageLocators.ORDER_BUTTON_BOTTOM)

    # --- Логотипы ---
    @allure.step("Клик по лого самоката должен вернуть на главную страницу")
    def click_scooter_logo(self):
        self.js_click(MainPageLocators.SCOOTER_LOGO)

    def is_on_main_page(self):
        return self.get_current_url() == MAIN_URL

    @allure.step("Клик по лого Яндекса должен открыть Дзен в новой вкладке через редирект")
    def click_yandex_logo_and_get_new_tab_url(self):
        original_handles = self.get_window_handles()
        self.js_click(MainPageLocators.YANDEX_LOGO)

        new_handle = self.wait_for_new_window(original_handles)
        self.switch_to_window(new_handle)

        self.wait_until_url_contains("dzen")
        redirected_url = self.get_current_url()

        self.close_current_window_and_switch_to(original_handles[0])
        return redirected_url