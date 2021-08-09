# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'gui.ui'
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
        MainWindow.resize(989, 1059)
        self.buildConnectionButton = QAction(MainWindow)
        self.buildConnectionButton.setObjectName(u"buildConnectionButton")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_3 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.diagTab = QWidget()
        self.diagTab.setObjectName(u"diagTab")
        self.verticalLayout_2 = QVBoxLayout(self.diagTab)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.diagTab)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.sidSeclectBox = QComboBox(self.diagTab)
        self.sidSeclectBox.setObjectName(u"sidSeclectBox")
        self.sidSeclectBox.setContextMenuPolicy(Qt.DefaultContextMenu)

        self.horizontalLayout.addWidget(self.sidSeclectBox)

        self.ecuSeclectBox = QComboBox(self.diagTab)
        self.ecuSeclectBox.setObjectName(u"ecuSeclectBox")

        self.horizontalLayout.addWidget(self.ecuSeclectBox)

        self.diagReqMsgLineEdit = QLineEdit(self.diagTab)
        self.diagReqMsgLineEdit.setObjectName(u"diagReqMsgLineEdit")

        self.horizontalLayout.addWidget(self.diagReqMsgLineEdit)

        self.sendDiagMsgButton = QPushButton(self.diagTab)
        self.sendDiagMsgButton.setObjectName(u"sendDiagMsgButton")

        self.horizontalLayout.addWidget(self.sendDiagMsgButton)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.phyAddressRadioButton = QRadioButton(self.diagTab)
        self.phyAddressRadioButton.setObjectName(u"phyAddressRadioButton")
        self.phyAddressRadioButton.setChecked(True)
        self.phyAddressRadioButton.setAutoRepeat(False)

        self.verticalLayout.addWidget(self.phyAddressRadioButton)

        self.funcAddressRadioButton = QRadioButton(self.diagTab)
        self.funcAddressRadioButton.setObjectName(u"funcAddressRadioButton")

        self.verticalLayout.addWidget(self.funcAddressRadioButton)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.horizontalLayout.setStretch(0, 2)
        self.horizontalLayout.setStretch(1, 2)
        self.horizontalLayout.setStretch(2, 8)
        self.horizontalLayout.setStretch(3, 15)
        self.horizontalLayout.setStretch(4, 2)
        self.horizontalLayout.setStretch(5, 2)

        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_2 = QLabel(self.diagTab)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_3.addWidget(self.label_2)

        self.doipUdpMsgSecletBox = QComboBox(self.diagTab)
        self.doipUdpMsgSecletBox.setObjectName(u"doipUdpMsgSecletBox")

        self.horizontalLayout_3.addWidget(self.doipUdpMsgSecletBox)

        self.emptyContentLineEdit = QLineEdit(self.diagTab)
        self.emptyContentLineEdit.setObjectName(u"emptyContentLineEdit")

        self.horizontalLayout_3.addWidget(self.emptyContentLineEdit)

        self.sendDoipUdpMsgButton = QPushButton(self.diagTab)
        self.sendDoipUdpMsgButton.setObjectName(u"sendDoipUdpMsgButton")

        self.horizontalLayout_3.addWidget(self.sendDoipUdpMsgButton)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)

        self.horizontalLayout_3.setStretch(0, 2)
        self.horizontalLayout_3.setStretch(1, 10)
        self.horizontalLayout_3.setStretch(2, 15)
        self.horizontalLayout_3.setStretch(3, 2)
        self.horizontalLayout_3.setStretch(4, 2)

        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.InfoPrintBrowser = QTextBrowser(self.diagTab)
        self.InfoPrintBrowser.setObjectName(u"InfoPrintBrowser")

        self.horizontalLayout_2.addWidget(self.InfoPrintBrowser)

        self.DiagMsgPrintBrowser = QTextBrowser(self.diagTab)
        self.DiagMsgPrintBrowser.setObjectName(u"DiagMsgPrintBrowser")
        self.DiagMsgPrintBrowser.setContextMenuPolicy(Qt.ActionsContextMenu)

        self.horizontalLayout_2.addWidget(self.DiagMsgPrintBrowser)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.DoipMsgBrowser = QTextBrowser(self.diagTab)
        self.DoipMsgBrowser.setObjectName(u"DoipMsgBrowser")

        self.verticalLayout_2.addWidget(self.DoipMsgBrowser)

        self.verticalLayout_2.setStretch(0, 1)
        self.verticalLayout_2.setStretch(1, 1)
        self.verticalLayout_2.setStretch(2, 4)
        self.verticalLayout_2.setStretch(3, 4)
        self.tabWidget.addTab(self.diagTab, "")
        self.settingTab = QWidget()
        self.settingTab.setObjectName(u"settingTab")
        self.tabWidget.addTab(self.settingTab, "")

        self.verticalLayout_3.addWidget(self.tabWidget)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 989, 26))
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QToolBar(MainWindow)
        self.toolBar.setObjectName(u"toolBar")
        MainWindow.addToolBar(Qt.TopToolBarArea, self.toolBar)

        self.menubar.addAction(self.menu.menuAction())
        self.toolBar.addAction(self.buildConnectionButton)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"DoIP App", None))
        self.buildConnectionButton.setText(QCoreApplication.translate("MainWindow", u"\u5efa\u7acb\u8fde\u63a5", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"SID", None))
        self.sidSeclectBox.setCurrentText("")
        self.sidSeclectBox.setPlaceholderText("")
        self.sendDiagMsgButton.setText(QCoreApplication.translate("MainWindow", u"Send", None))
        self.phyAddressRadioButton.setText(QCoreApplication.translate("MainWindow", u"Phy", None))
        self.funcAddressRadioButton.setText(QCoreApplication.translate("MainWindow", u"Func", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Type", None))
        self.sendDoipUdpMsgButton.setText(QCoreApplication.translate("MainWindow", u"Send", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.diagTab), QCoreApplication.translate("MainWindow", u"\u8bca\u65ad", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.settingTab), QCoreApplication.translate("MainWindow", u"\u8bbe\u7f6e", None))
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"\u6587\u4ef6", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar", None))
    # retranslateUi

