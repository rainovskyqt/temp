from PySide6.QtCore import QSortFilterProxyModel
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QMainWindow, QAbstractItemView, QMessageBox
from PySide6.QtSql import QSqlDatabase, QSqlQueryModel, QSqlRelation
from ui.ui_mainwindow import Ui_MainWindow
from database.models import User
from .database.query_manager import QueryManager
from .request_edit import EditRequest


class MainWindow(QMainWindow):
    def __init__(self, user: User, login_form):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.user = user
        self.login_form = login_form
        self.database = QSqlDatabase.database()
        self.query_manager = QueryManager(self.database)
        self.sql_model = QSqlQueryModel(self)
        self.proxy_model = QSortFilterProxyModel(self)
        self.proxy_model.setSourceModel(self.sql_model)
        self.ui.tv_orders.setModel(self.proxy_model)
        self.set_table()
        self.select_orders()
        self.init_connections()
        self.order_editor = EditRequest(1, self.query_manager)

    def exit(self):
        self.login_form.show()
        self.close()

    def set_table(self):
        self.ui.tv_orders.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.ui.tv_orders.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.ui.tv_orders.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)

    def select_orders(self):
        self.sql_model.setQuery(self.query_manager.get_requests())
        self.sql_model.setHeaderData(0, Qt.Orientation.Horizontal, "№ заявки")
        self.sql_model.setHeaderData(1, Qt.Orientation.Horizontal, "Дата получения")
        self.sql_model.setHeaderData(2, Qt.Orientation.Horizontal, "Дата выполнения")
        self.sql_model.setHeaderData(3, Qt.Orientation.Horizontal, "Тип авто")
        self.sql_model.setHeaderData(4, Qt.Orientation.Horizontal, "Марка")
        self.sql_model.setHeaderData(5, Qt.Orientation.Horizontal, "Модель")
        self.sql_model.setHeaderData(6, Qt.Orientation.Horizontal, "Клиент")
        self.sql_model.setHeaderData(7, Qt.Orientation.Horizontal, "Статус")
        self.sql_model.setHeaderData(8, Qt.Orientation.Horizontal, "Мастер")

        self.ui.tv_orders.resizeColumnsToContents()

    def edit_requests(self):
        rec_id = self.get_current_record_id()
        if not rec_id:
            return
        print(f" Editable order id = {rec_id}")
        self.order_editor = EditRequest(rec_id, self.query_manager)
        self.order_editor.show()

    def add_request(self):
        self.order_editor = EditRequest(0, self.query_manager)
        self.order_editor.show()

    def get_current_record_id(self):
        if not self.ui.tv_orders.selectedIndexes()[0]:
            return 0
        row = self.ui.tv_orders.selectedIndexes()[0].row()
        record_id = self.proxy_model.data(self.proxy_model.index(row, 0))
        return record_id

    def init_connections(self):
        self.ui.btn_exit.clicked.connect(self.exit)
        self.ui.tv_orders.doubleClicked.connect(self.edit_requests)
        self.ui.btn_edit.clicked.connect(self.edit_requests)
        self.ui.btn_delete.clicked.connect(self.delete_record)
        self.ui.btn_add.clicked.connect(self.add_request)

    def delete_record(self):
        rec_id = self.get_current_record_id()
        if not rec_id:
            return

        answer = QMessageBox.question(self, "Удаление записи", f"Удалить заказ {rec_id}?")
        if answer == QMessageBox.StandardButton.No:
            return

        self.query_manager.delete_request(rec_id)
        self.select_orders()
