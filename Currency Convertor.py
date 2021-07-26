from openexchangerate import OpenExchangeRates
client=OpenExchangeRates(api_key='522e7989e9f64eb1ba21a035674dc275')
currency_name=client.currencies()[0]
currency_value=client.latest()[0]
try:
    currency_name.pop('VEF')
except:
    pass
A=[]
for i in currency_name:
    A.append([currency_name[i],currency_value[i]])
A.sort()
data_dict={}
for i in A:
    data_dict[i[0]]=i[1]

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(705, 352)
        MainWindow.setMinimumSize(QtCore.QSize(705, 352))
        MainWindow.setMaximumSize(QtCore.QSize(705, 352))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.logoImage = QtWidgets.QLabel(self.centralwidget)
        self.logoImage.setGeometry(QtCore.QRect(0, 0, 300, 344))
        self.logoImage.setText("")
        self.logoImage.setPixmap(QtGui.QPixmap("UI FILE\\../money_ex.png"))
        self.logoImage.setObjectName("logoImage")
        self.fromCurrencyCombo = QtWidgets.QComboBox(self.centralwidget)
        self.fromCurrencyCombo.setGeometry(QtCore.QRect(320, 10, 371, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.fromCurrencyCombo.setFont(font)
        self.fromCurrencyCombo.setObjectName("fromCurrencyCombo")
        self.fromCurrencyEntry = QtWidgets.QLineEdit(self.centralwidget)
        self.fromCurrencyEntry.setGeometry(QtCore.QRect(320, 190, 371, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.fromCurrencyEntry.setFont(font)
        self.fromCurrencyEntry.textChanged.connect(self.calculate)
        self.fromCurrencyEntry.setObjectName("fromCurrencyEntry")
        self.toCurrencyCombo = QtWidgets.QComboBox(self.centralwidget)
        self.toCurrencyCombo.setGeometry(QtCore.QRect(320, 120, 371, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.toCurrencyCombo.setFont(font)
        self.toCurrencyCombo.setObjectName("toCurrencyCombo")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(320, 170, 371, 16))
        self.line.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line.setLineWidth(3)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setObjectName("line")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setGeometry(QtCore.QRect(320, 250, 371, 91))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.plainTextEdit.setFont(font)
        self.plainTextEdit.setReadOnly(True)
        self.plainTextEdit.setPlainText("")
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.toLabel = QtWidgets.QLabel(self.centralwidget)
        self.toLabel.setGeometry(QtCore.QRect(320, 60, 371, 51))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.toLabel.setFont(font)
        self.toLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.toLabel.setObjectName("toLabel")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.fromCurrencyCombo.addItems([i for i in data_dict])
        self.toCurrencyCombo.addItems([i for i in data_dict])
        self.fromCurrencyCombo.currentTextChanged.connect(self.from_curr)
        self.toCurrencyCombo.currentTextChanged.connect(self.to_curr)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Currency Convertor"))
        self.fromCurrencyEntry.setPlaceholderText(_translate("MainWindow", "Enter amount..."))
        self.toLabel.setText(_translate("MainWindow", "TO"))

    def calculate(self):
        try:
            calculated_amount=(data_dict[self.toCurrencyCombo.currentText()]*float(self.fromCurrencyEntry.text()))/data_dict[self.fromCurrencyCombo.currentText()]
            calculated_amount=round(calculated_amount,5)
            self.plainTextEdit.setPlainText(f'{self.fromCurrencyCombo.currentText()} {self.fromCurrencyEntry.text()} equals {calculated_amount} {self.toCurrencyCombo.currentText()}')
        except:
            self.plainTextEdit.setPlainText('')
    
    def from_curr(self):
        self.calculatee()
    
    def to_curr(self):
        self.calculatee()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())