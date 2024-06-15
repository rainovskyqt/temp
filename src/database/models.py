class User:
    def __init__(self, user_id: int, fio: str, phone: int, type_id: int):
        self.user_id = user_id
        self.fio = fio
        self.phone = phone
        self.type_id = type_id


class Request:
    def __init__(self, start_date, complete_date="", car_type_id=0, brand_id=0, model_id=0, description="",
                 client_id=0, status_id=1, master_id=0, request_id=0):
        self.start_date = start_date
        self.complete_date = complete_date
        self.car_type_id = car_type_id
        self.brand_id = brand_id
        self.model_id = model_id
        self.description = description
        self.client_id = client_id
        self.status_id = status_id
        self.master_id = master_id
        self.request_id = request_id


class Dictionary:
    def __init__(self, base_id: int, name: str):
        self.base_id = base_id
        self.name = name
