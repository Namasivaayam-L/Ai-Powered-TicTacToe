import mysql.connector

class Database:
    def __init__(self):
        self.db = mysql.connection = mysql.connector.connect(
        host = "localhost",
        user = "root",
        passwd = "6383512055",
        db ="MINIPROJECT")
        self.mycursor = self.db.cursor()
    def verifyLogIn(self,userId,passwd):
        try:
            logIn="SELECT userId,passwd FROM users  WHERE userId LIKE '"+userId+"' AND passwd LIKE '"+passwd+"';"
            self.mycursor.execute(logIn)
            return self.mycursor.fetchone()
        except Exception as err:
            print(err)
            return 'newAcc'
    def newAccount(self,name,rollNo,userId,passWd):
        try:
            newAcc="CREATE TABLE {} (userId VARCHAR(20) ,passwd VARCHAR(20),highScores INT,timeTaken VARCHAR(20),FOREIGN KEY (userId) REFERENCES users(userId));".format(userId)
            self.mycursor.execute(newAcc)
            self.userInsert="""CREATE FUNCTION userInsert(fname VARCHAR(20),rnum INT,id VARCHAR(20),pass VARCHAR(20)) 
            RETURNS INT 
            BEGIN 
                INSERT INTO users(full_name,rollNo,userId,passWd) 
                VALUES(fname,rnum,id,pass) 
                RETURN 1; 
            END;"""
            self.mycursor.execute(self.userInsert)
            q1="SELECT userInsesrt('{}',{},'{}');".format(name,rollNo,userId,passWd,)
            self.gameInsert="CREATE FUNCTION gameInsert(userId VARCHAR(20),passWd VARCHAR(20),highScores INT,timeTaken VARCHAR(20)) RETURNS INT BEGIN INSERT INTO {}(userId,passWd,highScores,timeTaken) VALUES(fname,rnum,id,pass) RETURN 1; END;"
            self.mycursor.execute(self.gameInsert)
            q2="SELECT gameInsesrt('{}','{}',{},'{}');".format(userId,passWd,0,'00:00')
            self.mycursor.execute(q1)
            self.mycursor.execute(q2)
            self.db.commit()
            return self.mycursor
        except Exception as err:
            print(err)
            return 'oldAcc'    

            