# Importing Libraries
from PyQt5 import QtCore, QtGui, QtWidgets
import pygame
from mutagen.mp3 import MP3
from time import strftime, gmtime

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(431, 410)
        MainWindow.setMinimumSize(431, 410)
        MainWindow.setMaximumSize(431, 410)
        self.pause_permit=True
        self.stop_permit=True
        self.total_songtime = 0
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.musicName = QtWidgets.QTextEdit(self.centralwidget)
        self.musicName.setGeometry(QtCore.QRect(10, 10, 411, 61))
        self.musicName.setReadOnly(True)
        self.musicName.setObjectName("musicName")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(10,75,411,21))
        self.progressBar.setTextVisible(False)
        self.progressBar.setObjectName("progressBar")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget,clicked=lambda:self.choose_music())
        self.pushButton.setGeometry(QtCore.QRect(10, 100, 411, 111))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pauseButton = QtWidgets.QPushButton(self.centralwidget,clicked=lambda:self.permit_pause())
        self.pauseButton.setGeometry(QtCore.QRect(10,220,120,50))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.pauseButton.setFont(font)
        self.pauseButton.setObjectName("pauseButton")
        self.stopButton = QtWidgets.QPushButton(self.centralwidget,clicked=lambda:self.permit_stop())
        self.stopButton.setGeometry(QtCore.QRect(130,220,100,50))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.stopButton.setFont(font)
        self.stopButton.setObjectName("stopButton")
        self.dial = QtWidgets.QDial(self.centralwidget)
        self.dial.setGeometry(QtCore.QRect(280, 220, 141, 141))
        self.dial.setMaximum(100)
        self.dial.setProperty("value", 100)
        self.dial.setNotchesVisible(True)
        self.dial.setObjectName("dial")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 270, 261, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.vol1 = QtWidgets.QProgressBar(self.centralwidget)
        self.vol1.setGeometry(QtCore.QRect(10, 370, 16, 31))
        self.vol1.setProperty("value", 100)
        self.vol1.setOrientation(QtCore.Qt.Vertical)
        self.vol1.setObjectName("vol1")
        self.vol2 = QtWidgets.QProgressBar(self.centralwidget)
        self.vol2.setGeometry(QtCore.QRect(30, 360, 16, 41))
        self.vol2.setProperty("value", 100)
        self.vol2.setOrientation(QtCore.Qt.Vertical)
        self.vol2.setObjectName("vol2")
        self.vol3 = QtWidgets.QProgressBar(self.centralwidget)
        self.vol3.setGeometry(QtCore.QRect(50, 350, 16, 51))
        self.vol3.setProperty("value", 100)
        self.vol3.setOrientation(QtCore.Qt.Vertical)
        self.vol3.setObjectName("vol3")
        self.vol4 = QtWidgets.QProgressBar(self.centralwidget)
        self.vol4.setGeometry(QtCore.QRect(70, 340, 16, 61))
        self.vol4.setProperty("value", 100)
        self.vol4.setOrientation(QtCore.Qt.Vertical)
        self.vol4.setObjectName("vol4")
        self.vol5 = QtWidgets.QProgressBar(self.centralwidget)
        self.vol5.setGeometry(QtCore.QRect(90, 330, 16, 71))
        self.vol5.setProperty("value", 100)
        self.vol5.setOrientation(QtCore.Qt.Vertical)
        self.vol5.setObjectName("vol5")
        MainWindow.setCentralWidget(self.centralwidget)

        self.pauseButton.setDisabled(True)
        self.stopButton.setDisabled(True)

        # Initialize pygame
        pygame.mixer.init()

        # Connecting Volume Dial to Chnage Volume
        self.dial.valueChanged.connect(self.volume_set)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def button_on_off(self):
        global total_songtime, stop_permit, pause_permit, total_songtime, pauseButton
        if pygame.mixer.music.get_busy()==False and self.stop_permit==True and self.pause_permit==True:
            self.pushButton.setText('BROWSE FILE')
            self.pushButton.setDisabled(False)
            self.label.setText("VOLUME : 100")
            self.dial.setValue(100)
            self.musicName.setText('')
            self.progressBar.setValue(0)
            self.pauseButton.setText('PAUSE')
            self.pauseButton.setDisabled(True)
            self.stopButton.setDisabled(True)
            self.total_songtime=0
            self.vol1.setValue(100)
            self.vol2.setValue(100)
            self.vol3.setValue(100)
            self.vol4.setValue(100)
            self.vol5.setValue(100)
            return
        else:
            timestamp='{} of {}'.format(strftime('%M:%S',gmtime(int(pygame.mixer.music.get_pos()/1000))),strftime('%M:%S',gmtime(self.total_songtime)))
            self.pushButton.setText(timestamp)
            self.progressBar.setValue(int((int(pygame.mixer.music.get_pos()/1000)/self.total_songtime)*100))
            QtCore.QTimer.singleShot(1000,self.button_on_off)

    def choose_music(self):
        global total_songtime
        music_file=QtWidgets.QFileDialog.getOpenFileName(None,'Select a MP3 File',None,'MP3 File (*.mp3)')
        if music_file[0]:
            self.musicName.setText(music_file[0].split('/')[-1])
            self.pushButton.setText('Playing...');self.pushButton.setDisabled(True)
            pygame.mixer.music.load(music_file[0])
            pygame.mixer.music.set_volume(int(self.dial.value())/100)
            pygame.mixer.music.play(loops=0)
            self.total_songtime=int(MP3(music_file[0]).info.length)
            self.pauseButton.setDisabled(False)
            self.stopButton.setDisabled(False)
            self.button_on_off()

    def volume_set(self,e):
        pygame.mixer.music.set_volume(int(self.dial.value())/100)
        self.label.setText('VOLUME : {}'.format(self.dial.value()))

        if 10<=self.dial.value()<=20:
            self.vol1.setValue(100)
            self.vol2.setValue(0)
            self.vol3.setValue(0)
            self.vol4.setValue(0)
            self.vol5.setValue(0)
        elif self.dial.value()<10:
            self.vol1.setValue(50)
            self.vol2.setValue(0)
            self.vol3.setValue(0)
            self.vol4.setValue(0)
            self.vol5.setValue(0)

        if 30<=self.dial.value()<=40:
            self.vol2.setValue(100)
            self.vol3.setValue(0)
            self.vol4.setValue(0)
            self.vol5.setValue(0)
        elif 20<=self.dial.value()<=30:
            self.vol2.setValue(50)
            self.vol3.setValue(0)
            self.vol4.setValue(0)
            self.vol5.setValue(0)

        if 50<=self.dial.value()<=60:
            self.vol3.setValue(100)
            self.vol4.setValue(0)
            self.vol5.setValue(0)
        elif 40<=self.dial.value()<=50:
            self.vol3.setValue(50)
            self.vol4.setValue(0)
            self.vol5.setValue(0)

        if 70<=self.dial.value()<=80:
            self.vol4.setValue(100)
            self.vol5.setValue(0)
        elif 60<=self.dial.value()<=70:
            self.vol4.setValue(50)
            self.vol5.setValue(0)

        if 90<=self.dial.value()<=100:
            self.vol5.setValue(100)
        elif 80<=self.dial.value()<=90:
            self.vol5.setValue(50)

        if self.dial.value()==0:
            self.vol1.setValue(0)
            self.vol2.setValue(0)
            self.vol3.setValue(0)
            self.vol4.setValue(0)
            self.vol5.setValue(0)

    def permit_pause(self):
        global stop_permit, pause_permit
        try:
            if self.pauseButton.text()=='PAUSE':
                self.stop_permit=False
                self.pause_permit=True
                pygame.mixer.music.pause()
                self.pauseButton.setText('RESUME')
                self.button_on_off()
            else:
                pygame.mixer.music.unpause()
                self.pauseButton.setText('PAUSE')
                self.button_on_off()
        except ZeroDivisionError:
            pass

    def permit_stop(self):
        global stop_permit, pause_permit
        self.stop_permit=True
        self.pause_permit=True
        pygame.mixer.music.stop()
        self.button_on_off()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Simple Music Player"))
        self.pushButton.setText(_translate("MainWindow", "BROWSE FILE"))
        self.label.setText(_translate("MainWindow", "VOLUME : 100"))
        self.pauseButton.setText(_translate("MainWindow", "PAUSE"))
        self.stopButton.setText(_translate("MainWindow", "STOP"))

# Running the App
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
# Thanks for Using