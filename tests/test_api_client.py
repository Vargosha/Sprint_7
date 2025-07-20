import pytest
from api_client import *
from data import DataForTests


class TestApiCreateCourier:
    @allure.title('Проверка успешного создания курьера с обязательными полями')
    def test_create_courier_with_valid_data_returns_201(self, delete_courier):
        payload = generate_random_register_data_for_courier()

        response = ApiClientMethods.create_courier(payload)
        assert response.status_code == 201
        assert response.json()["ok"] == True

        delete_courier(payload)

    @allure.title('Проверка невозможности создания дубликата курьера')
    def test_cannot_create_duplicate_courier_returns_409(self, create_courier_than_delete):
        payload = {
            "login": create_courier_than_delete["login"],
            "password": create_courier_than_delete["password"],
            "firstName": create_courier_than_delete["firstName"]
        }
        expected_message = "Этот логин уже используется. Попробуйте другой."
        response = ApiClientMethods.create_courier(payload)

        assert response.status_code == 409
        assert response.json()["message"] == expected_message

    @allure.title('Проверка невозможности создания курьера с незаполненными обязательными полями')
    @pytest.mark.parametrize('payload', DataForTests.REGISTRATION_DATA_EMPTY_FIELDS, ids=["empty_login", "empty_password"])
    def test_cannot_create_courier_with_empty_required_field_returns_400(self, payload):
        expected_message = "Недостаточно данных для создания учетной записи"
        response = ApiClientMethods.create_courier(payload)

        assert response.status_code == 400
        assert response.json()["message"] == expected_message

class TestApiLoginCourier:
    @allure.title('Проверка успешного логина курьера')
    def test_courier_can_login_with_valid_data_returns_200(self, create_courier_only):
        payload = create_courier_only
        response = ApiClientMethods.login_courier(payload)
        assert response.status_code == 200
        assert "id" in response.json()

        courier_id = response.json()["id"]
        ApiClientMethods.delete_courier(courier_id)

    @allure.title('Проверка невозможности логина курьера с незаполненными обязательными полями')
    @pytest.mark.parametrize('payload', DataForTests.LOGIN_DATA_EMPTY_FIELDS, ids=["empty_login", "empty_password", "empty_login_and_password"])
    def test_courier_connot_login_with_empty_required_field_returns_400(self, payload):
        expected_message = "Недостаточно данных для входа"
        response = ApiClientMethods.login_courier(payload)

        assert response.status_code == 400
        assert response.json()["message"] == expected_message

    @allure.title('Проверка невозможности логина курьера с неверными логином и паролем')
    def test_courier_connot_login_with_wrong_login_or_password_returns_404(self, create_courier_than_delete):
        expected_message = "Учетная запись не найдена"
        correct_login = create_courier_than_delete["login"]
        correct_password = create_courier_than_delete["password"]
        wrong_payloads = ApiClientMethods.get_wrong_login_payloads(correct_login, correct_password)

        for payload in wrong_payloads:
            response = ApiClientMethods.login_courier(payload)
            assert response.status_code == 404
            assert response.json()["message"] == expected_message

class TestApiCreateOrder:
    @allure.title('Проверка успешного создания заказа с разными вариантами выбора цвета самоката')
    @pytest.mark.parametrize('payload', DataForTests.CREATE_ORDER_DATA_VARIAL_COLOR, ids=["black_color", "grey_color", "black_and_grey_color", "empty_color"])
    def test_create_order_with_varial_color_returns_track_number(self, payload, delete_order):
        response = ApiClientMethods.create_order(payload)

        assert response.status_code == 201
        assert "track" in response.json()

        delete_order(response)

class TestApiGetOrdersList:
    @allure.title('Проверка успешного получения списка заказов')
    def test_get_orders_returns_list_of_orders(self):
        response = ApiClientMethods.get_orders_list()

        assert response.status_code == 200
        assert "orders" in response.json()
        assert isinstance(response.json()["orders"], list)

