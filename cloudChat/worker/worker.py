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
    if request.method == 'POST' and 'username' in request.form and 'RoomID' in request.form:
        username = request.form['username']
        roomID = request.form['RoomID']
        cursor = mySQL.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute(
            'INSERT INTO UserLogin WHERE UserName = % s \
            AND RoomID = % s', (username, roomID))
    return render_template('index.html', msg=msg)

@app.route('/getMessage', methods=['GET', 'POST'])
def getMessages():
    msg = ''
    if request.method == 'GET' and 'username' in request.form and 'RoomID' in request.form and 'Messages' in request.form:
        username = request.form['username']
        roomID = request.form['RoomID']
        messages = request.form['Messages']
        time = request.form['Time']
        cursor = mySQL.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute(
            'SELECT UserName, Messages, Time FROM RoomMessages WHERE RoomID = RmID', (username, roomID, messages, time)
        )
    return render_template('index.html', msg=msg)

@app.route('/addMessage', methods=['GET', 'POST'])
def addMessages():
    msg = ''
    if request.method == 'GET' and 'username' in request.form and 'RoomID' in request.form and 'Messages' in request.form:
        username = request.form['username']
        roomID = request.form['RoomID']
        messages = request.form['Messages']
        time = request.form['Time']
        cursor = mySQL.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute(
            'INSERT INTO RoomMessages WHERE UserName = %s \ AND Messages = %s \ AND Time = %s' (username, roomID, messages, time)
        )
    return render_template('index.html', msg=msg)

if __name__ == "__main__":
    app.run(host="localhost", port=int("5000"))
