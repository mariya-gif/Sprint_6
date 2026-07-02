# pages/main_page.py
from pages.base_page import BasePage
from locators.main_locators import MainPageLocators
from url import MAIN_URL

class MainPage(BasePage):
    def open_main(self):
        self.open(MAIN_URL)

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