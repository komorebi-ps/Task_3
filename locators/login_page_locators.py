from selenium.webdriver.common.by import By

class LoginPageLocators:

    EMAIL_INPUT = (By.XPATH, "//label[text()='Email']/../input")
    PASS_INPUT = (By.XPATH, "//label[text()='Пароль']/../input")
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти']")
    