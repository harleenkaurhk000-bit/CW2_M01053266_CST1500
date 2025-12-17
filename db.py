import sqlite3
def get_db_connection():
    conn = sqlite3.connect('DATA/intelligence_platform.db')
    return conn

def get_db_connection_user():
    conn = sqlite3.connect('DATA/intellegence_platform.db')
    return conn
                       #DATA/intelligence_platform.db

