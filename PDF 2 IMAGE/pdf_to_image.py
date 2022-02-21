from PyQt5 import QtCore, QtGui, QtWidgets
import pdf2image
import pikepdf
import os

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(671, 404)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        MainWindow.setFont(font)
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        MainWindow.setFocusPolicy(QtCore.Qt.NoFocus)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.appTitle = QtWidgets.QLabel(self.centralwidget)
        self.appTitle.setGeometry(QtCore.QRect(10, 10, 651, 91))
        font = QtGui.QFont()
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.appTitle.setFont(font)
        self.appTitle.setStyleSheet("QLabel{color:gold;background:crimson;border-radius:30px;}QLabel:hover{color:crimson;background:gold;}")
        self.appTitle.setAlignment(QtCore.Qt.AlignCenter)
        self.appTitle.setObjectName("appTitle")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 120, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.fileNameScreen = QtWidgets.QLineEdit(self.centralwidget)
        self.fileNameScreen.setGeometry(QtCore.QRect(112, 120, 441, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.fileNameScreen.setFont(font)
        self.fileNameScreen.setText("")
        self.fileNameScreen.setReadOnly(True)
        self.fileNameScreen.setObjectName("fileNameScreen")
        self.browsePDF = QtWidgets.QPushButton(self.centralwidget,clicked=self.browsePDFFile)
        self.browsePDF.setGeometry(QtCore.QRect(560, 120, 101, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.browsePDF.setFont(font)
        self.browsePDF.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.browsePDF.setStyleSheet("QPushButton{color:white;background:green;border-radius:15px;font-weight:bold;}QPushButton:hover{background:white;color:green;}")
        self.browsePDF.setObjectName("browsePDF")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 170, 651, 161))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox.setFont(font)
        self.groupBox.setStyleSheet("QGroupBox{color:red;}")
        self.groupBox.setObjectName("groupBox")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(30, 40, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.passwordEntry = QtWidgets.QLineEdit(self.groupBox)
        self.passwordEntry.setGeometry(QtCore.QRect(180, 40, 421, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.passwordEntry.setFont(font)
        self.passwordEntry.setText("")
        self.passwordEntry.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passwordEntry.setAlignment(QtCore.Qt.AlignCenter)
        self.passwordEntry.setObjectName("passwordEntry")
        self.verifyPassword = QtWidgets.QPushButton(self.groupBox,clicked=self.verifyPasswordFunction)
        self.verifyPassword.setGeometry(QtCore.QRect(30, 90, 591, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.verifyPassword.setFont(font)
        self.verifyPassword.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.verifyPassword.setStyleSheet("QPushButton{color:white;background:green;border-radius:15px;font-weight:bold;}QPushButton:hover{background:white;color:green;}")
        self.verifyPassword.setObjectName("verifyPassword")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(606, 40, 31, 31))
        self.label_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.label_3.setMouseTracking(True)
        self.label_3.enterEvent=self.changeMeIn
        self.label_3.leaveEvent=self.changeMeOut
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("pdf2image_securityImage/unlock.png"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.convertP2IButton = QtWidgets.QPushButton(self.centralwidget,clicked=self.convertPDF2IMAGE)
        self.convertP2IButton.setGeometry(QtCore.QRect(90, 350, 491, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.convertP2IButton.setFont(font)
        self.convertP2IButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.convertP2IButton.setStyleSheet("QPushButton{color:white;background:green;border-radius:15px;font-weight:bold;}QPushButton:hover{background:yellowgreen;color:green;}")
        self.convertP2IButton.setObjectName("convertP2IButton")
        MainWindow.setCentralWidget(self.centralwidget)

        self.fileName = ''
        self.attempts = 3

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    
    def changeMeIn(self,e):
        self.label_3.setPixmap(QtGui.QPixmap("pdf2image_securityImage/lock.png"))
        self.passwordEntry.setEchoMode(0)

    def changeMeOut(self,e):
        self.label_3.setPixmap(QtGui.QPixmap("pdf2image_securityImage/unlock.png"))
        self.passwordEntry.setEchoMode(2)
	
    def verifyPasswordFunction(self):
        if self.fileName!='' and self.passwordEntry.text()!='' and self.attempts>=0:
            try:
                pikepdf.open(filename_or_stream=self.fileName,password=self.passwordEntry.text())
                self.verifyPassword.setText('Verified...')
                self.verifyPassword.setDisabled(True)
                self.browsePDF.setDisabled(True)
                self.passwordEntry.setDisabled(True)
            except:
                errorMsg = QtWidgets.QMessageBox.critical(None,'Access Denied!',f'Password did not matched. {self.attempts} attempts remains.')
                self.attempts-=1


    def browsePDFFile(self):
        self.fileName,typeOf = QtWidgets.QFileDialog.getOpenFileName(None,'Select a PDF File','/','PDF File (*.pdf)')
        self.fileNameScreen.setText(self.fileName.split('/')[-1])

    def convertPDF2IMAGE(self):
        self.convertP2IButton.setText('Converting...')
        full_path = self.fileName.split('/')
        full_path.pop()
        full_path = '/'.join(full_path)
        otpt_folder = full_path+'/'+self.fileNameScreen.text().split('.')[0]
        try:
            os.makedirs(otpt_folder)
        except:
            pass
        images = pdf2image.convert_from_path(self.fileName,output_folder=otpt_folder,poppler_path='poppler-0.68.0/bin',userpw=self.passwordEntry.text())
        for i,image in enumerate(images):
            image.save(otpt_folder+'/'+self.fileNameScreen.text().split('.')[0]+f' Page - {i+1}.png',"PNG")
        
        os.chdir(otpt_folder)
        os.system('rm *ppm')
        os.system('rm *pgm')
        self.convertP2IButton.setText('.Converted.')
        self.fileName=''
        self.attempts=3
        self.fileNameScreen.setText('')
        self.passwordEntry.setText('')
        self.verifyPassword.setText('Verify...')
        self.verifyPassword.setDisabled(False)
        self.browsePDF.setDisabled(False)
        self.passwordEntry.setDisabled(False)
        self.convertP2IButton.setText('Convert .pdf to .png')

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "PDF to Image"))
        self.appTitle.setText(_translate("MainWindow", "PDF to Image"))
        self.label.setText(_translate("MainWindow", "File name:"))
        self.fileNameScreen.setPlaceholderText(_translate("MainWindow", "File name will display here."))
        self.browsePDF.setText(_translate("MainWindow", "Browse"))
        self.groupBox.setTitle(_translate("MainWindow", "If file is password protected then only fill these field, else leave."))
        self.label_2.setText(_translate("MainWindow", "Enter password:"))
        self.passwordEntry.setPlaceholderText(_translate("MainWindow", "Enter password"))
        self.verifyPassword.setText(_translate("MainWindow", "Verify..."))
        self.convertP2IButton.setText(_translate("MainWindow", "Covert .pdf to .png"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())