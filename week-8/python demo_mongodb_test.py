import pymongo #Python driver for working with MongoDB

myclient = pymongo.MongoClient('mongodb://localhost:27017/') #MongoDB connection

mydb = myclient['mydatabase']
mycol = mydb["customers"]

mydict = { "name": "John", "address": "Highway 37" }

x = mycol.insert_one(mydict)

print(x)

