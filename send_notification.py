import sys
import sqlite3
from twilio.rest import Client
username = sys.argv[1]
items = sys.argv[2]

conn = sqlite3.connect('users.db')

c = conn.cursor()
c.execute('''SELECT phonenumber,firstname, lastname FROM users WHERE username = ?''',(username,))
items = items.replace("+", " ")
items = items.replace("%3C%2Fbr%3E", "")
items = items.replace("item", "")
items = items.replace("&", " ")
items = items.replace("=selected", ", ")
items = items.replace("%26", "&")
items= items.replace("%2F", "/")

name = ""
orderName = items
phoneNumber = ""



for row in c:
    name = row[1].replace("+", " ") + ' ' + row[2].replace("+", " ")
    phonenumber = row[0]

conn.close()


# Your Account SID from twilio.com/console
account_sid = "ACfe5d1bbd16d795677bcd845ae605b441"
# Your Auth Token from twilio.com/console
auth_token  = "2c834a619fa4be2529a65f98a4a72110"

client = Client(account_sid, auth_token)

message = client.messages.create(
	to="+1"+str(phonenumber),
	from_="+12409701006",
    
	body= "Hello, " + name + "! Your order "  + orderName + " will be ready for pickup in 15 minutes")

print(message.sid)
