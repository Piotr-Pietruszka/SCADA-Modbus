# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1090, 726)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButtonSend_1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonSend_1.setGeometry(QtCore.QRect(250, 89, 75, 23))
        self.pushButtonSend_1.setObjectName("pushButtonSend_1")
        self.lineEditWrite_1 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditWrite_1.setGeometry(QtCore.QRect(21, 90, 217, 20))
        self.lineEditWrite_1.setObjectName("lineEditWrite_1")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(640, 230, 141, 16))
        self.label.setObjectName("label")
        self.lineEditResponse = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditResponse.setGeometry(QtCore.QRect(640, 180, 113, 20))
        self.lineEditResponse.setObjectName("lineEditResponse")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(21, 71, 217, 16))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(30, 10, 171, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.lineEditWrite_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditWrite_2.setGeometry(QtCore.QRect(21, 180, 217, 20))
        self.lineEditWrite_2.setObjectName("lineEditWrite_2")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(40, 160, 191, 16))
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.pushButtonSend_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonSend_2.setGeometry(QtCore.QRect(250, 179, 75, 23))
        self.pushButtonSend_2.setObjectName("pushButtonSend_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1090, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButtonSend_1.setText(_translate("MainWindow", "Wyślij"))
        self.label.setText(_translate("MainWindow", "Response"))
        self.label_2.setText(_translate("MainWindow", "Siłownik zaworu nagrzewnicy wstępnej 0-255"))
        self.label_3.setText(_translate("MainWindow", "Ustawianie Wyjść"))
        self.label_4.setText(_translate("MainWindow", "Siłownik zaworu chłodnicy"))
        self.pushButtonSend_2.setText(_translate("MainWindow", "Wyślij"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
