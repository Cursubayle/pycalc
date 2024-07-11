# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtWidgets import QApplication, QMainWindow

from ui_form import Ui_MainWindow

from enum import Enum

ops = ["+", "-", "*", "/"]
acts = ["AC", "C", "="]
digits = list("0123456789.")

#1233

class State(Enum):
    CLEAR = 0
    DIGITS = 1
    OPS = 2




class MyCalc():
    def __init__(self):
        self.current_line = ""
        self.input = []
        self.state = State.CLEAR
        self.stack = []
        print (self.state)

    def clear(self):
        return
    def number(self):
        return
    def op(self):
        return

    table = [ [State.CLEAR, clear] , [State.DIGITS , clear], [State.OPS, clear],
            [State.CLEAR, number  ],       [State.DIGITS, number],     [State.OPS, number],
            [State.CLEAR, op],       [State.DIGITS, op], [State.OPS, op]

    ]


    digitsTable = ['acts','number','op']


    def do_event(self, event, value):
        print (self.state)
        match self.state:
            case State.CLEAR:
                match event:
                    case 'number':
                        self.state = State.DIGITS
                        self.current_line += value
                        print(self.current_line)
                        return self.current_line

                    case 'op':
                        None

                    case 'acts':
                        None
            case State.DIGITS:
                match event:
                    case 'number':
                        self.current_line += value
                        print(self.current_line)
                        return self.current_line


                    case 'op':
                        self.state = State.OPS
                        self.stack.append(self.current_line)
                        self.current_line = ''
                        self.current_line += value
                        print(self.stack)
                        return self.current_line

                    case 'acts':
                        self.current_line = ''
                        self.stack.clear()
                        return

            case State.OPS:
                match event:
                    case 'number':
                        self.state = State.DIGITS
                        self.stack.append(self.current_line)
                        print(self.stack)
                        self.current_line = ''
                        self.current_line += value
                        print(self.current_line)
                        return self.current_line

                    case 'op':
                        self.current_line = value
                        return self.current_line

                    case 'acts':
                        match acts:
                            case "C":
                                None
                                                                                                           #acts = ["AC", "C", "="]
                            case "=":
                                None
                        self.current_line = ''
                        self.stack.clear()
                        return




    def send(self,s):


        if s in digits:
            return self.do_event('number', s)

        elif s in ops:
            return self.do_event('op', s)

        elif s in acts:
            return self.do_event('clear', s)




        print(self.state)
        print('typed ', s)
        self.current_line += s
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
