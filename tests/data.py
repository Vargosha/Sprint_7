from helpers import generate_random_register_data_for_courier, generate_random_courier_id, generate_random_order_id, generate_random_data_for_order


class DataForTests:
    courier_data = generate_random_register_data_for_courier()
    courier_id = generate_random_courier_id()
    order_id = generate_random_order_id()
    order_data = generate_random_data_for_order()

    REGISTRATION_DATA_EMPTY_FIELDS = [
        {
            "login": "",
            "password": courier_data["password"],
            "firstName": courier_data["firstName"]
        },
        {
            "login": courier_data["login"],
            "password": "",
            "firstName": courier_data["firstName"]
        }
    ]
    LOGIN_DATA_EMPTY_FIELDS = [
        {
            "login": "",
            "password": courier_data["password"]
        },
        {
            "login": courier_data["login"],
            "password": ""
        },
        {
            "login": "",
            "password": ""
        }
    ]
    CREATE_ORDER_DATA_VARIAL_COLOR = [
        {
            "firstName": order_data["firstName"],
            "lastName": order_data["lastName"],
            "address": order_data["address"],
            "metroStation": order_data["metroStation"],
            "phone": order_data["phone"],
            "rentTime": order_data["rentTime"],
            "deliveryDate": order_data["deliveryDate"],
            "comment": order_data["comment"],
            "color": ["BLACK"]
        },
        {
            "firstName": order_data["firstName"],
            "lastName": order_data["lastName"],
            "address": order_data["address"],
            "metroStation": order_data["metroStation"],
            "phone": order_data["phone"],
            "rentTime": order_data["rentTime"],
            "deliveryDate": order_data["deliveryDate"],
            "comment": order_data["comment"],
            "color": ["GREY"]
        },
        {
            "firstName": order_data["firstName"],
            "lastName": order_data["lastName"],
            "address": order_data["address"],
            "metroStation": order_data["metroStation"],
            "phone": order_data["phone"],
            "rentTime": order_data["rentTime"],
            "deliveryDate": order_data["deliveryDate"],
            "comment": order_data["comment"],
            "color": ["BLACK", "GREY"]
        },
        {
            "firstName": order_data["firstName"],
            "lastName": order_data["lastName"],
            "address": order_data["address"],
            "metroStation": order_data["metroStation"],
            "phone": order_data["phone"],
            "rentTime": order_data["rentTime"],
            "deliveryDate": order_data["deliveryDate"],
            "comment": order_data["comment"],
            "color": []
        }
    ]
    DELETE_COURIER_NONEXISTENT_AND_EMPTY_FIELDS = [
        {
            "expected_message": "Not Found.",
            "courier_id": "",
            "status_code": 404
        },
        {
            "expected_message": "Курьера с таким id нет.",
            "courier_id": courier_id,
            "status_code": 404
        }
    ]
    ACCEPT_ORDER_COURIER_NONEXISTENT_AND_EMPTY_FIELDS = [
        {
            "expected_message": "Недостаточно данных для поиска",
            "courier_id": "",
            "status_code": 400
        },
        {
            "expected_message": "Курьера с таким id не существует",
            "courier_id": courier_id,
            "status_code": 404
        }
    ]
    ACCEPT_ORDER_ORDER_NONEXISTENT_AND_EMPTY_FIELDS = [
        {
            "expected_message": "Not Found.",
            "order_id": "",
            "status_code": 404
        },
        {
            "expected_message": "Заказа с таким id не существует",
            "order_id": order_id,
            "status_code": 404
        }
    ]
    GET_ORDER_INFO_ORDER_NONEXISTENT_AND_EMPTY_FIELDS = [
        {
            "expected_message": "Недостаточно данных для поиска",
            "order_track": "",
            "status_code": 400
        },
        {
            "expected_message": "Заказ не найден",
            "order_track": order_id,
            "status_code": 404
        }
    ]
