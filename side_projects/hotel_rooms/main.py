import sqlite3
from sqlite3 import Error
import tkinter

def create_connection(path):
    connection = None
    try:
        connection = sqlite3.connect(path)
        print("Connection to SQLite Hotel DB was succesful.")
    except Error as e:
        print(f"The error '{e}' has occured.")
    return connection

conn = create_connection("./hotel_rooms/hotel_rooms.db")

#function that commits data to the database
def execute_query(conn, query):
    cur = conn.cursor()
    try:
        cur.execute(query)
        print(cur.rowcount, "record inserted.")
        conn.commit()
        print("Query executed successfully.")
    except Error as e:
        print(f"The error '{e}' has occured.")

#function that fetches data and returns the result.
def execute_read_query(conn, query):
    cur = conn.cursor()
    result = None
    try:
        cur.execute(query)
        result = cur.fetchall()
        return result
    except Error as e:
        print(f"The error '{e}' has occured.")

#GUI
m = tkinter.Tk() #m = main window





m.mainloop()
conn.close()