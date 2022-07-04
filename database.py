import sqlite3
from models import *

databaseName="commitv1.db"
def inicia():
    # if  open("commit.db","r") != None:
    #     return
    con = sqlite3.connect(databaseName)
    cur = con.cursor()
    cur.execute("create table if not exists comits (id integer auto_increment primary key,comit text, hasid text)")
    con.close()

def insertDB(comit:str, has:str):
    con = sqlite3.connect(databaseName)
    cur = con.cursor()
    
    cur.execute("insert into comits(comit,hasid) values (?, ?)", (comit,has))
    con.commit()
    con.close()

def leerDBall():
    con = sqlite3.connect(databaseName)
    cur = con.cursor()
    cur.execute('SELECT * FROM comits ')
    # print(cur.fetchall())
    commits= cur.fetchall()
    # print(commits)
    con.close()
    
    return commits
    
def leerDBlast():
    
    con = sqlite3.connect(databaseName)
    cur = con.cursor()
    cur.execute('SELECT * FROM comits ORDER BY id DESC LIMIT 1')
    # print(cur.fetchall())
    commits= cur.fetchone()
    lastrec:commit
    lastrec=commit(comit=commits[1],hasid=commits[2])
    # print(commits)
    con.close()
    
    return lastrec