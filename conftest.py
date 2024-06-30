import pytest
import requests
from selenium import webdriver
from data_static import MAIN_URL, LOGIN_USER_API, CREATE_ORDER_API, GET_INGREDIENTS_API, GET_ORDERS_USER, EMAIL_USER, \
    PASSWORD_USER, NAME_USER


@pytest.fixture()
def chrome_driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(MAIN_URL)
    yield driver
    driver.quit()


@pytest.fixture()
def api_login_user():
    # Авторизация пользователя
    payload = {"email": EMAIL_USER, "password": PASSWORD_USER, "name": NAME_USER}
    response_user = requests.post(f'{MAIN_URL}{LOGIN_USER_API}', data=payload)

    yield response_user


@pytest.fixture()
def api_create_order_authorized_user(api_login_user):
    ingredients = []

    # Получить список ингридиентов
    response = requests.get(f'{MAIN_URL}{GET_INGREDIENTS_API}')

    for i in response.json()['data']:
        ingredients.append(i.get('_id'))

    # Создать заказ
    payload = {"ingredients": ingredients}
    response_order = requests.post(f'{MAIN_URL}{CREATE_ORDER_API}', data=payload,
                                   headers={'Authorization': api_login_user.json()['accessToken']})

    yield response_order


@pytest.fixture()
def api_get_orders_user(api_login_user):
    # Получить список заказов
    response = requests.get(f'{MAIN_URL}{GET_ORDERS_USER}',
                            headers={'Authorization': api_login_user.json()['accessToken']})

    yield response
