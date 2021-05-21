# Importing Needed Libraries
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QFileDialog, QComboBox, QFontComboBox
import os

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(690, 598)
        MainWindow.setMinimumSize(QtCore.QSize(690, 598))
        MainWindow.setMaximumSize(QtCore.QSize(690, 598))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(10, 40, 671, 531))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        self.textEdit.setFont(font)
        self.textEdit.setObjectName("textEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget,clicked=lambda:self.openit())
        self.pushButton.setGeometry(QtCore.QRect(10, 10, 91, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget,clicked=lambda:self.saveit())
        self.pushButton_2.setGeometry(QtCore.QRect(110, 10, 91, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget,clicked=lambda:self.undo())
        self.pushButton_3.setGeometry(QtCore.QRect(210, 10, 91, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget,clicked=lambda:self.redo())
        self.pushButton_4.setGeometry(QtCore.QRect(310, 10, 91, 23))
        self.pushButton_4.setObjectName("pushButton_4")
        self.sizecomboBox = QComboBox(self.centralwidget)
        self.sizecomboBox.setGeometry(QtCore.QRect(410, 10, 91, 23))
        self.sizecomboBox.setObjectName('sizecomboBox')
        self.fontstylecomboBox = QFontComboBox(self.centralwidget)
        self.fontstylecomboBox.setGeometry(QtCore.QRect(510, 10, 120, 23))
        self.fontstylecomboBox.setObjectName('fontstylecomboBox')
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget,clicked=lambda:self.wrap_unwrap())
        self.pushButton_5.setGeometry(QtCore.QRect(635,10,50,23))
        self.pushButton_5.setObjectName('pushButton_5')
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        # Sets the range of sizes for text
        self.sizecomboBox.addItems([f'{i}' for i in range(1,101)])
        self.sizecomboBox.setCurrentText('16')
        self.sizecomboBox.currentTextChanged.connect(self.changefontsize)

        # Sets the names of text styles
        self.fontstylecomboBox.setEditable(False)
        self.fontstylecomboBox.setCurrentText('Times New Roman')
        self.fontstylecomboBox.currentTextChanged.connect(self.changefontstyle)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    # Wrap_Unwrap Text
    def wrap_unwrap(self):
        if self.pushButton_5.text()=='Unwrap':
            self.textEdit.setLineWrapMode(False)
            self.pushButton_5.setText('Wrap')
        else:
            self.textEdit.setLineWrapMode(True)
            self.pushButton_5.setText('Unwrap')

    # Define changefontstyle
    def changefontstyle(self):
        fontsize=int(self.sizecomboBox.currentText())
        font = QtGui.QFont()
        font.setFamily(self.fontstylecomboBox.currentText())
        font.setPointSize(fontsize)
        self.textEdit.setFont(font)

    # Define changefontsize
    def changefontsize(self):
        fontsize=int(self.sizecomboBox.currentText())
        font = QtGui.QFont()
        font.setFamily(self.fontstylecomboBox.currentText())
        font.setPointSize(fontsize)
        self.textEdit.setFont(font)

    # Define Redo
    def redo(self):
        self.textEdit.redo()

    # Define Undo
    def undo(self):
        self.textEdit.undo()

    # Define openit - Helps to open existing text file(s)
    def openit(self):
        dirs=QFileDialog.getOpenFileName(None,'Open File','/','Text Files (*.txt)')

        filename=dirs[0]
        if filename:
            self.textEdit.clear()

            f=open(filename,'r')
            data=f.read()
            f.close()

            self.textEdit.setText(data)

    # Define saveit - Helps to save text file(s)
    file_exists=''
    def saveit(self):
        global file_exists
        s=str(self.textEdit.toPlainText())
        if s:

            try:
                os.path.exists(self.file_exists)

                f=open(self.file_exists,'w')
                f.write(s)
                f.close()

                msg=QMessageBox()
                msg.setWindowTitle('Saved!')
                msg.setText('Your file has been saved.')
                msg.setIcon(QMessageBox.Information)
                msg.exec_()

            except:
                filename=QFileDialog.getSaveFileName(None,'Save File','/','Text Files (*.txt)')
                if filename[0]:

                    f=open(filename[0],'w')
                    f.write(s)
                    f.close()

                    msg=QMessageBox()
                    msg.setWindowTitle('Saved!')
                    msg.setText('Your file has been saved.')
                    msg.setIcon(QMessageBox.Information)
                    msg.exec_()

                    filenameonly=filename[0].split('/')[-1]

                    MainWindow.setWindowTitle('PyQt5 NotePad - {}'.format(filenameonly))
                    self.file_exists=filename[0]

                else:
                    msg=QMessageBox()
                    msg.setWindowTitle('Not Saved!')
                    msg.setText('File Name Not Provided.')
                    msg.setIcon(QMessageBox.Critical)
                    msg.exec_()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "PyQt5 NotePad"))
        self.pushButton.setText(_translate("MainWindow", "Open"))
        self.pushButton_2.setText(_translate("MainWindow", "Save"))
        self.pushButton_3.setText(_translate("MainWindow", "Undo"))
        self.pushButton_4.setText(_translate("MainWindow", "Redo"))
        self.pushButton_5.setText(_translate("MainWindow", "Unwrap"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())