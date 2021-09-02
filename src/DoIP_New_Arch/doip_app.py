import sys
from PySide2.QtWidgets import QApplication
from model.doip_model import Model
from controllers.doip_controller import DoIP_Controller
from views.doip_view import MainView


class App(QApplication):
    def __init__(self, sys_argv):
        super(App, self).__init__(sys_argv)
        self.model = Model()
        self.main_controller = DoIP_Controller(self.model)
        self.main_view = MainView(self.model, self.main_controller)
        self.main_view.show()


if __name__ == '__main__':
    app = App(sys.argv)
    sys.exit(app.exec_())