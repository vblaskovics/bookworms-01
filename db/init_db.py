import sqlite3

conn = sqlite3.connect("my.db")

cursor = conn.cursor()

cursor.execute("DROP TABLE IF EXISTS BOOK")

cursor.execute("CREATE TABLE BOOK (NAME VARCHAR(25));")

cursor.execute("INSERT INTO BOOK VALUES ('book1')") 
cursor.execute("INSERT INTO BOOK VALUES ('book2')") 
cursor.execute("INSERT INTO BOOK VALUES ('book3')") 

conn.commit()

conn.close()

