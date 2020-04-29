# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_GUI.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
#from main_updated import main, main_write, get_audio
import main_updated as m
import pyttsx3  #pip install pyttsx3==2.71
import speech_recognition as sr


#setting text to speech engine and voice rate property
engine = pyttsx3.init("sapi5")
engine.setProperty('rate', 150)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(616, 456)
        MainWindow.setMaximumSize(QtCore.QSize(616, 456))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("main_icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.ai_ouput = QtWidgets.QTextEdit(self.centralwidget)
        self.ai_ouput.setGeometry(QtCore.QRect(20, 40, 231, 301))
        self.ai_ouput.setReadOnly(True)
        self.ai_ouput.setObjectName("ai_ouput")

        #self.ai_ouput.append("Assistant: " + self.ai_display)

        self.user_display = QtWidgets.QTextEdit(self.centralwidget)
        self.user_display.setGeometry(QtCore.QRect(260, 40, 231, 301))
        self.user_display.setReadOnly(True)
        self.user_display.setObjectName("user_display")
        self.ai_name = QtWidgets.QLabel(self.centralwidget)
        self.ai_name.setGeometry(QtCore.QRect(20, 10, 55, 16))
        self.ai_name.setObjectName("ai_name")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(260, 10, 55, 16))
        self.label_2.setObjectName("label_2")
        self.user_input = QtWidgets.QLineEdit(self.centralwidget)
        self.user_input.setGeometry(QtCore.QRect(20, 380, 471, 31))
        self.user_input.setObjectName("user_input")
        self.sendBtn = QtWidgets.QPushButton(self.centralwidget)
        self.sendBtn.setGeometry(QtCore.QRect(510, 370, 91, 51))
        self.sendBtn.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("send.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.sendBtn.setIcon(icon1)
        self.sendBtn.setIconSize(QtCore.QSize(40, 40))
        self.sendBtn.setObjectName("sendBtn")

        #add signal to checkbox
        self.sendBtn.clicked.connect(self.changeContent)
        self.sendBtn.setToolTip("Send")
        self.sendBtnShortcut = QtWidgets.QShortcut(
                            QtGui.QKeySequence(QtCore.Qt.Key_Return), self.sendBtn, self.changeContent)
        

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 350, 101, 21))
        self.label_3.setObjectName("label_3")
        self.micBtn = QtWidgets.QPushButton(self.centralwidget)
        self.micBtn.setGeometry(QtCore.QRect(520, 170, 81, 61))
        self.micBtn.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("mic.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.micBtn.setIcon(icon2)
        self.micBtn.setIconSize(QtCore.QSize(40, 40))
        self.micBtn.setObjectName("micBtn")

        #add signal to checkbox
        self.micBtn.clicked.connect(self.listen)
        self.micBtn.setToolTip("Press SPACE to talk")
        self.shortcut = QtWidgets.QShortcut(
                            QtGui.QKeySequence(QtCore.Qt.Key_Space), self.micBtn, self.listen)


        MainWindow.setCentralWidget(self.centralwidget)
 
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Windows Assistant"))
        self.ai_name.setText(_translate("MainWindow", "DAVID:"))
        self.label_2.setText(_translate("MainWindow", "USER:"))
        self.label_3.setText(_translate("MainWindow", "USER INPUT:"))


    def changeContent(self):
        userInput = self.user_input.text()
        self.user_display.append("User: " + userInput)
        self.user_input.clear()
        m.main_write(userInput)

    def listen(self):
        said = m.get_audio()
        self.user_display.append("User: " + said)
        m.main(said)


   

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
