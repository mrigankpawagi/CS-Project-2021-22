import sqlite3 as sql
from typing import List, Tuple
import regex as re
import logging

def init():
    # Admin Database
    con = sql.connect('admin.db')
    cur = con.cursor()
    
    # Create Doctors table
    cur.execute('''CREATE TABLE IF NOT EXISTS doctors(
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        password TEXT,
                        hospitalid INTEGER, 
                        name TEXT, 
                        branch TEXT
                    );''')

    # Create Slots Table
    cur.execute('''CREATE TABLE IF NOT EXISTS slots(
                        id INTEGER PRIMARY KEY AUTOINCREMENT, 
                        docid INTEGER,
                        hospitalid INTEGER,
                        patientid INTEGER,
                        date TEXT,
                        starttime TEXT,
                        endtime TEXT,
                        prestext TEXT,
                        presfilename TEXT,
                        presfile BLOB 
                    );''')

    # Create Hospitals Table
    cur.execute('''CREATE TABLE IF NOT EXISTS hospitals(
                        id INTEGER PRIMARY KEY AUTOINCREMENT, 
                        password TEXT,
                        name TEXT,
                        address TEXT,
                        pincode INTEGER,
                        phone TEXT,
                        description TEXT 
                    );''')

    con.commit()
    con.close()

    # Patient Database
    con = sql.connect('patient.db')
    cur = con.cursor()
    
    # Create Patients table
    cur.execute('''CREATE TABLE IF NOT EXISTS patients(
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        password TEXT,
                        name TEXT,
                        phone TEXT
                    );''')
    con.commit()
    con.close()

def menu(init: str, items: list):
    # init = Menu Introduction Text
    # item = Tuple(prompt, function)
    print(init, '\n')
    for i, M in enumerate(items):
        print(str(i+1) + ".", M[0])
    while True:
        try:
            res = int(input("\n\nSelect one of the options above to continue: "))            
            items[res-1][1]() 
            break
        except Exception as e:
            logging.exception("message")
            continue
    return

def form(prompts: list, init: str='\nPlease provide the following details.'): 
    # prompt = Tuple(question, regex)
    print(init, '\n')
    res = []
    for P in prompts: 
        r = ''
        while r == '':
            r = input(P[0] + ": ").strip()
            if P[1] != '': 
                if not re.match(P[1], r):
                    print("Invalid input.")
                    r = ''
        res.append(r)
    return res

def getQuery(db: str, tables: str, cols: str, options: str):
    con = sql.connect(db + '.db')
    cur = con.cursor()
    cur.execute('SELECT ' + cols + ' FROM ' + tables + ' ' + options + ';')
    r = cur.fetchall()
    con.close()
    return r

def writeQuery(db: str, table: str, cols: str, values: str):
    con = sql.connect(db + '.db')
    cur = con.cursor()
    cur.execute('INSERT INTO ' + table + ' (' + cols + ') VALUES (' + values + ');')
    con.commit()
    cur.execute('SELECT last_insert_rowid();')
    r = cur.fetchone()
    con.close()
    return r[0]
    