import sqlite3
from sqlite3 import Error

def create_connection(path):
    connection = None
    try:
        connection = sqlite3.connect(path)
        print("Connection to SQLite DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")

    return connection
    
connection = create_connection("./data_base_maybe/pythonsqlite.db")

def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print(cursor.rowcount, "record inserted.")
        connection.commit()
        print("Query executed successfully")
    except Error as e:
        print(f"The error '{e}' occurred")


create_posts = """
INSERT INTO
  posts (title, description, user_id)
VALUES
  ("Happy", "I am feeling very happy today", 1),
  ("Hot Weather","Have you guys seen the temperature here? It's hot!", 2),
  ("Help","I need some help with finding me dog", 2),
  ("Great News", "I've just received a promotion! I cannot believe it!", 1),
  ("Interesting Game", "I just had a fantastic game of tennis. Get rekt lol", 5),
  ("Party", "Anyone up for a late-night party today?", 3);
  """

execute_query(connection, create_posts)


connection.close()