# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtWidgets import QApplication, QMainWindow

from ui_form import Ui_MainWindow

from enum import Enum

ops = ["=", "+", "-", "*", "/", "sqrt", "pow"]
acts = ["AC", "C"]
digits = list("0123456789.")

#1233

class State(Enum):
    OPS = 0
    ACTS = 1
    DIGITS = 2
    FRST = 3
    SCND = 4


class MyCalc():
    def __init__(self):
        self.current_line = "0"
        self.input = []
        self.state = State.OPS
        self.stack = []
        print (self.state)

    def compute(self,list):
        print("result is: ",eval(''.join(map(str, self.stack))))
        self.input.clear()
        self.stack.clear()
        print(self.input, self.stack)



    def send(self,s):
        print('typed ', s)



class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        for b in [self.ui.pushButton_0, self.ui.pushButton_1, self.ui.pushButton_2, self.ui.pushButton_3,
                          self.ui.pushButton_4, self.ui.pushButton_5, self.ui.pushButton_6, self.ui.pushButton_7,
                          self.ui.pushButton_8, self.ui.pushButton_9, self.ui.pushButton_C, self.ui.pushButton_eq,
                          self.ui.pushButton_plus, self.ui.pushButton_minus, self.ui.pushButton_mult, self.ui.pushButton_div,
                          self.ui.pushButton_dot, self.ui.pushButton_AC, self.ui.pushButton_sqrt, self.ui.pushButton_pow]:
            b.clicked.connect(self.click_eq)

    def click_eq(self):
        dtext = mc.send(self.sender().text())
        self.ui.digits.setText(dtext)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mc = MyCalc()
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())
