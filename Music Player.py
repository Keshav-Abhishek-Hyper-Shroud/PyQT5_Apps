# Importing Libraries
from PyQt5 import QtCore, QtGui, QtWidgets
import pygame
from mutagen.mp3 import MP3
from time import strftime, gmtime

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(431, 371)
        MainWindow.setMinimumSize(431, 371)
        MainWindow.setMaximumSize(431, 371)
        self.total_songtime = 0
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.musicName = QtWidgets.QTextEdit(self.centralwidget)
        self.musicName.setGeometry(QtCore.QRect(10, 10, 411, 81))
        self.musicName.setReadOnly(True)
        self.musicName.setObjectName("musicName")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget,clicked=lambda:self.choose_music())
        self.pushButton.setGeometry(QtCore.QRect(10, 100, 411, 111))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.dial = QtWidgets.QDial(self.centralwidget)
        self.dial.setGeometry(QtCore.QRect(280, 220, 141, 141))
        self.dial.setMaximum(100)
        self.dial.setProperty("value", 100)
        self.dial.setNotchesVisible(True)
        self.dial.setObjectName("dial")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 220, 261, 141))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)

        # Initialize pygame
        pygame.mixer.init()

        # Connecting Volume Dial to Chnage Volume
        self.dial.valueChanged.connect(self.volume_set)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def button_on_off(self):
        global total_songtime
        if pygame.mixer.music.get_busy()==False:
            self.pushButton.setText('BROWSE FILE')
            self.pushButton.setDisabled(False)
            self.label.setText("VOLUME : 100")
            self.dial.setValue(100)
            self.musicName.setText('')
            return
        else:
            timestamp='{} of {}'.format(strftime('%M:%S',gmtime(int(pygame.mixer.music.get_pos()/1000))),strftime('%M:%S',gmtime(self.total_songtime)))
            self.pushButton.setText(timestamp)
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
            self.button_on_off()

    def volume_set(self,e):
        pygame.mixer.music.set_volume(int(self.dial.value())/100)
        self.label.setText('VOLUME : {}'.format(self.dial.value()))

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Simple Music Player"))
        self.pushButton.setText(_translate("MainWindow", "BROWSE FILE"))
        self.label.setText(_translate("MainWindow", "VOLUME : 100"))

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