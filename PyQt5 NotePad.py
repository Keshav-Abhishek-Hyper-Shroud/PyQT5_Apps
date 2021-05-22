# Importing Needed Libraries
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QFileDialog
import os
import win32api

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(690, 598)
        MainWindow.setMinimumSize(QtCore.QSize(690, 598))
        MainWindow.setMaximumSize(QtCore.QSize(690, 598))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(10, 40, 671, 510))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        self.textEdit.setFont(font)
        self.textEdit.setObjectName("textEdit")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(10, 10, 91, 22))
        self.comboBox.setObjectName("comboBox")
        self.fontComboBox = QtWidgets.QFontComboBox(self.centralwidget)
        self.fontComboBox.setGeometry(QtCore.QRect(110, 10, 151, 22))
        self.fontComboBox.setEditable(False)
        self.fontComboBox.setObjectName("fontComboBox")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 690, 21))
        self.menuBar.setObjectName("menuBar")
        self.menuFile = QtWidgets.QMenu(self.menuBar)
        self.menuFile.setObjectName("menuFile")
        self.menuOptions = QtWidgets.QMenu(self.menuBar)
        self.menuOptions.setObjectName("menuOptions")
        MainWindow.setMenuBar(self.menuBar)
        self.actionNew = QtWidgets.QAction(MainWindow)
        self.actionNew.setObjectName("actionNew")
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionPrint=QtWidgets.QAction(MainWindow)
        self.actionPrint.setObjectName('actionPrint')
        self.actionUndo = QtWidgets.QAction(MainWindow)
        self.actionUndo.setObjectName("actionUndo")
        self.actionRedo = QtWidgets.QAction(MainWindow)
        self.actionRedo.setObjectName("actionRedo")
        self.actionWrap = QtWidgets.QAction(MainWindow)
        self.actionWrap.setObjectName("actionWrap")
        self.actionUnwrap = QtWidgets.QAction(MainWindow)
        self.actionUnwrap.setObjectName("actionUnwrap")
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionPrint)
        self.menuOptions.addAction(self.actionUndo)
        self.menuOptions.addAction(self.actionRedo)
        self.menuOptions.addSeparator()
        self.menuOptions.addAction(self.actionWrap)
        self.menuOptions.addAction(self.actionUnwrap)
        self.menuBar.addAction(self.menuFile.menuAction())
        self.menuBar.addAction(self.menuOptions.menuAction())

        # Sets the range of sizes for text
        self.comboBox.addItems([f'{i}' for i in range(1,101)])
        self.comboBox.setCurrentText('16')
        self.comboBox.currentTextChanged.connect(self.changefontsize)

        # Sets the names of text styles
        self.fontComboBox.setEditable(False)
        self.fontComboBox.setCurrentText('Times New Roman')
        self.fontComboBox.currentTextChanged.connect(self.changefontstyle)

        self.actionNew.triggered.connect(self.newfile)
        self.actionOpen.triggered.connect(self.openit)
        self.actionSave.triggered.connect(self.saveit)
        self.actionUndo.triggered.connect(self.undo)
        self.actionRedo.triggered.connect(self.redo)
        self.actionWrap.triggered.connect(self.wrap)
        self.actionUnwrap.triggered.connect(self.unwrap)
        self.actionPrint.triggered.connect(self.print_document)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    # Print the Text File
    def print_document(self):
        global file_exists
        if os.path.exists(self.file_exists):
            win32api.ShellExecute(0,'print',self.file_exists,None,'.',0)
        else:
            print_msg=QMessageBox()
            print_msg.setWindowTitle('Access Denied')
            print_msg.setText('File might not exists or printer not set as default.')
            print_msg.setIcon(QMessageBox.Warning)
            print_msg.exec_()

    # Wrap the text
    def wrap(self):
        self.textEdit.setLineWrapMode(True)

    # Unwrap the text
    def unwrap(self):
        self.textEdit.setLineWrapMode(False)

    # Initializes New File
    def newfile(self):
        global file_exists
        MainWindow.setWindowTitle('PyQt5 NotePad - Untitled')
        self.textEdit.setText('')
        self.file_exists=''

    # Define changefontstyle
    def changefontstyle(self):
        fontsize=int(self.comboBox.currentText())
        font = QtGui.QFont()
        font.setFamily(self.fontComboBox.currentText())
        font.setPointSize(fontsize)
        self.textEdit.setFont(font)

    # Define changefontsize
    def changefontsize(self):
        fontsize=int(self.comboBox.currentText())
        font = QtGui.QFont()
        font.setFamily(self.fontComboBox.currentText())
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

        MainWindow.setWindowTitle('PyQt5 NotePad - '+dirs[0].split('/')[-1])

        filename=dirs[0]
        if filename:
            self.textEdit.clear()

            f=open(filename,'r')
            data=f.read()
            f.close()

            self.textEdit.setText(data)

        global file_exists
        self.file_exists=filename

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
        MainWindow.setWindowTitle(_translate("MainWindow", "PyQt5 NotePad - Untitled"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuOptions.setTitle(_translate("MainWindow", "Options"))
        self.actionNew.setText(_translate("MainWindow", "New"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionUndo.setText(_translate("MainWindow", "Undo"))
        self.actionRedo.setText(_translate("MainWindow", "Redo"))
        self.actionWrap.setText(_translate("MainWindow", "Wrap"))
        self.actionUnwrap.setText(_translate("MainWindow", "Unwrap"))
        self.actionPrint.setText(_translate("MainWindow", "Print"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())