class TestApiDeleteCourier:
    @allure.title('Проверка успешного удаления курьера')
    def test_delete_courier_with_valid_data_returns_200(self, create_courier_only):
        payload = create_courier_only
        courier_id = ApiClientMethods.get_courier_id(payload)
        response = ApiClientMethods.delete_courier(courier_id)

        assert response.status_code == 200
        assert response.json()["ok"] == True

    @allure.title('Проверка невозможности удаления курьера с несуществующим ID курьера или без ID курьера')
    @pytest.mark.parametrize("data", DataForTests.DELETE_COURIER_NONEXISTENT_AND_EMPTY_FIELDS, ids=["empty_id", "nonexistent_id"])
    def test_cannot_delete_courier_with_empty_id_or_nonexistent_id_returns_error(self, data):
        response = ApiClientMethods.delete_courier(data["courier_id"])

        assert response.status_code == data["status_code"]
        assert response.json()["message"] == data["expected_message"]

class TestApiAcceptOrder:
    @allure.title('Проверка успешного принятия заказа курьером')
    def test_courier_can_accept_order(self, create_courier_and_order_than_delete):
        courier_dict, order_dict = create_courier_and_order_than_delete
        order_id = order_dict["orderId"]
        courier_id = courier_dict["courierId"]
        response = ApiClientMethods.accept_order(order_id, courier_id)

        assert response.status_code == 200
        assert response.json()["ok"] == True

    @allure.title('Проверка невозможности принятия заказа курьером с несуществующим ID курьера или без ID курьера')
    @pytest.mark.parametrize("data", DataForTests.ACCEPT_ORDER_COURIER_NONEXISTENT_AND_EMPTY_FIELDS, ids=["empty_id", "nonexistent_id"])
    def test_cannot_accept_order_with_nonexistent_courier_id_or_empty_courier_id_returns_error(self, create_order_than_delete, data):
        order_dict = create_order_than_delete
        order_id = order_dict["orderId"]

        response = ApiClientMethods.accept_order(order_id, data["courier_id"])

        assert response.status_code == data["status_code"]
        assert response.json()["message"] == data["expected_message"]

    @allure.title('Проверка невозможности принятия заказа курьером с несуществующим ID заказа или без ID заказа')
    @pytest.mark.parametrize("data", DataForTests.ACCEPT_ORDER_ORDER_NONEXISTENT_AND_EMPTY_FIELDS, ids=["empty_id", "nonexistent_id"])
    def test_cannot_accept_order_with_nonexistent_order_id_or_empty_order_id_returns_error(self, create_courier_than_delete, data):
        courier_dict = create_courier_than_delete
        courier_id = courier_dict["courierId"]

        response = ApiClientMethods.accept_order(data["order_id"], courier_id)

        assert response.status_code == data["status_code"]
        assert response.json()["message"] == data["expected_message"]

class TestApiGetOrderInfo:
    @allure.title('Проверка успешного получения информации заказа')
    def test_get_order_info_returns_order_info_and_200(self, create_order_than_delete):
        order_dict = create_order_than_delete
        order_track = order_dict["orderTrack"]
        response = ApiClientMethods.get_order_info(order_track)

        assert response.status_code == 200
        assert "order" in response.json()
        assert isinstance(response.json()["order"], dict)

    @allure.title('Проверка невозможности получения информации заказа с несуществующим Track заказа или без Track заказа')
    @pytest.mark.parametrize("data", DataForTests.GET_ORDER_INFO_ORDER_NONEXISTENT_AND_EMPTY_FIELDS, ids=["empty_track", "nonexistent_track"])
    def test_cannot_get_order_info_with_nonexistent_order_track_or_empty_order_track_returns_error(self, data):
        response = ApiClientMethods.get_order_info(data["order_track"])

        assert response.status_code == data["status_code"]
        assert response.json()["message"] == data["expected_message"]
