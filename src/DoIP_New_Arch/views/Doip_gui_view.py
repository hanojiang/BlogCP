# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Doip_gui_view.ui'
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
        MainWindow.resize(664, 611)
        icon = QIcon()
        icon.addFile(u"UDS14229_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
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

        self.projectSelectCcomboBox = QComboBox(self.diagTab)
        self.projectSelectCcomboBox.setObjectName(u"projectSelectCcomboBox")

        self.horizontalLayout.addWidget(self.projectSelectCcomboBox)

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
        self.horizontalLayout.setStretch(3, 8)
        self.horizontalLayout.setStretch(4, 15)
        self.horizontalLayout.setStretch(5, 2)
        self.horizontalLayout.setStretch(6, 2)

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

        self.canSelectComboBox = QComboBox(self.diagTab)
        self.canSelectComboBox.setObjectName(u"canSelectComboBox")

        self.horizontalLayout_3.addWidget(self.canSelectComboBox)

        self.diagRouteTestButton = QPushButton(self.diagTab)
        self.diagRouteTestButton.setObjectName(u"diagRouteTestButton")

        self.horizontalLayout_3.addWidget(self.diagRouteTestButton)

        self.horizontalLayout_3.setStretch(0, 2)
        self.horizontalLayout_3.setStretch(1, 10)
        self.horizontalLayout_3.setStretch(2, 15)
        self.horizontalLayout_3.setStretch(3, 2)

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

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.multiLineTableWidget = QTableWidget(self.diagTab)
        if (self.multiLineTableWidget.columnCount() < 2):
            self.multiLineTableWidget.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.multiLineTableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.multiLineTableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        self.multiLineTableWidget.setObjectName(u"multiLineTableWidget")

        self.horizontalLayout_9.addWidget(self.multiLineTableWidget)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_7 = QLabel(self.diagTab)
        self.label_7.setObjectName(u"label_7")

        self.verticalLayout_7.addWidget(self.label_7)

        self.sidLineEdit = QLineEdit(self.diagTab)
        self.sidLineEdit.setObjectName(u"sidLineEdit")

        self.verticalLayout_7.addWidget(self.sidLineEdit)

        self.label_8 = QLabel(self.diagTab)
        self.label_8.setObjectName(u"label_8")

        self.verticalLayout_7.addWidget(self.label_8)

        self.diagDataLineEdit = QLineEdit(self.diagTab)
        self.diagDataLineEdit.setObjectName(u"diagDataLineEdit")

        self.verticalLayout_7.addWidget(self.diagDataLineEdit)

        self.addLinePushButton = QPushButton(self.diagTab)
        self.addLinePushButton.setObjectName(u"addLinePushButton")

        self.verticalLayout_7.addWidget(self.addLinePushButton)

        self.clearPushButton = QPushButton(self.diagTab)
        self.clearPushButton.setObjectName(u"clearPushButton")

        self.verticalLayout_7.addWidget(self.clearPushButton)

        self.multiSendPushButton = QPushButton(self.diagTab)
        self.multiSendPushButton.setObjectName(u"multiSendPushButton")

        self.verticalLayout_7.addWidget(self.multiSendPushButton)

        self.secAccessPushButton = QPushButton(self.diagTab)
        self.secAccessPushButton.setObjectName(u"secAccessPushButton")

        self.verticalLayout_7.addWidget(self.secAccessPushButton)

        self.portMirrorLineEdit = QLineEdit(self.diagTab)
        self.portMirrorLineEdit.setObjectName(u"portMirrorLineEdit")

        self.verticalLayout_7.addWidget(self.portMirrorLineEdit)

        self.portMirrorSettingPushButton = QPushButton(self.diagTab)
        self.portMirrorSettingPushButton.setObjectName(u"portMirrorSettingPushButton")

        self.verticalLayout_7.addWidget(self.portMirrorSettingPushButton)


        self.horizontalLayout_9.addLayout(self.verticalLayout_7)

        self.horizontalLayout_9.setStretch(0, 9)
        self.horizontalLayout_9.setStretch(1, 1)

        self.verticalLayout_2.addLayout(self.horizontalLayout_9)

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

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer)

        self.loopbackIPSettingButton = QPushButton(self.settingTab)
        self.loopbackIPSettingButton.setObjectName(u"loopbackIPSettingButton")

        self.horizontalLayout_10.addWidget(self.loopbackIPSettingButton)

        self.applySettingButton = QPushButton(self.settingTab)
        self.applySettingButton.setObjectName(u"applySettingButton")

        self.horizontalLayout_10.addWidget(self.applySettingButton)


        self.verticalLayout_6.addLayout(self.horizontalLayout_10)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer)

        self.tabWidget.addTab(self.settingTab, "")
        self.logiticDataTab = QWidget()
        self.logiticDataTab.setObjectName(u"logiticDataTab")
        self.verticalLayout_8 = QVBoxLayout(self.logiticDataTab)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")

        self.verticalLayout_8.addLayout(self.formLayout)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.logiticDataReadPushButton = QPushButton(self.logiticDataTab)
        self.logiticDataReadPushButton.setObjectName(u"logiticDataReadPushButton")

        self.horizontalLayout_11.addWidget(self.logiticDataReadPushButton)


        self.verticalLayout_8.addLayout(self.horizontalLayout_11)

        self.tabWidget.addTab(self.logiticDataTab, "")

        self.verticalLayout_3.addWidget(self.tabWidget)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 664, 22))
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
        self.diagRouteTestButton.setText(QCoreApplication.translate("MainWindow", u"Route Test", None))
        ___qtablewidgetitem = self.multiLineTableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"SID", None));
        ___qtablewidgetitem1 = self.multiLineTableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"DiagData", None));
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"SID", None))
        self.sidLineEdit.setText(QCoreApplication.translate("MainWindow", u"10", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"DiagData", None))
        self.diagDataLineEdit.setText(QCoreApplication.translate("MainWindow", u"03", None))
        self.addLinePushButton.setText(QCoreApplication.translate("MainWindow", u"Add Line", None))
        self.clearPushButton.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
        self.multiSendPushButton.setText(QCoreApplication.translate("MainWindow", u"Multi Send", None))
        self.secAccessPushButton.setText(QCoreApplication.translate("MainWindow", u"Sec access", None))
        self.portMirrorSettingPushButton.setText(QCoreApplication.translate("MainWindow", u"Port mirror", None))
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
        self.loopbackIPSettingButton.setText(QCoreApplication.translate("MainWindow", u"\u56de\u73afip\u8bbe\u7f6e", None))
        self.applySettingButton.setText(QCoreApplication.translate("MainWindow", u"\u5e94\u7528\u914d\u7f6e", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.settingTab), QCoreApplication.translate("MainWindow", u"\u8bbe\u7f6e", None))
        self.logiticDataReadPushButton.setText(QCoreApplication.translate("MainWindow", u"\u8bfb\u53d6\u7269\u6d41\u6570\u636e", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.logiticDataTab), QCoreApplication.translate("MainWindow", u"\u7269\u6d41\u6570\u636e", None))
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"\u6587\u4ef6", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar", None))
    # retranslateUi

