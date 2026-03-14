from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.action_chains import ActionChains
import re


class BasePage:
    
    def __init__(self, driver):
        self.driver = driver
        self.timeout = 15
        self.wait = WebDriverWait(self.driver, self.timeout)
        self.browser_name = self._get_browser_name() 


    def _get_browser_name(self):
        capabilities = self.driver.capabilities
        browser = capabilities.get('browserName', '').lower()
        if 'chrome' in browser:
            return 'Chrome'
        elif 'firefox' in browser:
            return 'Firefox'
    

    def is_firefox(self):
        return self.browser_name == 'Firefox'    


    def go_to_url(self, url):
        self.driver.get(url)


    def find_element_with_wait(self, locator):
        self.wait.until(expected_conditions.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)
    

    def scroll_to_element(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)


    def wait_until_clickable(self, locator):
        self.wait.until(expected_conditions.element_to_be_clickable(locator))    
    

    def click_on_element(self, locator):
        self.wait.until(expected_conditions.element_to_be_clickable(locator))
        self.driver.find_element(*locator).click()   


    def add_text_to_input(self, locator, text):
        self.find_element_with_wait(locator).send_keys(text)


    def get_text_from_element(self, locator):
        return self.find_element_with_wait(locator).text    


    def format_locators(self, locator_1, num):
        method, locator = locator_1
        locator = locator.format(num)
        return method, locator
    

    def find_elements(self, locator):
        self.wait.until(expected_conditions.visibility_of_element_located(locator))
        return self.driver.find_elements(*locator)
    
    def find_child_elements(self, parent_element, child_locator):
        return parent_element.find_elements(*child_locator)
    
    def find_child_element(self, parent_element, child_locator):
        return parent_element.find_element(*child_locator)
    
    
    # метод для извлечения номеров заказов из списка заказов
    def extract_order_numbers_from_items(self, items_locator, number_locator):

        order_items = self.find_elements(items_locator)
        
        order_numbers = []
        
        for item in order_items:
            try:
                # в каждом элементе ищем номер заказа
                number_element = self.find_child_element(item, number_locator)
                number = number_element.text
                order_numbers.append(number)
                    
            except Exception as e:
                # если номер не найден, получаем исключение
                print(f"Не удалось найти номер в элементе: {e}")
                continue
        
        return order_numbers
    

    # метод для извлечения номеров заказов из списка заказов, в зависимости от структуры дерева для разных списков
    def extract_order_numbers(self, items_locator, number_locator=None, text_in_element=False):

        order_items = self.find_elements(items_locator)
        order_numbers = []
    
        for item in order_items:
            try:
                if number_locator and not text_in_element:
                    # если номер в дочернем элементе
                    number_element = self.find_child_element(item, number_locator)
                    text = number_element.text
                else:
                    text = item.text
                    text = text.replace('#0', '')
            
                order_numbers.append(text)
            
            except Exception as e:
                print(f"Ошибка: {e}")
                continue
    
        return order_numbers

    
    
    def drag_and_drop(self, source_locator, target_locator):
            
        source_element = self.find_element_with_wait(source_locator)
        target_element = self.find_element_with_wait(target_locator)

        script = """
            function simulateHTML5DragAndDrop(sourceNode, destinationNode) {
                var dataTransfer = new DataTransfer();  // Исправлено: убрана лишняя скобка
                var dragStartEvent = new DragEvent('dragstart', {
                    bubbles: true, 
                    cancelable: true, 
                    dataTransfer: dataTransfer
                });
                sourceNode.dispatchEvent(dragStartEvent);

                var dropEvent = new DragEvent('drop', {
                    bubbles: true, 
                    cancelable: true, 
                    dataTransfer: dataTransfer
                });
                destinationNode.dispatchEvent(dropEvent);
            
                var dragEndEvent = new DragEvent('dragend', {
                    bubbles: true, 
                    cancelable: true, 
                    dataTransfer: dataTransfer
                }); 
                sourceNode.dispatchEvent(dragEndEvent);
            }  
            simulateHTML5DragAndDrop(arguments[0], arguments[1]);  // Исправлено: правильное имя функции
            """
        self.driver.execute_script(script, source_element, target_element)


    def wait_until_element_invisibility(self, locator):
        self.wait.until(expected_conditions.invisibility_of_element_located(locator))


    def wait_for_text_to_disappear(self, locator, text):
        self.wait.until_not(expected_conditions.text_to_be_present_in_element(locator, text))
        return self.get_text_from_element(locator)


    def click_virt_mouse(self, locator):
        element = self.wait.until(expected_conditions.element_to_be_clickable(locator))
        ActionChains(self.driver).click(element).perform()

    # метод для ожидания появления хотя бы одного элемента с цифрами по указанному локатору
    def wait_for_elements_with_digits(self, locator):   
        
        self.wait.until(
        lambda driver: any(
            re.search(r'\d', el.text) 
            for el in self.find_elements(locator)
        ),
        message=f"Не найдены элементы с цифрами по локатору {locator}"
        )