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
def execute_ready_query(conn, query):
    cur = conn.cursor()
    result = None
    try:
        cur.execute(query)
        result = cur.fetchall()
        return result
    except Error as e:
        print(f"The error '{e}' has occured.")

create_caretakers_table = """
CREATE TABLE IF NOT EXISTS caretakers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER,
    gender TEXT,
    room_id INTEGER NOT NULL,
    FOREIGN KEY (room_id) REFERENCES hotelRooms (id)
);
"""

create_tenants_table = """
CREATE TABLE IF NOT EXISTS tenants (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    age INTEGER,
    gender TEXT,
    room_id INTEGER NOT NULL,
    FOREIGN KEY (room_id) REFERENCES hotelRooms (id)
);
"""

create_hotelRooms_table = """
CREATE TABLE IF NOT EXISTS hotelRooms (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    beds INTEGER,
    bathrooms INTEGER,
    caretakers_id INTEGER NOT NULL,
    tenant_id INTEGER NOT NULL,
    FOREIGN KEY (caretakers_id) REFERENCES caretakers (id) FOREIGN KEY (tenant_id) REFERENCES tenants (id)
);
"""


execute_query(conn, create_caretakers_table)
execute_query(conn, create_tenants_table)
execute_query(conn, create_hotelRooms_table)

conn.close()