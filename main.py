import sqlite3
from flask import Flask, g, render_template, redirect, request, url_for
from markupsafe import escape

# Connect database, create database functions
database = 'user_info.db'
app = Flask(__name__)

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(database)
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if 'username' in request.form and 'password' in request.form:
            username = request.form['username']
            password = request.form['password']
            conn = get_db()
            cur = conn.cursor()
            cur.execute("SELECT * FROM users WHERE username=:username AND password=:password", 
                                                    {'username':username, 'password':password})
            info = cur.fetchone()
            if info is not None:
                return redirect(url_for('profile', username=username))
            else:
                return "Username doesn't exist or password is incorrect." 

            conn.close()
    
    return render_template('login.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        if 'username' in request.form and 'password' in request.form:
            username = request.form['username']
            password = request.form['password']
            conn = get_db()
            cur = conn.cursor()
            cur.execute("SELECT * FROM users WHERE username=:username", {'username':username})
            info = cur.fetchone()
            if info == None:
                cur.execute("INSERT INTO users VALUES (:username, :password)", {'username':username, 'password': password})
                conn.commit()
                return redirect(url_for('login'))
            else:
                return "Username already exists."

            conn.close()
    
    return render_template('register.html')


@app.route('/profile/<username>')
def profile(username):
    return 'Welcome to your profile %s' % escape(username) 


if __name__ == '__main__':
    app.run(debug=True)