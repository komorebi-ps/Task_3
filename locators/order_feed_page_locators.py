from selenium.webdriver.common.by import By

class OrderFeedLocators:

    ORDER_FEED_LOCATOR = (By.XPATH, "//*[text()='В работе:']") # локатор для проверки перехода на эту страницу
    LAST_ORDER = (By.XPATH, "//ul[contains(@class, 'OrderFeed_list')]/li[1]") # 
    LAST_ORDER_NUMBER = (By.XPATH, "//ul[contains(@class, 'OrderFeed_list')]/li[1]/a/div/p[1]") #
    ORDER_MODAL_WINDOW = (By.XPATH, "//*[contains(@class, 'Modal_orderBox')]")  #
    ORDER_NUMBER_IN_WINDOW = (By.XPATH, "//*[contains(@class, 'Modal_orderBox')]/p[1]") #
    ORDER1_NUMBER = (By.XPATH, "//ul[contains(@class, 'OrderHistory_profileList')]/li[1]/a/div/p[1]") #
    ORDER2_NUMBER = (By.XPATH, "//ul[contains(@class, 'OrderHistory_profileList')]/li[2]/a/div/p[1]") #
    ALL_TIME_ORDERS_COUNTER = (By.XPATH, "//*[text()='Выполнено за все время:']/following-sibling::p") #
    TODAY_ORDERS_COUNTER = (By.XPATH, "//*[text()='Выполнено за сегодня:']/following-sibling::p") #
    FEED_ORDERS_LIST = (By.XPATH, "//ul[contains(@class, 'OrderFeed_list')]") # 
    FEED_ORDER_ITEMS = (By.XPATH, "//ul[contains(@class, 'OrderFeed_list')]/li")
    ORDER_NUMBER = (By.CLASS_NAME, "text_type_digits-default") 
    IN_PROCESS_ORDERS_LIST = (By.XPATH, "//ul[contains(@class, 'OrderFeed_orderListReady')]") #
    IN_PROCESS_ORDERS_ITEMS = (By.XPATH, "//ul[contains(@class, 'OrderFeed_orderListReady')]/li")



                              