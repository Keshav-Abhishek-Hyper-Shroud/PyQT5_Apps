# Importing needed libraries
from PyQt5 import QtCore, QtGui, QtWidgets
from PyPDF3 import PdfFileReader, PdfFileWriter
from PyQt5.QtWidgets import QMessageBox

filename=''

class Ui_MainWindow(object):
	def setupUi(self, MainWindow):
		MainWindow.setObjectName("MainWindow")
		MainWindow.resize(432, 312)
		MainWindow.setMinimumSize(QtCore.QSize(432, 312))
		MainWindow.setMaximumSize(QtCore.QSize(432, 312))
		MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
		MainWindow.setFocusPolicy(QtCore.Qt.StrongFocus)
		MainWindow.setAnimated(True)
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
		self.browsePDF.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
		self.browsePDF.setFocusPolicy(QtCore.Qt.StrongFocus)
		self.browsePDF.setAutoDefault(False)
		self.browsePDF.setDefault(False)
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
		self.userPassword.setText("")
		self.userPassword.setDragEnabled(False)
		self.userPassword.setObjectName("userPassword")
		self.ownerPassword = QtWidgets.QLineEdit(self.centralwidget)
		self.ownerPassword.setGeometry(QtCore.QRect(220, 190, 191, 31))
		font = QtGui.QFont()
		font.setFamily("Times New Roman")
		font.setPointSize(14)
		font.setBold(True)
		font.setWeight(75)
		self.ownerPassword.setFont(font)
		self.ownerPassword.setDragEnabled(False)
		self.ownerPassword.setReadOnly(False)
		self.ownerPassword.setObjectName("ownerPassword")
		self.line = QtWidgets.QFrame(self.centralwidget)
		self.line.setGeometry(QtCore.QRect(0, 115, 431, 31))
		self.line.setFrameShadow(QtWidgets.QFrame.Plain)
		self.line.setLineWidth(2)
		self.line.setFrameShape(QtWidgets.QFrame.HLine)
		self.line.setObjectName("line")
		self.startEncryption = QtWidgets.QPushButton(self.centralwidget,clicked=lambda:self.start_Encryption())
		self.startEncryption.setGeometry(QtCore.QRect(10, 250, 411, 41))
		font = QtGui.QFont()
		font.setFamily("Times New Roman")
		font.setPointSize(14)
		font.setBold(True)
		font.setWeight(75)
		self.startEncryption.setFont(font)
		self.startEncryption.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
		self.startEncryption.setFlat(False)
		self.startEncryption.setObjectName("startEncryption")
		self.line_2 = QtWidgets.QFrame(self.centralwidget)
		self.line_2.setGeometry(QtCore.QRect(0, 220, 431, 41))
		self.line_2.setFrameShadow(QtWidgets.QFrame.Plain)
		self.line_2.setLineWidth(2)
		self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
		self.line_2.setObjectName("line_2")
		MainWindow.setCentralWidget(self.centralwidget)
		self.statusbar = QtWidgets.QStatusBar(MainWindow)
		self.statusbar.setObjectName("statusbar")
		MainWindow.setStatusBar(self.statusbar)

		self.retranslateUi(MainWindow)
		QtCore.QMetaObject.connectSlotsByName(MainWindow)

	# Browse PDF File
	def browse_PDF(self):
		global filename
		self.filename=QtWidgets.QFileDialog.getOpenFileName(None,'Select PDF File','/','PDF Files (*.pdf)')

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


if __name__ == "__main__":
	import sys
	app = QtWidgets.QApplication(sys.argv)
	MainWindow = QtWidgets.QMainWindow()
	ui = Ui_MainWindow()
	ui.setupUi(MainWindow)
	MainWindow.show()
	sys.exit(app.exec_())