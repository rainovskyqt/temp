from PySide6.QtSql import QSqlQuery
from .db_namager import DBManager
from .models import User, Dictionary, Request


class QueryManager:
    def __init__(self, database: DBManager):
        self.base = database

    @staticmethod
    def execute_query(query_row: str, params=None):
        if params is None:
            params = {}
        query = QSqlQuery()
        query.prepare(query_row)

        for key, value in params.items():
            query.bindValue(key, value)

        query.exec()

        if query.lastError().isValid():
            print(f'Query error: {query.lastError().text()}')

        return query

    def check_login(self, login: str, password: str):
        query_string = "SELECT user_id, fio, phone, type_id FROM users WHERE login = :login AND password = :password"
        params = {":login": login, ":password":  password}

        answer = self.execute_query(query_string, params)
        if answer.next():
            user = User(answer.value("user_id"), answer.value("fio"), answer.value("phone"), answer.value("type_id"))
            return user
        else:
            return 0

    def get_requests(self):
        query_string = '''SELECT request_id, start_date, complete_date, CT.name, CB.name, CM.name, U.fio, R.description, 
                        S.name, U1.fio 
                        FROM requests R 
                        INNER JOIN cars C ON C.car_id = R.car_id 
                        INNER JOIN car_types CT ON C.type_id = CT.type_id
                        INNER JOIN car_brands CB ON CB.brand_id = C.brand_id 
                        INNER JOIN car_models CM ON C.model_id = CM.model_id 
                        INNER JOIN users U ON R.client_id = U.user_id 
                        INNER JOIN status S ON R.status_id = S.status_id 
                        INNER JOIN users U1 ON R.master_id = U1.user_id'''
        return self.execute_query(query_string)

    def delete_request(self, request_id: int):
        query_string = "DELETE FROM requests WHERE request_id = :id"
        self.execute_query(query_string, {":id": request_id})

    def get_request(self, request_id: int):
        query_string = """ SELECT R.start_date, R.complete_date, C.type_id, C.brand_id, C.model_id, R.client_id, 
        R.description, R.status_id, R.master_id
        FROM requests R
        INNER JOIN cars C ON C.car_id = R.car_id
        WHERE request_id = :request_id
        """
        answer = self.execute_query(query_string, {":request_id": request_id})

        if answer.next():
            order = Request(
                answer.value("start_date"),
                answer.value("complete_date"),
                answer.value("type_id"),
                answer.value("brand_id"),
                answer.value("model_id"),
                answer.value("description"),
                answer.value("client_id"),
                answer.value("status_id"),
                answer.value("master_id"),
                request_id
            )
            return order
        else:
            return 0

    def get_dictionary(self, column: str, table: str):
        query_string = f"SELECT {column}, name FROM {table}"
        answer = self.execute_query(query_string)
        dic = []
        while answer.next():
            dic.append(Dictionary(answer.value(column), answer.value("name")))
        return dic

    def get_car_types(self):
        return self.get_dictionary("type_id","car_types")

    def get_car_brands(self):
        return self.get_dictionary("brand_id","car_brands")

    def get_car_models(self):
        return self.get_dictionary("model_id","car_models")

    def get_status(self):
        return self.get_dictionary("status_id","status")

    def get_users(self, type_id: int):
        query_string = "SELECT user_id, fio FROM users WHERE type_id = :type_id"
        answer = self.execute_query(query_string, {":type_id": type_id})
        users = []
        while answer.next():
            users.append(User(answer.value("user_id"), answer.value("fio"), "", answer.value(type_id)))
        return users
