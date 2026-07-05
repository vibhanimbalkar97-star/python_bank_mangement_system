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
   
   @classmethod
   def find_user(cls, data, acc_no, pin):
      for user in data:
         if user["acc_no"] == acc_no and user["pin"] == pin:
            return user
      return None
   
   @classmethod
   def deposit(cls, acc_no, pin, amount):
      data = cls.__load_data()
      user = cls.find_user(data, acc_no, pin)

      if not user:
         return False,"Invalid account number or PIN"
      
      if amount <=0 or amount > 10000:
         return False,"Amount must be between 1 to 10000"
      
      user["balance"]+=amount
      cls.__save_data(data)
      return True,"Deposit successful"
   
   @classmethod
   def withdraw(cls, acc_no, pin, amount):
      data = cls.__load_data()
      user = cls.find_user(data,acc_no, pin)

      if not user:
         return False, "Invalid acc number or PIN"
      
      if amount <= 0 or user["balance"] < amount:
         return False, "Amount is more than available balance or negative value"
      
      user["balance"] -= amount
      cls.__save_data(data)
      return True, "Withdrawn sucessful"
   
   @classmethod
   def show_details(cls, acc_no, pin):
      data = cls.__load_data()
      user = cls.find_user(data, acc_no, pin)

      if not user:
         return False,"Invalid acc number or PIN"
      
      for details in user:
         print(f"{details} : {user[details]}")
      return True, "Details fetched successfully"

   
   @classmethod
   def update_details(cls, acc_no, pin, name=None, email=None, new_pin=None):
      data = cls.__load_data()
      user = cls.find_user(data, acc_no, pin)

      if not user:
         return False, "Invalid account number or PIN"
      
      user["name"] = name
      user["email"] = email
      user["pin"] = new_pin

      cls.__save_data(data)
      return True, "Details updated successfully"
      



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

   message = Bank.create_account(name, age, email, pin)
   print(message)

elif check == 2:
   acc_no = input("Enter account number:- ")
   pin = int(input("Enter pin:- "))
   amount = int(input("Enter amount:- "))

   message = Bank.deposit(acc_no, pin, amount)
   print(message)

elif check == 3:
   acc_no = input("Enter account number:- ")
   pin = int(input("Enter pin:- "))
   amount = int(input("Enter amount:- "))

   message = Bank.withdraw(acc_no, pin, amount)
   print(message)

elif check == 4:
   acc_no = input("Enter account number:- ")
   pin = int(input("Enter pin:- "))

   message = Bank.show_details(acc_no, pin)
   print(message)

elif check == 5:
   acc_no = input("Enter account number:- ")
   pin = int(input("Enter account pin:- "))

   data = Bank._Bank__load_data()
   user = Bank.find_user(data, acc_no, pin)

   if not user:
      print("Invalid account number or PIN")
   else:
      print("\nCurrent details")
      print("------------------------")
      print(f"Name : {user["name"]}")
      print(f"Email : {user["email"]}")
      print(f"Pin : {user["pin"]}")

      print("\nPress Enter to keep the current values ")

      name = input(f"New name ({user["name"]})")
      if name == "":
         name = user["name"]

      email = input(f"New email ({user["email"]})")
      if email == "":
         email = user["email"]

      pin_input = input("New PIN (Press Enter to keep current)")
      if pin_input == "":
         new_pin = user['pin']
      else:
         new_pin = int(pin_input)

         if len(str(new_pin)) != 4:
            print("PIN must be 4 digits")
            exit()

      success, message = Bank.update_details(acc_no, pin, name, email, new_pin)
      print(message)
      