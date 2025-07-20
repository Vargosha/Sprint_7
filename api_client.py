import allure
import requests
from endpoints import Endpoints
from helpers import *


class ApiClientMethods:
    @staticmethod
    @allure.step('Получаем данные для логина курьера')
    def get_wrong_login_payloads(correct_login, correct_password):
        return [
            {"login": correct_login, "password": generate_random_string(10)},
            {"login": generate_random_string(10), "password": correct_password},
            {"login": generate_random_string(10), "password": generate_random_string(10)}
        ]

    @staticmethod
    @allure.step('Создаем курьера')
    def create_courier(payload):
        return requests.post(Endpoints.CREATE_COURIER, data=payload)

    @staticmethod
    @allure.step('Получаем ID курьера')
    def get_courier_id(payload):
        login_response = requests.post(Endpoints.LOGIN_COURIER, data=payload)
        assert login_response.status_code == 200
        courier_id = login_response.json()["id"]
        return courier_id

    @staticmethod
    @allure.step('Удаляем курьера')
    def delete_courier(courier_id):
        url = f"{Endpoints.DELETE_COURIER}{courier_id}"
        return requests.delete(url)

    @staticmethod
    @allure.step('Удаляем заказ')
    def delete_order(order_track):
        return requests.put(Endpoints.DELETE_ORDER, params={"track": order_track})

    @staticmethod
    @allure.step('Получаем список заказов')
    def get_orders_list():
        return requests.get(Endpoints.GET_ORDERS_LIST)

    @staticmethod
    @allure.step('Создаем заказ')
    def create_order(payload):
        return requests.post(Endpoints.CREATE_ORDER, json=payload)

    @staticmethod
    @allure.step('Логинимся в профиль курьера')
    def login_courier(payload):
        return requests.post(Endpoints.LOGIN_COURIER, json=payload)

    @staticmethod
    @allure.step('Принимаем заказ')
    def accept_order(order_id, courier_id):
        url = f"{Endpoints.ACCEPT_ORDER}{order_id}"
        return requests.put(url, params={"courierId": courier_id})

    @staticmethod
    @allure.step('Получаем ID заказа')
    def get_order_id(order_track):
        order_response = requests.get(Endpoints.GET_ORDER_INFO, params={"t": int(order_track)})
        return order_response.json()["order"]["id"]

    @staticmethod
    @allure.step('Получаем информацию заказа')
    def get_order_info(order_track):
        params = {}
        if order_track:
            params["t"] = int(order_track)
        else:
            params["t"] = ""
        return requests.get(Endpoints.GET_ORDER_INFO, params=params)
