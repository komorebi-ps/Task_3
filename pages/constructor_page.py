from pages.base_page import BasePage
from locators.construtor_page_locators import ConstructorPageLocators
from locators.header_locators import HeaderLocators
import allure

class ConstructorPage(BasePage):

    @allure.step('Клик на "Конструктор" в хедере')
    def click_on_constructor_button(self):

        self.click_on_element(HeaderLocators.CONSTRUCTOR_BUTTON)

    @allure.step('Клик на ингредиент ("Флюоресцентная булка")')
    def click_on_ingredient_fluorescent_bun(self):

        self.click_on_element(ConstructorPageLocators.FLUORESCENT_BUN)


    @allure.step('Проверка открытого модального окна c деталями ингредиента ("Флюоресцентной булки")')
    def modal_window_check(self):

        return self.find_element_with_wait(ConstructorPageLocators.FLUORESCENT_BUN_DETAILS_WINDOW)    
    

    @allure.step('Клик на крестик в модальном окне с деталями ингредиента')
    def click_on_modal_close_button(self):

        self.click_on_element(ConstructorPageLocators.DETAILS_WINDOW_CLOSE_BUTTON)


    @allure.step('Проверка того, что окно с деталями ингредиента закрылось')    
    def modal_window_is_closed(self):

        self.wait_until_element_invisibility(ConstructorPageLocators.FLUORESCENT_BUN_DETAILS_WINDOW)
        return True 

    @allure.step('Клик на крестик в модальном окне созданного заказа')
    def click_on_order_close_button(self):

        self.click_virt_mouse_in_firefox(ConstructorPageLocators.ORDER_WINDOW_CLOSE_BUTTON)

    @allure.step('Перетаскивание ингредиента в заказ')
    def add_ingredient_to_order(self, ingredients_dict, ingredient_name):    
        
        # получаем локатор ингредиента из словаря c ингредиентами
        ingredient = ingredients_dict.get(ingredient_name)

        if not ingredient:
            raise ValueError(
                f"Ингредиент '{ingredient_name}' не найден в словаре. "
                f"Доступны: {list(ingredients_dict.keys())}"
            )

        self.find_element_with_wait(ingredient)
        self.drag_and_drop(ingredient, ConstructorPageLocators.DROP_AREA)

        return ingredient


    @allure.step('Проверка каунтера ингредиента')
    def ingredient_counter_check(self, ingredients_dict, ingredient_name):

        ingredient_counter = ingredients_dict.get(ingredient_name)

        counter_number = self.get_text_from_element(ingredient_counter)  
        return counter_number


    @allure.step('Проверка наличия третьего добавленного ингредиента в заказе')   #нужна чтобы дождаться перемещения вниз кнопки "Заказать" перед ее нажатием
    def third_added_ingredient_in_order(self): 

        return self.find_element_with_wait(ConstructorPageLocators.THIRD_ADDED_INGREDIENT_IN_BASKET)


    @allure.step('Клик на кнопку "Оформить заказ"')
    def click_on_create_order_button(self):

        self.click_virt_mouse(ConstructorPageLocators.CREATE_ORDER_BUTTON)


    @allure.step('Проверка появившегося модального окна с номером заказа')
    def order_modal_window_check(self):

        return self.find_element_with_wait(ConstructorPageLocators.ORDER_MODAL_WINDOW)     
    

    @allure.step('Создание заказа')
    def create_order(self, ingredients_dict, ingredients_list):
        
        for ingredient_name in ingredients_list:
            self.add_ingredient_to_order(ingredients_dict, ingredient_name)
        
        self.third_added_ingredient_in_order()
        self.click_on_create_order_button()
        self.order_modal_window_check()
        order_number = self.wait_for_text_to_disappear(ConstructorPageLocators.ORDER_NUMBER, '9999')
        return order_number






        



