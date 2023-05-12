import py-database
from py-database import server

db = py-database

db.danger.newdb("test")
action = db.action("test")
action.add("test","text")
print(action.all())

user = db.user("g7y7y75nnv4oth7777888777777om77g8ju")
user.register_user("test","test")

server.run()