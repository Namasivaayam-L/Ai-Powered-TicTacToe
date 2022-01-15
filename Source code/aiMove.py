from time import sleep
from variables import *
from verifyWinner import *

class ai(verifyStatus):
    score={X:1,O:-1,0:0}
    def MiniMax(self,player,labels):
        if(self.verifyStatus()[0]):
            return ai.score[self.verifyStatus()[0]],0
        elif(self.isDraw()):
            return 0,10
        if player == 'X':
            maxval=-2
            bestMove=0
            for i in self.allMoves():
                placeHolder=self.board[i]
                self.board[i]=player
                score=self.MiniMax(O,labels)[0]
                self.board[i]=placeHolder
                if score>maxval:
                    maxval=score
                    bestMove=i
            return maxval,bestMove
        elif player == 'O':
            minval=2
            bestMove=0
            for i in self.allMoves():
                placeHolder=self.board[i]
                self.board[i]=player                
                score=self.MiniMax(X,labels)[0]
                self.board[i]=placeHolder
                if score<minval:
                    minval=score
                    bestMove=i
            return minval,bestMove