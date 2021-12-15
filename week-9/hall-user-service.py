"""
Name: Web-335 Exercise 9.2
Author: Keith Hall
Date: 12/14/2021
Description: Query and create documents in a MongoDB database
instance through Python and pymongo.
"""
#Import built-in modules
import pymongo  #Python driver for working with MongoDB
import pprint   #Customize formatting of output
import datetime #Supplies classes to work with date and time.

#Connect to MongoDB instance using pymongo
myDatabase = pymongo.MongoClient("mongodb://localhost:27017/")
db = myDatabase.web335
myEmployees = db["employees"] #Create employees collection in web-335 database.

#Create a document
employee = {
    "first_name": "Claude",
    "last_name": "Debussy",
    "email": "cdebussy@me.com",
    "employee_id": "0000008",
    "date_created": datetime.datetime.utcnow()
}

#Insert document
newEmployee = myEmployees.insert_one(employee)

print(newEmployee)

employee = {
    "first_name": "John",
    "last_name": "Doe",
    "email": "jdoe@me.com",
    "employee_id": "000000800",
    "date_created": datetime.datetime.utcnow()
}

#Output the auto-generated user_id
user_id = db.employees.insert_one(employee).inserted_id
print(user_id)

#Find document by id using findOne()
employee_id = "000000800"
pprint.pprint(db.employees.find_one({"employee_id": employee_id}))





