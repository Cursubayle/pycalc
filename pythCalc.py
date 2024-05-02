import sys
from PySide6.QtWidgets import QApplication, QMainWindow

from ui_form import Ui_MainWindow  

class MyCalc():
    def __init__(self):
        pass

    def send(self, s):
        print(f"Нажал {s}")


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushBtn_1.clicked.connect(self.click_eq)
        self.ui.pushBtn_2.clicked.connect(self.click_eq)
        self.ui.pushBtn_3.clicked.connect(self.click_eq)
        self.ui.pushBtn_4.clicked.connect(self.click_eq)
        self.ui.pushBtn_5.clicked.connect(self.click_eq)
        self.ui.pushBtn_6.clicked.connect(self.click_eq)
        self.ui.pushBtn_7.clicked.connect(self.click_eq)
        self.ui.pushBtn_8.clicked.connect(self.click_eq)
        self.ui.pushBtn_9.clicked.connect(self.click_eq)
        self.ui.pushBtn_0.clicked.connect(self.click_eq)

    def click_eq(self):
        mc.send(self.sender().text())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mc = MyCalc()
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())