import sqlite3
import sys
conn = sqlite3.connect('allFoods.db')
date = sys.argv[1]
c = conn.cursor()
c.execute('''SELECT * FROM ALLFOOD WHERE date = ?''',(date,))
l = []
for row in c:
    l.append(row)
c.execute('''SELECT * FROM ALLFOOD WHERE date = "NULL"''')
for row in c:
    l.append(row)
conn.close()
print(l)