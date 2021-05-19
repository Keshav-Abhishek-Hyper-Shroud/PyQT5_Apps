from PyQt5 import QtCore, QtGui, QtWidgets
from pyautogui import size as py_size

screen_size=py_size()

window_width=int(0.318*screen_size[0])
window_height=int(0.807*screen_size[1])

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(window_width,window_height)
        MainWindow.setMinimumSize(QtCore.QSize(window_width,window_height))
        MainWindow.setMaximumSize(QtCore.QSize(window_width,window_height))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(int(0.025*window_width), int(0.017*window_height), int(0.961*window_width), int(0.088*window_height)))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget,clicked=lambda:self.pressed_OF())
        self.pushButton.setGeometry(QtCore.QRect(int(0.025*window_width), int(0.12*window_height), int(0.224*window_width), int(0.157*window_height)))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(48)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget,clicked=lambda:self.pressed_C())
        self.pushButton_2.setGeometry(QtCore.QRect(int(0.27*window_width), int(0.12*window_height), int(0.224*window_width), int(0.157*window_height)))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(48)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget,clicked=lambda:self.pressed_percent())
        self.pushButton_3.setGeometry(QtCore.QRect(int(0.516*window_width), int(0.12*window_height), int(0.224*window_width), int(0.157*window_height)))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(48)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget,clicked=lambda:self.pressed_DEL())
        self.pushButton_4.setGeometry(QtCore.QRect(int(0.762*window_width), int(0.12*window_height), int(0.224*window_width), int(0.157*window_height)))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(48)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget,clicked=lambda:self.pressed_7())
        self.pushButton_5.setGeometry(QtCore.QRect(int(0.025*window_width), int(0.293*window_height), int(0.224*window_width), int(0.157*window_height)))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(48)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget,clicked=lambda:self.pressed_8())
        self.pushButton_6.setGeometry(QtCore.QRect(int(0.27*window_width), int(0.293*window_height), int(0.224*window_width), int(0.157*window_height)))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(48)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget,clicked=lambda:self.pressed_9())
        self.pushButton_7.setGeometry(QtCore.QRect(int(0.516*window_width), int(0.293*window_height), int(0.224*window_width), int(0.157*window_height)))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(48)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget,clicked=lambda:self.pressed_div())
        self.pushButton_8.setGeometry(QtCore.QRect(int(0.762*window_width), int(0.293*window_height), int(0.224*window_width), int(0.157*window_height)))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(48)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(self.centralwidget,clicked=lambda:self.pressed_4())
        self.pushButton_9.setGeometry(QtCore.QRect(int(0.025*window_width), int(0.465*window_height), int(0.224*window_width), int(0.157*window_height)))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(48)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_10 = QtWidgets.QPushButton(self.centralwidget,clicked=lambda:self.pressed_5())
        self.pushButton_10.setGeometry(QtCore.QRect(int(0.27*window_width), int(0.465*window_height), int(0.224*window_width), int(0.157*window_height)))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(48)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_10.setFont(font)
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_11 = QtWidgets.QPushButton(self.centralwidget,clicked=lambda:self.pressed_6())
        self.pushButton_11.setGeometry(QtCore.QRect(int(0.516*window_width), int(0.465*window_height), int(0.224*window_width), int(0.157*window_height)))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(48)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_11.setFont(font)
        self.pushButton_11.setObjectName("pushButton_11")
        self.pushButton_12 = QtWidgets.QPushButton(self.centralwidget,clicked=lambda:self.pressed_x())
        self.pushButton_12.setGeometry(QtCore.QRect(int(0.762*window_width), int(0.465*window_height), int(0.224*window_width), int(0.157*window_height)))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(48)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_12.setFont(font)
        self.pushButton_12.setObjectName("pushButton_12")
        self.pushButton_13 = QtWidgets.QPushButton(self.centralwidget,clicked=lambda:self.pressed_1())
        self.pushButton_13.setGeometry(QtCore.QRect(int(0.025*window_width), int(0.637*window_height), int(0.224*window_width), int(0.157*window_height)))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(48)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_13.setFont(font)
        self.pushButton_13.setObjectName("pushButton_13")
        self.pushButton_14 = QtWidgets.QPushButton(self.centralwidget,clicked=lambda:self.pressed_2())
        self.pushButton_14.setGeometry(QtCore.QRect(int(0.27*window_width), int(0.637*window_height), int(0.224*window_width), int(0.157*window_height)))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(48)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_14.setFont(font)
        self.pushButton_14.setObjectName("pushButton_14")
        self.pushButton_15 = QtWidgets.QPushButton(self.centralwidget,clicked=lambda:self.pressed_3())
        self.pushButton_15.setGeometry(QtCore.QRect(int(0.516*window_width), int(0.637*window_height), int(0.224*window_width), int(0.157*window_height)))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(48)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_15.setFont(font)
        self.pushButton_15.setObjectName("pushButton_15")
        self.pushButton_16 = QtWidgets.QPushButton(self.centralwidget,clicked=lambda:self.pressed_minus())
        self.pushButton_16.setGeometry(QtCore.QRect(int(0.762*window_width), int(0.637*window_height), int(0.224*window_width), int(0.157*window_height)))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(48)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_16.setFont(font)
        self.pushButton_16.setObjectName("pushButton_16")
        self.pushButton_17 = QtWidgets.QPushButton(self.centralwidget,clicked=lambda:self.pressed_0())
        self.pushButton_17.setGeometry(QtCore.QRect(int(0.025*window_width), int(0.809*window_height), int(0.224*window_width), int(0.157*window_height)))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(48)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_17.setFont(font)
        self.pushButton_17.setObjectName("pushButton_17")
        self.pushButton_18 = QtWidgets.QPushButton(self.centralwidget,clicked=lambda:self.pressed_decimal())
        self.pushButton_18.setGeometry(QtCore.QRect(int(0.27*window_width), int(0.809*window_height), int(0.224*window_width), int(0.157*window_height)))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(48)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_18.setFont(font)
        self.pushButton_18.setObjectName("pushButton_18")
        self.pushButton_19 = QtWidgets.QPushButton(self.centralwidget,clicked=lambda:self.pressed_equal())
        self.pushButton_19.setGeometry(QtCore.QRect(int(0.516*window_width), int(0.809*window_height), int(0.224*window_width), int(0.157*window_height)))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(48)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_19.setFont(font)
        self.pushButton_19.setObjectName("pushButton_19")
        self.pushButton_20 = QtWidgets.QPushButton(self.centralwidget,clicked=lambda:self.pressed_add())
        self.pushButton_20.setGeometry(QtCore.QRect(int(0.762*window_width), int(0.809*window_height), int(0.224*window_width), int(0.157*window_height)))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(48)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_20.setFont(font)
        self.pushButton_20.setObjectName("pushButton_20")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.lineEdit.setDisabled(True)

    permission=True

    def screen(self):
        self.lineEdit.setText('')

    def pressed_OF(self):
        global permission
        if self.permission==True:
            self.lineEdit.setDisabled(False)
            self.permission=False
            self.pushButton.setText('OFF')
            self.lineEdit.setText('Calculator Turned ON')
            QtCore.QTimer.singleShot(500,self.screen)
            return
        else:
            self.lineEdit.setText('')
            self.lineEdit.setDisabled(True)
            self.permission=True
            self.pushButton.setText('ON')
            self.lineEdit.setText('Calculator Turned OFF')
            QtCore.QTimer.singleShot(500,self.screen)
            return

    def pressed_C(self):
        global permission
        if self.permission==False:
            a=self.lineEdit.setText('')

    def pressed_percent(self):
        global permission
        if self.permission==False:
            curr_button=self.pushButton_3.text()
            self.lineEdit.setText(str(self.lineEdit.text())+str(curr_button))

    def pressed_DEL(self):
        global permission
        if self.permission==False:
            data=str(self.lineEdit.text())
            data=data[:len(data)-1:]
            self.lineEdit.setText(data)

    def pressed_7(self):
        global permission
        if self.permission==False:
            curr_button=self.pushButton_5.text()
            self.lineEdit.setText(str(self.lineEdit.text())+str(curr_button))

    def pressed_8(self):
        global permission
        if self.permission==False:
            curr_button=self.pushButton_6.text()
            self.lineEdit.setText(str(self.lineEdit.text())+str(curr_button))

    def pressed_9(self):
        global permission
        if self.permission==False:
            curr_button=self.pushButton_7.text()
            self.lineEdit.setText(str(self.lineEdit.text())+str(curr_button))

    def pressed_div(self):
        global permission
        if self.permission==False:
            curr_button=self.pushButton_8.text()
            self.lineEdit.setText(str(self.lineEdit.text())+str(curr_button))

    def pressed_4(self):
        global permission
        if self.permission==False:
            curr_button=self.pushButton_9.text()
            self.lineEdit.setText(str(self.lineEdit.text())+str(curr_button))

    def pressed_5(self):
        global permission
        if self.permission==False:
            curr_button=self.pushButton_10.text()
            self.lineEdit.setText(str(self.lineEdit.text())+str(curr_button))

    def pressed_6(self):
        global permission
        if self.permission==False:
            curr_button=self.pushButton_11.text()
            self.lineEdit.setText(str(self.lineEdit.text())+str(curr_button))

    def pressed_x(self):
        global permission
        if self.permission==False:
            curr_button=self.pushButton_12.text()
            self.lineEdit.setText(str(self.lineEdit.text())+str(curr_button))

    def pressed_1(self):
        global permission
        if self.permission==False:
            curr_button=self.pushButton_13.text()
            self.lineEdit.setText(str(self.lineEdit.text())+str(curr_button))

    def pressed_2(self):
        global permission
        if self.permission==False:
            curr_button=self.pushButton_14.text()
            self.lineEdit.setText(str(self.lineEdit.text())+str(curr_button))

    def pressed_3(self):
        global permission
        if self.permission==False:
            curr_button=self.pushButton_15.text()
            self.lineEdit.setText(str(self.lineEdit.text())+str(curr_button))

    def pressed_minus(self):
        global permission
        if self.permission==False:
            curr_button=self.pushButton_16.text()
            self.lineEdit.setText(str(self.lineEdit.text())+str(curr_button))

    def pressed_0(self):
        global permission
        if self.permission==False:
            curr_button=self.pushButton_17.text()
            self.lineEdit.setText(str(self.lineEdit.text())+str(curr_button))

    def pressed_decimal(self):
        global permission
        if self.permission==False:
            curr_button=self.pushButton_18.text()
            self.lineEdit.setText(str(self.lineEdit.text())+str(curr_button))

    def pressed_equal(self):
        global permission
        if self.permission==False:
            data=str(self.lineEdit.text())
            data=data.replace('%','/100x')
            data=data.replace('x','*')
            data=data.replace('÷','/')

            try:
                calculated=float(eval(data))
                after_decimal=str(calculated)
                after_decimal=after_decimal.split('.')
                after_decimal=after_decimal[-1]
                after_decimal=len(after_decimal)+1
                calculated=round(calculated,after_decimal)
                calculated=str(calculated)
                self.lineEdit.setText(calculated)
            except:
                self.lineEdit.setText('Error')
                QtCore.QTimer.singleShot(1500,self.screen)
            return

    def pressed_add(self):
        global permission
        if self.permission==False:
            curr_button=self.pushButton_20.text()
            self.lineEdit.setText(str(self.lineEdit.text())+str(curr_button))

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "PyQt5 Calculator"))
        self.pushButton.setText(_translate("MainWindow", "ON"))
        self.pushButton_2.setText(_translate("MainWindow", "C"))
        self.pushButton_3.setText(_translate("MainWindow", "%"))
        self.pushButton_4.setText(_translate("MainWindow", "DEL"))
        self.pushButton_5.setText(_translate("MainWindow", "7"))
        self.pushButton_6.setText(_translate("MainWindow", "8"))
        self.pushButton_7.setText(_translate("MainWindow", "9"))
        self.pushButton_8.setText(_translate("MainWindow", "÷"))
        self.pushButton_9.setText(_translate("MainWindow", "4"))
        self.pushButton_10.setText(_translate("MainWindow", "5"))
        self.pushButton_11.setText(_translate("MainWindow", "6"))
        self.pushButton_12.setText(_translate("MainWindow", "x"))
        self.pushButton_13.setText(_translate("MainWindow", "1"))
        self.pushButton_14.setText(_translate("MainWindow", "2"))
        self.pushButton_15.setText(_translate("MainWindow", "3"))
        self.pushButton_16.setText(_translate("MainWindow", "-"))
        self.pushButton_17.setText(_translate("MainWindow", "0"))
        self.pushButton_18.setText(_translate("MainWindow", "."))
        self.pushButton_19.setText(_translate("MainWindow", "="))
        self.pushButton_20.setText(_translate("MainWindow", "+"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())