from PyQt5 import QtCore, QtGui, QtWidgets
import os
from PyPDF3 import PdfFileReader, PdfFileMerger

def checkEncryption(filename):
    obj = PdfFileReader(filename)
    global trueFalse
    trueFalse = obj.getIsEncrypted()
    return trueFalse

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(506, 427)
        MainWindow.setMinimumSize(QtCore.QSize(506, 427))
        MainWindow.setMaximumSize(QtCore.QSize(506, 427))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 491, 51))
        self.label.setStyleSheet("QLabel{font-size:40px;font-family:\'Times New Roman\', cursive;color:white;background-color:#000;border-radius:20px;}")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget,clicked=self.extractFromFolder)
        self.pushButton.setGeometry(QtCore.QRect(10, 80, 241, 51))
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setStyleSheet("QPushButton{font-size:20px;font-family:\'Times New Roman\', cursive;color:white;background-color:#000;border-radius:20px;}QPushButton:hover{background-color:crimson;color:gold;font-weight:bold;}")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget,clicked=self.selectFiles)
        self.pushButton_2.setGeometry(QtCore.QRect(270, 80, 231, 51))
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_2.setStyleSheet("QPushButton{font-size:20px;font-family:\'Times New Roman\', cursive;color:white;background-color:#000;border-radius:20px;}QPushButton:hover{background-color:crimson;color:gold;font-weight:bold;}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 150, 221, 201))
        self.groupBox.setStyleSheet("border:2px solid #000;")
        self.groupBox.setObjectName("groupBox")
        self.listWidget = QtWidgets.QListWidget(self.groupBox)
        self.listWidget.setGeometry(QtCore.QRect(10, 20, 201, 171))
        self.listWidget.setStyleSheet("border:0;")
        self.listWidget.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.listWidget.setObjectName("listWidget")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(290, 150, 211, 201))
        self.groupBox_2.setStyleSheet("border:2px solid #000;")
        self.groupBox_2.setObjectName("groupBox_2")
        self.listWidget_2 = QtWidgets.QListWidget(self.groupBox_2)
        self.listWidget_2.setGeometry(QtCore.QRect(10, 20, 191, 171))
        self.listWidget_2.setStyleSheet("border:0;")
        self.listWidget_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.listWidget_2.setObjectName("listWidget_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget,clicked=self.mergePDFFile)
        self.pushButton_3.setGeometry(QtCore.QRect(10, 360, 491, 51))
        self.pushButton_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_3.setStyleSheet("QPushButton{font-size:20px;font-family:\'Times New Roman\', cursive;color:white;background-color:#000;border-radius:20px;}QPushButton:hover{background-color:crimson;color:gold;font-weight:bold;}")
        self.pushButton_3.setObjectName("pushButton_3")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(240, 170, 41, 41))
        self.label_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("transferFileIcon.png"))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(240, 300, 41, 41))
        self.label_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("backupFileIcon.png"))
        self.label_3.setObjectName("label_3")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.mainPDFDictionary = {}
        self.mergePDFDictionary = {}
        self.label_2.mousePressEvent=self.transferFile
        self.label_3.mousePressEvent=self.reverseTransferFile

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "PDF Merger"))
        self.label.setText(_translate("MainWindow", "PDF MERGER"))
        self.pushButton.setText(_translate("MainWindow", "Select folder"))
        self.pushButton_2.setText(_translate("MainWindow", "Select multiple PDF Files"))
        self.groupBox.setTitle(_translate("MainWindow", "Files Found"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Files to be merged"))
        self.pushButton_3.setText(_translate("MainWindow", "Merge"))

    def selectFiles(self):
        listPdfFiles = QtWidgets.QFileDialog.getOpenFileNames(None,'Select PDF Files','/','PDF (*.pdf)')

        if listPdfFiles[0]!=[]:
            for i in listPdfFiles[0]:
                checkEncryption(i)
                if trueFalse==False:
                    self.listWidget.addItem(i.split('/')[-1])
                    self.mainPDFDictionary[i.split('/')[-1]]=i

    def extractFromFolder(self):
        pdfInsideFolderListPath = QtWidgets.QFileDialog.getExistingDirectory(None,'Select folder which contains PDF','/')

        if pdfInsideFolderListPath!='':
            for i in os.listdir(pdfInsideFolderListPath):
                if i.endswith('.pdf'):
                    checkEncryption(pdfInsideFolderListPath+'/'+str(i))
                    if trueFalse==False:
                        self.listWidget.addItem(str(i))
                        self.mainPDFDictionary[str(i)]=pdfInsideFolderListPath+'/'+str(i)
    
    def transferFile(self,e):
        try:
            transferFileName = self.listWidget.currentIndex().data()
            curr_selected=self.listWidget.currentRow()
            self.listWidget.takeItem(curr_selected)

            self.listWidget_2.addItem(transferFileName)
            self.mergePDFDictionary[transferFileName]=self.mainPDFDictionary.pop(transferFileName)
        except KeyError:
            pass

    def reverseTransferFile(self,e):
        try:
            transferFileName = self.listWidget_2.currentIndex().data()
            curr_selected=self.listWidget_2.currentRow()
            self.listWidget_2.takeItem(curr_selected)

            self.listWidget.addItem(transferFileName)
            self.mainPDFDictionary[transferFileName]=self.mergePDFDictionary.pop(transferFileName)
        except KeyError:
            pass
    
    def mergePDFFile(self):
        try:
            if self.mergePDFDictionary!={}:
                saveFileName = QtWidgets.QFileDialog.getSaveFileName(None,'Save As','/','PDF (*.pdf)')
                if saveFileName[0]:
                    merger = PdfFileMerger()
                    [merger.append(self.mergePDFDictionary[i]) for i in self.mergePDFDictionary]
                    merger.write(saveFileName[0])
                    merger.close()

                    self.listWidget.clear()
                    self.listWidget_2.clear()
                    self.mainPDFDictionary={}
                    self.mergePDFDictionary={}
            else:
                QtWidgets.QMessageBox.information(None,'!-Error-!','Oops!, No files found to be merged.',QtWidgets.QMessageBox.StandardButton(1),QtWidgets.QMessageBox.StandardButton(1))
        except KeyError:
            pass


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())