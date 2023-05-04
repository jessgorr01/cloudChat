from flask import Flask, render_template, request, redirect, url_for, session
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re

app = Flask(__name__)

app.secret_key = "secret"

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'cloud'
app.config['MYSQL_PASSWORD'] = 'cloud'
app.config['MYSQL_DB'] = 'CloudChat'

mySQL = MySQL(app)

@app.route('/')
@app.route('/login', methods=['GET', 'POST'])
def login():
    msg = ''
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        username = request.form['username']
        password = request.form['password']
        cursor = mySQL.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute(
            'SELECT * FROM UserLogin WHERE UserName = % s \
            AND PasswordHash = % s', (username, password, ))
        account = cursor.fetchone()
        if account:
            session['loggedin'] = True
            session['id'] = account['id']
            session['username'] = account['UserName']
            msg = 'Logged in successfully !'
            return render_template('index.html', msg=msg)
        else:
            msg = 'Incorrect username / password !'
    return render_template('login.html', msg=msg)

@app.route('/logout')
def logout():
    session.pop('loggedin', None)
    session.pop('id', None)
    session.pop('UserName', None)
    return redirect(url_for('login'))

@app.route("/update", methods=['GET', 'POST'])
def update():
    msg = ''
    if 'loggedin' in session:
        if request.method == 'POST' and 'UserName' in request.form and 'PasswordHash' in request.form and 'email' in request.form:
            username = request.form['UserName']
            password = request.form['PasswordHash']
            email = request.form['email']
            cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
            cursor.execute(
                'SELECT * FROM UserLogin WHERE UserName = % s',
                      (username, ))
            account = cursor.fetchone()
            if account:
                msg = 'Account already exists !'
            elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
                msg = 'Invalid email address !'
            elif not re.match(r'[A-Za-z0-9]+', username):
                msg = 'name must contain only characters and numbers !'
            else:
                cursor.execute('UPDATE accounts SET UserName =% s,\
                PasswordHash =% s, email =% s, WHERE id =% s', (
                    username, password, email, (session['id'], ), ))
                mysql.connection.commit()
                msg = 'You have successfully updated !' 
                request.method == 'POST'
        msg = 'Please fill out the form !'
        return render_template("update.html", msg=msg)
    return redirect(url_for('login'))

@app.route("/register", methods=['GET', 'POST'])
def register():
    msg = ''
    if 'loggedin' in session:
        if request.method == 'POST' and 'UserName' in request.form and 'PasswordHash' in request.form and 'email' in request.form:
            username = request.form['UserName']
            password = request.form['PasswordHash']
            email = request.form['email']
            cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
            cursor.execute(
                'SELECT * FROM UserLogin WHERE UserName = % s',
                      (username, ))
            account = cursor.fetchone()
            if account:
                msg = 'Account already exists !'
            elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
                msg = 'Invalid email address !'
            elif not re.match(r'[A-Za-z0-9]+', username):
                msg = 'name must contain only characters and numbers !'
            else:
                cursor.execute('INSERT INTO accounts SET UserName =% s,\
                PasswordHash =% s, email =% s, WHERE id =% s', (
                    username, password, email, (session['id'], ), ))
                mysql.connection.commit()
                msg = 'You have successfully updated !' 
                request.method == 'POST'
        msg = 'Please fill out the form !'
        return render_template("update.html", msg=msg)
    return redirect(url_for('login'))



if __name__ == "__main__":
    app.run(host="localhost", port=int("5000"))
