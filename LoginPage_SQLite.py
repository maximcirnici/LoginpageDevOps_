import pyotp #generates python library one-time passwords
import sqlite3 #database for username/passwords
import hashlib #secure hashes and message digests
import uuid #for creating universally unique identifiers
from flask import Flask, request, render_template
app = Flask(__name__)
#aanmaken van database met de naam ''
db_name = 'users.db'

@app.route('/')
def index():
    return render_template("login.html")



#Dit bekijkt als de gebruiker wel bestaat
#Hiervoor kijkt de code naar de functie 'verifie_hash'
@app.route('/')
@app.route('/login', methods=['GET', 'POST'])
def login_v2():
    error = None
    if request.method == 'POST':
        if verify_hash(request.form['username'], request.form['password']):
            error = 'Login successful ! '
        else:
            error = 'Invalid username/password'
    else:
        error = 'Invalid Method'
    return error

#Dit maakt een nieuwe gebruiker in de de databank
@app.route('/')
@app.route('/register', methods=['POST'])
def signup():
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS USER_HASH (USERNAME TEXT PRIMARY KEY NOT NULL, HASH TEXT NOT NULL);''')
    conn.commit()
    try:
        hash_value = hashlib.sha256(request.form['password2'].encode()).hexdigest()
        c.execute("INSERT INTO USER_HASH (USERNAME,HASH)" "VALUES ('{0}', '{1}')".format(request.form['username2'], hash_value))
        conn.commit()
    except sqlite3.IntegrityError:
        return "username already taken !"
    print('username: ', request.form['username2'], ' password: ',request.form['password2'], ' hash: ', hash_value)
    return "You have been successfully registreded !"


def verify_hash(username, password):
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    query = "SELECT HASH FROM USER_HASH WHERE USERNAME = '{0}'".format(username)
    c.execute(query)
    records = c.fetchone()
    conn.close()
    if not records:
        return False
    return records[0] == hashlib.sha256(password.encode()).hexdigest()



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050)



