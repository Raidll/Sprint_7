import allure
import pytest
import requests
from data import helpers

from data.urls import URLS
from data import create_courier_parameters


class TestCreateCourier:
    @allure.title("Регистрация курьера с корректными данными")
    @allure.description("Проверка успешной регистрации курьера с корректными данными")
    def test_create_courier_with_correct_data_success(self, register_new_courier):
        assert register_new_courier.status_code == 201
        assert register_new_courier.json()["ok"] == True

    @allure.title("Создание курьера с дублирующимися данными")
    @allure.description("Создание курьера с данными, которые уже были указаны при регитсрации ранее")
    def test_create_courier_with_diplicate_data_error(self, register_new_courier_return_courier_data):
        login_pass_first_name = register_new_courier_return_courier_data

        payload = {
            "login": login_pass_first_name[0],
            "password": login_pass_first_name[1],
            "firstName": login_pass_first_name[2]
        }

        response = requests.post(URLS.API_URL_CREATE_COURIER, data=payload)
        assert response.status_code == 409
        assert response.json()["message"] == "Этот логин уже используется. Попробуйте другой."

    @allure.title("Создание курьера без одного из обязательных полей")
    @allure.description("Создание курьера без каждого из обязательных полей")
    @pytest.mark.parametrize('payload', create_courier_parameters.payloads_for_parameters)
    def test_create_courier_without_required_field_error(self, payload):
        response = requests.post(URLS.API_URL_CREATE_COURIER, data=payload)
        assert response.status_code == 400
        assert response.json()["message"] == "Недостаточно данных для создания учетной записи"
