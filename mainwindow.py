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
        self.input = []
        self.state = State.OPS
        self.stack = []
        print (self.state)

    def compute(self,list):
        print("result is: ",eval(''.join(map(str, self.stack))))
        self.input.clear()
        self.stack.clear()



    def send(self,s):
        if s == 'C':
            self.input.clear()
            self.stack.clear()
            self.state = State.OPS


        match self.state:
            case State.DIGITS:
                if s in digits:
                    self.input.append(s)

                elif s in ops and len(self.input) > 0 and len(self.stack) == 2:
                    self.stack.append(''.join(map(str, self.input)))
                    self.compute(self.stack)

                elif s in ops:
                    self.stack.append(''.join(map(str, self.input)))
                    self.stack.append(s)
                    self.input.clear()
                    self.state = State.OPS




                print("input",self.input)
                print('state',self.state)
                print("stack",self.stack)
                print(f"Нажал {s}")


                return State.DIGITS

            case State.OPS:

                if s in ops:
                    if  len(self.stack) > 0 and self.stack[0] in ops or len(self.stack) == 2 and self.stack[1] in ops:
                        self.stack.pop()

                    self.stack.append(s)
                    print('wew')

                elif s in digits:
                    self.input.append(s)
                    self.state = State.DIGITS
                    print('wow')
                print("input",self.input)
                print('state',self.state)
                print("stack",self.stack)
                print(f"Нажал {s}")








    def seend(self, s):
        if self.state == State.DIGITS:
            if len(self.input) == 0 and s == '-':
                self.input.append(s)
            elif s == 'C':
                self.input.clear()
                self.stack.clear()
            elif s in digits:
                self.input.append(s)
            elif len(self.input) > 1 and s in ops:
                if s in ops and len(self.input) > 1 and len(self.stack) > 1:
                    self.stack.append(''.join(map(str, self.input)))
                    self.compute(self.stack)
                else:
                    self.stack.append(''.join(map(str, self.input)))
                    self.state = State.OPS
                    self.input.clear()

        if self.state == State.OPS and s in ops:


            self.stack.append(s)
            self.state = State.DIGITS







        print('len stack',len(self.stack))
        print(f"Нажал {s}")
        print ("input",self.input)
        print ('state',self.state)
        print ("stack",self.stack)

    def set_state(self, state):
        if self.state == "number":
            self.state = "operator"
            return self.state
        if self.state == "operator":
            self.state = "number"
            return self.state









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
        mc.send(self.sender().text())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mc = MyCalc()
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())
