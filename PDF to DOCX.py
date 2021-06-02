from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from pdf2docx import Converter,parse
from PyPDF3 import PdfFileReader
import os

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(334, 213)
        MainWindow.setMinimumSize(QtCore.QSize(334, 213))
        MainWindow.setMaximumSize(QtCore.QSize(334, 213))
        self.filename=''
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(60, 10, 211, 51))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setWordWrap(False)
        self.label.setIndent(10)
        self.label.setObjectName("label")
        self.browsePDF = QtWidgets.QPushButton(self.centralwidget,clicked=lambda:self.browse_PDF())
        self.browsePDF.setGeometry(QtCore.QRect(70, 70, 191, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.browsePDF.setFont(font)
        self.browsePDF.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.browsePDF.setObjectName("browsePDF")
        self.allowOpen = QtWidgets.QCheckBox(self.centralwidget)
        self.allowOpen.setGeometry(QtCore.QRect(70, 120, 191, 21))
        self.allowOpen.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.allowOpen.setCheckable(True)
        self.allowOpen.setTristate(False)
        self.allowOpen.setObjectName("allowOpen")
        self.convertPDF = QtWidgets.QPushButton(self.centralwidget,clicked=lambda:self.saveasdocx())
        self.convertPDF.setGeometry(QtCore.QRect(70, 150, 191, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.convertPDF.setFont(font)
        self.convertPDF.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.convertPDF.setCheckable(False)
        self.convertPDF.setObjectName("convertPDF")
        MainWindow.setCentralWidget(self.centralwidget)

        self.convertPDF.setDisabled(True)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def browse_PDF(self):
        try:
            global filename
            self.filename=QtWidgets.QFileDialog.getOpenFileName(None,'Select PDF File','/','PDF File (*.pdf)')

            if self.filename[0] and PdfFileReader(self.filename[0]).getIsEncrypted()==False:
                self.convertPDF.setDisabled(False)
            else:
                if PdfFileReader(self.filename[0]).getIsEncrypted()==False:
                    msg=QMessageBox()
                    msg.setWindowTitle('Error')
                    msg.setText('File curropted or encrypted.')
                    msg.setIcon(3)
                    msg.exec_()
        except:
            pass

    def saveasdocx(self):
        global filename
        
        converted_filename=self.filename[0].replace('.pdf','_converted.docx')

        parse(self.filename[0],converted_filename)

        if self.allowOpen.checkState():
            os.startfile(converted_filename)

            self.allowOpen.setCheckState(False)
            self.convertPDF.setDisabled(True)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "PDF to DOCX"))
        self.label.setText(_translate("MainWindow", "PDF to DOCX"))
        self.browsePDF.setText(_translate("MainWindow", "Browse PDF File"))
        self.allowOpen.setText(_translate("MainWindow", "Open After Conversion"))
        self.convertPDF.setText(_translate("MainWindow", "Convert"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())