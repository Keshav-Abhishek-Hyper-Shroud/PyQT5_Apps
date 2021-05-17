from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3

# Create Database
mydb=sqlite3.connect('todo list.db')
cursor=mydb.cursor()
s='create table if not exists todolist(thingstodo text)'
cursor.execute(s)
mydb.commit() #Commit Changes
mydb.close() #Close Connection

# Making GUI
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(468, 410)
        MainWindow.setMinimumSize(QtCore.QSize(468, 410))
        MainWindow.setMaximumSize(QtCore.QSize(468, 410))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(10, 10, 451, 41))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit.setFont(font)
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget,clicked=lambda:self.add_item())
        self.pushButton.setGeometry(QtCore.QRect(10, 60, 131, 31))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget,clicked=lambda:self.delete_item())
        self.pushButton_2.setGeometry(QtCore.QRect(150, 60, 161, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget,clicked=lambda:self.save_to())
        self.pushButton_3.setGeometry(QtCore.QRect(320, 60, 141, 31))
        self.pushButton_3.setObjectName("pushButton_3")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(10, 310, 451, 31))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 350, 281, 41))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(10, 100, 451, 201))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.listWidget.setFont(font)
        self.listWidget.setObjectName("listWidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # Grab all and show it
        self.grabdata()

    # Grab Data from Database
    def grabdata(self):
        mydb=sqlite3.connect('todo list.db')
        cursor=mydb.cursor()

        cursor.execute('select * from todolist')
        data=cursor.fetchall()

        for i in data:
            self.listWidget.addItem(str(i[0]))

        mydb.commit()
        mydb.close()

    # Add Items to ToDo List
    def add_item(self):
        item=self.lineEdit.text()
        self.listWidget.addItem(item)
        self.lineEdit.setText('')

    # Delete Items from Todo List
    def delete_item(self):
        curr_selected=self.listWidget.currentRow()
        self.listWidget.takeItem(curr_selected)

    # Clear Pop-up Message
    def clear_label(self):
        self.label.setText('')

    i=1
    # Save ToDo List to a Database
    def save_to(self):
        global i

        self.progressBar.setProperty('value',self.i)
        if self.i!=100:
            self.i+=1
            QtCore.QTimer.singleShot(10,self.save_to)
        else:
            self.label.setText('Saved to Database Successfully')
            self.progressBar.setProperty('value',0)
            self.i=1

            mydb=sqlite3.connect('todo list.db')
            cursor=mydb.cursor()

            cursor.execute('delete from todolist')

            items=[]

            for i in range(self.listWidget.count()):
                values=self.listWidget.item(i)
                values=values.text()
                items.append((values,))

            cursor.executemany('insert into todolist values(?)',items)

            mydb.commit()
            mydb.close()

            QtCore.QTimer.singleShot(1000,self.clear_label)

            return


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Add Item"))
        self.pushButton_2.setText(_translate("MainWindow", "Delete Item"))
        self.pushButton_3.setText(_translate("MainWindow", "Save to Database"))
        self.label.setText(_translate("MainWindow", ""))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
