BASE_URL = "https://qa-scooter.praktikum-services.ru"

class Endpoints:
    CREATE_COURIER = f"{BASE_URL}/api/v1/courier"
    LOGIN_COURIER = f"{BASE_URL}/api/v1/courier/login"
    DELETE_COURIER = f"{BASE_URL}/api/v1/courier/"
    CREATE_ORDER = f"{BASE_URL}/api/v1/orders"
    GET_ORDERS_LIST = f"{BASE_URL}/api/v1/orders"
    DELETE_ORDER = f"{BASE_URL}/api/v1/orders/cancel"
    ACCEPT_ORDER = f"{BASE_URL}/api/v1/orders/accept/"
    GET_ORDER_INFO = f"{BASE_URL}/api/v1/orders/track"
