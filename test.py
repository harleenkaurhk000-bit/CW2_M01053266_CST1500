import sqlite3
import pandas as pd

def create_user_table(conn):
    curr = conn.cursor()
    sql = """ CREATE TABLE IF NOT EXISTS users ( 
    id INTEGER PRIMARY KEY AUTOINCREMENT, 
    username TEXT NOT NULL UNIQUE, 
    password_hash TEXT NOT NULL) """ 
    curr.execute(sql)
    conn.commit()


def add_user(conn,name, hash_password):
    curr = conn.cursor()
    sql = "INSERT INTO users (username, password_hash) VALUES(?,?)"
    parram = (name,hash_password)
    curr.execute(sql, parram)
    conn.commit()



def migrate_users():
    with open('DATA/user.txt','r') as f:
        users = f.readlines()

    for user in users:
        name, hash = (user.strip().split(','))
        add_user(conn, name, hash)



def get_all_users(conn):
    curr = conn.cursor()
    sql = "SELECT * from users"
    curr.execute(sql)
    users = curr.fetchall()
    conn.close()
    return(users)



def get_user(conn):
    curr = conn.cursor()
    sql = "SELECT * FROM users WHERE username = ?"
    param = ('Harleen123',)
    curr.execute(sql,param)
    user = curr.fetchone
    conn.close()
    return user

conn = sqlite3.connect('DATA/intellegence_platform.db')   

def migrate_dataset_metdata():
    data = pd.read_csv("DATA/datasets_metadata.csv")
    data.to_sql('datasets_metadata', conn, if_exists="append", index = False)
    conn.close()

def get_all_users_pandas():
    sql = "SELECT *from datasets_metdata"
    data = pd.read_sql(sql, conn)
    return(data)

# INSERT, UPDATE, and DELETE operations
conn = sqlite3.connect('DATA/intelligence_platform.db')
curr = conn.cursor()
sql = ""
parr = ""
curr.execute(sql. parr)
conn.commit()
conn.close()
 
# GET DATA from table
conn = sqlite3.connect('DATA/intelligence_platform.db')
curr = conn.cursor()
sql = ""
parr = ""
curr.execute(sql. parr)
cur.fetchall()
curr.fetchone()
conn.close()