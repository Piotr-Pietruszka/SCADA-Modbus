# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1090, 726)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButtonSend_1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonSend_1.setGeometry(QtCore.QRect(180, 430, 75, 23))
        self.pushButtonSend_1.setObjectName("pushButtonSend_1")
        self.lineEditWrite_1 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditWrite_1.setGeometry(QtCore.QRect(10, 430, 161, 20))
        self.lineEditWrite_1.setObjectName("lineEditWrite_1")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(810, 370, 121, 20))
        self.label.setObjectName("label")
        self.lineEditResponse = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditResponse.setGeometry(QtCore.QRect(940, 370, 141, 20))
        self.lineEditResponse.setReadOnly(True)
        self.lineEditResponse.setObjectName("lineEditResponse")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 410, 241, 16))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.lineEditWrite_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditWrite_2.setGeometry(QtCore.QRect(10, 470, 161, 20))
        self.lineEditWrite_2.setObjectName("lineEditWrite_2")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 450, 241, 20))
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.pushButtonSend_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonSend_2.setGeometry(QtCore.QRect(180, 470, 75, 23))
        self.pushButtonSend_2.setObjectName("pushButtonSend_2")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(0, 500, 1101, 21))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(10, 520, 47, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.logsBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.logsBrowser.setGeometry(QtCore.QRect(10, 550, 1061, 131))
        self.logsBrowser.setObjectName("logsBrowser")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(10, 10, 141, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(10, 380, 151, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(-10, 350, 1101, 21))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(170, 60, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(750, 60, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(20, 90, 131, 16))
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(20, 150, 201, 16))
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(20, 200, 211, 16))
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(20, 260, 251, 16))
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(240, 90, 251, 16))
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(550, 90, 221, 16))
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(self.centralwidget)
        self.label_16.setGeometry(QtCore.QRect(550, 150, 191, 16))
        self.label_16.setObjectName("label_16")
        self.label_17 = QtWidgets.QLabel(self.centralwidget)
        self.label_17.setGeometry(QtCore.QRect(550, 210, 231, 16))
        self.label_17.setObjectName("label_17")
        self.label_18 = QtWidgets.QLabel(self.centralwidget)
        self.label_18.setGeometry(QtCore.QRect(550, 270, 231, 16))
        self.label_18.setObjectName("label_18")
        self.label_19 = QtWidgets.QLabel(self.centralwidget)
        self.label_19.setGeometry(QtCore.QRect(810, 90, 201, 16))
        self.label_19.setObjectName("label_19")
        self.label_20 = QtWidgets.QLabel(self.centralwidget)
        self.label_20.setGeometry(QtCore.QRect(810, 150, 281, 16))
        self.label_20.setObjectName("label_20")
        self.label_21 = QtWidgets.QLabel(self.centralwidget)
        self.label_21.setGeometry(QtCore.QRect(810, 210, 221, 16))
        self.label_21.setObjectName("label_21")
        self.label_22 = QtWidgets.QLabel(self.centralwidget)
        self.label_22.setGeometry(QtCore.QRect(810, 270, 231, 16))
        self.label_22.setObjectName("label_22")
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(520, 70, 20, 281))
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.lineEditWrite_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditWrite_3.setGeometry(QtCore.QRect(270, 430, 161, 20))
        self.lineEditWrite_3.setObjectName("lineEditWrite_3")
        self.pushButtonSend_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonSend_3.setGeometry(QtCore.QRect(440, 430, 75, 23))
        self.pushButtonSend_3.setObjectName("pushButtonSend_3")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(270, 410, 241, 16))
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.pushButtonSend_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonSend_4.setGeometry(QtCore.QRect(440, 470, 75, 23))
        self.pushButtonSend_4.setObjectName("pushButtonSend_4")
        self.lineEditWrite_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditWrite_4.setGeometry(QtCore.QRect(270, 470, 161, 20))
        self.lineEditWrite_4.setObjectName("lineEditWrite_4")
        self.label_23 = QtWidgets.QLabel(self.centralwidget)
        self.label_23.setGeometry(QtCore.QRect(270, 450, 241, 20))
        self.label_23.setAlignment(QtCore.Qt.AlignCenter)
        self.label_23.setObjectName("label_23")
        self.lineEditWrite_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditWrite_5.setGeometry(QtCore.QRect(530, 430, 161, 20))
        self.lineEditWrite_5.setObjectName("lineEditWrite_5")
        self.pushButtonSend_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonSend_5.setGeometry(QtCore.QRect(700, 430, 75, 23))
        self.pushButtonSend_5.setObjectName("pushButtonSend_5")
        self.label_24 = QtWidgets.QLabel(self.centralwidget)
        self.label_24.setGeometry(QtCore.QRect(530, 450, 241, 20))
        self.label_24.setAlignment(QtCore.Qt.AlignCenter)
        self.label_24.setObjectName("label_24")
        self.pushButtonSend_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonSend_6.setGeometry(QtCore.QRect(700, 470, 75, 23))
        self.pushButtonSend_6.setObjectName("pushButtonSend_6")
        self.lineEditWrite_6 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditWrite_6.setGeometry(QtCore.QRect(530, 470, 161, 20))
        self.lineEditWrite_6.setObjectName("lineEditWrite_6")
        self.label_25 = QtWidgets.QLabel(self.centralwidget)
        self.label_25.setGeometry(QtCore.QRect(530, 410, 217, 16))
        self.label_25.setAlignment(QtCore.Qt.AlignCenter)
        self.label_25.setObjectName("label_25")
        self.pushButtonSend_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonSend_7.setGeometry(QtCore.QRect(960, 430, 75, 23))
        self.pushButtonSend_7.setObjectName("pushButtonSend_7")
        self.lineEditWrite_7 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditWrite_7.setGeometry(QtCore.QRect(790, 430, 161, 20))
        self.lineEditWrite_7.setObjectName("lineEditWrite_7")
        self.lineEditWrite_8 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditWrite_8.setGeometry(QtCore.QRect(790, 470, 161, 20))
        self.lineEditWrite_8.setObjectName("lineEditWrite_8")
        self.label_26 = QtWidgets.QLabel(self.centralwidget)
        self.label_26.setGeometry(QtCore.QRect(790, 410, 241, 16))
        self.label_26.setAlignment(QtCore.Qt.AlignCenter)
        self.label_26.setObjectName("label_26")
        self.label_27 = QtWidgets.QLabel(self.centralwidget)
        self.label_27.setGeometry(QtCore.QRect(790, 450, 241, 20))
        self.label_27.setAlignment(QtCore.Qt.AlignCenter)
        self.label_27.setObjectName("label_27")
        self.pushButtonSend_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonSend_8.setGeometry(QtCore.QRect(960, 470, 75, 23))
        self.pushButtonSend_8.setObjectName("pushButtonSend_8")
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setGeometry(QtCore.QRect(800, 390, 291, 20))
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.line_5 = QtWidgets.QFrame(self.centralwidget)
        self.line_5.setGeometry(QtCore.QRect(790, 360, 16, 41))
        self.line_5.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.lineEditValue_1 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditValue_1.setGeometry(QtCore.QRect(20, 110, 191, 21))
        self.lineEditValue_1.setReadOnly(True)
        self.lineEditValue_1.setObjectName("lineEditValue_1")
        self.lineEditValue_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditValue_2.setGeometry(QtCore.QRect(20, 170, 191, 21))
        self.lineEditValue_2.setReadOnly(True)
        self.lineEditValue_2.setObjectName("lineEditValue_2")
        self.lineEditValue_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditValue_3.setGeometry(QtCore.QRect(20, 220, 191, 21))
        self.lineEditValue_3.setReadOnly(True)
        self.lineEditValue_3.setObjectName("lineEditValue_3")
        self.lineEditValue_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditValue_4.setGeometry(QtCore.QRect(20, 280, 191, 21))
        self.lineEditValue_4.setReadOnly(True)
        self.lineEditValue_4.setObjectName("lineEditValue_4")
        self.lineEditValue_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditValue_5.setGeometry(QtCore.QRect(240, 110, 191, 21))
        self.lineEditValue_5.setReadOnly(True)
        self.lineEditValue_5.setObjectName("lineEditValue_5")
        self.lineEditValue_6 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditValue_6.setGeometry(QtCore.QRect(550, 110, 191, 21))
        self.lineEditValue_6.setReadOnly(True)
        self.lineEditValue_6.setObjectName("lineEditValue_6")
        self.lineEditValue_7 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditValue_7.setGeometry(QtCore.QRect(550, 170, 191, 21))
        self.lineEditValue_7.setReadOnly(True)
        self.lineEditValue_7.setObjectName("lineEditValue_7")
        self.lineEditValue_8 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditValue_8.setGeometry(QtCore.QRect(550, 230, 191, 21))
        self.lineEditValue_8.setReadOnly(True)
        self.lineEditValue_8.setObjectName("lineEditValue_8")
        self.lineEditValue_9 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditValue_9.setGeometry(QtCore.QRect(550, 290, 191, 21))
        self.lineEditValue_9.setReadOnly(True)
        self.lineEditValue_9.setObjectName("lineEditValue_9")
        self.lineEditValue_10 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditValue_10.setGeometry(QtCore.QRect(810, 110, 191, 21))
        self.lineEditValue_10.setReadOnly(True)
        self.lineEditValue_10.setObjectName("lineEditValue_10")
        self.lineEditValue_11 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditValue_11.setGeometry(QtCore.QRect(810, 170, 191, 21))
        self.lineEditValue_11.setReadOnly(True)
        self.lineEditValue_11.setObjectName("lineEditValue_11")
        self.lineEditValue_12 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditValue_12.setGeometry(QtCore.QRect(810, 230, 191, 21))
        self.lineEditValue_12.setReadOnly(True)
        self.lineEditValue_12.setObjectName("lineEditValue_12")
        self.lineEditValue_13 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditValue_13.setGeometry(QtCore.QRect(810, 290, 191, 21))
        self.lineEditValue_13.setReadOnly(True)
        self.lineEditValue_13.setObjectName("lineEditValue_13")
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
        self.label.setText(_translate("MainWindow", "Odpowiedz na zmiane"))
        self.label_2.setText(_translate("MainWindow", "Siłownik zaworu nagrzewnicy wstępnej 0-255"))
        self.label_4.setText(_translate("MainWindow", "Siłownik zaworu chłodnicy 0-255"))
        self.pushButtonSend_2.setText(_translate("MainWindow", "Wyślij"))
        self.label_5.setText(_translate("MainWindow", "LOGS"))
        self.logsBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">!PROGRAM START!</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.label_6.setText(_translate("MainWindow", "AKTUALNE STANY"))
        self.label_7.setText(_translate("MainWindow", "ZMIEN STAN WYJŚĆ"))
        self.label_8.setText(_translate("MainWindow", "WEJSCIA"))
        self.label_9.setText(_translate("MainWindow", "WYJSCIA"))
        self.label_10.setText(_translate("MainWindow", "Czujnik temp. zewnetrznej"))
        self.label_11.setText(_translate("MainWindow", "Czujnik temp. powietrza wywiewanego"))
        self.label_12.setText(_translate("MainWindow", "Termostat p-zamr. nagrzewnicy [true/false]"))
        self.label_13.setText(_translate("MainWindow", "Prostat filtra podstawowego nawiewu [true/false]"))
        self.label_14.setText(_translate("MainWindow", "Prostat filtra podstawowego wywiewu [true/false]"))
        self.label_15.setText(_translate("MainWindow", "Siłownik zaworu nagrzewnicy wstępnej [%]"))
        self.label_16.setText(_translate("MainWindow", "Siłownik zaworu chłodnicy [%]"))
        self.label_17.setText(_translate("MainWindow", "Prędkość obrotowa wentylatora nawieru [%]"))
        self.label_18.setText(_translate("MainWindow", "Prędkość obrotowa wentylatora wywieru [%] "))
        self.label_19.setText(_translate("MainWindow", "Recylkulacja [%]"))
        self.label_20.setText(_translate("MainWindow", "Załączenie pompy nagrzewnicy wstępnej  [true/false]"))
        self.label_21.setText(_translate("MainWindow", "Załączenie wentylatora nawiewu [true/false]"))
        self.label_22.setText(_translate("MainWindow", "Załączenie wentylatora wywieru [true/talse]"))
        self.pushButtonSend_3.setText(_translate("MainWindow", "Wyślij"))
        self.label_3.setText(_translate("MainWindow", "Predkość obrotowa wentylatora nawiewu 0-255"))
        self.pushButtonSend_4.setText(_translate("MainWindow", "Wyślij"))
        self.label_23.setText(_translate("MainWindow", "Predkość obrotowa wentylatora wywiewu 0-255"))
        self.pushButtonSend_5.setText(_translate("MainWindow", "Wyślij"))
        self.label_24.setText(_translate("MainWindow", "Załączenie pompy nagrzewnicy wstępnej 0-255"))
        self.pushButtonSend_6.setText(_translate("MainWindow", "Wyślij"))
        self.label_25.setText(_translate("MainWindow", "Recyrkulacja 0-255"))
        self.pushButtonSend_7.setText(_translate("MainWindow", "Wyślij"))
        self.label_26.setText(_translate("MainWindow", "Załączenie wentylatora nawiewu 0-1"))
        self.label_27.setText(_translate("MainWindow", "Załączenie wentylatora wywiewu 0-1"))
        self.pushButtonSend_8.setText(_translate("MainWindow", "Wyślij"))
        self.lineEditValue_1.setText(_translate("MainWindow", "UNKNOWN"))
        self.lineEditValue_2.setText(_translate("MainWindow", "UNKNOWN"))
        self.lineEditValue_3.setText(_translate("MainWindow", "UNKNOWN"))
        self.lineEditValue_4.setText(_translate("MainWindow", "UNKNOWN"))
        self.lineEditValue_5.setText(_translate("MainWindow", "UNKNOWN"))
        self.lineEditValue_6.setText(_translate("MainWindow", "UNKNOWN"))
        self.lineEditValue_7.setText(_translate("MainWindow", "UNKNOWN"))
        self.lineEditValue_8.setText(_translate("MainWindow", "UNKNOWN"))
        self.lineEditValue_9.setText(_translate("MainWindow", "UNKNOWN"))
        self.lineEditValue_10.setText(_translate("MainWindow", "UNKNOWN"))
        self.lineEditValue_11.setText(_translate("MainWindow", "UNKNOWN"))
        self.lineEditValue_12.setText(_translate("MainWindow", "UNKNOWN"))
        self.lineEditValue_13.setText(_translate("MainWindow", "UNKNOWN"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
