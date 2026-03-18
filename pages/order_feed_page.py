from pages.base_page import BasePage
from locators.profile_page_locators import ProfilePageLocators
from locators.header_locators import HeaderLocators
from locators.construtor_page_locators import ConstructorPageLocators
from locators.order_feed_page_locators import OrderFeedLocators
import allure




class OrderFeedPage(BasePage):

    @allure.step('Клик на "Ленту заказов" в хедере')
    def click_on_order_feed_button(self):

        self.click_virt_mouse(HeaderLocators.ORDER_FEED_BUTTON)


    @allure.step('Сохранение номера последнего заказа в ленте')
    def get_last_order_number(self):

        text = self.get_text_from_element(OrderFeedLocators.LAST_ORDER_NUMBER)
        last_order_number = text[2:] # сохранение номера заказа без первых двух символов - "#0"
        return last_order_number
    

    @allure.step('Клик на последний заказ в ленте')
    def click_on_last_order(self):

        self.click_on_element(OrderFeedLocators.LAST_ORDER)


    @allure.step('Проверка открытого окна с деталями заказа')
    def order_details_window_check(self):

        self.find_element_with_wait(OrderFeedLocators.ORDER_MODAL_WINDOW)


    @allure.step('Получение номера заказа в окне с деталями заказа')    
    def get_order_number_in_details_window(self):

        text = self.get_text_from_element(OrderFeedLocators.ORDER_NUMBER_IN_WINDOW)
        if '\n' in text:
            order_number = text.split('\n')[-1].strip()
        else:
            order_number = text.replace('#0', '')
        return order_number


    @allure.step('Получение значения на счетчике "Выполнено за все время"')
    def get_all_time_orders_counter(self):

        return self.get_text_from_element(OrderFeedLocators.ALL_TIME_ORDERS_COUNTER)
    

    @allure.step('Получение значения на счетчике "Выполнено за сегодня')
    def get_today_orders_counter(self):

        return self.get_text_from_element(OrderFeedLocators.TODAY_ORDERS_COUNTER)
    

    @allure.step('Получение номеров заказов в ленте')
    def get_feed_order_numbers(self):
            
        return self.extract_order_numbers(
        OrderFeedLocators.FEED_ORDER_ITEMS,
        OrderFeedLocators.ORDER_NUMBER,
        text_in_element=False
        )
    

    @allure.step('Получение номеров заказов в разделе "В работе"')
    def get_in_process_order_numbers(self):

        # Ждем исчезновения сообщения 'Все текущие заказы готовы!'
        try:
            self.wait_for_text_to_disappear(
            OrderFeedLocators.IN_PROCESS_ORDERS_ITEMS, 
            'Все текущие заказы готовы!',
        )
        except Exception:
            pass

        try:
            self.wait_for_elements_with_digits(OrderFeedLocators.IN_PROCESS_ORDERS_ITEMS)
        except Exception as e:
            allure.attach(
            f"Заказы с номерами не появились: {type(e).__name__}",
            name="wait_for_orders_error",
            attachment_type=allure.attachment_type.TEXT
            )
        order_numbers = self.extract_order_numbers(
            OrderFeedLocators.IN_PROCESS_ORDERS_LIST,
            OrderFeedLocators.IN_PROCESS_ORDERS_ITEMS,
            text_in_element=True    
        )
        return [num.lstrip('0') for num in order_numbers] # возвращаем номера заказов без 0 в начале
    

    




