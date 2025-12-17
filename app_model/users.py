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



def get_user(conn, name_):
    curr = conn.cursor()
    sql = "SELECT * FROM users WHERE username = ?"
    param = (name_,)
    curr.execute(sql,param)
    user = curr.fetchone()
    return user

