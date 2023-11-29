import json

import allure
import pytest
import requests
from data.urls import URLS
from data import helpers


class TestLoginCourier:
    login_for_parameters = helpers.generate_random_string(10)
    password_for_parameters = helpers.generate_random_string(10)

    payloads_for_parameters = [
        [{"login": login_for_parameters, "password": ""}],
        [{"login": "", "password": password_for_parameters}]
    ]

    @allure.title("Логин курьера с корректными данными")
    @allure.description("Проверка успешной авторизации курьера с корректными данными")
    def test_login_courier_with_valid_data_success(self, register_new_courier_return_courier_data):
        login_pass_first_name = register_new_courier_return_courier_data

        payload = {
            "login": login_pass_first_name[0],
            "password": login_pass_first_name[1],
            "firstName": login_pass_first_name[2]
        }

        response = requests.post(URLS.API_URL_LOGIN, data=payload)
        assert response.status_code == 200
        assert "id" in response.json()

    @allure.title("Логин курьера с невалидными данными")
    @allure.description("Проверка ошибки при попытке логина курьера с невалидными данными")
    def test_login_courier_with_invalid_credentionals(self):
        payload = {
            "login": helpers.generate_random_string(10),
            "password": helpers.generate_random_string(10)
        }

        response = requests.post(URLS.API_URL_LOGIN, data=payload)
        assert response.status_code == 404
        assert response.json()["message"] == "Учетная запись не найдена"

    @allure.title("Логин курьера с невалидными данными")
    @allure.description("Проверка ошибки при попытке логина курьера с невалидными данными")
    @pytest.mark.parametrize('payload', payloads_for_parameters)
    def test_login_courier_without_required_fields_error(self, payload):
        response = requests.post(URLS.API_URL_LOGIN, data=payload)
        assert response.status_code == 400
        assert response.json()["message"] == "Недостаточно данных для входа"


