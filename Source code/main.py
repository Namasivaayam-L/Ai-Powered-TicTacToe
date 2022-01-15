from PyQt5 import *
from PyQt5.QtCore import QTime,QDate
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
import sys
from AivsHumanCode import *
from HumanvsHumanCode import *
from AivsAiCode import *
from qt_material import *
# from sqlfile import *
from time import *

class LogInPage(QMainWindow):
    def __init__(self):
        super(LogInPage,self).__init__()
        loadUi("C:\\Users\\NAMASIVAAYAM\\Documents\\Mini Project 3rd Sem\\PYQT5 GUI\\logInTab.ui",self)
        d=QDate.currentDate()
        t=QTime.currentTime()
        self.timeOutputLabel.setText(t.toString()[:5])
        self.dateOutputLabel.setText(d.toString())
        self.logInButton.clicked.connect(self.verifyCredentials)
        self.createAccButton.clicked.connect(self.createCredentials)
    def verifyCredentials(self):
        widget.setCurrentIndex(1)
        # self.userid=self.userIdInput.text()
        # self.passwd=self.passwdInput.text()
        # self.result=self.verifyLogIn(self.userid,self.passwd)
        # if self.result==0:
        #     self.checkLogInLabel.setText('Kindly Create A New Account')     
        # elif self.result==-1:
        #     self.checkLogInLabel.setText('Incorrect Password')
        # elif self.result==1:
        #     self.checkLogInLabel.setText('LogIn Successfull')
        #     widget.setCurrentIndex(1)    
    def createCredentials(self):
        widget.setCurrentIndex(1)
        # self.name=self.nameInput.text()
        # self.rollNo=self.rollNoInput.text()
        # self.userid=self.newUserIdInput.text()
        # self.passwd=self.newPasswdInput.text()
        # self.result=self.newAccount(self.name,self.rollNo,self.userid,self.passwd)
        # if self.result==0:
        #     self.checkCreationLabel.setText('Kindly give correct values')     
        # elif self.result==-1:
        #     self.checkCreationLabel.setText('Kindly Log In (Account exists already)')
        # elif self.result==1:
        #     self.checkCreationLabel.setText('Account Successfully Created')    
        #     sleep(2)

        
class TitleCard(QMainWindow):
    def __init__(self):
        super(TitleCard,self).__init__()
        loadUi("C:\\Users\\NAMASIVAAYAM\\Documents\\Mini Project 3rd Sem\\PYQT5 GUI\\starterPage.ui",self)
        self.mode1vsAiButton.clicked.connect(self.AivsHuman)
        self.mode1v1Button.clicked.connect(self.HumanvsHuman)
        self.modeAivsAiButton.clicked.connect(self.AivsAi)
        self.exitGame.clicked.connect(self.exit)
    def goBack(self):
        widget.setCurrentIndex(1)
    def exit(self):
        # self.truncate()
        sys.exit()
    def AivsHuman(self):
        # self.fillTable()
        widget.setCurrentIndex(2)
        AivsHumanWin.goBack1vAiButton.clicked.connect(self.goBack)   
        AivsHumanWin.exit.clicked.connect(self.exit) 
    def HumanvsHuman(self):
        widget.setCurrentIndex(3)
        humanvhuman.goBack1v1Button.clicked.connect(self.goBack)
        humanvhuman.exit.clicked.connect(self.exit) 
    def AivsAi(self):
        widget.setCurrentIndex(4)
        aivsai.goBackAivAiButton.clicked.connect(self.goBack)
        aivsai.exit.clicked.connect(self.exit) 
    #   def fillTable(self):
    #     AivsHumanWin.highScoreTable.setRowCount(10)
    #     rows=self.getRows()
    #     tableRow=0
    #     for row in rows:
    #         AivsHumanWin.highScoreTable.setItem(tableRow,0,QtWidgets.QTableWidgetItem(row[0]))
    #         AivsHumanWin.highScoreTable.setItem(tableRow,1,QtWidgets.QTableWidgetItem(str(row[1])))
    #         AivsHumanWin.highScoreTable.setItem(tableRow,2,QtWidgets.QTableWidgetItem(row[2]))
    #         tableRow+=1
app=QApplication(sys.argv)
# apply_stylesheet(app,theme='dark_amber.xml')
widget=QtWidgets.QStackedWidget()
win=LogInPage()
widget.addWidget(win)
mainWin=TitleCard()
widget.addWidget(mainWin)
AivsHumanWin=AivsHuman()
humanvhuman=HumanvsHuman()
aivsai=AivsAi()
widget.addWidget(AivsHumanWin)
widget.addWidget(humanvhuman)
widget.addWidget(aivsai)
widget.setFixedHeight(1080)
widget.setFixedWidth(1920)
widget.show()
app.exec_()