from board import *
class verifyStatus(Board):
    def verifyStatus(self):
        diagonal,vertical,horizontal=self.verifyDiagonal(),self.verifyVertical(),self.verifyHorizontal()
        if diagonal[0]:
            return diagonal
        elif vertical[0]:
            return vertical
        elif horizontal[0]:
            return horizontal
        else:
            if (self.isDraw()):
                return 0,(0,0,0)
            else:
                return 0,(0,0,0)
            
    def verifyDiagonal(self):
        if(self.board[1]==self.board[5]==self.board[9]):
            return self.board[1],(1,5,9)
        elif(self.board[3]==self.board[5]==self.board[7]):
            return self.board[3],(3,5,7)
        else:
            return 0,(0,0,0)
        
    def verifyVertical(self):
        if(self.board[1]==self.board[4]==self.board[7]):
            return self.board[1],(1,4,7)
        elif(self.board[2]==self.board[5]==self.board[8]):
            return self.board[2],(2,5,8)
        elif(self.board[3]==self.board[6]==self.board[9]):
            return self.board[3],(3,6,9)
        else:
            return 0,(0,0,0)
        
    def verifyHorizontal(self):
        if(self.board[1]==self.board[2]==self.board[3]):
            return self.board[1],(1,2,3)
        elif(self.board[4]==self.board[5]==self.board[6]):
            return self.board[4],(4,5,6)
        elif(self.board[7]==self.board[8]==self.board[9]):
            return self.board[7],(7,8,9)
        else:
            return 0,(0,0,0)
             
    def isDraw(self):
        for values in self.board.values():
            if(values == X or values == O):
                continue
            else:
                return 0
        return 1