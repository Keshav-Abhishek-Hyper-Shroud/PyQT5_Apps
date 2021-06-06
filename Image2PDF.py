from PyQt5 import QtCore, QtGui, QtWidgets
import os
from PIL import Image
from time import strftime

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(271, 171)
        MainWindow.setMinimumSize(QtCore.QSize(271, 171))
        MainWindow.setMaximumSize(QtCore.QSize(271, 171))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 10, 211, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.oneimgButton = QtWidgets.QPushButton(self.centralwidget,clicked=lambda:self.one_image())
        self.oneimgButton.setGeometry(QtCore.QRect(30, 70, 211, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.oneimgButton.setFont(font)
        self.oneimgButton.setObjectName("oneimgButton")
        self.manyimgButton = QtWidgets.QPushButton(self.centralwidget,clicked=lambda:self.many_image())
        self.manyimgButton.setGeometry(QtCore.QRect(30, 120, 211, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.manyimgButton.setFont(font)
        self.manyimgButton.setObjectName("manyimgButton")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def one_image(self):
        file=QtWidgets.QFileDialog.getOpenFileName(None,'Select any Image','/','PNG (*.png);;JPG (*.jpg);;JPEG (*.jpeg);;ICON (*.ico)')
        if file[0]:
            genetaredfilename=r'{}\Batch {} {}-{}-{} {}.pdf'.format(os.getcwd(),strftime('%A'),strftime('%I'),strftime('%M'),strftime('%S'),strftime('%p'))

            data=Image.open(file[0])
            data=data.convert('RGB')
            data.save(genetaredfilename)

    def many_image(self):
        files=QtWidgets.QFileDialog.getOpenFileNames(None,'Select any Image','/','PNG (*.png);;JPG (*.jpg);;JPEG (*.jpeg);;ICON (*.ico)')
        if files[0][0]:
            foldername=QtWidgets.QFileDialog.getExistingDirectory(None,'Select a Folder')
            if foldername:
                finalfoldername=foldername+'/Batch {} {}-{}-{} {}'.format(strftime('%A'),strftime('%I'),strftime('%M'),strftime('%S'),strftime('%p'))
                makefolder=os.makedirs(finalfoldername)

                for i in files[0]:
                    data=Image.open(i)
                    data=data.convert('RGB')
                    data.save(finalfoldername+'/Image {}.pdf'.format(files[0].index(i)+1))

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Image2PDF"))
        self.label.setText(_translate("MainWindow", "Image to PDF"))
        self.oneimgButton.setText(_translate("MainWindow", "One Image to PDF"))
        self.manyimgButton.setText(_translate("MainWindow", "Many Images to PDF"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())