import csv
import os
import pathlib

class action():
    db = "main"
    def __init__(self,dbname):
        self.db = str(pathlib.Path(__file__).parent.resolve()) + "/" + dbname + ".db"
    def add(self,name,data):
        list = open(self.db,"r").read()
        listnew = open(self.db,"w")
        listnew.write(list + name + "," + data)  
        return "finsh"

class danger():
    def newdb(name):
        open(name + ".db","w").write("name,data\n")
    def resetdb(name):
        open(name + ".db","w").write("")


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
  
  def all():
    with open('user.txt', mode='r') as csv_file:
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
    with open('user.txt', mode='r') as csv_file:
      csv_reader = csv.DictReader(csv_file)
      for row in csv_reader:
        if row["geoloup"] == geoloup:
          js = {
            "email":row["email"],
            "name":row["name"]
          }
          final = json.dumps(js)
 
    return final
