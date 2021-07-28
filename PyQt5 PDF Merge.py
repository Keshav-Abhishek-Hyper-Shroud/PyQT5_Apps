from PyQt5 import QtCore, QtGui, QtWidgets
from PyPDF3 import PdfFileReader, PdfFileWriter
pfw=PdfFileWriter()
import os

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(582, 512)
        MainWindow.setMinimumSize(QtCore.QSize(582, 512))
        MainWindow.setMaximumSize(QtCore.QSize(582, 512))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 561, 391))
        self.tabWidget.setObjectName("tabWidget")
        self.CF = QtWidgets.QWidget()
        self.CF.setObjectName("CF")
        self.fileBox = QtWidgets.QComboBox(self.CF)
        self.fileBox.setGeometry(QtCore.QRect(10, 100, 541, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.fileBox.setFont(font)
        self.fileBox.setCurrentText("")
        self.fileBox.currentTextChanged.connect(self.onchange)
        self.fileBox.setObjectName("fileBox")
        self.chooseFolder = QtWidgets.QPushButton(self.CF,clicked=lambda:self.loadfile())
        self.chooseFolder.setGeometry(QtCore.QRect(10, 10, 541, 71))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.chooseFolder.setFont(font)
        self.chooseFolder.setStyleSheet("color:red;\nborder-radius:20px;\nbackground-color:yellow;\nborder:2px solid red;")
        self.chooseFolder.setObjectName("chooseFolder")
        self.tabWidget.addTab(self.CF, "")
        self.SA = QtWidgets.QWidget()
        self.SA.setObjectName("SA")
        self.fileNameSP = QtWidgets.QPlainTextEdit(self.SA)
        self.fileNameSP.setGeometry(QtCore.QRect(10, 10, 541, 51))
        self.fileNameSP.setReadOnly(True)
        self.fileNameSP.setPlainText("")
        self.fileNameSP.setObjectName("fileNameSP")
        self.SAButton = QtWidgets.QPushButton(self.SA,clicked=lambda:self.spbutton())
        self.SAButton.setGeometry(QtCore.QRect(10, 80, 540, 40))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.SAButton.setFont(font)
        self.SAButton.setObjectName("SAButton")
        self.tabWidget.addTab(self.SA, "")
        self.SR = QtWidgets.QWidget()
        self.SR.setObjectName("SR")
        self.fileNameSR = QtWidgets.QPlainTextEdit(self.SR)
        self.fileNameSR.setGeometry(QtCore.QRect(10, 10, 541, 51))
        self.fileNameSR.setReadOnly(True)
        self.fileNameSR.setObjectName("fileNameSR")
        self.SRListbox = QtWidgets.QListWidget(self.SR)
        self.SRListbox.setGeometry(QtCore.QRect(10, 80, 311, 271))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.SRListbox.setFont(font)
        self.SRListbox.currentTextChanged.connect(self.srlistbox)
        self.SRListbox.setObjectName("SRListbox")
        self.SRButton = QtWidgets.QPushButton(self.SR,clicked=lambda:self.srbutton())
        self.SRButton.setGeometry(QtCore.QRect(330, 80, 221, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.SRButton.setFont(font)
        self.SRButton.setObjectName("SRButton")
        self.popUpMessageLabel = QtWidgets.QLabel(self.SR)
        self.popUpMessageLabel.setGeometry(QtCore.QRect(330, 150, 221, 21))
        self.popUpMessageLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.popUpMessageLabel.setObjectName("popUpMessageLabel")
        self.tabWidget.addTab(self.SR, "")
        self.SRP = QtWidgets.QWidget()
        self.SRP.setObjectName("SRP")
        self.fileNameSRP = QtWidgets.QPlainTextEdit(self.SRP)
        self.fileNameSRP.setGeometry(QtCore.QRect(10, 10, 541, 51))
        self.fileNameSRP.setReadOnly(True)
        self.fileNameSRP.setObjectName("fileNameSRP")
        self.fromPage = QtWidgets.QLabel(self.SRP)
        self.fromPage.setGeometry(QtCore.QRect(10, 80, 92, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.fromPage.setFont(font)
        self.fromPage.setObjectName("fromPage")
        self.toPage = QtWidgets.QLabel(self.SRP)
        self.toPage.setGeometry(QtCore.QRect(10, 120, 48, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.toPage.setFont(font)
        self.toPage.setObjectName("toPage")
        self.fromCombo = QtWidgets.QComboBox(self.SRP)
        self.fromCombo.setGeometry(QtCore.QRect(110, 80, 141, 31))
        self.fromCombo.setObjectName("fromCombo")
        self.toCombo = QtWidgets.QComboBox(self.SRP)
        self.toCombo.setGeometry(QtCore.QRect(110, 120, 141, 31))
        self.toCombo.setObjectName("toCombo")
        self.SRPButton = QtWidgets.QPushButton(self.SRP,clicked=self.srpbutton)
        self.SRPButton.setGeometry(QtCore.QRect(10, 170, 540, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.SRPButton.setFont(font)
        self.SRPButton.setObjectName("SRPButton")
        self.tabWidget.addTab(self.SRP, "")
        self.SS = QtWidgets.QWidget()
        self.SS.setObjectName("SS")
        self.fileNameSS = QtWidgets.QPlainTextEdit(self.SS)
        self.fileNameSS.setGeometry(QtCore.QRect(10, 10, 541, 51))
        self.fileNameSS.setReadOnly(True)
        self.fileNameSS.setObjectName("fileNameSS")
        self.SSLabel = QtWidgets.QLabel(self.SS)
        self.SSLabel.setGeometry(QtCore.QRect(10, 70, 201, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.SSLabel.setFont(font)
        self.SSLabel.setObjectName("SSLabel")
        self.SSCombo = QtWidgets.QComboBox(self.SS)
        self.SSCombo.setGeometry(QtCore.QRect(210, 70, 141, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.SSCombo.setFont(font)
        self.SSCombo.setObjectName("SSCombo")
        self.SSButton = QtWidgets.QPushButton(self.SS,clicked=self.ssbutton)
        self.SSButton.setGeometry(QtCore.QRect(10, 130, 541, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.SSButton.setFont(font)
        self.SSButton.setObjectName("SSButton")
        self.tabWidget.addTab(self.SS, "")
        self.mergeFile = QtWidgets.QPushButton(self.centralwidget,clicked=lambda:self.finalmerge())
        self.mergeFile.setGeometry(QtCore.QRect(10, 410, 561, 71))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.mergeFile.setFont(font)
        self.mergeFile.setStyleSheet("color:red;\nborder-radius:20px;\nbackground-color:yellow;\nborder:1px solid black;")
        self.mergeFile.setObjectName("mergeFile")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 582, 21))
        self.menuBar.setObjectName("menuBar")
        self.menuOption = QtWidgets.QMenu(self.menuBar)
        self.menuOption.setObjectName("menuOption")
        MainWindow.setMenuBar(self.menuBar)
        self.actionReset = QtWidgets.QAction(MainWindow)
        self.actionReset.setObjectName("actionReset")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.menuOption.addAction(self.actionReset)
        self.menuOption.addAction(self.actionAbout)
        self.menuOption.addSeparator()
        self.menuOption.addAction(self.actionExit)
        self.menuBar.addAction(self.menuOption.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.SS.setDisabled(True)
        self.SR.setDisabled(True)
        self.SRP.setDisabled(True)
        self.SA.setDisabled(True)

        self.actionReset.triggered.connect(self.reset)
        self.actionExit.triggered.connect(lambda:sys.exit())
        
        self.chooseFolder.enterEvent=self.hoverinchoosefolder
        self.chooseFolder.leaveEvent=self.hoveroutchoosefolder

        self.mergeFile.enterEvent=self.hoverinmergefile
        self.mergeFile.leaveEvent=self.hoveroutmergefile

        self.actionAbout.triggered.connect(self.about)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "PDF MERGER"))
        self.chooseFolder.setText(_translate("MainWindow", "CLICK TO CHOOSE DIRECTORY CONTAINING PDF FILES"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.CF), _translate("MainWindow", "Choose File"))
        self.SAButton.setText(_translate("MainWindow", "PROCCED"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.SA), _translate("MainWindow", "Select all pages"))
        self.SRButton.setText(_translate("MainWindow", "Add page no. 0"))
        self.popUpMessageLabel.setText(_translate("MainWindow", ""))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.SR), _translate("MainWindow", "Select random pages"))
        self.fromPage.setText(_translate("MainWindow", "FROM:"))
        self.toPage.setText(_translate("MainWindow", "TO:"))
        self.SRPButton.setText(_translate("MainWindow", "PROCCED"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.SRP), _translate("MainWindow", "Select range of pages"))
        self.SSLabel.setText(_translate("MainWindow", "From page no. 1 to"))
        self.SSButton.setText(_translate("MainWindow", "PROCCED"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.SS), _translate("MainWindow", "Select pages serially.."))
        self.mergeFile.setText(_translate("MainWindow", "CLICK TO MERGE THE FILE"))
        self.menuOption.setTitle(_translate("MainWindow", "Option..."))
        self.actionReset.setText(_translate("MainWindow", "Reset"))
        self.actionAbout.setText(_translate("MainWindow", "About"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
    
    final_list=[]
    def loadfile(self):
        global foldername
        foldername=QtWidgets.QFileDialog.getExistingDirectory(None,'Choose Folder Contains PDF Files','/')
        if foldername:
            pdf_list=os.listdir(foldername)

            global final_list
            final_list=[]

            for i in pdf_list:
                if i.endswith('.pdf'):
                    try:
                        f=PdfFileReader(foldername+'/'+i)
                        f.numPages
                        final_list.append(i)
                    except:
                        pass
            
            self.fileBox.addItems(final_list)
            self.chooseFolder.setDisabled(True)


            self.fileNameSP.setPlainText(final_list[0])
            self.fileNameSR.setPlainText(final_list[0])
            self.fileNameSRP.setPlainText(final_list[0])
            self.fileNameSS.setPlainText(final_list[0])

            self.SS.setDisabled(False)
            self.SR.setDisabled(False)
            self.SRP.setDisabled(False)
            self.SA.setDisabled(False)

    def onchange(self):
        try:
            self.fileNameSP.setPlainText(self.fileBox.currentText())
            self.fileNameSR.setPlainText(self.fileBox.currentText())
            self.fileNameSRP.setPlainText(self.fileBox.currentText())
            self.fileNameSS.setPlainText(self.fileBox.currentText())

            self.SRListbox.clear()
            self.SSCombo.clear()
            self.fromCombo.clear()
            self.toCombo.clear()

            global foldername
            page_count=PdfFileReader(foldername+'/'+self.fileBox.currentText()).numPages
            self.SRListbox.addItems([str(i+1) for i in range(page_count)])
            self.SSCombo.addItems([str(i+1) for i in range(1,page_count)])
            self.fromCombo.addItems([str(i+1) for i in range(page_count-1)])
            self.toCombo.addItems([str(i+1) for i in range(1,page_count)])
        except:
            pass
    
    def srlistbox(self):
        curr_selected=self.SRListbox.currentItem()
        try:
            self.SRButton.setText('Add page no. '+curr_selected.text())
        except:
            self.SRButton.setText('Add page no. 0')
    
    def srbutton(self):
        global foldername
        file=PdfFileReader(foldername+'/'+self.fileNameSRP.toPlainText())
        page_no=int(self.SRButton.text().split('. ')[-1])
        pfw.addPage(file.getPage(page_no-1))

        self.popUpMessageLabel.setText('Added Successfully')
        QtCore.QTimer.singleShot(350,lambda:self.popUpMessageLabel.setText(''))
    
    def srpbutton(self):
        try:
            if int(self.fromCombo.currentText())>=int(self.toCombo.currentText()):
                msg=QtWidgets.QMessageBox()
                msg.setWindowTitle("Oops!!")
                msg.setText('Invaid page arrangement!')
                msg.setIcon(2)
                msg.exec_()
            else:
                global foldername
                file=PdfFileReader(foldername+'/'+self.fileNameSRP.toPlainText())

                for i in range(int(self.fromCombo.currentText())-1,int(self.toCombo.currentText())):
                    page=file.getPage(i)
                    pfw.addPage(page)
                
                self.SRPButton.setText('Done...')
                QtCore.QTimer.singleShot(350,lambda:self.SRPButton.setText('PROCCED'))
        except:
            pass
    
    def ssbutton(self):
        global foldername
        file=PdfFileReader(foldername+'/'+self.fileNameSS.toPlainText())

        for i in range(int(self.SSCombo.currentText())):
            page=file.getPage(i)
            pfw.addPage(page)
        
        self.SSButton.setText('Done...')
        QtCore.QTimer.singleShot(350,lambda:self.SSButton.setText('PROCCED'))
    
    def spbutton(self):
        global foldername
        file=PdfFileReader(foldername+'/'+self.fileNameSP.toPlainText())

        for i in range(file.numPages):
            page=file.getPage(i)
            pfw.addPage(page)
        
        self.SAButton.setText('Done...')
        QtCore.QTimer.singleShot(350,lambda:self.SAButton.setText('PROCCED'))
    
    def finalmerge(self):
        mergedfilename=QtWidgets.QFileDialog.getSaveFileName(None,'Name the file','/','PDF File (*.pdf);;Text File (*.txt)')
        if mergedfilename[0]:
            savefile=open(mergedfilename[0],'wb')
            pfw.write(savefile)
            savefile.close()

            msg=QtWidgets.QMessageBox()
            msg.setWindowTitle('Merge Done!!!')
            msg.setText('All desired files are completely merged, successfully...')
            msg.setIcon(1)
            msg.exec_()
    
    def reset(self):
        self.SS.setDisabled(True)
        self.SR.setDisabled(True)
        self.SRP.setDisabled(True)
        self.SA.setDisabled(True)
        self.chooseFolder.setDisabled(False)
        self.fileNameSP.setPlainText('')
        self.fileNameSR.setPlainText('')
        self.fileNameSRP.setPlainText('')
        self.fileNameSS.setPlainText('')
        self.SRListbox.clear()
        self.SSCombo.clear()
        self.fromCombo.clear()
        self.toCombo.clear()
        self.fileBox.clear()
    
    def hoverinchoosefolder(self,e):
        self.chooseFolder.setStyleSheet('background-color:black;color:white;font-size:18px')
    
    def hoveroutchoosefolder(self,e):
        self.chooseFolder.setStyleSheet("color:red;\nborder-radius:20px;\nbackground-color:yellow;\nborder:2px solid red;")

    def hoverinmergefile(self,e):
        self.mergeFile.setStyleSheet('background-color:black;color:white;font-size:18px')
    
    def hoveroutmergefile(self,e):
        self.mergeFile.setStyleSheet("color:red;\nborder-radius:20px;\nbackground-color:yellow;\nborder:2px solid red;")
    
    def about(self):
        msg=QtWidgets.QMessageBox()
        msg.setWindowTitle('About the Application')
        msg.setText('Hi Guys,\n\nThis is "KESHAV ABHISHEK" (owner) of this "PDF Files Merging Software"\n\nThis is a nice and easiest way to merge the desired "PDF Files" and that too "OFFLINE".\n\nHope you like the application and found useful.\n\nThanks for using...\n\nAny Query:-\nContact Us: crystaled2003@gmail.com')
        msg.setIcon(1)
        msg.exec_()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())