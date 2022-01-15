from variables import *

class Board:    
    board={1:'1',2:'2',3:'3',4:'4',5:'5',6:'6',7:'7',8:'8',9:'9'}
    def makeMove(self,player,index,label):
        if index in self.allMoves():
            Board.board[index]=player
            label.setText(player)
    def nextMove(self,player):
        if player == X:
            return O
        if player == O:
            return X
    def allMoves(self):
        self.possibleMoves=[]
        for key,value in Board.board.items():
            if  value != X and value != O:
                self.possibleMoves.append(key)
        return self.possibleMoves