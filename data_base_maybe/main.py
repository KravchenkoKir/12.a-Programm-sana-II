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


create_likes_table = """
CREATE TABLE IF NOT EXISTS likes (
  id INTEGER PRIMARY KEY AUTOINCREMENT, 
  user_id INTEGER NOT NULL, 
  post_id integer NOT NULL, 
  FOREIGN KEY (user_id) REFERENCES users (id) FOREIGN KEY (post_id) REFERENCES posts (id)
);
"""
create_comments_table = """
CREATE TABLE IF NOT EXISTS comments (
  id INTEGER PRIMARY KEY AUTOINCREMENT, 
  text TEXT NOT NULL, 
  user_id INTEGER NOT NULL, 
  post_id INTEGER NOT NULL, 
  FOREIGN KEY (user_id) REFERENCES users (id) FOREIGN KEY (post_id) REFERENCES posts (id)
);
"""


execute_query(connection, create_comments_table)  
execute_query(connection, create_likes_table)  

create_comments = """
INSERT INTO
  comments (text, user_id, post_id)
VALUES
  ('Count me in', 1, 6),
  ('What can I do to help?', 5 , 3),
  ('Congrats! Happy for you buddy', 2, 4),
  ('I was rooting for Henry though.', 4,5),
  ('Ayyyy gz', 5, 4);
"""
create_likes = """
INSERT INTO
  likes (user_id, post_id)
VALUES
  (1,6),
  (2,3),
  (1,5),
  (5,4),
  (2,4),
  (4,2),
  (3,6);
"""

execute_query(connection, create_comments)
execute_query(connection, create_likes)

connection.close()