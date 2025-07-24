import pytest
from api_client import ApiClientMethods
from helpers import generate_random_register_data_for_courier, generate_random_data_for_order


@pytest.fixture
def create_courier_than_delete():
    payload = generate_random_register_data_for_courier()
    ApiClientMethods.create_courier(payload)
    courier_id = ApiClientMethods.get_courier_id(payload)
    courier_data_dict = {
        "login": payload["login"],
        "password": payload["password"],
        "firstName": payload["firstName"],
        "courierId": courier_id
    }

    yield courier_data_dict

    ApiClientMethods.delete_courier(courier_id)

@pytest.fixture
def create_order_than_delete():
    order_data = generate_random_data_for_order()
    order_response = ApiClientMethods.create_order(order_data)
    order_track = order_response.json()["track"]
    order_id = ApiClientMethods.get_order_id(order_track)
    order_dict = {
        "firstName": order_data["firstName"],
        "lastName": order_data["lastName"],
        "address": order_data["address"],
        "metroStation": order_data["metroStation"],
        "phone": order_data["phone"],
        "rentTime": order_data["rentTime"],
        "deliveryDate": order_data["deliveryDate"],
        "comment": order_data["comment"],
        "color": order_data["color"],
        "orderTrack": order_track,
        "orderId": order_id
    }

    yield order_dict

    ApiClientMethods.delete_order(order_track)

@pytest.fixture
def create_courier_and_order_than_delete():
    payload = generate_random_register_data_for_courier()
    ApiClientMethods.create_courier(payload)
    courier_id = ApiClientMethods.get_courier_id(payload)
    courier_dict = {
        "login": payload["login"],
        "password": payload["password"],
        "firstName": payload["firstName"],
        "courierId": courier_id
    }
    order_data = generate_random_data_for_order()
    order_response = ApiClientMethods.create_order(order_data)
    order_track = order_response.json()["track"]
    order_id = ApiClientMethods.get_order_id(order_track)
    order_dict = {
            "firstName": order_data["firstName"],
            "lastName": order_data["lastName"],
            "address": order_data["address"],
            "metroStation": order_data["metroStation"],
            "phone": order_data["phone"],
            "rentTime": order_data["rentTime"],
            "deliveryDate": order_data["deliveryDate"],
            "comment": order_data["comment"],
            "color": order_data["color"],
            "orderTrack": order_track,
            "orderId": order_id
        }

    yield courier_dict, order_dict

    ApiClientMethods.delete_courier(courier_id)
    ApiClientMethods.delete_order(order_track)

@pytest.fixture
def create_courier_only():
    payload = generate_random_register_data_for_courier()
    ApiClientMethods.create_courier(payload)
    courier_data_dict = {
        "login": payload["login"],
        "password": payload["password"]
    }

    return courier_data_dict

@pytest.fixture
def create_order_only():
    order_data = generate_random_data_for_order()
    order_response = ApiClientMethods.create_order(order_data)
    order_track = order_response.json()["track"]
    order_id = ApiClientMethods.get_order_id(order_track)
    order_dict = {
        "firstName": order_data["firstName"],
        "lastName": order_data["lastName"],
        "address": order_data["address"],
        "metroStation": order_data["metroStation"],
        "phone": order_data["phone"],
        "rentTime": order_data["rentTime"],
        "deliveryDate": order_data["deliveryDate"],
        "comment": order_data["comment"],
        "color": order_data["color"],
        "orderTrack": order_track,
        "orderId": order_id
    }

    return order_dict

@pytest.fixture
def delete_courier():
    courier_id = None

    def get_id_for_delete(payload):
        nonlocal courier_id
        courier_id = ApiClientMethods.get_courier_id(payload)
        return courier_id

    yield get_id_for_delete

    if courier_id is not None:
        ApiClientMethods.delete_courier(courier_id)

@pytest.fixture
def delete_order():
    order_track = None

    def get_order_track_dor_delete(response):
        nonlocal order_track
        order_track = response.json()["track"]
        return order_track

    yield get_order_track_dor_delete

    if order_track is not None:
        ApiClientMethods.delete_order(order_track)
