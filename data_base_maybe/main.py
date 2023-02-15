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

select_users_posts = """
SELECT
  users.id,
  users.name,
  posts.description
FROM
  posts
  INNER JOIN users ON users.id = posts.user_id
"""
# INNER JOIN means that it will get data that is common between the two tables
execute_users_post = execute_read_query(connection, select_users_posts)

for print_users_post in execute_users_post:
  print(print_users_post)

connection.close()