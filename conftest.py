import pytest
from selenium import webdriver
from pages.order_feed_page import OrderFeedPage 
from pages.constructor_page import ConstructorPage
from pages.password_recovery_page import PasswordRecoveryPage
from pages.login_page import LoginPage
from pages.profile_page import ProfilePage
import requests
from helpers import generate_random_string, random_email
from data import user_login_data


browser_name = None

@pytest.fixture(params=['Chrome', 'Firefox']) 
def driver(request):
    if request.param == 'Chrome':
        driver = webdriver.Chrome()
        driver.browser_name = 'Chrome'
    else:
        driver = webdriver.Firefox()
        driver.browser_name = 'Firefox'
            
    yield driver 
    driver.quit()


@pytest.fixture
def pass_recovery_page(driver):
    page = PasswordRecoveryPage(driver)
    return page

@pytest.fixture
def profile_page(driver):
    page = ProfilePage(driver)
    return page

@pytest.fixture
def login_page(driver):
    page = LoginPage(driver)
    return page

@pytest.fixture
def constructor_page(driver):
    page = ConstructorPage(driver)
    return page

@pytest.fixture
def order_feed_page(driver):
    page = OrderFeedPage(driver)
    return page


# фикстура для авторизации под УЗ существующего пользователя
@pytest.fixture
def user_login_fixture(login_page):

    login_page.user_login()

    yield login_page


# фикстура для создания нового пользователя по API
@pytest.fixture
def create_user():

    email = random_email()
    password = generate_random_string(8)
    name = generate_random_string(7)
    payload = {
        "email": email,
        "password": password,
        "name": name
    }
    response = requests.post(
        f'{"https://stellarburgers.education-services.ru/api/auth/register"}', 
        json=payload,
        headers={'Content-Type': 'application/json'}
    )
    response_data = response.json()
    result_data = {}
    result_data['user'] = response_data.get('user')
    result_data['accessToken'] = response_data.get('accessToken')
    result_data['password'] = password 
    result_data['email'] = email 

    yield result_data 
    if 'accessToken' in response_data and response_data['accessToken']:
        url = "https://stellarburgers.education-services.ru/api/auth/user"
        headers = {'Content-Type': 'application/json'}
        headers['authorization'] = response_data['accessToken']
        requests.delete(url, headers=headers)


# фикстура для атворизации нового пользователя, созданного в фикстуре create_user
@pytest.fixture
def new_user_login_fixture(login_page, create_user):

    user_data = create_user
    email = user_data['user']['email']
    password = user_data['password']
    login = login_page.new_user_login(email, password)
    yield login


    
