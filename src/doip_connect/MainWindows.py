import sys
from PySide2.QtWidgets import QApplication, QMainWindow, QAction, QTextBrowser
from doip import Ui_MainWindow
from Ecu_Const import get_all_ecu, DIAG_SID


class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.__init_all_components()


    def __init_all_components(self):
        self.__init_ecuSeclectBox()

    def __init_ecuSeclectBox(self):
        self.ui.ecuSeclectBox.addItems(DIAG_SID)



if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())