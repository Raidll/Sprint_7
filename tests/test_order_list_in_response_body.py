import allure
import requests
from data.urls import URLS


class TestReturnOrderListInResponseBody:
    @allure.title("Успешное получение списка заказов")
    @allure.description("Проверка успешного получения списка заказов")
    def test_return_order_list_success(self):
        response = requests.get(URLS.API_URL_ORDERS)
        assert response.status_code == 200
        assert "orders" in response.json()
