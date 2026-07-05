from pathlib import Path
import json
import random
import string

class Bank:
   database = 'data.json'

   @classmethod
   def __load_data(cls):
      if Path(cls.database).exists():
         with open(cls.database, "r") as fs:
            try:
               return json.load(fs)
            except Exception as err:
               print(f"An error occurred as {err}")
               return []
      return []
   
   @classmethod
   def __save_data(cls, data):
      with open(cls.database, "w") as fs:
         json.dump(data, fs, indent=4)

   @classmethod
   def __generate_acc_number(cls):
      data = cls.__load_data()
      while True:
         chars = (random.choices(string.ascii_letters, k=3) + \
                 random.choices(string.digits, k=3) + \
                 random.choices("!@#$%^&*", k=1))
         random.shuffle(chars)
         acc_no = "".join(chars) 
         
         for user in data:
            if user["acc_no"] == acc_no:
               break
         else:
               return acc_no
             
             
   
   @classmethod
   def create_account(cls, name, age, email, pin):
      data = cls.__load_data()
      if age < 18 or len(str(pin)) != 4:
         return None, "Age must be 18+ and pin should be 4 digits"
      acc_no = cls.__generate_acc_number()
      user = {
         "name":name,
         "age":age,
         "email":email,
         "acc_no":acc_no,
         "pin":pin,
         "balance":0
      }
      data.append(user)
      cls.__save_data(data)   
      return user, "Account created successfully" 
            

print("Press 1 for creating an account:- ")
print("Press 2 for depositing money in the bank:- ")
print("Press 3 for withdrawing money:- ")
print("Press 4 for details:- ")
print("Press 5 for updating the details:- ")
print("Press 6 for deleting the details:- ")

check = int(input("Tell your response:- "))

if check == 1:
   name = input("Enter your name: ")
   age = int(input("Enter your age: "))
   email = input("Enter your email: ")
   pin = int(input("Enter 4-digit PIN: "))

   user, message = Bank.create_account(name, age, email, pin)
   print(message)
   print(user)

elif check == 2:
   acc_no = input("Enter your account number")
   pin = int(input("Enter your pin"))

 




