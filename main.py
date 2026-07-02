from pathlib import Path
import json

class Bank:
   # create dummy data
   database='data.json'
   data=[]

   # open databse file
   try:
      if Path(database).exists():
         with open(database) as fs:
            data = json.loads(fs.read())
      else:
         print("No such file")
   except Exception as err:
      print(f"An error occurred as {err}")

      @classmethod
      def __update(cls):
         with open(cls.database, "w") as fs:
            fs.write(json.dumps(Bank.data))

   def createaccount(self):
      info = {
         "name": input("Tell your name:- "),
         "age": int(input("Tell your age:- ")),
         "email": input("Tell your email:- "),
         "pin": int(input("Tell your 4 number pin:- ")),
         "accountnumber": 1234,
         "balance": 0
      }
      if info["age"] < 18 or len(str(info["pin"])) != 4:
         print("Sorry you can not create your account")
      else:
         print("Your account created successfully")
         # show the info
         for i in info:
            print(f"{i} : {info[i]}")
         print("Please note down your account number")
         
         Bank.data.append(info)

         Bank.__update()
user = Bank()




print("Press 1 for creating an account:- ")
print("Press 2 for depositing money in the bank:- ")
print("Press 3 for withdrawing money:- ")
print("Press 4 for details:- ")
print("Press 5 for updating the details:- ")
print("Press 6 for deleting the details:- ")

check = int(input("Tell your response:- "))

if check == 1:
   user.createaccount() 
