import pytest
import requests
from selenium import webdriver
from data_static import MAIN_URL, LOGIN_USER_API, CREATE_ORDER_API, GET_INGREDIENTS_API, GET_ORDERS_USER


@pytest.fixture()
def chrome_driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(MAIN_URL)
    yield driver
    driver.quit()


@pytest.fixture()
def api_login_user_and_create_order():
    ingredients = []
    # Авторизация пользователя
    payload = {"email": 'petergaas8126@yandex.ru', "password": '123456', "name": 'Pert Gaas'}
    response_user = requests.post(f'{MAIN_URL}{LOGIN_USER_API}', data=payload)

    # Получить список ингридиентов
    response = requests.get(f'{MAIN_URL}{GET_INGREDIENTS_API}')

    for i in response.json()['data']:
        ingredients.append(i.get('_id'))

    # Создать заказ
    payload = {"ingredients": ingredients}
    response = requests.post(f'{MAIN_URL}{CREATE_ORDER_API}', data=payload, headers={'Authorization': response_user.json()['accessToken']})

    yield response


@pytest.fixture()
def api_get_orders_user():
    # Авторизация пользователя
    payload = {"email": 'petergaas8126@yandex.ru', "password": '123456', "name": 'Pert Gaas'}
    response_user = requests.post(f'{MAIN_URL}{LOGIN_USER_API}', data=payload)

    # Получить список заказов
    response = requests.get(f'{MAIN_URL}{GET_ORDERS_USER}', headers={'Authorization': response_user.json()['accessToken']})

    yield response