from pages.base_page import BasePage
from locators.password_recovery_page_locators import PassRecoveryPageLocators
from locators.header_locators import HeaderLocators
import allure

class PasswordRecoveryPage(BasePage):

    @allure.step('Клик на кнопку "Восстановить пароль"')
    def click_on_pass_recovery_button(self):

        self.click_virt_mouse(PassRecoveryPageLocators.PASS_RECOVERY_BUTTON)


    @allure.step('Проверка перехода на страницу восстановления пароля')    
    def pass_recovery_page_check(self):

        return self.find_element_with_wait(PassRecoveryPageLocators.PASS_RECOVERY_PAGE_LOCATOR)


    @allure.step('Заполнение поля Email')
    def fill_email_input(self, email):

        self.add_text_to_input(PassRecoveryPageLocators.EMAIL_INPUT, email)


    @allure.step('Клик на кнопку "Восстановить"')
    def click_on_recover_button(self):

        self.click_on_element(PassRecoveryPageLocators.RECOVER_BUTTON)


    @allure.step('Проверка перехода к следующему этапу восстановления пароля')    
    def pass_recovery_next_step_check(self):
        
        return self.find_element_with_wait(PassRecoveryPageLocators.SAVE_BUTTON)
    

    @allure.step('Клик на кнопку показать/скрыть пароль')
    def click_on_show_pass_button(self):

        self.click_virt_mouse_in_firefox(PassRecoveryPageLocators.SHOW_PASS_BUTTON)


    @allure.step('Проверка активности поля после нажатия на кнопку показать/скрыть пароль')
    def pass_input_is_active_check(self):

        return self.find_element_with_wait(PassRecoveryPageLocators.PASS_INPUT_ACTIVE)
    

    


    

    

    













