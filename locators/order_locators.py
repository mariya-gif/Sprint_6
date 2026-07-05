# locators/order_locators.py
from selenium.webdriver.common.by import By


class OrderPageLocators:
    # Шаг 1
    NAME_INPUT = (By.CSS_SELECTOR, "input[placeholder='* Имя']")
    SURNAME_INPUT = (By.CSS_SELECTOR, "input[placeholder='* Фамилия']")
    ADDRESS_INPUT = (By.CSS_SELECTOR, "input[placeholder='* Адрес: куда привезти заказ']")
    METRO_INPUT = (By.CSS_SELECTOR, ".select-search__input")
    PHONE_INPUT = (By.CSS_SELECTOR, "input[placeholder='* Телефон: на него позвонит курьер']")
    NEXT_BUTTON = (By.CSS_SELECTOR, ".Order_NextButton__1_rCA button")
    CONFIRM_YES_BUTTON = (By.XPATH, "//div[contains(@class, 'Order_Modal')]//button[text()='Да']")
    SUCCESS_MODAL_HEADING = (By.XPATH, "//div[contains(@class, 'Order_Modal')]//div[text()='Заказ оформлен']")

    @staticmethod
    def metro_option(station_name):
        return (By.XPATH, f"//div[contains(@class, 'select-search__select')]//*[contains(., '{station_name}')]")

    # Шаг 2
    DATE_INPUT = (By.CSS_SELECTOR, "input[placeholder='* Когда привезти самокат']")
    DATE_TODAY_OPTION = (By.CSS_SELECTOR, ".react-datepicker__day--today")
    RENT_PERIOD_DROPDOWN = (By.CSS_SELECTOR, ".Dropdown-control")
    COMMENT_INPUT = (By.CSS_SELECTOR, "input[placeholder='Комментарий для курьера']")
    BLACK_COLOR_CHECKBOX = (By.ID, "black")
    GREY_COLOR_CHECKBOX = (By.ID, "grey")
    BACK_BUTTON = (By.XPATH, "//div[contains(@class, 'Order_Buttons')]//button[text()='Назад']")
    CREATE_ORDER_BUTTON = (By.XPATH, "//div[contains(@class, 'Order_Buttons')]//button[text()='Заказать']")

    @staticmethod
    def rent_period_option(period_text):
        return (By.XPATH, f"//div[contains(@class, 'Dropdown-menu')]//div[text()='{period_text}']")