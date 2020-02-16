from datetime import datetime
import sqlite3
from sqlite3 import Error
import pathlib

def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)
    return conn

def create_note(conn, note):
    sql = '''INSERT INTO notes(note_time, note_data) VALUES (?,?)'''
    cur = conn.cursor()
    cur.execute(sql, note)
    return cur.lastrowid

def main():
    note = input('Write:: ')
    current_path = pathlib.Path().absolute()
    database_path = str(current_path) + '/database.sqlite3'
    conn = create_connection(database_path)
    with conn:
        note_data = (str(datetime.now()), note)
        create_note(conn, note_data)


if __name__=='__main__':
    main()
