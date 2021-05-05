from flask import Flask, render_template, request
from markupsafe import escape

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def login():
    return render_template('login.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    return render_template('register.html')


@app.route('/profile/<username>')
def profile(username):
    return 'Welcome to your profile %s' % escape(username) 


if __name__ == '__main__':
    app.run(debug=True)