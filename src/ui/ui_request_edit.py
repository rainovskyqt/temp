# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'request_edit.ui'
##
## Created by: Qt User Interface Compiler version 6.7.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QDialog,
    QGridLayout, QGroupBox, QHBoxLayout, QLabel,
    QPlainTextEdit, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_EditRequest(object):
    def setupUi(self, EditRequest):
        if not EditRequest.objectName():
            EditRequest.setObjectName(u"EditRequest")
        EditRequest.resize(718, 491)
        self.verticalLayout_2 = QVBoxLayout(EditRequest)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(EditRequest)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.date_add_date = QDateEdit(EditRequest)
        self.date_add_date.setObjectName(u"date_add_date")

        self.gridLayout.addWidget(self.date_add_date, 0, 1, 1, 2)

        self.label_2 = QLabel(EditRequest)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 2)

        self.date_complite_date = QDateEdit(EditRequest)
        self.date_complite_date.setObjectName(u"date_complite_date")

        self.gridLayout.addWidget(self.date_complite_date, 1, 2, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_6 = QLabel(EditRequest)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_2.addWidget(self.label_6, 0, 0, 1, 1)

        self.cb_status = QComboBox(EditRequest)
        self.cb_status.setObjectName(u"cb_status")

        self.gridLayout_2.addWidget(self.cb_status, 0, 1, 1, 1)

        self.label_7 = QLabel(EditRequest)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_2.addWidget(self.label_7, 1, 0, 1, 1)

        self.cb_employeer = QComboBox(EditRequest)
        self.cb_employeer.setObjectName(u"cb_employeer")

        self.gridLayout_2.addWidget(self.cb_employeer, 1, 1, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout_2)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.groupBox = QGroupBox(EditRequest)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout_3 = QGridLayout(self.groupBox)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_3.addWidget(self.label_3, 0, 0, 1, 1)

        self.cb_autoType = QComboBox(self.groupBox)
        self.cb_autoType.setObjectName(u"cb_autoType")

        self.gridLayout_3.addWidget(self.cb_autoType, 0, 1, 1, 1)

        self.label_8 = QLabel(self.groupBox)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_3.addWidget(self.label_8, 1, 0, 1, 1)

        self.cb_autoBrand = QComboBox(self.groupBox)
        self.cb_autoBrand.setObjectName(u"cb_autoBrand")

        self.gridLayout_3.addWidget(self.cb_autoBrand, 1, 1, 1, 1)

        self.label_9 = QLabel(self.groupBox)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout_3.addWidget(self.label_9, 2, 0, 1, 1)

        self.cb_autoModel = QComboBox(self.groupBox)
        self.cb_autoModel.setObjectName(u"cb_autoModel")

        self.gridLayout_3.addWidget(self.cb_autoModel, 2, 1, 1, 1)


        self.horizontalLayout.addWidget(self.groupBox)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.horizontalLayout.setStretch(1, 1)
        self.horizontalLayout.setStretch(2, 1)

        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_5 = QLabel(EditRequest)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_2.addWidget(self.label_5)

        self.cb_client = QComboBox(EditRequest)
        self.cb_client.setObjectName(u"cb_client")

        self.horizontalLayout_2.addWidget(self.cb_client)

        self.horizontalLayout_2.setStretch(1, 1)

        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.text_description = QPlainTextEdit(EditRequest)
        self.text_description.setObjectName(u"text_description")

        self.verticalLayout_2.addWidget(self.text_description)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_2)

        self.btn_save = QPushButton(EditRequest)
        self.btn_save.setObjectName(u"btn_save")

        self.horizontalLayout_4.addWidget(self.btn_save)

        self.btn_cancel = QPushButton(EditRequest)
        self.btn_cancel.setObjectName(u"btn_cancel")

        self.horizontalLayout_4.addWidget(self.btn_cancel)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_3)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)


        self.retranslateUi(EditRequest)

        QMetaObject.connectSlotsByName(EditRequest)
    # setupUi

    def retranslateUi(self, EditRequest):
        EditRequest.setWindowTitle(QCoreApplication.translate("EditRequest", u"\u0420\u0430\u0434\u0430\u043a\u0442\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u0435 \u0437\u0430\u044f\u0432\u043a\u0438", None))
        self.label.setText(QCoreApplication.translate("EditRequest", u"\u0414\u0430\u0442\u0430 \u043f\u043e\u043b\u0443\u0447\u0435\u043d\u0438\u044f", None))
        self.label_2.setText(QCoreApplication.translate("EditRequest", u"\u0414\u0430\u0442\u0430 \u0432\u044b\u043f\u043e\u043b\u043d\u0435\u043d\u0438\u044f", None))
        self.label_6.setText(QCoreApplication.translate("EditRequest", u"\u0421\u0442\u0430\u0442\u0443\u0441", None))
        self.label_7.setText(QCoreApplication.translate("EditRequest", u"\u041c\u0430\u0441\u0442\u0435\u0440", None))
        self.groupBox.setTitle(QCoreApplication.translate("EditRequest", u"\u0410\u0432\u0442\u043e\u043c\u043e\u0431\u0438\u043b\u044c", None))
        self.label_3.setText(QCoreApplication.translate("EditRequest", u"\u0422\u0438\u043f", None))
        self.label_8.setText(QCoreApplication.translate("EditRequest", u"\u041c\u0430\u0440\u043a\u0430", None))
        self.label_9.setText(QCoreApplication.translate("EditRequest", u"\u041c\u043e\u0434\u0435\u043b\u044c", None))
        self.label_5.setText(QCoreApplication.translate("EditRequest", u"\u041a\u043b\u0438\u0435\u043d\u0442", None))
        self.btn_save.setText(QCoreApplication.translate("EditRequest", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
        self.btn_cancel.setText(QCoreApplication.translate("EditRequest", u"\u041e\u0442\u043c\u0435\u043d\u0430", None))
    # retranslateUi

