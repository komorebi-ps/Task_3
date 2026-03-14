from selenium.webdriver.common.by import By

class ProfilePageLocators:

    ORDER_HISTORY_BUTTON = (By.XPATH, "//*[@href='/account/order-history']")
    LOGOUT_BUTTON = (By.XPATH, "//button[text()='Выход']")
    ORDERS_HISTORY_LIST = (By.XPATH, "//*[contains(@class, 'OrderHistory_profileList')]")
    ORDER_HISTORY_ITEMS = (By.XPATH, "//*[contains(@class, 'OrderHistory_profileList')]/li")
    ORDER_NUMBER = (By.CLASS_NAME, "text_type_digits-default")

    