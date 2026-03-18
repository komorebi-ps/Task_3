import pytest
import allure
from data import INGREDIENT_LOCATORS, INGREDIENT_COUNTERS, INGREDIENT_LIST


class TestConstructorPage:

    @allure.title('Авторизованный пользователь может сделать заказ')
    def test_authorised_user_creates_order_successfully(self, constructor_page, user_login_fixture):

        order_number = constructor_page.create_order(INGREDIENT_LOCATORS, INGREDIENT_LIST)
        
        assert order_number
        assert order_number != '9999', f"Номер заказа не получен" 


    @allure.title('По клику на ингредиент открывается окно с его деталями')
    def test_ingredient_details_window_opens(self, constructor_page, user_login_fixture):

        constructor_page.click_on_ingredient_fluorescent_bun()
        ingredient_details_window = constructor_page.modal_window_check()

        assert ingredient_details_window


    @allure.title('Окно с деталями ингредиента закрывается по клику на крестик')   
    def test_ingredient_details_window_closes(self, constructor_page, user_login_fixture):

        constructor_page.click_on_ingredient_fluorescent_bun()
        constructor_page.modal_window_check()
        constructor_page.click_on_modal_close_button()
        modal_window_is_closed = constructor_page.modal_window_is_closed()

        assert modal_window_is_closed


    @allure.title('Увеличение каунтера ингредиента при добавлении этого ингредиента в заказ: у булки на 2')
    def test_counter_number_increases_bun(self, constructor_page, user_login_fixture):
        
        constructor_page.add_ingredient_to_order(INGREDIENT_LOCATORS, 'bun')
        bun_counter_number = constructor_page.ingredient_counter_check(INGREDIENT_COUNTERS, 'bun')
        assert bun_counter_number == '2'

    @allure.title('Увеличение каунтера ингредиента при добавлении этого ингредиента в заказ: у соуса на 1')
    def test_counter_number_increases_sauce(self, constructor_page, user_login_fixture):
        
        constructor_page.add_ingredient_to_order(INGREDIENT_LOCATORS, 'sauce')
        sauce_counter_number = constructor_page.ingredient_counter_check(INGREDIENT_COUNTERS, 'sauce')
        assert sauce_counter_number == '1'


