import pytest
import allure
from urls import LOGIN_PAGE_URL, PASS_RESET_PAGE
from data import RECOVERY_EMAIL


@allure.suite('Проверки процесса восстановления пароля')
class TestPasswordRecoveryPage:

    @allure.title('Переход на страницу восстановления пароля по кнопке «Восстановить пароль»')
    def test_pass_recovery_button(self, pass_recovery_page):

        pass_recovery_page.go_to_url(LOGIN_PAGE_URL)
        pass_recovery_page.click_on_pass_recovery_button()
        is_on_pass_recovery_page = pass_recovery_page.pass_recovery_page_check()
        assert is_on_pass_recovery_page


    @allure.title('Ввод почты и клик по кнопке «Восстановить»')
    def test_recover_button(self, pass_recovery_page):

        pass_recovery_page.go_to_url(PASS_RESET_PAGE)
        email = RECOVERY_EMAIL
        pass_recovery_page.fill_email_input(email)
        pass_recovery_page.click_on_recover_button()
        is_on_pass_recovery_next_step = pass_recovery_page.pass_recovery_next_step_check()
        assert is_on_pass_recovery_next_step


    
    @allure.title('Клик по кнопке показать/скрыть пароль делает поле активным — подсвечивает его')
    def test_show_pass_button(self, pass_recovery_page):
        
        pass_recovery_page.go_to_url(PASS_RESET_PAGE)
        email = RECOVERY_EMAIL
        pass_recovery_page.fill_email_input(email)
        pass_recovery_page.click_on_recover_button()
        pass_recovery_page.pass_recovery_next_step_check()
        pass_recovery_page.click_on_show_pass_button()
        pass_input_is_active = pass_recovery_page.pass_input_is_active_check()
        assert pass_input_is_active


    
