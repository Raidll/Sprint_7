import json

import allure
import pytest
import requests
from data.urls import URLS


class TestCreateOrder:
    @allure.title("Успешное создание заказа с указанием различных цветов")
    @allure.description(
        "Проверка возможности указать цвета: BLACK, GRAY, два цвета вместе. В теле ответа возвращается track")
    @pytest.mark.parametrize("colors", [["BLACK"], ["GREY"], ["BLACK", "GREY"]])
    def test_create_order_with_different_colors_success(self, colors):
        payload = {
            "firstName": "TestFirstName",
            "lastName": "TestLastName",
            "address": "TestAddress",
            "metroStation": "TestMetroStation",
            "phone": "79111111111",
            "rentTime": 1,
            "deliveryDate": "2023-11-27",
            "comment": "TestComment",
            "color": colors
        }
        payload_string = json.dumps(payload)
        response = requests.post(URLS.API_URL_ORDERS, data=payload_string)
        assert response.status_code == 201

    @allure.title("Успешное создание заказа без указания цвета")
    @allure.description(
        "Проверка возможность создать заказ без указания цвета")
    def test_create_order_with_different_colors_success(self):
        payload = {
            "firstName": "TestFirstName",
            "lastName": "TestLastName",
            "address": "TestAddress",
            "metroStation": "TestMetroStation",
            "phone": "79111111111",
            "rentTime": 1,
            "deliveryDate": "2023-11-27",
            "comment": "TestComment"
        }
        payload_string = json.dumps(payload)
        response = requests.post(URLS.API_URL_ORDERS, data=payload_string)
        assert response.status_code == 201

    @allure.title("Проверка наличия track в теле ответа")
    @allure.description(
        "Проверка возврата track в теле ответа на запрос создания заказа")
    def test_create_order_with_different_colors_success(self):
        payload = {
            "firstName": "TestFirstName",
            "lastName": "TestLastName",
            "address": "TestAddress",
            "metroStation": "TestMetroStation",
            "phone": "79111111111",
            "rentTime": 1,
            "deliveryDate": "2023-11-27",
            "comment": "TestComment",
            "color": "BLACK"
        }
        payload_string = json.dumps(payload)
        response = requests.post(URLS.API_URL_ORDERS, data=payload_string)
        assert "track" in response.json()
