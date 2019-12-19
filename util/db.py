'''

Johnny Wong
Read and Write to a DB with this script

'''

import sqlite3 # enables control of sqlite3 database

DB_FILE = "data/pubmix.db"

def create_db():
    '''Creates tables for DB_FILE'''
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()

    # replace these executes depending on necessary tables
    c.execute("CREATE TABLE IF NOT EXISTS users (username TEXT PRIMARY KEY, password TEXT)")
    c.execute("CREATE TABLE IF NOT EXISTS workouts (username TEXT PRIMARY KEY, date TEXT, exercise TEXT, reps INTEGER, sets INTEGER)")
    c.execute("CREATE TABLE IF NOT EXISTS todo (username TEXT PRIMARY KEY, date TEXT, goal TEXT, due TEXT)")

    db.close()
    return True

# create_db() # call this on initial creation of database

def get_users():
    '''Returns a dictionary containing all current users and corresponding passwords'''
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()

    cmd = 'SELECT username, password FROM users'
    c.execute(cmd)
    selectedVal = c.fetchall()

    db.close()
    return dict(selectedVal)

def find_user(username):
    '''Checks if username is unique'''
    users = get_users()
    return username in list(users.keys())

def register_user(username, password):
    '''Registers a user to the database'''
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()

    if find_user(username):
        return False
    else:
        c.execute('INSERT INTO users VALUES (?, ?)', (username, password))

        db.commit()
        db.close()
        return True

def verify_user(username, password):
    '''Checks if username and password matches those found in database'''
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()

    c.execute('SELECT username, password FROM users where username=?', (username,))

    selectedVal = c.fetchone()

    db.close()

    if selectedVal == None:
        return False
    elif username == selectedVal[0] and password == selectedVal[1]:
        return True
    return False
