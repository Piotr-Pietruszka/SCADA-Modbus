# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(799, 531)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButtonSend = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonSend.setGeometry(QtCore.QRect(60, 210, 75, 23))
        self.pushButtonSend.setObjectName("pushButtonSend")
        self.lineEditWritePacket = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditWritePacket.setGeometry(QtCore.QRect(40, 170, 113, 20))
        self.lineEditWritePacket.setObjectName("lineEditWritePacket")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(290, 210, 141, 16))
        self.label.setObjectName("label")
        self.lineEditResponse = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditResponse.setGeometry(QtCore.QRect(290, 170, 113, 20))
        self.lineEditResponse.setObjectName("lineEditResponse")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 799, 21))
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
        self.pushButtonSend.setText(_translate("MainWindow", "Send"))
        self.label.setText(_translate("MainWindow", "Response"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
