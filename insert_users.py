import sqlite3
import sys
username = sys.argv[1]
password = sys.argv[2]
email = sys.argv[3]
phonenumber = sys.argv[4]
creditcard = sys.argv[5]
securitycode = sys.argv[6]
firstname = sys.argv[7]
lastname = sys.argv[8]
zip = sys.argv[9]

log = "True"

conn = sqlite3.connect('users.db')
c = conn.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS users (username TEXT PRIMARY KEY NOT NULL, password TEXT NOT NULL, creditcard INT NOT NULL, securitycode INT NOT NULL, firstname TEXT NOT NULL, lastname TEXT NOT NULL, zip INT, phonenumber INT NOT NULL, email TEXT)''')
c.execute('''INSERT OR IGNORE INTO users(username, password, creditcard, securitycode, firstname, lastname, zip, phonenumber, email) VALUES (?,?,?,?,?,?,?,?,?)''', ("Swiftintern", "Swift1@3$", 1234432112344321, 333, "Interns", "Best", 23455, 5404972557, "hyunsukr@gmail.com"))

c.execute('''SELECT * FROM users''')
for row in c:
    if row[0] == username:
        log = "False"

if log == "True":
    c.execute('''INSERT OR IGNORE INTO users(username, password, creditcard, securitycode, firstname, lastname, zip, phonenumber, email) VALUES (?,?,?,?,?,?,?,?,?)''', (username, password, int(creditcard), int(securitycode), firstname, lastname, int(zip), int(phonenumber), email))
    log = "made"
conn.commit()
conn.close()

print(log)
