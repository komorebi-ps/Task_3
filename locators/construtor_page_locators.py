from selenium.webdriver.common.by import By

class ConstructorPageLocators:

    CONSTRUCTOR_PAGE_LOCATOR = (By.XPATH, "//*[text()='Соберите бургер']") 
    FLUORESCENT_BUN_DETAILS_WINDOW = (By.XPATH, "//div[contains(@class, 'Modal_modal__contentBox')]/p[text()='Флюоресцентная булка R2-D3']")
    FLUORESCENT_BUN = (By.XPATH, "//*[@alt='Флюоресцентная булка R2-D3']")
    SAUCE_SPICY_X = (By.XPATH, "//*[@alt='Соус Spicy-X']")
    BIO_MARSIAN_MAGNOLIA = (By.XPATH, "//*[@alt='Биокотлета из марсианской Магнолии']")
    DROP_AREA = (By.XPATH, "//section[contains(@class, 'BurgerConstructor_basket')]")
    FLUORESCENT_BUN_COUNTER = (By.XPATH, "//*[@alt='Флюоресцентная булка R2-D3']/../div/p[contains(@class, 'counter')]")
    SAUCE_SPICY_X_COUNTER = (By.XPATH, "//*[@alt='Соус Spicy-X']/../div/p[contains(@class, 'counter')]")   
    BIO_MARSIAN_MAGNOLIA_COUNTER = (By.XPATH, "//*[@alt='Биокотлета из марсианской Магнолии']/../div/p[contains(@class, 'counter')]")
    DETAILS_WINDOW_CLOSE_BUTTON = (By.XPATH, "//*[text()='Флюоресцентная булка R2-D3']/../../button")
    CREATE_ORDER_BUTTON = (By.XPATH, "//button[text()='Оформить заказ']")
    ORDER_MODAL_WINDOW = (By.XPATH, "//*[text()='Ваш заказ начали готовить']")
    ORDER_WINDOW_CLOSE_BUTTON = (By.XPATH, "//button[contains(@class, 'Modal_modal__close')]")
    ORDER_NUMBER = (By.XPATH, "//*[text()='идентификатор заказа']/preceding-sibling::h2")
    THIRD_ADDED_INGREDIENT_IN_BASKET = (By.XPATH, "//span[contains(@class, 'BurgerConstructor_basket__listContainer')]/li[2]")
