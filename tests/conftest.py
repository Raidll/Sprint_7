import string

import allure
import pytest
import random
import requests
from data.helpers import Helpers
from data import helpers

from data.urls import URLS


@allure.title("Регистрация нового курьера и удаление после теста")
@allure.description("Регистрация курьера, возврат response и удаление курьера после теста")
@pytest.fixture
def register_new_courier():

    login = helpers.generate_random_string(10)
    password = helpers.generate_random_string(10)
    first_name = helpers.generate_random_string(10)

    payload = {
        "login": login,
        "password": password,
        "firstName": first_name
    }

    response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier', data=payload)
    yield response
    response_login = requests.post(URLS.API_URL_LOGIN, data={'login': login, 'password': password})
    id_courier = response_login.json()['id']
    requests.delete(URLS.API_URL_DELETE_COURIER + f'{id_courier}')


@allure.title("Регистрация нового курьера, возврат логина, пароля, имени")
@allure.description("Регистрация курьера, возврат логина, пароля, имени и удаление курьера после теста.")
@pytest.fixture
def register_new_courier_return_courier_data():
    def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string

    login_pass_first_name = []
    login = helpers.generate_random_string(10)
    password = helpers.generate_random_string(10)
    first_name = helpers.generate_random_string(10)

    payload = {
        "login": login,
        "password": password,
        "firstName": first_name
    }

    response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier', data=payload)

    if response.status_code == 201:
        login_pass_first_name.append(login)
        login_pass_first_name.append(password)
        login_pass_first_name.append(first_name)

    yield login_pass_first_name
    response_login = requests.post(URLS.API_URL_LOGIN, data={'login': login, 'password': password})
    id_courier = response_login.json()['id']
    requests.delete(URLS.API_URL_DELETE_COURIER + f'{id_courier}')