import csv
import os
import pathlib
import hashlib
import random

class action():
    db = "main"
    def __init__(self,dbname):
        self.db = str(pathlib.Path(__file__).parent.resolve()) + "/" + dbname + ".db"
    def add(self,name,data):
        list = open(self.db,"r").read()
        listnew = open(self.db,"w")
        listnew.write(list + name + "," + data + "\n")  
        return "finsh"

class danger():
    def newdb(name):
        open(str(pathlib.Path(__file__).parent.resolve()) + "/" + name + ".db","w").write("name,data\n")
    def resetdb(name):
        open(str(pathlib.Path(__file__).parent.resolve()) + "/" + name + ".db","w").write("")


class database():
  def check(email,password):
    salt = os.environ['salt']
    hash = hashlib.sha512(password.encode('utf-8') + salt.encode('utf-8')).hexdigest()
    with open('user.txt', mode='r') as csv_file:
      csv_reader = csv.DictReader(csv_file)
      for row in csv_reader:
          if row["email"] == email:
            if row["password"] == hash:
              final = row["geoloup"]
            else:
              final = "no"
      try :
        return final
      except:
        return "no"
  
  def all(self):
    with open('user.geoloup.db', mode='r') as csv_file:
      csv_reader = csv.DictReader(csv_file)
      line_count = 0
      for row in csv_reader:
          if line_count == 0:
              print(f'Column names are {", ".join(row)}')
              line_count += 1
          print(f'\t{row["email"]} works in the {row["password"]}')
          line_count += 1
      print(f'Processed {line_count} lines.')
  def getuser(geoloup):
    with open('user.geoloup.db', mode='r') as csv_file:
      csv_reader = csv.DictReader(csv_file)
      for row in csv_reader:
        if row["geoloup"] == geoloup:
          js = {
            "email":row["email"],
            "name":row["name"]
          }
          final = str(js)
    return final


class user():
  salt = "9vy3v7vr8yg3ygrgnny7rueriub34newiubgerilbherbl7erin7bte4nh8ifbtret87bver7"
  def __init__(self,set_salt_key):
    self.salt = set_salt_key
  def register_user(name,passwrod):
    salt = self.salt
    hash = hashlib.sha512(password.encode('utf-8') + salt.encode('utf-8')).hexdigest()
    with open('user.geoloup.db', mode='r') as csv_file:
      csv_reader = csv.DictReader(csv_file)
      hash = hash
      for row in csv_reader:
        email2 = row["email"]
        if email2 == email:
          end = "no"
        else:
          size = random.randint(100,10000)
          geoloup = ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(size))
          end = "yes"
          list = open("user.geoloup.db","r").read()
          listnew = open("user.geoloup.db","w")
          listnew.write(list + "\n" + "geoloup_" + geoloup + "," + email + "," + name +  "," + hash)  
    return end
  def login_user(geoloup):
    with open('user.geoloup.db', mode='r') as csv_file:
      csv_reader = csv.DictReader(csv_file)
      for row in csv_reader:
        if row["geoloup"] == geoloup:
          js = {
            "email":row["email"],
            "name":row["name"]
          }
          final = str(js)
    return final