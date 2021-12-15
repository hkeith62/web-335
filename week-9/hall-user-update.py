"""
Name: Web-335 Exercise 9.3
Author: Keith Hall
Date: 12/14/2021
Description: Update and delete documents in a MongoDB database
instance through Python and pymongo.
"""
#Import built-in modules
import pymongo  #Python driver for working with MongoDB
import pprint   #Customize formatting of output
import datetime #Supplies classes to work with date and time.

#Connect to MongoDB instance using pymongo
myDatabase = pymongo.MongoClient("mongodb://localhost:27017/")
db = myDatabase.web335

#Update email by employee_id
db.employees.update_one(
    {"employee_id": "0000008"},
    {
        "$set": {
            "email": "kmhall@my365.bellevue.edu" #Update using developers Bellevue email.
        }
    }
)
#Find employees document by id and check to see if email has been updated.
pprint.pprint(db.employees.find_one({"employee_id": "0000008"}))

#Output the following fields
pprint.pprint(db.employees.find_one({}, {"_id": 0, "employee_id": 1}))
pprint.pprint(db.employees.find_one({}, {"_id": 0, "first_name": 1}))
pprint.pprint(db.employees.find_one({}, {"_id": 0, "last_name": 1}))
pprint.pprint(db.employees.find_one({}, {"_id": 0, "email": 1}))

#Output all first_name fields
for x in db.employees.find({}, { "_id": 0, "first_name": 1}):
  print(x)






