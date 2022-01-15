import mysql.connector
from randomGen import *
class Database:
    def __init__(self):
        self.db = mysql.connection = mysql.connector.connect(
        host = "localhost",
        user = "root",
        passwd = "6383512055",
        db ="MINIPROJECT")
        self.mycursor = self.db.cursor()
    def verifyLogIn(self,userId,passwd):
        for i in range(8):
            values="INSERT INTO highscores(userId,highScore,timeTaken) VALUES ('{}',{},'{}')".format(names(),highscore(),time())
            self.mycursor.execute(values)
            self.db.commit()
        try:
            user="SELECT userId FROM users  WHERE userId LIKE '"+userId+"';"
            pas="SELECT passWd FROM users WHERE passWd LIKE '"+passwd+"';"
            self.mycursor.execute(user)
            if not self.mycursor.fetchone():
                return 0 
            self.mycursor.execute(pas)
            if not self.mycursor.fetchone():
                return -1
            return 1
        except Exception as err:
            print(err)
    def newAccount(self,name,rollNo,userId,passWd):
        for i in range(8):
            values="INSERT INTO highscores(userId,highScore,timeTaken) VALUES ('{}',{},'{}')".format(names(),highscore(),time())
            self.mycursor.execute(values)
            self.db.commit()        
        try:         
            newAcc="CREATE TABLE {} (userId VARCHAR(20) ,highScores INT,timeTaken VARCHAR(20),FOREIGN KEY (userId) REFERENCES USERS(userId));".format(userId)
            self.mycursor.execute(newAcc)
            q1="INSERT INTO users(full_name,rollNo,userId,passWd) VALUES('{}',{},'{}','{}')".format(name,int(rollNo),userId,passWd)
            q2="INSERT INTO "+userId+"(userId,highScores,timeTaken) VALUES('{}',{},'{}')".format(userId,0,'00:00:00')
            self.mycursor.execute(q1)
            self.mycursor.execute(q2)
            self.db.commit()
            return 1
        except Exception as err:
            print(err)
            err=str(err)
            if err[14:19] =='Table' :
                return -1
            else:
                return 
    def getRows(self):
        rows="SELECT * FROM highscores ORDER BY highScore DESC;"
        self.mycursor.execute(rows)
        return self.mycursor
    def truncate(self):
        trunc="TRUNCATE TABLE highscores;"
        self.mycursor.execute(trunc)
        self.db.commit()
    def getTimeDate(self):
        time="SELECT * FROM (SELECT current_time());"
        date="SELECT current_date();"
