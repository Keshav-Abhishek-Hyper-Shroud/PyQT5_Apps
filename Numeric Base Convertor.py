from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(521, 353)
        MainWindow.setMinimumSize(QtCore.QSize(521, 353))
        MainWindow.setMaximumSize(QtCore.QSize(521, 353))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.title1 = QtWidgets.QLabel(self.centralwidget)
        self.title1.setGeometry(QtCore.QRect(30, 10, 216, 87))
        font = QtGui.QFont()
        font.setFamily("Vani")
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.title1.setFont(font)
        self.title1.setObjectName("title1")
        self.title2 = QtWidgets.QLabel(self.centralwidget)
        self.title2.setGeometry(QtCore.QRect(110, 60, 381, 87))
        font = QtGui.QFont()
        font.setFamily("Vani")
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.title2.setFont(font)
        self.title2.setObjectName("title2")
        self.sep1 = QtWidgets.QFrame(self.centralwidget)
        self.sep1.setGeometry(QtCore.QRect(0, 120, 521, 20))
        self.sep1.setFrameShadow(QtWidgets.QFrame.Plain)
        self.sep1.setFrameShape(QtWidgets.QFrame.HLine)
        self.sep1.setObjectName("sep1")
        self.basesComboBox = QtWidgets.QComboBox(self.centralwidget)
        self.basesComboBox.setGeometry(QtCore.QRect(40, 170, 201, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.basesComboBox.setFont(font)
        self.basesComboBox.setObjectName("basesComboBox")
        self.basesComboBox.addItem("")
        self.basesComboBox.addItem("")
        self.basesComboBox.addItem("")
        self.basesComboBox.addItem("")
        self.basesComboBox.addItem("")
        self.basesComboBox.addItem("")
        self.basesComboBox.addItem("")
        self.basesComboBox.addItem("")
        self.basesComboBox.addItem("")
        self.basesComboBox.addItem("")
        self.basesComboBox.addItem("")
        self.basesComboBox.addItem("")
        self.writeableFieldLabel = QtWidgets.QLabel(self.centralwidget)
        self.writeableFieldLabel.setGeometry(QtCore.QRect(40, 210, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.writeableFieldLabel.setFont(font)
        self.writeableFieldLabel.setObjectName("writeableFieldLabel")
        self.writeableEntry = QtWidgets.QLineEdit(self.centralwidget)
        self.writeableEntry.setGeometry(QtCore.QRect(40, 240, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.writeableEntry.setFont(font)
        self.writeableEntry.setText("")
        self.writeableEntry.setObjectName("writeableEntry")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(250, 210, 3, 61))
        self.line.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setObjectName("line")
        self.readableFieldLabel = QtWidgets.QLabel(self.centralwidget)
        self.readableFieldLabel.setGeometry(QtCore.QRect(260, 210, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.readableFieldLabel.setFont(font)
        self.readableFieldLabel.setObjectName("readableFieldLabel")
        self.readableEntry = QtWidgets.QLineEdit(self.centralwidget)
        self.readableEntry.setGeometry(QtCore.QRect(260, 240, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.readableEntry.setFont(font)
        self.readableEntry.setText("")
        self.readableEntry.setReadOnly(True)
        self.readableEntry.setObjectName("readableEntry")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget,clicked=lambda:self.startconversion())
        self.pushButton.setGeometry(QtCore.QRect(40, 290, 421, 31))
        font = QtGui.QFont()
        font.setFamily("Playball")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 521, 21))
        self.menubar.setObjectName("menubar")
        self.menuColor_Theme = QtWidgets.QMenu(self.menubar)
        self.menuColor_Theme.setObjectName("menuColor_Theme")
        MainWindow.setMenuBar(self.menubar)
        self.actionChoose_Color = QtWidgets.QAction(MainWindow)
        self.actionChoose_Color.setObjectName("actionChoose_Color")
        self.menuColor_Theme.addAction(self.actionChoose_Color)
        self.menubar.addAction(self.menuColor_Theme.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.basesComboBox.currentTextChanged.connect(self.comboBoxToggled)
        self.actionChoose_Color.triggered.connect(self.pickthemecolor)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Numeric Base Convertor"))
        self.title1.setText(_translate("MainWindow", "Numeric"))
        self.title2.setText(_translate("MainWindow", "Base Convertor"))
        self.basesComboBox.setItemText(0, _translate("MainWindow", "Dec to Bin"))
        self.basesComboBox.setItemText(1, _translate("MainWindow", "Dec to Oct"))
        self.basesComboBox.setItemText(2, _translate("MainWindow", "Dec to Hex"))
        self.basesComboBox.setItemText(3, _translate("MainWindow", "Bin to Dec"))
        self.basesComboBox.setItemText(4, _translate("MainWindow", "Bin to Oct"))
        self.basesComboBox.setItemText(5, _translate("MainWindow", "Bin to Hex"))
        self.basesComboBox.setItemText(6, _translate("MainWindow", "Oct to Dec"))
        self.basesComboBox.setItemText(7, _translate("MainWindow", "Oct to Bin"))
        self.basesComboBox.setItemText(8, _translate("MainWindow", "Oct to Hex"))
        self.basesComboBox.setItemText(9, _translate("MainWindow", "Hex to Dec"))
        self.basesComboBox.setItemText(10, _translate("MainWindow", "Hex to Bin"))
        self.basesComboBox.setItemText(11, _translate("MainWindow", "Hex to Oct"))
        self.writeableFieldLabel.setText(_translate("MainWindow", "Enter the Dec"))
        self.readableFieldLabel.setText(_translate("MainWindow", "Generated Bin"))
        self.pushButton.setText(_translate("MainWindow", "CONVERT"))
        self.menuColor_Theme.setTitle(_translate("MainWindow", "Color Theme"))
        self.actionChoose_Color.setText(_translate("MainWindow", "Choose Color"))
    
    def comboBoxToggled(self):
        condition=self.basesComboBox.currentText()
        condition=condition.split(' to ')
        self.writeableFieldLabel.setText(f'Enter the {condition[0]}')
        self.readableFieldLabel.setText(f'Generated {condition[1]}')

        self.readableEntry.setText('')
        self.writeableEntry.setText('')
    
    def startconversion(self):
        condition=self.basesComboBox.currentText()
        condition=condition.split(' to ')

        conversion_factor_dict={'Dec':10,'Bin':2,'Oct':8,'Hex':16}

        data=self.writeableEntry.text()
        data=data.lower()

        permission=True

        if condition[0]=='Bin' and '2' in data:
            msg=QtWidgets.QMessageBox()
            msg.setWindowTitle('Error!')
            msg.setText('Binary System accepts only 0 and 1')
            msg.setIcon(2)
            msg.exec_()
            permission=False
        
        elif condition[0]=='Oct' and '8' in data:
            msg=QtWidgets.QMessageBox()
            msg.setWindowTitle('Error!')
            msg.setText('Octal System accepts values from 0 and 7')
            msg.setIcon(2)
            msg.exec_()
            permission=False
        
        if permission==True:

            data_list=[]
            curr_position=0

            lengthofentry=len(data)

            for i in data:
                value=data[curr_position]

                if value=='a':
                    value=10
                if value=='b':
                    value=11
                if value=='c':
                    value=12
                if value=='d':
                    value=13
                if value=='e':
                    value=14
                if value=='f':
                    value=15

                data_list.append([int(value),conversion_factor_dict[condition[0]]**(lengthofentry-1)])
                curr_position+=1
                lengthofentry-=1
            
            int_value=0

            for i in data_list:
                int_value+=i[0]*i[1]
            
            if condition[1].lower()=='dec':
                to_set=f'{int_value}'
                self.readableEntry.setText(to_set)

            if condition[1].lower()=='bin':
                to_set=f'{bin(int_value)}'.replace('0b','')
                self.readableEntry.setText(to_set)

            if condition[1].lower()=='oct':
                to_set=f'{oct(int_value)}'.replace('0o','')
                self.readableEntry.setText(to_set)

            if condition[1].lower()=='hex':
                to_set=f'{hex(int_value)}'.replace('0x','')
                self.readableEntry.setText(to_set)
            
        permission=True
    
    def pickthemecolor(self):
        color=QtWidgets.QColorDialog()
        color_name=color.getColor().name()
        self.title1.setStyleSheet(f'color: {color_name};')
        self.title2.setStyleSheet(f'color: {color_name};')
        self.readableEntry.setStyleSheet(f'color: {color_name};')
        self.readableFieldLabel.setStyleSheet(f'color: {color_name};')
        self.writeableEntry.setStyleSheet(f'color: {color_name};')
        self.writeableFieldLabel.setStyleSheet(f'color: {color_name};')
        self.pushButton.setStyleSheet(f'color: {color_name};')
        self.basesComboBox.setStyleSheet(f'color: {color_name};')

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())