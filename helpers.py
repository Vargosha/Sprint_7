import random
import string


def generate_random_string(length):
    letters = string.ascii_lowercase
    random_string = ''.join(random.choice(letters) for _ in range(length))
    return random_string

def generate_random_register_data_for_courier():
    login = generate_random_string(10)
    password = generate_random_string(10)
    first_name = generate_random_string(10)

    payload = {
        "login": login,
        "password": password,
        "firstName": first_name
    }

    return payload

def generate_random_data_for_order():
    first_name = generate_random_string(6)
    last_name = generate_random_string(6)
    address = generate_random_string(10)
    metro_station = random.randint(1,5)
    phone = f"+7{random.randint(1000000000,9999999999)}"
    rent_time = random.randint(1,5)
    delivery_date = f"{random.randint(2025,2030)}-{random.randint(1,12)}-{random.randint(1,28)}"
    comment = generate_random_string(10)

    order_data = {
            "firstName": first_name,
            "lastName": last_name,
            "address": address,
            "metroStation": metro_station,
            "phone": phone,
            "rentTime": rent_time,
            "deliveryDate": delivery_date,
            "comment": comment,
            "color": []
        }
    return order_data

def generate_random_courier_id():
    courier_id = random.randint(100000000,999999999)
    return courier_id

def generate_random_order_id():
    order_id = random.randint(100000000, 999999999)
    return order_id
