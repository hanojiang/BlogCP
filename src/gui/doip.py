# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'doip.ui'
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
        MainWindow.resize(1017, 937)
        self.action_buildConnection = QAction(MainWindow)
        self.action_buildConnection.setObjectName(u"action_buildConnection")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_3 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.verticalLayout_2 = QVBoxLayout(self.tab)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.tab)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.sidSeclectBox = QComboBox(self.tab)
        self.sidSeclectBox.setObjectName(u"sidSeclectBox")
        self.sidSeclectBox.setContextMenuPolicy(Qt.DefaultContextMenu)

        self.horizontalLayout.addWidget(self.sidSeclectBox)

        self.ecuSeclectBox = QComboBox(self.tab)
        self.ecuSeclectBox.setObjectName(u"ecuSeclectBox")

        self.horizontalLayout.addWidget(self.ecuSeclectBox)

        self.msgLineEdit = QLineEdit(self.tab)
        self.msgLineEdit.setObjectName(u"msgLineEdit")

        self.horizontalLayout.addWidget(self.msgLineEdit)

        self.sendMsgButton = QPushButton(self.tab)
        self.sendMsgButton.setObjectName(u"sendMsgButton")

        self.horizontalLayout.addWidget(self.sendMsgButton)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.localDevRadioButton = QRadioButton(self.tab)
        self.localDevRadioButton.setObjectName(u"localDevRadioButton")
        self.localDevRadioButton.setChecked(True)
        self.localDevRadioButton.setAutoRepeat(False)

        self.verticalLayout.addWidget(self.localDevRadioButton)

        self.remoteDevRadioButton = QRadioButton(self.tab)
        self.remoteDevRadioButton.setObjectName(u"remoteDevRadioButton")

        self.verticalLayout.addWidget(self.remoteDevRadioButton)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.horizontalLayout.setStretch(0, 2)
        self.horizontalLayout.setStretch(1, 2)
        self.horizontalLayout.setStretch(2, 5)
        self.horizontalLayout.setStretch(3, 18)
        self.horizontalLayout.setStretch(4, 2)
        self.horizontalLayout.setStretch(5, 2)

        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_2 = QLabel(self.tab)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_3.addWidget(self.label_2)

        self.payloadSecletBox = QComboBox(self.tab)
        self.payloadSecletBox.setObjectName(u"payloadSecletBox")

        self.horizontalLayout_3.addWidget(self.payloadSecletBox)

        self.payloadContent = QLineEdit(self.tab)
        self.payloadContent.setObjectName(u"payloadContent")

        self.horizontalLayout_3.addWidget(self.payloadContent)

        self.sendDoipMsgButton = QPushButton(self.tab)
        self.sendDoipMsgButton.setObjectName(u"sendDoipMsgButton")

        self.horizontalLayout_3.addWidget(self.sendDoipMsgButton)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)

        self.horizontalLayout_3.setStretch(0, 2)
        self.horizontalLayout_3.setStretch(1, 8)
        self.horizontalLayout_3.setStretch(2, 18)
        self.horizontalLayout_3.setStretch(3, 2)
        self.horizontalLayout_3.setStretch(4, 2)

        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.InfoMsgBrowser = QTextBrowser(self.tab)
        self.InfoMsgBrowser.setObjectName(u"InfoMsgBrowser")

        self.horizontalLayout_2.addWidget(self.InfoMsgBrowser)

        self.DiagMsgTxRxBrowser = QTextBrowser(self.tab)
        self.DiagMsgTxRxBrowser.setObjectName(u"DiagMsgTxRxBrowser")
        self.DiagMsgTxRxBrowser.setContextMenuPolicy(Qt.ActionsContextMenu)

        self.horizontalLayout_2.addWidget(self.DiagMsgTxRxBrowser)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.DoipMsgBrowser = QTextBrowser(self.tab)
        self.DoipMsgBrowser.setObjectName(u"DoipMsgBrowser")

        self.verticalLayout_2.addWidget(self.DoipMsgBrowser)

        self.verticalLayout_2.setStretch(0, 1)
        self.verticalLayout_2.setStretch(1, 1)
        self.verticalLayout_2.setStretch(2, 4)
        self.verticalLayout_2.setStretch(3, 4)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.tabWidget.addTab(self.tab_2, "")

        self.verticalLayout_3.addWidget(self.tabWidget)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1017, 26))
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
        self.toolBar.addAction(self.action_buildConnection)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"DoIP App", None))
        self.action_buildConnection.setText(QCoreApplication.translate("MainWindow", u"\u5efa\u7acb\u8fde\u63a5", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"SID", None))
        self.sidSeclectBox.setCurrentText("")
        self.sidSeclectBox.setPlaceholderText("")
        self.sendMsgButton.setText(QCoreApplication.translate("MainWindow", u"Send", None))
        self.localDevRadioButton.setText(QCoreApplication.translate("MainWindow", u"local", None))
        self.remoteDevRadioButton.setText(QCoreApplication.translate("MainWindow", u"remote", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Payload", None))
        self.sendDoipMsgButton.setText(QCoreApplication.translate("MainWindow", u"Send", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"\u8bca\u65ad", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Tab 2", None))
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"\u6587\u4ef6", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar", None))
    # retranslateUi

