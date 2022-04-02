from distutils.log import debug
from multiprocessing import connection
import sqlite3
from flask import Flask,render_template,request,url_for, session
import re
from flask import render_template

app=Flask(__name__)
app._static_folder = r"C:\Users\Sanjay Kumar\flask\login-page\static"
app.secret_key = '__privatekey__'
connection =sqlite3.connect("user1.db")
cursor = connection.cursor()


@app.route('/')
def test():
    connection =sqlite3.connect("user1.db")
    cursor = connection.cursor()
    return render_template("home.html")
@app.route('/home', methods =['GET', 'POST'])
def home():
    connection =sqlite3.connect("user1.db")
    cursor = connection.cursor()
    msg = ''
    if request.method == 'POST' and 'email' in request.form and 'password' in request.form:
        email = request.form['email']
        password = request.form['password']
        
        cursor.execute('SELECT * FROM users WHERE emailaddress = ? AND password = ?', (email, password, ))
        account = cursor.fetchone()
        if account:
            # session['loggedin'] = True
            session['email'] = account[1]
            session['password'] = account[3]
            msg = 'Logged in successfully !'
            print(msg)
            return render_template('index.html', msg = msg)
        else:
            msg = 'Incorrect username / password !'
            print(msg)
            return render_template('error.html', msg = msg)
    return render_template('home.html', msg = msg)
    

@app.route('/register', methods =['GET', 'POST'])
def register():
    msg = ''
    if request.method == 'POST' and 'full-name' in request.form and 'nid-number' in request.form and 'email-address' in request.form and 'phone_number' in request.form :
        username = request.form['full-name']
        Email = request.form['email-address']
        Phonno = request.form['phone_number']
        password = request.form['nid-number']
        
        
        
        con =sqlite3.connect("user1.db")
        cursor = con.cursor()
        # cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        # cursor.execute('SELECT * FROM users WHERE username = % s', (username, ))
        chk=f"SELECT * FROM users WHERE name = '{username}' AND password='{password}' AND emailaddress='{Email}' AND phonenumber='{Phonno}'"
        cursor.execute(chk)
        account = cursor.fetchone()
        if account:
            msg = 'Account already exists !'
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', Email):
            msg = 'Invalid email address !'
        elif not re.match(r'[A-Za-z0-9]+', username):
            msg = 'Username must contain only characters and numbers !'
        elif not username or not password or not Email:
            msg = 'Please fill out the form !'
        else:
            #cursor.execute('INSERT INTO users VALUES (?, ?, ?, ?)', (username, Email,Phonno,password ))
            cursor.execute('INSERT OR REPLACE INTO users VALUES (?, ?, ?, ?)', (username, Email,Phonno,password ))

            con.commit()
            msg = 'You have successfully registered !'
    elif request.method == 'POST':
        msg = 'Please fill out the form !'
    return render_template('register.html', msg = msg)


   

    

# cursor.execute("INSERT INTO users (name,password) VALUES ('Rishab', '123')")
# cursor.execute("INSERT INTO users (name,password) VALUES ('sanjay', '777')")
connection.commit()

if __name__=="__main__":
    app.run(debug=True)