 #Import built-in modules
import pymongo  #Python driver for working with MongoDB
import pprint   #Customize formatting of output
import datetime #Supplies classes to work with date and time.

myDatabase = pymongo.MongoClient("mongodb://localhost:27017/")
db = myDatabase.web335
myEmployees = db["employees"]

employee = {
    "first_name": "Claude",
    "last_name": "Debussy",
    "email": "cdebussy@me.com",
    "employee_id": "0000008",
    "date_created": datetime.datetime.utcnow()
}

newEmployee = myEmployees.insert_one(employee)

print(newEmployee)

employee = {
    "first_name": "John",
    "last_name": "Doe",
    "email": "jdoe@me.com",
    "employee_id": "000000800",
    "date_created": datetime.datetime.utcnow()
}

user_id = db.employees.insert_one(employee).inserted_id
print(user_id)

employee_id = "000000800"
pprint.pprint(db.employees.find_one({"employee_id": employee_id}))





