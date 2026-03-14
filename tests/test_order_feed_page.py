import pytest
import allure
from data import INGREDIENT_LOCATORS, INGREDIENT_LIST
import time

class TestOrderFeed:

    @allure.title('Увеличение счетчика "Выполнено за все время" после поздания нового заказа')
    def test_all_time_orders_counter_gets_bigger(self, order_feed_page, constructor_page, new_user_login_fixture):

        order_feed_page.click_on_order_feed_button() # Переход в Ленту заказов после авторизации с помощью фикстуры user_login_fixture
        order_feed_counter_before = order_feed_page.get_all_time_orders_counter() # Сохранение значения на счетчике
        constructor_page.click_on_constructor_button() # Переход в Конструктор
        constructor_page.create_order(INGREDIENT_LOCATORS, INGREDIENT_LIST) # Создание заказа
        constructor_page.click_on_order_close_button() # Закрывается модалка с информацией по созданному заказу
        order_feed_page.click_on_order_feed_button() # Переход в Ленту заказов
        order_feed_counter_after = order_feed_page.get_all_time_orders_counter() # Сохранение обновленного значения на счетчике

        difference = int(order_feed_counter_after) - int(order_feed_counter_before) 
        assert difference == 1, f"Счетчик должен был увеличиться на 1, а увеличился на {difference}"    


    @allure.title('Увеличение счетчика "Выполнено за сегодня" после создания нового заказа')
    def test_today_orders_counter_gets_bigger(self, order_feed_page, constructor_page, new_user_login_fixture):

        order_feed_page.click_on_order_feed_button()
        order_feed_counter_before = order_feed_page.get_today_orders_counter()
        constructor_page.click_on_constructor_button()
        constructor_page.create_order(INGREDIENT_LOCATORS, INGREDIENT_LIST)
        constructor_page.click_on_order_close_button()
        order_feed_page.click_on_order_feed_button()
        order_feed_counter_after = order_feed_page.get_today_orders_counter()

        difference = int(order_feed_counter_after) - int(order_feed_counter_before)
        assert difference == 1, f"Счетчик должен был увеличиться на 1, а увеличился на {difference}"      


    @allure.title('Окно с деталями заказа открывается по клику на заказ')
    def test_order_window_opens(self, order_feed_page, new_user_login_fixture):

        order_feed_page.click_on_order_feed_button() # Переход в Ленту заказов
        order_number_in_feed = order_feed_page.get_last_order_number() # Сохранение номера последнего заказа
        order_feed_page.click_on_last_order() # Клик на последний заказ
        order_feed_page.order_details_window_check() # Проверка, что открылось окно с деталями заказа
        order_number_in_window = order_feed_page.get_order_number_in_details_window() # Сохранение номера заказа, отображаемого в окне
        assert order_number_in_feed == order_number_in_window # Сравнение номера заказа, на который кликнули, и номера в окне


    @allure.title('Заказы пользователя отображаются в ленте заказов')
    def test_user_orders_appear_in_feed(self, profile_page, order_feed_page, constructor_page, new_user_login_fixture):
        
        constructor_page.create_order(INGREDIENT_LOCATORS, INGREDIENT_LIST)
        constructor_page.click_on_order_close_button()
        profile_page.click_on_profile_button() # Переход в профиль
        profile_page.click_on_order_history_button() # Переход в Историю заказов в профиле
        profile_orders = profile_page.get_profile_order_numbers() # Получение номеров заказов в профиле
        if len(profile_orders) == 0:
            raise Exception("В профиле нет заказов, тест не может быть выполнен") # Если в профиле нет заказов, тест закончится с ошибкой 
        order_feed_page.click_on_order_feed_button()
        feed_orders = order_feed_page.get_feed_order_numbers() # Получение номеров заказов в ленте заказов
        for order in profile_orders:
            assert order in feed_orders, f"Заказ {order} не найден в ленте" # Проверка того, что каждый номер заказа из профиля есть в ленте заказов


    @allure.title('Номер созданного заказа появляется в разделе "В работе"')
    def test_order_number_appears_in_process_after_creation(self, order_feed_page, constructor_page, new_user_login_fixture):

            order_number = constructor_page.create_order(INGREDIENT_LOCATORS, INGREDIENT_LIST) # Cоздание заказа и сохранение его номера
            constructor_page.click_on_order_close_button() # Закрывается окно с номером заказа
            order_feed_page.click_on_order_feed_button() # Переход в Ленту заказов
            order_numbers_in_process = order_feed_page.get_in_process_order_numbers() # Получение номеров заказов в блоке "В работе"
            assert order_number in order_numbers_in_process # Проверка, что номер созданного заказа отображается в блоке "В работе" после создания





