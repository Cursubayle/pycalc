# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayoutWidget = QWidget(self.centralwidget)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(190, 151, 340, 271))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.pushButton_5 = QPushButton(self.gridLayoutWidget)
        self.pushButton_5.setObjectName(u"pushButton_5")

        self.gridLayout.addWidget(self.pushButton_5, 1, 2, 1, 1)

        self.pushButton_8 = QPushButton(self.gridLayoutWidget)
        self.pushButton_8.setObjectName(u"pushButton_8")

        self.gridLayout.addWidget(self.pushButton_8, 2, 2, 1, 1)

        self.pushButton_4 = QPushButton(self.gridLayoutWidget)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.gridLayout.addWidget(self.pushButton_4, 1, 1, 1, 1)

        self.pushButton_6 = QPushButton(self.gridLayoutWidget)
        self.pushButton_6.setObjectName(u"pushButton_6")

        self.gridLayout.addWidget(self.pushButton_6, 1, 3, 1, 1)

        self.pushButton_9 = QPushButton(self.gridLayoutWidget)
        self.pushButton_9.setObjectName(u"pushButton_9")

        self.gridLayout.addWidget(self.pushButton_9, 2, 3, 1, 1)

        self.pushButton_C = QPushButton(self.gridLayoutWidget)
        self.pushButton_C.setObjectName(u"pushButton_C")

        self.gridLayout.addWidget(self.pushButton_C, 4, 2, 1, 1)

        self.pushButton_plus = QPushButton(self.gridLayoutWidget)
        self.pushButton_plus.setObjectName(u"pushButton_plus")

        self.gridLayout.addWidget(self.pushButton_plus, 0, 0, 1, 1)

        self.pushButton_sqrt = QPushButton(self.gridLayoutWidget)
        self.pushButton_sqrt.setObjectName(u"pushButton_sqrt")

        self.gridLayout.addWidget(self.pushButton_sqrt, 4, 0, 1, 1)

        self.pushButton_div = QPushButton(self.gridLayoutWidget)
        self.pushButton_div.setObjectName(u"pushButton_div")

        self.gridLayout.addWidget(self.pushButton_div, 3, 0, 1, 1)

        self.pushButton_dot = QPushButton(self.gridLayoutWidget)
        self.pushButton_dot.setObjectName(u"pushButton_dot")

        self.gridLayout.addWidget(self.pushButton_dot, 3, 1, 1, 1)

        self.pushButton_minus = QPushButton(self.gridLayoutWidget)
        self.pushButton_minus.setObjectName(u"pushButton_minus")

        self.gridLayout.addWidget(self.pushButton_minus, 1, 0, 1, 1)

        self.pushButton_2 = QPushButton(self.gridLayoutWidget)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.gridLayout.addWidget(self.pushButton_2, 0, 2, 1, 1)

        self.pushButton_AC = QPushButton(self.gridLayoutWidget)
        self.pushButton_AC.setObjectName(u"pushButton_AC")

        self.gridLayout.addWidget(self.pushButton_AC, 4, 3, 1, 1)

        self.pushButton_3 = QPushButton(self.gridLayoutWidget)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.gridLayout.addWidget(self.pushButton_3, 0, 3, 1, 1)

        self.pushButton_7 = QPushButton(self.gridLayoutWidget)
        self.pushButton_7.setObjectName(u"pushButton_7")

        self.gridLayout.addWidget(self.pushButton_7, 2, 1, 1, 1)

        self.pushButton_0 = QPushButton(self.gridLayoutWidget)
        self.pushButton_0.setObjectName(u"pushButton_0")

        self.gridLayout.addWidget(self.pushButton_0, 3, 2, 1, 1)

        self.pushButton_mult = QPushButton(self.gridLayoutWidget)
        self.pushButton_mult.setObjectName(u"pushButton_mult")

        self.gridLayout.addWidget(self.pushButton_mult, 2, 0, 1, 1)

        self.pushButton_eq = QPushButton(self.gridLayoutWidget)
        self.pushButton_eq.setObjectName(u"pushButton_eq")

        self.gridLayout.addWidget(self.pushButton_eq, 3, 3, 1, 1)

        self.pushButton_pow = QPushButton(self.gridLayoutWidget)
        self.pushButton_pow.setObjectName(u"pushButton_pow")

        self.gridLayout.addWidget(self.pushButton_pow, 4, 1, 1, 1)

        self.pushButton_1 = QPushButton(self.gridLayoutWidget)
        self.pushButton_1.setObjectName(u"pushButton_1")

        self.gridLayout.addWidget(self.pushButton_1, 0, 1, 1, 1)

        self.digits = QLabel(self.centralwidget)
        self.digits.setObjectName(u"digits")
        self.digits.setGeometry(QRect(197, 40, 321, 101))
        self.digits.setBaseSize(QSize(0, 0))
        font = QFont()
        font.setFamilies([u"Monaco"])
        font.setPointSize(56)
        font.setBold(True)
        self.digits.setFont(font)
        self.digits.setTextFormat(Qt.AutoText)
        self.digits.setScaledContents(False)
        self.digits.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.history = QLabel(self.centralwidget)
        self.history.setObjectName(u"history")
        self.history.setGeometry(QRect(530, 40, 211, 381))
        self.history.setBaseSize(QSize(0, 0))
        self.history.setFont(font)
        self.history.setTextFormat(Qt.AutoText)
        self.history.setScaledContents(False)
        self.history.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 23))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"8", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"6", None))
        self.pushButton_9.setText(QCoreApplication.translate("MainWindow", u"9", None))
        self.pushButton_C.setText(QCoreApplication.translate("MainWindow", u"C", None))
        self.pushButton_plus.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.pushButton_sqrt.setText(QCoreApplication.translate("MainWindow", u"sqrt", None))
        self.pushButton_div.setText(QCoreApplication.translate("MainWindow", u"/", None))
        self.pushButton_dot.setText(QCoreApplication.translate("MainWindow", u".", None))
        self.pushButton_minus.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.pushButton_AC.setText(QCoreApplication.translate("MainWindow", u"AC", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"7", None))
        self.pushButton_0.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.pushButton_mult.setText(QCoreApplication.translate("MainWindow", u"*", None))
        self.pushButton_eq.setText(QCoreApplication.translate("MainWindow", u"=", None))
#if QT_CONFIG(shortcut)
        self.pushButton_eq.setShortcut(QCoreApplication.translate("MainWindow", u"=", None))
#endif // QT_CONFIG(shortcut)
        self.pushButton_pow.setText(QCoreApplication.translate("MainWindow", u"x^2", None))
        self.pushButton_1.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.digits.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.history.setText(QCoreApplication.translate("MainWindow", u"0", None))
    # retranslateUi

