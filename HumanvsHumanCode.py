from PyQt5 import *
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
import sys
from variables import *
from verifyWinner import *

class HumanvsHuman(QMainWindow,verifyStatus):
    def SideSelection(self,player):
        if player==X:
            self.player=X
        else: 
            self.player=O
    def onClick(self,index):
        self.labels={1:[self.l1,self.Button1],2:[self.l2,self.Button2],3:[self.l3,self.Button3],4:[self.l4,self.Button4],5:[self.l5,self.Button5],
                6:[self.l6,self.Button6],7:[self.l7,self.Button7],8:[self.l8,self.Button8],9:[self.l9,self.Button9],10:'Draw'}
        if index<10:
            self.labels[index][1].setEnabled(False)
            self.makeMove(self.player,index,self.labels[index][0])
            self.player=self.nextMove(self.player)
            self.isWinner()
                
    def isWinner(self):
        if self.isDraw():
            self.resultLabel.setText(' Draw Match')        
        self.winner,self.winners=self.verifyStatus()
        if self.winner==X:
            self.resultLabel.setText(' X is the Winner')
        elif self.winner==O:
            self.resultLabel.setText(' O is the Winner')
        if self.winner!=0:
            for i in self.winners:
                self.labels[i][0].setStyleSheet('background:cyan')
    def resetBoard(self):
        Board.board={1:'1',2:'2',3:'3',4:'4',5:'5',6:'6',7:'7',8:'8',9:'9'}
        for i in range(1,10):
            self.labels[i][0].setText('')
            self.labels[i][1].setEnabled(True)
            self.labels[i][0].setStyleSheet('border:3px solid color')    
    
    def __init__(self):
        super(HumanvsHuman,self).__init__()
        loadUi("C:\\Users\\NAMASIVAAYAM\\Documents\\Mini Project 3rd Sem\\PYQT5 GUI\\HumanvsHuman.ui",self)
        self.Button1.clicked.connect(lambda:self.onClick(1))
        self.Button2.clicked.connect(lambda:self.onClick(2))
        self.Button3.clicked.connect(lambda:self.onClick(3))
        self.Button4.clicked.connect(lambda:self.onClick(4))
        self.Button5.clicked.connect(lambda:self.onClick(5))
        self.Button6.clicked.connect(lambda:self.onClick(6))
        self.Button7.clicked.connect(lambda:self.onClick(7))
        self.Button8.clicked.connect(lambda:self.onClick(8))
        self.Button9.clicked.connect(lambda:self.onClick(9))
        self.XSideButton.clicked.connect(lambda:self.SideSelection(X))
        self.OSideButton.clicked.connect(lambda:self.SideSelection(O))
        self.l1=self.label1
        self.l2=self.label2
        self.l3=self.label3
        self.l4=self.label4
        self.l5=self.label5
        self.l6=self.label6
        self.l7=self.label7
        self.l8=self.label8
        self.l9=self.label9
        self.reset.clicked.connect(self.resetBoard)