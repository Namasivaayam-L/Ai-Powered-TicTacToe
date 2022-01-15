from PyQt5 import *
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets
from PyQt5.uic import loadUi
import sys
from qt_material import *
from sqlfile import *
 
class LogInPage(QMainWindow,Database):
    def __init__(self):
        super(LogInPage,self).__init__()
        loadUi("C:\\Users\\NAMASIVAAYAM\\Documents\\Mini Project 3rd Sem\\PYQT5 GUI\\logInTab.ui",self)
        self.logInButton.clicked.connect(self.verifyCredetials)
        self.createAccButton.clicked.connect(self.createCredetials)
        
    def verifyCredetials(self):
        self.userid=self.userIdInput.text()
        self.passwd=self.passwdInput.text()
        self.result=self.verifyLogIn(self.userid,self.passwd)
        if self.result=='newAcc':
            self.checkLogInLabel.setText('Not Working. Create A New Account')     
        elif self.result!=None:
            self.checkLogInLabel.setText('Worked')     
    def createCredetials(self):
        self.name=self.nameInput.text()
        self.rollNo=self.rollNoInput.text()
        self.userid=self.newUserIdInput.text()
        self.passwd=self.newPasswdInput.text()
        self.result=self.newAccount(self.name,self.rollNo,self.userid,self.passwd)
        if self.result=='oldAcc':
            self.checkCreationLabel.setText('Not Working. Create A New Account')     
        else:
            self.checkCreationLabel.setText('Worked')     
        # print(self.result)

     
app=QApplication(sys.argv)
widget=QtWidgets.QStackedWidget()
win=LogInPage()
widget.addWidget(win)
widget.show()
app.exec_()