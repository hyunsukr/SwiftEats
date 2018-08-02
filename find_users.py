import sqlite3
import sys

username = sys.argv[1]
password = sys.argv[2]

log = "Notlogged"

conn = sqlite3.connect('users.db')
c = conn.cursor()


c.execute('''SELECT * FROM users''')
for row in c:
    if str(row[0]) == str(username):
        if str(row[1]) == str(password):
            log = "loggedin"

conn.close()
print(log)
