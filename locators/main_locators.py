from selenium.webdriver.common.by import By

class MainPageLocators:
    ORDER_BUTTON_TOP = (By.CSS_SELECTOR, ".Header_Nav__AGCXC button")
    ORDER_BUTTON_BOTTOM = (By.CSS_SELECTOR, ".Home_FinishButton__1_cWm button")
    ACCORDION_ITEMS = (By.CSS_SELECTOR, ".accordion__item")

    @staticmethod
    def accordion_heading(index):
        return (By.CSS_SELECTOR, f"#accordion__heading-{index}")

    @staticmethod
    def accordion_panel(index):
        return (By.CSS_SELECTOR, f"#accordion__panel-{index}")