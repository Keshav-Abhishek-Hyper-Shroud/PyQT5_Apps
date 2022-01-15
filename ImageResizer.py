from PyQt5 import QtCore, QtGui, QtWidgets
from PIL import Image

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        # MainWindow.resize(571, 451)
        MainWindow.setFixedSize(571, 451)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.titleLabel = QtWidgets.QLabel(self.centralwidget)
        self.titleLabel.setGeometry(QtCore.QRect(10, 10, 551, 71))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.titleLabel.setFont(font)
        self.titleLabel.setStyleSheet("QLabel{background-color:black;color:white;font-weight:600;font-size:;}")
        self.titleLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.titleLabel.setObjectName("titleLabel")
        self.chooseImageArea = QtWidgets.QGroupBox(self.centralwidget)
        self.chooseImageArea.setGeometry(QtCore.QRect(30, 100, 191, 121))
        self.chooseImageArea.setObjectName("chooseImageArea")
        self.browseImageButton = QtWidgets.QPushButton(self.chooseImageArea,clicked = self.browseImage)
        self.browseImageButton.setGeometry(QtCore.QRect(10, 50, 171, 31))
        self.browseImageButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.browseImageButton.setStyleSheet("QPushButton{border:2px solid green;border-radius:10px;}\n"
"QPushButton:hover{background-color:green;border:2px solid yellow;font-weight:bold;}")
        self.browseImageButton.setObjectName("browseImageButton")
        self.imageDetailsArea = QtWidgets.QGroupBox(self.centralwidget)
        self.imageDetailsArea.setGeometry(QtCore.QRect(230, 100, 311, 121))
        self.imageDetailsArea.setObjectName("imageDetailsArea")
        self.imageNameLabel = QtWidgets.QLabel(self.imageDetailsArea)
        self.imageNameLabel.setGeometry(QtCore.QRect(20, 30, 281, 21))
        self.imageNameLabel.setObjectName("imageNameLabel")
        self.imageHeightWidthLabel = QtWidgets.QLabel(self.imageDetailsArea)
        self.imageHeightWidthLabel.setGeometry(QtCore.QRect(20, 60, 281, 21))
        self.imageHeightWidthLabel.setObjectName("imageHeightWidthLabel")
        self.imageAspectRatioLabel = QtWidgets.QLabel(self.imageDetailsArea)
        self.imageAspectRatioLabel.setGeometry(QtCore.QRect(20, 90, 281, 21))
        self.imageAspectRatioLabel.setObjectName("imageAspectRatioLabel")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(30, 230, 511, 16))
        self.line.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line.setLineWidth(1)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setObjectName("line")
        self.widthHeightManager = QtWidgets.QGroupBox(self.centralwidget)
        self.widthHeightManager.setGeometry(QtCore.QRect(30, 250, 511, 91))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.widthHeightManager.setFont(font)
        self.widthHeightManager.setObjectName("widthHeightManager")
        self.label = QtWidgets.QLabel(self.widthHeightManager)
        self.label.setGeometry(QtCore.QRect(10, 30, 41, 21))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.widthHeightManager)
        self.label_2.setGeometry(QtCore.QRect(280, 30, 41, 21))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.widthEntry = QtWidgets.QLineEdit(self.widthHeightManager)
        self.widthEntry.setGeometry(QtCore.QRect(60, 30, 171, 20))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.widthEntry.setFont(font)
        self.widthEntry.setObjectName("widthEntry")
        self.heightEntry = QtWidgets.QLineEdit(self.widthHeightManager)
        self.heightEntry.setGeometry(QtCore.QRect(330, 30, 171, 20))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.heightEntry.setFont(font)
        self.heightEntry.setObjectName("heightEntry")
        self.keepAspectRatio = QtWidgets.QCheckBox(self.widthHeightManager)
        self.keepAspectRatio.setGeometry(QtCore.QRect(170, 60, 171, 21))
        self.keepAspectRatio.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.keepAspectRatio.setObjectName("keepAspectRatio")
        self.resizeSave = QtWidgets.QGroupBox(self.centralwidget)
        self.resizeSave.setGeometry(QtCore.QRect(30, 370, 511, 71))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.resizeSave.setFont(font)
        self.resizeSave.setObjectName("resizeSave")
        self.resizeImage = QtWidgets.QPushButton(self.resizeSave,clicked=self.resizeImageFunction)
        self.resizeImage.setGeometry(QtCore.QRect(10, 30, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.resizeImage.setFont(font)
        self.resizeImage.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.resizeImage.setStyleSheet("QPushButton{border:2px solid red;border-radius:10px;}\n"
"QPushButton:hover{background-color:red;border:2px solid red;font-weight:bold;color:white;}")
        self.resizeImage.setObjectName("resizeImage")
        self.saveFile = QtWidgets.QPushButton(self.resizeSave,clicked=self.saveImageFunction)
        self.saveFile.setGeometry(QtCore.QRect(280, 30, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.saveFile.setFont(font)
        self.saveFile.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.saveFile.setStyleSheet("QPushButton{border:2px solid green;border-radius:10px;}\n"
"QPushButton:hover{background-color:green;border:2px solid green;font-weight:bold;color:white;}")
        self.saveFile.setObjectName("saveFile")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(30, 350, 511, 16))
        self.line_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_2.setLineWidth(1)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setObjectName("line_2")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.imageLoaction = ''
        self.heightEntry.textEdited.connect(self.renderWidth)
        self.widthEntry.textEdited.connect(self.renderHeight)
        self.ratio = 0
        self.resizedImage = None

        self.widthHeightManager.setDisabled(True)
        self.resizeSave.setDisabled(True)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Image Resizer"))
        self.titleLabel.setText(_translate("MainWindow", "Image Resizer"))
        self.chooseImageArea.setTitle(_translate("MainWindow", "Choose Image File"))
        self.browseImageButton.setText(_translate("MainWindow", "Browse Image"))
        self.imageDetailsArea.setTitle(_translate("MainWindow", "Image Details"))
        self.imageNameLabel.setText(_translate("MainWindow", ""))
        self.imageHeightWidthLabel.setText(_translate("MainWindow", ""))
        self.imageAspectRatioLabel.setText(_translate("MainWindow", ""))
        # self.imageNameLabel.setText(_translate("MainWindow", "Image Name: no-image-choosen"))
        # self.imageHeightWidthLabel.setText(_translate("MainWindow", "Width: , Height:"))
        # self.imageAspectRatioLabel.setText(_translate("MainWindow", "Aspect-Ratio (Width:Height) = "))
        self.widthHeightManager.setTitle(_translate("MainWindow", "Manage: Width | Height"))
        self.label.setText(_translate("MainWindow", "Width:"))
        self.label_2.setText(_translate("MainWindow", "Height:"))
        self.widthEntry.setPlaceholderText(_translate("MainWindow", "Enter Width"))
        self.heightEntry.setPlaceholderText(_translate("MainWindow", "Enter Height"))
        self.keepAspectRatio.setText(_translate("MainWindow", "Maintain Aspect Ratio"))
        self.resizeSave.setTitle(_translate("MainWindow", "Resize | Save"))
        self.resizeImage.setText(_translate("MainWindow", "Resize Image"))
        self.saveFile.setText(_translate("MainWindow", "Save File"))

    def browseImage(self):
        imgLocation,_ = QtWidgets.QFileDialog.getOpenFileName(None,None,'/','PNG File (*.png);;JPG File (*.jpg);;JPEG File (*.jpeg)')

        if imgLocation:

            self.imageLoaction = imgLocation
            imageName = imgLocation.split('/')[-1]
            self.imageNameLabel.setText(f'{imageName}')

            img = Image.open(imgLocation)
            self.imageHeightWidthLabel.setText(f'Width: {img.size[0]}px, Height: {img.size[1]}px')
            self.ratio = round(img.size[0]/img.size[1],3)
            self.imageAspectRatioLabel.setText(f'Aspect-Ratio (Width:Height) = {self.ratio}')
            self.keepAspectRatio.setChecked(True)

            self.widthHeightManager.setDisabled(False)
            self.resizeSave.setDisabled(False)
        else:
            self.renew()
    
    def renderWidth(self):
        try:
            if self.keepAspectRatio.isChecked()==True:
                width = f'{int(int(self.heightEntry.text())*self.ratio)}'
                self.widthEntry.setText(width)
        except:
            self.heightEntry.setText('')
            self.widthEntry.setText('')

    def renderHeight(self):
        try:
            if self.keepAspectRatio.isChecked()==True:
                height = f'{int(int(self.widthEntry.text())*(1/self.ratio))}'
                self.heightEntry.setText(height)
        except:
            self.heightEntry.setText('')
            self.widthEntry.setText('')
    
    def resizeImageFunction(self):
        image = Image.open(self.imageLoaction)
        self.resizedImage = image.resize((int(self.widthEntry.text()),int(self.heightEntry.text())))
        self.resizeImage.setText('Resized Successfully !')
        self.resizeImage.setDisabled(True)

    def saveImageFunction(self):
        chooseSavingFileLocation,_ = QtWidgets.QFileDialog.getSaveFileName(None,'Save As','/','PNG File (*.png);;JPG File (*.jpg);;JPEG File (*.jpeg)')
        if chooseSavingFileLocation:
            savingImage=self.resizedImage.save(chooseSavingFileLocation)

            self.renew()
    
    def renew(self):
        self.imageDetailsArea.setTitle("Image Details")
        self.imageNameLabel.setText("")
        self.imageHeightWidthLabel.setText("")
        self.imageAspectRatioLabel.setText("")
        self.widthEntry.setText("")
        self.heightEntry.setText("")
        self.resizeImage.setText("Resize Image")

        self.ratio = 0
        self.resizedImage = None

        self.resizeImage.setDisabled(False)
        self.widthHeightManager.setDisabled(True)
        self.resizeSave.setDisabled(True)
        self.keepAspectRatio.setChecked(False)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())