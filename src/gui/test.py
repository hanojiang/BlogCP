# from PySide2.QtWidgets import QApplication, QMessageBox, QAction
# from doip import Ui_MainWindow
# from PySide2.QtUiTools import QUiLoader


import sys
from PySide2.QtWidgets import QApplication, QMainWindow, QAction
from PySide2.QtCore import QFile
from doip import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.sendMsgButton.clicked.connect(self.handleMsgSend)

        self.init_sidSeclectBox()
        self.init_MsgTxRxBrowser()
        self.init_ecuSeclectBox()

    def init_sidSeclectBox(self):
        self.ui.sidSeclectBox.addItems(['10', '11', '22', '2E'])

    def init_ecuSeclectBox(self):
        self.ui.ecuSeclectBox.addItems(['GW', 'TBOX', 'BCM', 'ICM'])

    def init_MsgTxRxBrowser(self):

        # 具体菜单项
        msg_clear_option = QAction(self.ui.MsgTxRxBrowser)
        msg_clear_option.setText("清空")
        msg_clear_option.triggered.connect(self.clearMsgTxRxBrowser)  # 点击菜单中的“发送控制代码”执行的函数

        # tableView 添加具体的右键菜单
        self.ui.MsgTxRxBrowser.addAction(msg_clear_option)

    def handleMsgSend(self):

        sidMsg = self.ui.sidSeclectBox.currentText()
        ecuName = self.ui.ecuSeclectBox.currentText()


        diag_msg = self.ui.msgLineEdit.text()

        self.ui.MsgTxRxBrowser.append(sidMsg + diag_msg)
        self.ui.MsgTxRxBrowser.ensureCursorVisible()

        self.ui.otherMsgBrowser.append(ecuName)
        self.ui.otherMsgBrowser.ensureCursorVisible()

    def clearMsgTxRxBrowser(self):
        self.ui.MsgTxRxBrowser.clear()
        self.ui.otherMsgBrowser.clear()


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())