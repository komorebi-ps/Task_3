from pages.base_page import BasePage
from locators.profile_page_locators import ProfilePageLocators
from locators.header_locators import HeaderLocators
from locators.login_page_locators import LoginPageLocators
from locators.construtor_page_locators import ConstructorPageLocators
import allure


class ProfilePage(BasePage):

    @allure.step('Клик на "Личный кабинет" в хедере')
    def click_on_profile_button(self):

        if self.is_firefox():
            self.click_virt_mouse(HeaderLocators.PROFILE_BUTTON)    
        else:
            self.click_on_element(HeaderLocators.PROFILE_BUTTON)


    @allure.step('Проверка перехода в личный кабинет')    
    def profile_page_check(self):

        return self.find_element_with_wait(ProfilePageLocators.ORDER_HISTORY_BUTTON)
    

    @allure.step('Клик на историю заказов')   
    def click_on_order_history_button(self):

        self.click_on_element(ProfilePageLocators.ORDER_HISTORY_BUTTON)  


    @allure.step('Проверка перехода в историю заказов')
    def order_history_page_check(self):

        return self.find_element_with_wait(ProfilePageLocators.ORDER_HISTORY_LIST)
    

    @allure.step('Клик на кнопку "Выход"')
    def click_on_logout_button(self):

        self.click_on_element(ProfilePageLocators.LOGOUT_BUTTON)


    @allure.step('Проверка выхода')
    def going_to_login_page_after_logout(self):

        return self.find_element_with_wait(LoginPageLocators.LOGIN_BUTTON)
    

    @allure.step('Клик на кнопку "Конструктор"')    
    def click_on_constructor_button(self):

        if self.is_firefox():
            self.click_virt_mouse(HeaderLocators.CONSTRUCTOR_BUTTON)
        else:
            self.click_on_element(HeaderLocators.CONSTRUCTOR_BUTTON)
            

    @allure.step('Проверка перехода в Конструктор')        
    def constructor_page_check(self):

        return self.find_element_with_wait(ConstructorPageLocators.CONSTRUCTOR_PAGE_LOCATOR)
    

    @allure.step('Получение номеров заказов в истории профиля')
    def get_profile_order_numbers(self):

        return self.extract_order_numbers_from_items(
            ProfilePageLocators.ORDER_HISTORY_ITEMS,
            ProfilePageLocators.ORDER_NUMBER
        )
    

    
    


        





