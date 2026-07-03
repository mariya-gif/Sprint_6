# pages/order_page.py
from pages.base_page import BasePage
from locators.order_locators import OrderPageLocators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class OrderPage(BasePage):
    # --- Шаг 1 ---
    def fill_name(self, name):
        self.driver.find_element(*OrderPageLocators.NAME_INPUT).send_keys(name)

    def fill_surname(self, surname):
        self.driver.find_element(*OrderPageLocators.SURNAME_INPUT).send_keys(surname)

    def fill_address(self, address):
        self.driver.find_element(*OrderPageLocators.ADDRESS_INPUT).send_keys(address)

    def select_metro_station(self, search_text, station_name):
        self.driver.find_element(*OrderPageLocators.METRO_INPUT).send_keys(search_text)
        locator = OrderPageLocators.metro_option(station_name)
        option = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(locator)
        )
        option.click()

    def fill_phone(self, phone):
        self.driver.find_element(*OrderPageLocators.PHONE_INPUT).send_keys(phone)

    def click_next(self):
        self.click(OrderPageLocators.NEXT_BUTTON)

    def fill_step_one(self, name, surname, address, metro_search, metro_station, phone):
        self.fill_name(name)
        self.fill_surname(surname)
        self.fill_address(address)
        self.select_metro_station(metro_search, metro_station)
        self.fill_phone(phone)
        self.click_next()

    # --- Шаг 2 ---
    def select_delivery_date_today(self):
        self.click(OrderPageLocators.DATE_INPUT)
        self.click(OrderPageLocators.DATE_TODAY_OPTION)

    def select_rent_period(self, period_text):
        self.click(OrderPageLocators.RENT_PERIOD_DROPDOWN)
        option = self.driver.find_element(*OrderPageLocators.rent_period_option(period_text))
        option.click()

    def select_color(self, color):
        locator = (
            OrderPageLocators.BLACK_COLOR_CHECKBOX
            if color == "black"
            else OrderPageLocators.GREY_COLOR_CHECKBOX
        )
        self.driver.find_element(*locator).click()

    def fill_comment(self, comment):
        if comment:
            self.driver.find_element(*OrderPageLocators.COMMENT_INPUT).send_keys(comment)

    def click_create_order(self):
        self.click(OrderPageLocators.CREATE_ORDER_BUTTON)
        self.click(OrderPageLocators.CONFIRM_YES_BUTTON)

    def is_order_success_shown(self):
        return self.is_element_visible(OrderPageLocators.SUCCESS_MODAL_HEADING)

    def fill_step_two(self, rent_period, color, comment=""):
        self.select_delivery_date_today()
        self.select_rent_period(rent_period)
        self.select_color(color)
        self.fill_comment(comment)
        self.click_create_order()