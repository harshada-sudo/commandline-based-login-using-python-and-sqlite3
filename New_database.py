import sqlite3

#create new database or connect to existing one
with sqlite3.connect("Quiz.db") as db:
    #create cursor
    cursor=db.cursor()

#create table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS user_info(
    userid INTEGER PRIMARY KEY,
    username VARCHAR(20) NOT NULL,
    firstname VARCHAR(20) NOT NULL,
    lastname VARCHAR(20) NOT NULL,
    password VARCHAR(20) NOT NULL
    );
   """)

#insert one entry into table
cursor.execute("""
INSERT INTO user_info(username,firstname,lastname,password)
VALUES("test_User","harshada","nakod","vijay")
""")

db.commit()

cursor.execute("SELECT * FROM user_info")
print(cursor.fetchall())
