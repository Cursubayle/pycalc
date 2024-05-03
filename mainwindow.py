# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtWidgets import QApplication, QMainWindow

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_MainWindow                                                               

ops = ["=", "+", "-", "*", "/", "sqrt", "pow"]
acts = ["AC", "C"]
digits = list("0123456789.")

from enum import Enum
class State(Enum):
    OPS = 0
    ACTS = 1
    DIGITS = 2

class MyCalc():
    def __init__(self):
        self.stack = []
        self.current_line = "0"
        self.state = State.ACTS

    def last(self) -> str:
        try:
            return self.stack[-1]
        except:
            return ""

    def is_ops(self, s:str) -> bool:
        if s in ops:
            return True
        return False

    def is_digits(self, s:str) -> bool:
        if s in digits:
            return True
        return False

    def is_acts(self, s:str) -> bool:
        if s in acts:
            return True
        return False

    def evaluate(self) -> str:
        print(f"Вычисляю {self.stack}")
        if self.stack[1] == '+':
            rc = str(float(self.stack[0])+float(self.stack[2]))
            self.stack = []
            return rc
        if self.stack[1] == '-':
            rc = str(float(self.stack[0])-float(self.stack[2]))
            self.stack = []
            return rc
        if self.stack[1] == '*':
            rc = str(float(self.stack[0])*float(self.stack[2]))
            self.stack = []
            return rc
        if self.stack[1] == '/':
            rc = str(float(self.stack[0])/float(self.stack[2]))
            self.stack = []
            return rc

    # МКА
    def send(self, s) -> str:
        print(f"Нажал {s} {self.state}")
        if self.is_ops(s):
            if self.state == State.OPS:
                if s == '-':
                    self.stack.append(self.current_line)
                    self.current_line = s
                    self.state = State.DIGITS
                else:
                    # После операции операция заменяет старую
                    print(f"Была уже операция {self.last()}")
                    self.stack[-1] = s
            elif self.state == State.DIGITS:
                self.stack.append(self.current_line)
                self.current_line = s
                self.state = State.OPS
                if s == '=':
                    self.current_line = self.evaluate()
                    self.state = State.DIGITS
            elif self.state == State.ACTS:
                if s == '-':
                    self.current_line = s
                    self.state = State.DIGITS

        elif self.is_digits(s):
            if self.state == State.OPS:
                self.stack.append(self.current_line)
                self.current_line = s
                self.state = State.DIGITS
            elif self.state == State.DIGITS:
                if self.current_line == "0":
                     self.current_line = s
                else:
                    self.current_line += s
            elif self.state == State.ACTS:
                self.current_line = s
                self.state = State.DIGITS

        elif self.is_acts(s):
            if s == "AC":
                self.stack = []
                self.current_line = "0"
                self.state = State.ACTS
            elif s == "C":
                if self.state == State.OPS:
                    self.current_line = "0"
                    self.state = State.ACTS
                elif self.state == State.DIGITS:
                    self.current_line = "0"
                    self.state = State.ACTS
                elif self.state == State.ACTS:
                    pass
        print(f"Стек {self.stack}")
        print(f"Строка {self.current_line}")
        return self.current_line


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
