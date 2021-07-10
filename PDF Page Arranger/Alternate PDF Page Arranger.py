from PyQt5 import QtCore, QtGui, QtWidgets
from PyPDF3 import PdfFileReader,PdfFileWriter
import os
import pygame

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(661, 212)
        MainWindow.setMinimumSize(QtCore.QSize(661, 212))
        MainWindow.setMaximumSize(QtCore.QSize(661, 212))
        self.bothfile='*'
        self.permission=False
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.titleLabel = QtWidgets.QLabel(self.centralwidget)
        self.titleLabel.setGeometry(QtCore.QRect(30, 10, 601, 54))
        font = QtGui.QFont()
        font.setFamily("Algerian")
        font.setPointSize(28)
        self.titleLabel.setFont(font)
        self.titleLabel.setStyleSheet("color:red;")
        self.titleLabel.setObjectName("titleLabel")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(30, 50, 601, 16))
        self.line.setStyleSheet("color:red;")
        self.line.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line.setLineWidth(5)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setObjectName("line")
        self.oddFileLoad = QtWidgets.QPushButton(self.centralwidget,clicked=self.loadfile1)
        self.oddFileLoad.setGeometry(QtCore.QRect(30, 80, 75, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.oddFileLoad.setFont(font)
        self.oddFileLoad.setObjectName("oddFileLoad")
        self.oddFileLoadLabel = QtWidgets.QLabel(self.centralwidget)
        self.oddFileLoadLabel.setGeometry(QtCore.QRect(110, 80, 301, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.oddFileLoadLabel.setFont(font)
        self.oddFileLoadLabel.setObjectName("oddFileLoadLabel")
        self.evenFileLoad = QtWidgets.QPushButton(self.centralwidget,clicked=self.loadfile2)
        self.evenFileLoad.setGeometry(QtCore.QRect(30, 110, 75, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.evenFileLoad.setFont(font)
        self.evenFileLoad.setObjectName("evenFileLoad")
        self.evenFileLoadLabel = QtWidgets.QLabel(self.centralwidget)
        self.evenFileLoadLabel.setGeometry(QtCore.QRect(110, 110, 311, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.evenFileLoadLabel.setFont(font)
        self.evenFileLoadLabel.setObjectName("evenFileLoadLabel")
        self.arrangeThem = QtWidgets.QPushButton(self.centralwidget,clicked=self.arrangethem)
        self.arrangeThem.setGeometry(QtCore.QRect(30, 150, 601, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.arrangeThem.setFont(font)
        self.arrangeThem.setObjectName("arrangeThem")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 661, 21))
        self.menubar.setObjectName("menubar")
        self.menuOptions = QtWidgets.QMenu(self.menubar)
        self.menuOptions.setObjectName("menuOptions")
        MainWindow.setMenuBar(self.menubar)
        self.actionReset = QtWidgets.QAction(MainWindow)
        self.actionReset.setObjectName("actionReset")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.menuOptions.addAction(self.actionReset)
        self.menuOptions.addSeparator()
        self.menuOptions.addAction(self.actionExit)
        self.menubar.addAction(self.menuOptions.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        pygame.mixer.init()

        self.actionExit.triggered.connect(lambda:sys.exit())
        self.actionReset.triggered.connect(self.resetall)

        self.oddFileLoad.enterEvent=self.hoveroddbutton
        self.oddFileLoad.leaveEvent=self.dishoveroddbutton

        self.evenFileLoad.enterEvent=self.hoverevenbutton
        self.evenFileLoad.leaveEvent=self.dishoverevenbutton

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Alternate PDF Page Arranger"))
        self.titleLabel.setText(_translate("MainWindow", "Alternate PDF Page Arranger"))
        self.oddFileLoad.setText(_translate("MainWindow", "Load File"))
        self.oddFileLoadLabel.setText(_translate("MainWindow", "which contains pages numbered as 1, 3, 5, 7, 9, ...."))
        self.evenFileLoad.setText(_translate("MainWindow", "Load File"))
        self.evenFileLoadLabel.setText(_translate("MainWindow", "which contains pages numbered as 2, 4, 6, 8, 10, ...."))
        self.arrangeThem.setText(_translate("MainWindow", "ARRANGE"))
        self.menuOptions.setTitle(_translate("MainWindow", "Options"))
        self.actionReset.setText(_translate("MainWindow", "Reset"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
    
    def permit(self):
        if self.oddFileLoad.isEnabled()==False and self.evenFileLoad.isEnabled()==False:
            self.permission=True

    def loadfile1(self):
        pygame.mixer.music.load('MCS.mp3')
        pygame.mixer.music.play(loops=0)
        filename=QtWidgets.QFileDialog.getOpenFileName(None,'Select 1st PDF File','/','PDF File (*.pdf)')
        if filename[0]:
            self.bothfile=filename[0]+self.bothfile
            self.oddFileLoad.setDisabled(True)
            self.oddFileLoad.setText('1st File')
            self.oddFileLoadLabel.setText('Loaded Successfully...')

            self.permit()

    def loadfile2(self):
        pygame.mixer.music.load('MCS.mp3')
        pygame.mixer.music.play(loops=0)
        filename=QtWidgets.QFileDialog.getOpenFileName(None,'Select 2nd PDF File','/','PDF File (*.pdf)')
        if filename[0]:
            self.bothfile+=filename[0]
            self.evenFileLoad.setDisabled(True)
            self.evenFileLoad.setText('2nd File')
            self.evenFileLoadLabel.setText('Loaded Successfully...')

            self.permit()

    def arrangethem(self):
        if self.permission==True:
            saveto=QtWidgets.QFileDialog.getExistingDirectory()
            if saveto:
                try:
                    file1=PdfFileReader(self.bothfile.split('*')[0])
                    file2=PdfFileReader(self.bothfile.split('*')[1])

                    element1=[file1.getPage(i) for i in range(file1.numPages)]
                    element2=[file2.getPage(i) for i in range(file2.numPages)]

                    pdfwriter=PdfFileWriter()

                    j=0
                    while True:
                        try:
                            pdfwriter.addPage(element1[j])
                            pdfwriter.addPage(element2[j])
                            j+=1
                        except:
                            break
                    
                    f=open(saveto+'/'+self.bothfile.split('*')[0].replace('.pdf','').split('/').pop()+'_'+self.bothfile.split('*')[1].replace('.pdf','').split('/').pop()+'.pdf','wb')
                    pdfwriter.write(f)
                    f.close()

                    msg=QtWidgets.QMessageBox()
                    msg.setWindowTitle('Done!')
                    msg.setIcon(1)
                    msg.setText('Arranging the pages done.')
                    msg.exec_()

                    os.startfile(saveto+'/'+self.bothfile.split('*')[0].replace('.pdf','').split('/').pop()+'_'+self.bothfile.split('*')[1].replace('.pdf','').split('/').pop()+'.pdf')

                    self.bothfile=''

                    self.oddFileLoad.setDisabled(False)
                    self.oddFileLoad.setText('Load File')
                    self.oddFileLoadLabel.setText('which contains pages numbered as 1, 3, 5, 7, 9, ....')
                    
                    self.evenFileLoad.setDisabled(False)
                    self.evenFileLoad.setText('Load File')
                    self.evenFileLoadLabel.setText('which contains pages numbered as 2, 4, 6, 8, 10, ....')
                    
                    self.permission==False
                except:
                    msg=QtWidgets.QMessageBox()
                    msg.setWindowTitle('Error!')
                    msg.setIcon(3)
                    msg.setText('File(s) may be locked or corrupted.')
                    msg.exec_()

                    self.resetall()

    def resetall(self):
        self.bothfile=''

        self.oddFileLoad.setDisabled(False)
        self.oddFileLoad.setText('Load File')
        self.oddFileLoadLabel.setText('which contains pages numbered as 1, 3, 5, 7, 9, ....')
        
        self.evenFileLoad.setDisabled(False)
        self.evenFileLoad.setText('Load File')
        self.evenFileLoadLabel.setText('which contains pages numbered as 2, 4, 6, 8, 10, ....')

    def hoveroddbutton(self,e):
        if self.oddFileLoad.isEnabled()==True:
            self.oddFileLoad.setStyleSheet('background-color:yellow;')

    def dishoveroddbutton(self,e):
        self.oddFileLoad.setStyleSheet('background-color:none;')

    def hoverevenbutton(self,e):
        if self.evenFileLoad.isEnabled()==True:
            self.evenFileLoad.setStyleSheet('background-color:yellow;')

    def dishoverevenbutton(self,e):
        self.evenFileLoad.setStyleSheet('background-color:none;')

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
