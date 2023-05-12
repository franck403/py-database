import csv
import os
import pathlib
import hashlib
import random
import string

class action():
    db = "main"
    def __init__(self,dbname):
        self.db = str(pathlib.Path(__file__).parent.resolve()) + "/" + dbname + ".db"
    def add(self,name,data):
        list = open(self.db,"r").read()
        listnew = open(self.db,"w")
        listnew.write(list + name + "," + data + "\n")  
        return "finsh"
    def get(self,name):
      with open(self.db, mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        final = ""
        for row in csv_reader:
          if row['name'] == name:
            final = row
      return final
    def all(self):
      with open(self.db, mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        line_count = 0
        alldatabase = []
        for row in csv_reader:
          line_count += 1
          alldatabase.append(row["name"])
          alldatabase.append(row["data"])
      return alldatabase
    def replace(self,name,data):
      final = "error this not exisit"
      with open(self.db, mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        line_count = 0
        line_modify = line_count
        for row in csv_reader:
          if row['name'] != name:
            line_count =  line_count + 1
          else:
            line_modify = line_count
      with open(self.db, 'r', encoding='utf-8') as file:
          datam = file.readlines()
      if line_modify == 0:
        datam[line_modify] = name + "," + data + "\n"
        with open(self.db, 'w', encoding='utf-8') as file:
            file.writelines(datam)
        with open(self.db, mode='r') as csv_file:
          csv_reader = csv.DictReader(csv_file)
          for row in csv_reader:
            if row['name'] == name:
              final = row
      return final


class danger():
  def newdb(name):
    open(str(pathlib.Path(__file__).parent.resolve()) + "/" + name + ".db","w").write("name,data\n")
  def resetdb(name):
    open(str(pathlib.Path(__file__).parent.resolve()) + "/" + name + ".db","w").write("")



class user():
  salt = "9vy3v7vr8yg3ygrgnny7rueriub34newiubgerilbherbl7erin7bte4nh8ifbtret87bver7"
  geoloup = "default user name"
  def __init__(self,set_salt_key):
    self.salt = set_salt_key
  def check(self,email,password):
    salt = self.slat
    hash = hashlib.sha512(password.encode('utf-8') + salt.encode('utf-8')).hexdigest()
    with open(str(pathlib.Path(__file__).parent.resolve()) + "/" + 'user.geoloup.txt', mode='r') as csv_file:
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
  def register_user(self,name,password):
    salt = self.salt
    hash = hashlib.sha512(password.encode('utf-8') + salt.encode('utf-8')).hexdigest()
    with open(str(pathlib.Path(__file__).parent.resolve()) + "/" + 'user.geoloup.db', mode='r') as csv_file:
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
          list = open(str(pathlib.Path(__file__).parent.resolve()) + "/" + "user.geoloup.db","r").read()
          listnew = open(str(pathlib.Path(__file__).parent.resolve()) + "/" + "user.geoloup.db","w")
          listnew.write(list + "\n" + "geoloup_" + geoloup + "," + email + "," + name +  "," + hash)  
          self.geoloup = geoloup
    return self.geoloup
  def login_user(user_id):
    with open(str(pathlib.Path(__file__).parent.resolve()) + "/" + 'user.geoloup.db', mode='r') as csv_file:
      csv_reader = csv.DictReader(csv_file)
      for row in csv_reader:
        if row["geoloup"] == geoloup:
          js = {
            "email":row["email"],
            "name":row["name"]
          }
          final = str(js)
    return final
