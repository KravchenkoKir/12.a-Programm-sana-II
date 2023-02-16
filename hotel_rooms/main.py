import sqlite3
from sqlite3 import Error

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

create_caretakers = """
CREATE TABLE IF NOT EXISTS caretakers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER,
    gender TEXT
);
"""

create_rooms = """
INSERT INTO
    hotelRooms (beds, bathrooms, caretakers_id, tenant_id)
VALUES
    (2,1,1,3),
    (1,1,2,4),
    (2,2,2,1),
    (3,1,2,5),
    (3,2,3,2);
"""


create_tenants = """
INSERT INTO
    tenants (name, age, gender, room_id) 
VALUES
    ("Ashley Baker", 26, "Female", 3),
    ("Jonathan Friwo", 22, "Male", 5),
    ("Max N. Tenala", 17, "Non-binary", 1),
    ("Robert Dennir", 43, "Male", 2),
    ("Lynda Weyen", 35, "Female", 4)
"""


execute_query(conn,create_caretakers)
execute_query(conn, create_rooms)
execute_query(conn, create_tenants)

conn.close()