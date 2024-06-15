from typing import List

from PySide6.QtWidgets import QDialog, QComboBox
from ui.ui_request_edit import Ui_EditRequest
from database.query_manager import QueryManager
from database.models import Dictionary, Request, User
from datetime import date, datetime


class EditRequest(QDialog):
    def __init__(self, request_id: int, query_manager: QueryManager):
        super(EditRequest, self).__init__()
        self.ui = Ui_EditRequest()
        self.ui.setupUi(self)
        self.request_id = request_id
        self.query_manager = query_manager
        self.load_dict()
        self.to_form(self.request_id)

    def get_request_data(self, request_id):
        if request_id:
            return self.query_manager.get_request(request_id)
        else:
            return Request(date.today().strftime("%Y-%m-%d"))

    def load_dict(self):
        car_types = self.query_manager.get_car_types()
        self.set_dict(car_types, self.ui.cb_autoType)

        car_brand = self.query_manager.get_car_brands()
        self.set_dict(car_brand, self.ui.cb_autoBrand)

        car_models = self.query_manager.get_car_models()
        self.set_dict(car_models, self.ui.cb_autoModel)

        car_status = self.query_manager.get_status()
        self.set_dict(car_status, self.ui.cb_status)

        masters = self.query_manager.get_users(2)
        self.set_user(masters, self.ui.cb_employeer)

        clients = self.query_manager.get_users(4)
        self.set_user(clients, self.ui.cb_client)

    def set_dict(self, vals: List[Dictionary], box: QComboBox):
        box.clear()
        box.addItem("-", 0)
        for row in vals:
            box.addItem(row.name, row.base_id)

    def set_user(self, vals: List[User], box: QComboBox):
        box.clear()
        box.addItem("-", 0)
        for row in vals:
            box.addItem(row.fio, row.user_id)

    def to_form(self, request_id):
        request = self.get_request_data(request_id)
        self.ui.date_add_date.setDate(datetime.strptime(request.start_date, "%Y-%m-%d"))
        self.ui.cb_status.setCurrentIndex(self.ui.cb_status.findData(request.status_id))
        self.ui.cb_client.setCurrentIndex(self.ui.cb_client.findData(request.client_id))
        self.ui.cb_employeer.setCurrentIndex(self.ui.cb_employeer.findData(request.master_id))
        self.ui.cb_autoType.setCurrentIndex(self.ui.cb_autoType.findData(request.car_type_id))
        self.ui.cb_autoBrand.setCurrentIndex(self.ui.cb_autoBrand.findData(request.brand_id))
        self.ui.cb_autoModel.setCurrentIndex(self.ui.cb_autoModel.findData(request.model_id))
        self.ui.text_description.setPlainText(request.description)