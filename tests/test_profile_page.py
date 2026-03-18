import pytest
import allure

@allure.suite('Проверки для страницы профиля')
class TestProfilePage:

    @allure.title('Переход по клику на "Личный кабинет"')
    def test_click_on_profile_button(self, profile_page, user_login_fixture):
        
        profile_page.click_on_profile_button()
        is_on_profile_page = profile_page.profile_page_check()
        assert is_on_profile_page 

    @allure.title('Переход по клику на "Конструктор" с другой страницы (профиля)')
    def test_going_to_constructor(self, profile_page, user_login_fixture):
        
        profile_page.click_on_profile_button()
        profile_page.profile_page_check()
        profile_page.click_on_constructor_button()
        is_on_constructor_page = profile_page.constructor_page_check()
        assert is_on_constructor_page

    @allure.title('Выход из аккаунта') 
    def test_logout(self, profile_page, user_login_fixture):

        profile_page.click_on_profile_button()
        profile_page.profile_page_check()
        profile_page.click_on_logout_button()
        is_on_login_page = profile_page.going_to_login_page_after_logout()
        assert is_on_login_page




