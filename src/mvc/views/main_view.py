from PySide2.QtWidgets import QMainWindow
from PySide2.QtCore import Slot
from views.main_view_ui import Ui_MainWindow


class MainView(QMainWindow):
    def __init__(self, model, main_controller):
        super().__init__()

        self._model = model
        self._main_controller = main_controller
        self._ui = Ui_MainWindow()
        self._ui.setupUi(self)

        # connect widgets to controller
        self._ui.spinBox_amount.valueChanged.connect(self._main_controller.change_amount)
        self._ui.pushButton_reset.clicked.connect(lambda: self._main_controller.change_amount(0))

        # listen for model event signals
        self._model.amount_changed.connect(self.on_amount_changed)
        self._model.even_odd_changed.connect(self.on_even_odd_changed)
        self._model.enable_reset_changed.connect(self.on_enable_reset_changed)

        # set a default value
        self._main_controller.change_amount(42)

    @Slot(int)
    def on_amount_changed(self, value):
        self._ui.spinBox_amount.setValue(value)
        pass

    @Slot(str)
    def on_even_odd_changed(self, value):
        self._ui.label_even_odd.setText(value)

    @Slot(bool)
    def on_enable_reset_changed(self, value):
        self._ui.pushButton_reset.setEnabled(value)