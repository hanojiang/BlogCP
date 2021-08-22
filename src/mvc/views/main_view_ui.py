# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_view.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(349, 356)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.vboxLayout = QVBoxLayout(self.centralwidget)
        self.vboxLayout.setObjectName(u"vboxLayout")
        self.spinBox_amount = QSpinBox(self.centralwidget)
        self.spinBox_amount.setObjectName(u"spinBox_amount")

        self.vboxLayout.addWidget(self.spinBox_amount)

        self.label_even_odd = QLabel(self.centralwidget)
        self.label_even_odd.setObjectName(u"label_even_odd")

        self.vboxLayout.addWidget(self.label_even_odd)

        self.pushButton_reset = QPushButton(self.centralwidget)
        self.pushButton_reset.setObjectName(u"pushButton_reset")
        self.pushButton_reset.setEnabled(False)

        self.vboxLayout.addWidget(self.pushButton_reset)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        self.pushButton_reset.setText(QCoreApplication.translate("MainWindow", u"clear", None))
        pass
    # retranslateUi

