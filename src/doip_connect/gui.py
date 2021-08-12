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
        MainWindow.resize(559, 565)
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

        self.tableWidget = QTableWidget(self.diagTab)
        if (self.tableWidget.columnCount() < 2):
            self.tableWidget.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        if (self.tableWidget.rowCount() < 10):
            self.tableWidget.setRowCount(10)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(5, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(6, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(7, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(8, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(9, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableWidget.setItem(0, 0, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tableWidget.setItem(0, 1, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tableWidget.setItem(7, 0, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tableWidget.setItem(7, 1, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tableWidget.setItem(8, 0, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.tableWidget.setItem(8, 1, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.tableWidget.setItem(9, 0, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.tableWidget.setItem(9, 1, __qtablewidgetitem19)
        self.tableWidget.setObjectName(u"tableWidget")

        self.verticalLayout_2.addWidget(self.tableWidget)

        self.verticalLayout_2.setStretch(0, 1)
        self.verticalLayout_2.setStretch(1, 1)
        self.verticalLayout_2.setStretch(2, 4)
        self.tabWidget.addTab(self.diagTab, "")
        self.settingTab = QWidget()
        self.settingTab.setObjectName(u"settingTab")
        self.verticalLayout_6 = QVBoxLayout(self.settingTab)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.ipSettingGroupBox = QGroupBox(self.settingTab)
        self.ipSettingGroupBox.setObjectName(u"ipSettingGroupBox")
        self.verticalLayout_5 = QVBoxLayout(self.ipSettingGroupBox)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_5 = QLabel(self.ipSettingGroupBox)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_6.addWidget(self.label_5)

        self.testerIpAddresslineEdit = QLineEdit(self.ipSettingGroupBox)
        self.testerIpAddresslineEdit.setObjectName(u"testerIpAddresslineEdit")

        self.horizontalLayout_6.addWidget(self.testerIpAddresslineEdit)


        self.verticalLayout_5.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_6 = QLabel(self.ipSettingGroupBox)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_7.addWidget(self.label_6)

        self.ecuIpAddressLineEdit = QLineEdit(self.ipSettingGroupBox)
        self.ecuIpAddressLineEdit.setObjectName(u"ecuIpAddressLineEdit")

        self.horizontalLayout_7.addWidget(self.ecuIpAddressLineEdit)


        self.verticalLayout_5.addLayout(self.horizontalLayout_7)


        self.horizontalLayout_8.addWidget(self.ipSettingGroupBox)

        self.logicalAddressSettingGroupBox = QGroupBox(self.settingTab)
        self.logicalAddressSettingGroupBox.setObjectName(u"logicalAddressSettingGroupBox")
        self.verticalLayout_4 = QVBoxLayout(self.logicalAddressSettingGroupBox)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_3 = QLabel(self.logicalAddressSettingGroupBox)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_4.addWidget(self.label_3)

        self.testerLogicalAddressLineEdit = QLineEdit(self.logicalAddressSettingGroupBox)
        self.testerLogicalAddressLineEdit.setObjectName(u"testerLogicalAddressLineEdit")

        self.horizontalLayout_4.addWidget(self.testerLogicalAddressLineEdit)


        self.verticalLayout_4.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_4 = QLabel(self.logicalAddressSettingGroupBox)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_5.addWidget(self.label_4)

        self.ecuLogicalAddressLineEdit = QLineEdit(self.logicalAddressSettingGroupBox)
        self.ecuLogicalAddressLineEdit.setObjectName(u"ecuLogicalAddressLineEdit")

        self.horizontalLayout_5.addWidget(self.ecuLogicalAddressLineEdit)


        self.verticalLayout_4.addLayout(self.horizontalLayout_5)


        self.horizontalLayout_8.addWidget(self.logicalAddressSettingGroupBox)


        self.verticalLayout_6.addLayout(self.horizontalLayout_8)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer)

        self.tabWidget.addTab(self.settingTab, "")

        self.verticalLayout_3.addWidget(self.tabWidget)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 559, 22))
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
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"SID", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"DiagData", None));
        ___qtablewidgetitem2 = self.tableWidget.verticalHeaderItem(0)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u884c", None));
        ___qtablewidgetitem3 = self.tableWidget.verticalHeaderItem(1)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u884c", None));
        ___qtablewidgetitem4 = self.tableWidget.verticalHeaderItem(2)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u884c", None));
        ___qtablewidgetitem5 = self.tableWidget.verticalHeaderItem(3)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u884c", None));
        ___qtablewidgetitem6 = self.tableWidget.verticalHeaderItem(4)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u884c", None));
        ___qtablewidgetitem7 = self.tableWidget.verticalHeaderItem(5)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u884c", None));
        ___qtablewidgetitem8 = self.tableWidget.verticalHeaderItem(6)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u884c", None));
        ___qtablewidgetitem9 = self.tableWidget.verticalHeaderItem(7)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u884c", None));
        ___qtablewidgetitem10 = self.tableWidget.verticalHeaderItem(8)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u884c", None));
        ___qtablewidgetitem11 = self.tableWidget.verticalHeaderItem(9)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u884c", None));

        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        ___qtablewidgetitem12 = self.tableWidget.item(0, 0)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"1", None));
        ___qtablewidgetitem13 = self.tableWidget.item(0, 1)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"2", None));
        ___qtablewidgetitem14 = self.tableWidget.item(7, 0)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"3", None));
        ___qtablewidgetitem15 = self.tableWidget.item(7, 1)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"4", None));
        ___qtablewidgetitem16 = self.tableWidget.item(8, 0)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"5", None));
        ___qtablewidgetitem17 = self.tableWidget.item(8, 1)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"6", None));
        ___qtablewidgetitem18 = self.tableWidget.item(9, 0)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"7", None));
        ___qtablewidgetitem19 = self.tableWidget.item(9, 1)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"8", None));
        self.tableWidget.setSortingEnabled(__sortingEnabled)

        self.tabWidget.setTabText(self.tabWidget.indexOf(self.diagTab), QCoreApplication.translate("MainWindow", u"\u8bca\u65ad", None))
        self.ipSettingGroupBox.setTitle(QCoreApplication.translate("MainWindow", u"Ip Address", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Tester", None))
        self.testerIpAddresslineEdit.setText(QCoreApplication.translate("MainWindow", u"172.31.7.2", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Ecu   ", None))
        self.ecuIpAddressLineEdit.setText(QCoreApplication.translate("MainWindow", u"172.31.7.1", None))
        self.logicalAddressSettingGroupBox.setTitle(QCoreApplication.translate("MainWindow", u"Node Logical Address", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Tester", None))
        self.testerLogicalAddressLineEdit.setText(QCoreApplication.translate("MainWindow", u"0e80", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Ecu   ", None))
        self.ecuLogicalAddressLineEdit.setText(QCoreApplication.translate("MainWindow", u"1000", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.settingTab), QCoreApplication.translate("MainWindow", u"\u8bbe\u7f6e", None))
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"\u6587\u4ef6", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar", None))
    # retranslateUi

