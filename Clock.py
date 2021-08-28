from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QPushButton, QLineEdit, QColorDialog, QFontDialog
from PyQt5 import QtCore, QtGui
from PyQt5 import uic
import sys
from time import strftime

class UI(QMainWindow):
	def __init__(self):
		super(UI,self).__init__()

		# For filenamed 'CLOCK.ui' goto "https://github.com/Keshav-Abhishek-Hyper-Shroud/PyQT5_Apps/blob/master/CLOCK.ui"
		uic.loadUi('CLOCK.ui',self)
		self.show()

		self.setFixedSize(411,191)

		self.bgcolor='none'
		self.fgcolor='black'
		self.bg_fg=''
		self.fontFamily='Times New Roman'

		self.screen=self.findChild(QLabel,'screen')

		self.fgButton=self.findChild(QPushButton,'changeFG')
		self.fgButton.clicked.connect(lambda:self.themeapplyer('fg'))
		self.fgButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

		self.bgButton=self.findChild(QPushButton,'changeBG')
		self.bgButton.clicked.connect(lambda:self.themeapplyer('bg'))
		self.bgButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

		self.colorEntry=self.findChild(QLineEdit,'colorEntry')
		self.colorEntry.setReadOnly(True)

		self.apply=self.findChild(QPushButton,'applyTheme')
		self.apply.setDisabled(True)
		self.apply.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
		self.apply.clicked.connect(self.applyit)

		self.fontEntry=self.findChild(QLineEdit,'fontEntry')
		self.fontEntry.setReadOnly(True)

		self.fontStyleButton=self.findChild(QPushButton,'fontStyleButton')
		self.fontStyleButton.clicked.connect(self.applyfontstyle)
		self.fontStyleButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

		self.applyFont=self.findChild(QPushButton,'applyFont')
		self.applyFont.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
		self.applyFont.setDisabled(True)
		self.applyFont.clicked.connect(self.applyit)

		self.updateclock()

	def updateclock(self):
		self.screen.setText(strftime('%I:%M:%S %p'))
		QtCore.QTimer.singleShot(1000,self.updateclock)

	def themeapplyer(self,options):
		# self.resize(411,191)
		self.apply.setDisabled(False)
		self.bg_fg=options
		self.setFixedSize(411,227)
		colour=QColorDialog.getColor()
		self.colorEntry.setText(colour.name())

	def applyit(self):
		if self.bg_fg=='fg' and self.colorEntry.text()!='':
			self.fgcolor=self.colorEntry.text()
		elif self.bg_fg=='bg' and self.colorEntry.text()!='':
			self.bgcolor=self.colorEntry.text()

		if self.fontEntry.text()!='':
			self.fontFamily=self.fontEntry.text()
			self.screen.setStyleSheet('color:'+self.fgcolor+';'+'background-color:'+self.bgcolor+';'+f'font-family:{self.fontFamily};')
		else:
			self.screen.setStyleSheet('color:'+self.fgcolor+';'+'background-color:'+self.bgcolor+';'+f'font-family:{self.fontFamily};')
		
		self.colorEntry.clear()
		self.fontEntry.clear()
		self.apply.setDisabled(True)
		self.applyFont.setDisabled(True)
		self.setFixedSize(411,191)
	
	def applyfontstyle(self):
		self.setFixedSize(411,272)
		self.applyFont.setDisabled(False)
		fontfam, ok=QFontDialog.getFont()
		if ok==False:
			self.fontEntry.setText(self.fontFamily)
		else:
			self.fontEntry.setText(fontfam.toString().split(',')[0])

app=QApplication(sys.argv)
window=UI()
app.exec_()