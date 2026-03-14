from selenium.webdriver.common.by import By

class PassRecoveryPageLocators:
    
    PASS_RECOVERY_BUTTON = (By.XPATH, "//*[text()='Восстановить пароль']")
    PASS_RECOVERY_PAGE_LOCATOR = (By.XPATH, "//h2[text()='Восстановление пароля']")
    EMAIL_INPUT = (By.XPATH, "//label[text()='Email']/../input")
    RECOVER_BUTTON = (By.XPATH, "//button[text()='Восстановить']")
    SAVE_BUTTON = (By.XPATH, "//button[text()='Сохранить']")
    SHOW_PASS_BUTTON = (By.XPATH, "//*[@class='input__icon input__icon-action']")
    PASS_INPUT_ACTIVE = (By.XPATH, "//div[contains(@class, 'input_status_active')]")
    
    

