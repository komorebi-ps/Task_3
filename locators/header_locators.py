from selenium.webdriver.common.by import By

class HeaderLocators:
    
    PROFILE_BUTTON = (By.XPATH, "//*[text()='Личный Кабинет']/..")   
    ORDER_FEED_BUTTON = (By.XPATH, "//*[text()='Лента Заказов']/..")
    CONSTRUCTOR_BUTTON = (By.XPATH, "//*[text()='Конструктор']/..")
    OVERLAY_MODAL_WINDOW = (By.XPATH, "//*[contains(@class, 'Modal_modal_overlay')]")
    