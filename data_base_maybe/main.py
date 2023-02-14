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


def execute_read_query(connection, query):
  cursor = connection.cursor()
  result = None
  try:
    cursor.execute(query)
    result = cursor.fetchall()
    return result
  except Error as e:
    print(f"The error '{e}' has occured.")

select_users = "SELECT * from users"
users = execute_read_query(connection, select_users)

select_posts = "SELECT * from posts"
posts = execute_read_query(connection, select_posts)

for user in users:
  print(user)

for post in posts:
  print(post)

connection.close()