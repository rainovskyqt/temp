from PySide6.QtSql import QSqlDatabase, QSqlQuery
import os


class DBManager:
    def __init__(self, db_path: str) -> None:
        self.db_path = db_path
        print(db_path, self.db_path)

    def check_base(self):
        exist = os.path.exists(self.db_path)
        print(f'Database exists = {exist}')
        return exist

    def connect_to_base(self):
        con = QSqlDatabase.addDatabase("QSQLITE")
        con.setDatabaseName(self.db_path)
        print(con.databaseName())
        print(con.connectionName())
        print(f'Database is open = {con.open()}')
        if con.lastError().isValid():
            print(f"Database error: {con.lastError().text()}")

    @staticmethod
    def execute_file(file_path: str):
        query = QSqlQuery()  #
        with open(file_path) as file:
            rows = file.read().split(";")
            for row in rows:
                query.exec(row)

    def create_base(self, script_tables_path: str):
        self.execute_file(script_tables_path)

    def fill_init_data(self, script_data_path: str):
        self.execute_file(script_data_path)
