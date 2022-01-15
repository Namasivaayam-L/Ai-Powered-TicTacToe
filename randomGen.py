import mysql.connector
import random as rd
def highscore():
    num=[x for x in range(1,10)]
    highScore=''
    for i in range(2):
        highScore+=str(rd.choice(num))
    return int(highScore)
def time():
    min=[x for x in range(7)]
    hour=[x for x in range(1,13)]
    time=m=s=h=''
    h=str(rd.choice(hour))
    for i in range(2):
        m+=str(rd.choice(min))
        s+=str(rd.choice(min))
    time=h+':'+m+':'+s
    return time
def names():
    names=['Namasivaayam','Nitheeshwaran','Siyon','Jegan','Sweeton','Buvanesh','Aakash','Salman ALi','Ponkumaran','Vimal','Siddarth']
    return rd.choice(names)
