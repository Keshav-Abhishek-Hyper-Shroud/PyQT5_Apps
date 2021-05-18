from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
import pyautogui

a=pyautogui.size() # Return a tuple (width,height) of screen.

# Create Database
mydb=sqlite3.connect('todo list.db')
cursor=mydb.cursor()
s='create table if not exists todolist(thingstodo text)'
cursor.execute(s)
mydb.commit() #Commit Changes
mydb.close() #Close Connection

window_width=int(0.365625*a[0])
window_height=int(0.6138*a[1])

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(window_width,window_height)
        MainWindow.setMinimumSize(QtCore.QSize(window_width,window_height))
        MainWindow.setMaximumSize(QtCore.QSize(window_width,window_height))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(int(0.021*window_width), int(0.022*window_height), int(0.96*window_width), int(0.092*window_height)))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit.setFont(font)
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget,clicked=lambda:self.add_item())
        self.pushButton.setGeometry(QtCore.QRect(int(0.021*window_width), int(0.135*window_height), int(0.279*window_width), int(0.070*window_height)))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget,clicked=lambda:self.delete_item())
        self.pushButton_2.setGeometry(QtCore.QRect(int(0.320*window_width), int(0.135*window_height), int(0.344*window_width), int(0.070*window_height)))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget,clicked=lambda:self.save_to())
        self.pushButton_3.setGeometry(QtCore.QRect(int(0.683*window_width), int(0.135*window_height), int(0.301*window_width), int(0.070*window_height)))
        self.pushButton_3.setObjectName("pushButton_3")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(int(0.021*window_width), int(0.701*window_height), int(0.963*window_width), int(0.070*window_height)))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(int(0.021*window_width), int(0.859*window_height), int(0.600*window_width), int(0.092*window_height)))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(int(0.021*window_width), int(0.226*window_height), int(0.963*window_width), int(0.454*window_height)))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.listWidget.setFont(font)
        self.listWidget.setObjectName("listWidget")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget,clicked=lambda:self.cleardatabase())
        self.pushButton_4.setGeometry(QtCore.QRect(int(0.021*window_width), int(0.791*window_height), int(0.963*window_width), int(0.070*window_height)))
        self.pushButton_4.setObjectName("pushButton_4")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # Grab all and show it
        self.grabdata()

    # Clear database
    def cleardatabase(self):
        mydb=sqlite3.connect('todo list.db')
        cursor=mydb.cursor();cursor.execute('delete from todolist')
        mydb.commit()
        mydb.close()
        self.label.setText('Database cleared successfully.')
        QtCore.QTimer.singleShot(1500,self.clear_label)

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
        if self.listWidget.count()==0:
        	self.label.setText('Nothing to Save.')
        	QtCore.QTimer.singleShot(1500,self.clear_label)
        	return
        else:
	        global i

	        self.progressBar.setProperty('value',self.i)
	        if self.i!=100:
	            self.i+=1
	            QtCore.QTimer.singleShot(10,self.save_to)
	        else:
	            self.label.setText('Successfully Saved.')
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

	            QtCore.QTimer.singleShot(1500,self.clear_label)
	            return

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ToDo App"))
        self.pushButton.setText(_translate("MainWindow", "Add Item"))
        self.pushButton_2.setText(_translate("MainWindow", "Delete Item"))
        self.pushButton_3.setText(_translate("MainWindow", "Save to Database"))
        self.label.setText(_translate("MainWindow", ""))
        self.pushButton_4.setText(_translate("MainWindow", "Clear Database"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())