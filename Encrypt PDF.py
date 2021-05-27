# Importing needed libraries
from PyQt5 import QtCore, QtGui, QtWidgets
from PyPDF3 import PdfFileReader, PdfFileWriter
from PyQt5.QtWidgets import QMessageBox

filename=''

class Ui_MainWindow(object):
	def setupUi(self, MainWindow):
		MainWindow.setObjectName("MainWindow")
		MainWindow.resize(440, 312)
		MainWindow.setMinimumSize(QtCore.QSize(440, 312))
		MainWindow.setMaximumSize(QtCore.QSize(440, 312))
		MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
		self.centralwidget = QtWidgets.QWidget(MainWindow)
		self.centralwidget.setObjectName("centralwidget")
		self.label = QtWidgets.QLabel(self.centralwidget)
		self.label.setGeometry(QtCore.QRect(80, 10, 271, 61))
		font = QtGui.QFont()
		font.setFamily("Times New Roman")
		font.setPointSize(36)
		font.setBold(True)
		font.setWeight(75)
		self.label.setFont(font)
		self.label.setWordWrap(False)
		self.label.setStyleSheet('background:yellow;color:red')
		self.label.setObjectName("label")
		self.label_2 = QtWidgets.QLabel(self.centralwidget)
		self.label_2.setGeometry(QtCore.QRect(10, 140, 201, 41))
		font = QtGui.QFont()
		font.setFamily("Times New Roman")
		font.setPointSize(20)
		font.setBold(True)
		font.setWeight(75)
		self.label_2.setFont(font)
		self.label_2.setObjectName("label_2")
		self.label_3 = QtWidgets.QLabel(self.centralwidget)
		self.label_3.setGeometry(QtCore.QRect(10, 180, 201, 51))
		font = QtGui.QFont()
		font.setFamily("Times New Roman")
		font.setPointSize(20)
		font.setBold(True)
		font.setWeight(75)
		self.label_3.setFont(font)
		self.label_3.setObjectName("label_3")
		self.browsePDF = QtWidgets.QPushButton(self.centralwidget,clicked=lambda:self.browse_PDF())
		self.browsePDF.setGeometry(QtCore.QRect(130, 80, 171, 41))
		font = QtGui.QFont()
		font.setFamily("Times New Roman")
		font.setPointSize(20)
		font.setBold(True)
		font.setWeight(75)
		self.browsePDF.setFont(font)
		self.browsePDF.setFocus(True)
		self.browsePDF.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
		self.browsePDF.setFlat(False)
		self.browsePDF.setObjectName("browsePDF")
		self.userPassword = QtWidgets.QLineEdit(self.centralwidget)
		self.userPassword.setGeometry(QtCore.QRect(220, 150, 191, 31))
		font = QtGui.QFont()
		font.setFamily("Times New Roman")
		font.setPointSize(14)
		font.setBold(True)
		font.setWeight(75)
		self.userPassword.setFont(font)
		self.userPassword.setStyleSheet('color:red;')
		self.userPassword.setEchoMode(2) # Refer PyQt5.QtWidgets.QtLineEdit (Documentation)
		self.userPassword.setObjectName("userPassword")
		self.ownerPassword = QtWidgets.QLineEdit(self.centralwidget)
		self.ownerPassword.setGeometry(QtCore.QRect(220, 190, 191, 31))
		font = QtGui.QFont()
		font.setFamily("Times New Roman")
		font.setPointSize(14)
		font.setBold(True)
		font.setWeight(75)
		self.ownerPassword.setFont(font)
		self.ownerPassword.setStyleSheet('color:red;')
		self.ownerPassword.setEchoMode(2) # Refer PyQt5.QtWidgets.QtLineEdit (Documentation)
		self.ownerPassword.setObjectName("ownerPassword")
		self.startEncryption = QtWidgets.QPushButton(self.centralwidget,clicked=lambda:self.start_Encryption())
		self.startEncryption.setGeometry(QtCore.QRect(10, 250, 411, 41))
		font = QtGui.QFont()
		font.setFamily("Times New Roman")
		font.setPointSize(14)
		font.setBold(True)
		font.setWeight(75)
		self.startEncryption.setFont(font)
		self.startEncryption.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
		self.startEncryption.setObjectName("startEncryption")
		self.viewUserPassword = QtWidgets.QLabel(self.centralwidget)
		self.viewUserPassword.setGeometry(QtCore.QRect(420, 150, 20, 31))
		font = QtGui.QFont()
		font.setFamily("Times New Roman")
		font.setPointSize(15)
		font.setBold(True)
		font.setWeight(75)
		self.viewUserPassword.setFont(font)
		self.viewUserPassword.setStyleSheet('color:red;')
		self.viewUserPassword.enterEvent=self.viewUser
		self.viewUserPassword.leaveEvent=self.hideUser
		self.viewUserPassword.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
		self.viewUserPassword.setObjectName("viewUserPassword")
		self.viewOwnerPassword = QtWidgets.QLabel(self.centralwidget)
		self.viewOwnerPassword.setGeometry(QtCore.QRect(420, 190, 20, 31))
		font = QtGui.QFont()
		font.setFamily("Times New Roman")
		font.setPointSize(15)
		font.setBold(True)
		font.setWeight(75)
		self.viewOwnerPassword.setFont(font)
		self.viewOwnerPassword.setStyleSheet('color:red;')
		self.viewOwnerPassword.enterEvent=self.viewOwner
		self.viewOwnerPassword.leaveEvent=self.hideOwner
		self.viewOwnerPassword.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
		self.viewOwnerPassword.setObjectName("viewOwnerPassword")

		MainWindow.setCentralWidget(self.centralwidget)
		self.statusbar = QtWidgets.QStatusBar(MainWindow)
		self.statusbar.setObjectName("statusbar")
		MainWindow.setStatusBar(self.statusbar)

		self.userPassword.setDisabled(True)
		self.ownerPassword.setDisabled(True)
		self.startEncryption.setDisabled(True)

		self.retranslateUi(MainWindow)
		QtCore.QMetaObject.connectSlotsByName(MainWindow)
	
	# Shows User Password on hover
	def viewUser(self,event):
		self.userPassword.setEchoMode(0)
	
	# Shows Owner Password on hover
	def viewOwner(self,event):
		self.ownerPassword.setEchoMode(0)
	
	# Hides User Password on hover
	def hideUser(self,event):
		self.userPassword.setEchoMode(2)
	
	# Hides User Password on hover
	def hideOwner(self,event):
		self.ownerPassword.setEchoMode(2)

	# Browse PDF File
	def browse_PDF(self):
		global filename
		self.filename=QtWidgets.QFileDialog.getOpenFileName(None,'Select PDF File','/','PDF Files (*.pdf)')
		if self.filename[0]:
			self.userPassword.setDisabled(False)
			self.ownerPassword.setDisabled(False)
			self.startEncryption.setDisabled(False)

	# Start Encryption
	def start_Encryption(self):
		global filename

		try:

			if self.filename[0] and self.userPassword.text() and self.ownerPassword.text():

				pfw=PdfFileWriter()
				pdffile=PdfFileReader(self.filename[0])

				total_pages=pdffile.numPages

				for page in range(total_pages):
					current_page=pdffile.getPage(page)
					pfw.addPage(current_page)

				pfw.encrypt(self.userPassword.text(),self.ownerPassword.text())

				file=open(self.filename[0].replace('.pdf','_encrypted.pdf'),'wb')
				pfw.write(file)
				file.close()

				msg=QMessageBox()
				msg.setWindowTitle('Done')
				msg.setIcon(QMessageBox.Information)
				msg.setText('File encryption done successfully.')
				msg.exec_()

				self.filename=''

				self.userPassword.setText('')
				self.ownerPassword.setText('')
				self.userPassword.setDisabled(True)
				self.ownerPassword.setDisabled(True)
				self.startEncryption.setDisabled(True)

			else:
				if self.ownerPassword.text()=='':
					msg=QMessageBox()
					msg.setWindowTitle('Error')
					msg.setIcon(QMessageBox.Critical)
					msg.setText('Owner Password Field is Empty.')
					msg.exec_()
				
				if self.userPassword.text()=='':
					msg=QMessageBox()
					msg.setWindowTitle('Error')
					msg.setIcon(QMessageBox.Critical)
					msg.setText('User Password Field is Empty.')
					msg.exec_()
		except:
			pass

	def retranslateUi(self, MainWindow):
		_translate = QtCore.QCoreApplication.translate
		MainWindow.setWindowTitle(_translate("MainWindow", "PDF File Encrypter"))
		self.label.setText(_translate("MainWindow", "Encrypt PDF"))
		self.label_2.setText(_translate("MainWindow", "User Password"))
		self.label_3.setText(_translate("MainWindow", "Owner Password"))
		self.browsePDF.setText(_translate("MainWindow", "Browse PDF"))
		self.startEncryption.setText(_translate("MainWindow", "Start Encryption"))
		self.viewUserPassword.setText(_translate("MianWindow", "i"))
		self.viewOwnerPassword.setText(_translate("MianWindow", "i"))

if __name__ == "__main__":
	import sys
	app = QtWidgets.QApplication(sys.argv)
	MainWindow = QtWidgets.QMainWindow()
	ui = Ui_MainWindow()
	ui.setupUi(MainWindow)
	MainWindow.show()
	sys.exit(app.exec_())
