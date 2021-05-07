import sqlite3

con = sqlite3.connect('users.db')

cur = con.cursor()

cur.execute('''CREATE TABLE users(
            username VARCHAR(10),
            password VARCHAR(10)
            )''')

con.commit()

con.close()