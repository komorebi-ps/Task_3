RECOVERY_EMAIL = 'test_nujo@mail.ru'

user_login_data = {
    "email": "test_test38745@ya.ru",
    "password": "qazwsx123"
}

from locators.construtor_page_locators import ConstructorPageLocators

INGREDIENT_LOCATORS = {
    "bun": ConstructorPageLocators.FLUORESCENT_BUN,
    "sauce": ConstructorPageLocators.SAUCE_SPICY_X_COUNTER,
    "cutlet": ConstructorPageLocators.BIO_MARSIAN_MAGNOLIA
}

INGREDIENT_LIST = ['bun', 'sauce', 'cutlet']

INGREDIENT_COUNTERS = {
    "bun": ConstructorPageLocators.FLUORESCENT_BUN_COUNTER,
    "sauce": ConstructorPageLocators.SAUCE_SPICY_X_COUNTER,
    "cutlet": ConstructorPageLocators.BIO_MARSIAN_MAGNOLIA_COUNTER
}
