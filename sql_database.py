import sqlite3
import os.path

def checkbd():
    if not os.path.exists('users.db'):
        create_table()
def create_table():
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE users (chat_id INTEGER, branch TEXT, registered BOOLEAN)''')
    conn.commit()
    conn.close()

def add_user(chat_id, branch):
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute("INSERT INTO users VALUES (?, ?, 1)", (chat_id, branch))
    conn.commit()
    conn.close()

def get_user(chat_id):
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE chat_id=?", (chat_id,))
    user = c.fetchone()
    conn.close()
    return user

def check_user_details(chat_id):
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE chat_id=?", (chat_id,))
    user = c.fetchone()
    conn.close()
    return user