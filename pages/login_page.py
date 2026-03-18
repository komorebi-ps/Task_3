from pages.base_page import BasePage
from locators.login_page_locators import LoginPageLocators
from locators.construtor_page_locators import ConstructorPageLocators
import allure
from urls import LOGIN_PAGE_URL
from data import user_login_data

class LoginPage(BasePage):

    @allure.step('Ввод логина (имейла)')
    def fill_email_input(self, email):

        self.add_text_to_input(LoginPageLocators.EMAIL_INPUT, email)

    @allure.title('Ввод пароля')
    def fill_password_input(self, password):
        
        self.add_text_to_input(LoginPageLocators.PASS_INPUT, password)    

    @allure.title('Клик на кнопку "Войти"')
    def click_on_login_button(self):

        self.click_virt_mouse(LoginPageLocators.LOGIN_BUTTON)

    @allure.title('Проверка нахождения на странице конструктора авторизованным пользователем')
    def going_to_constructor_page_check(self):

        return self.find_element_with_wait(ConstructorPageLocators.CREATE_ORDER_BUTTON)    
    

    # метод авторизации для фикстуры user_login_fixture
    @allure.title('Авторизация')
    def user_login(self):

        email = user_login_data['email']
        password = user_login_data['password']

        self.go_to_url(LOGIN_PAGE_URL)
        self.fill_email_input(email)
        self.fill_password_input(password)
        self.click_on_login_button()
        self.going_to_constructor_page_check()

    # метод авторизации для фикстуры new_user_login_fixture
    @allure.title('Авторизация')
    def new_user_login(self, email, password):

        self.go_to_url(LOGIN_PAGE_URL)
        self.fill_email_input(email)
        self.fill_password_input(password)
        self.click_on_login_button()
        self.going_to_constructor_page_check()


