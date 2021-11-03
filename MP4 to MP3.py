from PyQt5 import QtCore, QtGui, QtWidgets
import pygame
from moviepy.editor import *
import wget
import os

if 'mp4-to-mp3.png' in os.listdir(os.getcwd()):
    pass
else:
    wget.download('https://keshavabhishek.github.io/web/mp4-to-mp3.png','mp4-to-mp3.png')


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(251, 371)
        MainWindow.setMinimumSize(QtCore.QSize(251, 371))
        MainWindow.setMaximumSize(QtCore.QSize(251, 371))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.appMainLabel = QtWidgets.QLabel(self.centralwidget)
        self.appMainLabel.setGeometry(QtCore.QRect(10, 10, 235, 101))
        self.appMainLabel.setStyleSheet("")
        self.appMainLabel.setText("")
        self.appMainLabel.setPixmap(QtGui.QPixmap("mp4-to-mp3.png"))
        self.appMainLabel.setObjectName("appMainLabel")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 120, 231, 61))
        self.groupBox.setObjectName("groupBox")
        self.chooseFileLabel = QtWidgets.QLabel(self.groupBox)
        self.chooseFileLabel.setGeometry(QtCore.QRect(10, 20, 121, 31))
        self.chooseFileLabel.setStyleSheet("background-color:#fc9a9a;font-weight:bold;")
        self.chooseFileLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.chooseFileLabel.setObjectName("chooseFileLabel")
        self.browseVideoFile = QtWidgets.QPushButton(self.groupBox,clicked=self.chooseVideoFile)
        self.browseVideoFile.setGeometry(QtCore.QRect(140, 22, 81, 31))
        self.browseVideoFile.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.browseVideoFile.setStyleSheet("color:#fff;background-color:green;font-weight:bold;border:0;border-radius:15px;")
        self.browseVideoFile.setObjectName("browseVideoFile")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 190, 231, 61))
        self.groupBox_2.setObjectName("groupBox_2")
        self.nameFileLabel = QtWidgets.QLabel(self.groupBox_2)
        self.nameFileLabel.setGeometry(QtCore.QRect(10, 20, 121, 31))
        self.nameFileLabel.setStyleSheet("background-color:#fc9a9a;font-weight:bold;")
        self.nameFileLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.nameFileLabel.setObjectName("nameFileLabel")
        self.nameAudioFile = QtWidgets.QPushButton(self.groupBox_2,clicked=self.chooseAudioFile)
        self.nameAudioFile.setGeometry(QtCore.QRect(140, 22, 81, 31))
        self.nameAudioFile.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.nameAudioFile.setStyleSheet("color:#fff;background-color:green;font-weight:bold;border:0;border-radius:15px;")
        self.nameAudioFile.setObjectName("nameAudioFile")
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 270, 231, 91))
        self.groupBox_3.setObjectName("groupBox_3")
        self.multiFunctionButton = QtWidgets.QPushButton(self.groupBox_3,clicked=self.mainProcess)
        self.multiFunctionButton.setGeometry(QtCore.QRect(10, 20, 211, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.multiFunctionButton.setFont(font)
        self.multiFunctionButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.multiFunctionButton.setStyleSheet("color:#fff;background-color:green;font-weight:bold;border:0;border-radius:30px;")
        self.multiFunctionButton.setObjectName("saveVideoFile")
        MainWindow.setCentralWidget(self.centralwidget)

        self.videoFileName=''
        self.audioFileName=''

        pygame.mixer.init()

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    
    def chooseVideoFile(self):
        if  self.browseVideoFile.text()=='Browse':
            self.videoFileName = QtWidgets.QFileDialog.getOpenFileName(None,'Select a Video File','/','MP4 *.mp4;;MKV *.mkv;;WMV *.wmv;;XESC *.xesc')

            if self.videoFileName[0]!='':
                self.videoFileName=self.videoFileName[0]
                self.chooseFileLabel.setText('File Choosen')
                self.browseVideoFile.setText('Remove')
        else:
            self.chooseFileLabel.setText('No File Choosen')
            self.browseVideoFile.setText('Browse')
    
    def chooseAudioFile(self):
        if self.videoFileName!='':
            if  self.nameAudioFile.text()=='Name the file':
                self.audioFileName = QtWidgets.QFileDialog.getSaveFileName(None,'Name the Audio File','/','MP3 *.mp3')

                if self.audioFileName[0]!='':
                    self.audioFileName=self.audioFileName[0]
                    self.nameFileLabel.setText('File Named')
                    self.nameAudioFile.setText('Change')
            else:
                self.nameFileLabel.setText('Not Yet Named')
                self.nameAudioFile.setText('Name the file')
    
    def mainProcess(self):
        if self.multiFunctionButton.text()=='Convert and Save':
            self.multiFunctionButton.setText('Converting...')
            videoClip=VideoFileClip(self.videoFileName)
            audioClip=videoClip.audio
            audioClip.write_audiofile(self.audioFileName)
            audioClip.close()
            videoClip.close()
            self.multiFunctionButton.setText('Play Music')
            self.groupBox_3.setTitle('Play')
        elif self.multiFunctionButton.text()=='Play Music':
            pygame.mixer.music.load(self.audioFileName)
            pygame.mixer.music.play()
            self.multiFunctionButton.setText('Exit')
        elif self.multiFunctionButton.text()=='Exit':
            exit()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Video to Audio"))
        self.groupBox.setTitle(_translate("MainWindow", "Choose Video File"))
        self.chooseFileLabel.setText(_translate("MainWindow", "No File Choosen"))
        self.browseVideoFile.setText(_translate("MainWindow", "Browse"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Save as Audio File"))
        self.nameFileLabel.setText(_translate("MainWindow", "Not Yet Named"))
        self.nameAudioFile.setText(_translate("MainWindow", "Name the file"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Save Audio File"))
        self.multiFunctionButton.setText(_translate("MainWindow", "Convert and Save"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())