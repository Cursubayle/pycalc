# This Python file uses the following encoding: utf-8
import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from ui_form import Ui_MainWindow
from mycalc import MyCalc
class MainWindow(QMainWindow):
    """окно с кнопками"""
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        for b in [self.ui.pushButton_0, self.ui.pushButton_1, self.ui.pushButton_2, self.ui.pushButton_3,
                          self.ui.pushButton_4, self.ui.pushButton_5, self.ui.pushButton_6, self.ui.pushButton_7,
                          self.ui.pushButton_8, self.ui.pushButton_9, self.ui.pushButton_C, self.ui.pushButton_eq,
                          self.ui.pushButton_plus, self.ui.pushButton_minus, self.ui.pushButton_mult, self.ui.pushButton_div,
                          self.ui.pushButton_dot, self.ui.pushButton_AC, self.ui.pushButton_sqrt, self.ui.pushButton_pow, self.ui.pushButton_10, self.ui.pushButton]:
            b.clicked.connect(self.click_eq)

        self.ui.clearButton.clicked.connect(self.historyClear)

    def historyClear(self):
        self.ui.listWidget.clear()

    def click_eq(self):
        mc.send(self.sender().text())
        self.update()
        
    def update(self):
        self.ui.state_2.setText(str(mc.event_type))
        self.ui.state.setText(str(mc.state))
        self.ui.digits.setText(mc.current_line)
        if mc.history is not None:
            self.ui.listWidget.addItem(mc.history)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mc = MyCalc()
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())
