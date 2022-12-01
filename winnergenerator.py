# Form implementation generated from reading ui file 'winnergenerator.ui'
#
# Created by: PyQt6 UI code generator 6.4.0

from PyQt6 import QtCore, QtGui, QtWidgets
import random


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(271, 396)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        #add entry(item)
        self.additem_pushbutton = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.add_it())
        self.additem_pushbutton.setGeometry(QtCore.QRect(10, 40, 71, 21))
        self.additem_pushbutton.setObjectName("additem_pushbutton")

        #delete entry (item)
        self.deleteitem_pushButton_2 = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.delete_it())
        self.deleteitem_pushButton_2.setGeometry(QtCore.QRect(100, 40, 71, 21))
        self.deleteitem_pushButton_2.setObjectName("deleteitem_pushButton_2")
        
        #clear all
        self.clearall_pushButton_3 = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.clear_it())
        self.clearall_pushButton_3.setGeometry(QtCore.QRect(190, 40, 71, 20))
        self.clearall_pushButton_3.setObjectName("clearall_pushButton_3")
        
        #generate winner from listWidget
        self.generateWinner_pushButton = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.winnerPush())
        self.generateWinner_pushButton.setGeometry(QtCore.QRect(10, 330, 251, 31))
        self.generateWinner_pushButton.setObjectName("generatewinner_pushbutton")
        
        #bar where you type in the items
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(10, 10, 251, 21))
        self.lineEdit.setObjectName("lineEdit")
        
        #list of entries
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(10, 70, 251, 201))
        self.listWidget.setObjectName("listWidget")
        
        #where the winner will be displayed
        self.winnerLabel = QtWidgets.QLabel(self.centralwidget)
        self.winnerLabel.setGeometry(QtCore.QRect(10, 290, 241, 31))
        self.winnerLabel.setText("")
        self.winnerLabel.setObjectName("winnerLabel")

        self.deleteitem_pushButton_2.raise_()
        self.clearall_pushButton_3.raise_()
        self.additem_pushbutton.raise_()
        self.lineEdit.raise_()
        self.listWidget.raise_()
        self.generateWinner_pushButton.raise_()
        self.winnerLabel.raise_()

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 271, 18))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        #solution to it not allowing listWidget to pick winner.
        
    print ("Testing this to test array function. Array was created successfully.")


    def add_it(self):
        #grab item from lineEdit box. The .text grabs text.
        item = self.lineEdit.text()
        
        if item == "":          
            #print and array had to be copied in all the def so that the gui would recognize it.
            self.winnerLabel.setText("Error: Cannot add blank entry.")
            print("Testing for error. Error was triggered successfully.")

        else:
        #adds Entry from lineEdit box to the listWidget
            self.listWidget.addItem(item)

            #for testing purposes. Confirmed working.
            entryArray=[]
            entryArray.append(item)
            print (item + " was added to the array successfully.")

        #clears entry box so more text can be added
        self.lineEdit.setText("")

    def delete_it(self):
        #grabs selected/current row
        clicked = self.listWidget.currentRow()

        #deletes the row after taking it from the selected item in the list
        print(self.listWidget.currentItem().text())
        self.listWidget.takeItem(clicked)

        #this section for testing purposes
        print(clicked, " was deleted successfully")
        #print("The variable of this object is this:", type(clicked)) #returned an int

    def clear_it(self):
        self.listWidget.clear()
        #for testing purposes
        entryArray.clear()
        print ("The list was cleared successfully.")

    def winnerPush(self):
            self.winnerLabel.setText("")
            #testing to make sure button works.
            print("Generate Winner Button has been pressed.")
            self.generate_it()

    #adding the signal for the button that generates the winner
    def generate_it(self):
        index = random.randint(0, self.listWidget.count()-1)
        winner = self.listWidget.item(index).text()
        print (winner + " was the winner. Generate winner button is working.")
        self.winnerLabel.setText(winner)
        
        #putting the winner on the label just above generate winner button
        self.generateWinner_pushButton.clicked.connect(self.winnerPush)
        
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Giveaway Generator"))
        self.deleteitem_pushButton_2.setText(_translate("MainWindow", "Remove"))
        self.clearall_pushButton_3.setText(_translate("MainWindow", "Clear All"))
        self.additem_pushbutton.setText(_translate("MainWindow", "Add Entry"))
        self.generateWinner_pushButton.setText(_translate("MainWindow", "Who\'s the lucky winner??"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())

#To convert .ui to .py:  Right-click folder .ui is located in and open Terminal
#Enter this command: pyuic6 -x generatewinner.ui -o generatewinner.py
#to run python file: Open Terminal file is located in, then: python generatewinner.py
