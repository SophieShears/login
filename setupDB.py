import sqlite3

con = sqlite3.connect('users.db')

cur = con.cursor()

# cur.execute('''CREATE TABLE users(
#             username VARCHAR(10),
#             password VARCHAR(10)
#             )''')

cur.execute("INSERT INTO users VALUES (:username, :password)", {'username':'test', 'password': '12345'})
con.commit()

con.close()