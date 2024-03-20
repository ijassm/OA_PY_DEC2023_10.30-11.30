from pymongo.mongo_client import MongoClient
from bson import ObjectId, datetime
from pymongo.server_api import ServerApi
import time
from datetime import timezone


username = "Ijass"
password = "kQNCjfE3K0a3CXgn"

uri = f"mongodb+srv://{username}:{password}@python.lvsvs4f.mongodb.net/?retryWrites=true&w=majority&appName=PYTHON"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi("1"))

# Send a ping to confirm a successful connection
try:
    client.admin.command("ping")
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)


db = client["OA_PY_DEC2023"]

students = db["students"]

# Return a list of all collections in your database:

# print(db.list_collection_names())

# print(type(time.time()))
# print(time.time())

# create
# user = {
#     "firstName": "John",
#     "lastName": "Wick",
#     "email": "john@gmail.com",
#     "mobileNumber": 9876543210,
#     "countryCode": 91,
#     "age": 23,
#     "address": {
#         "doorNo": 10,
#         "street": "123 Main St",
#         "city": "Chennai",
#         "state": "Tamil Nadu",
#         "country": "India",
#         "pinCode": 600001,
#     },
#     "courses": ["Python", "Java", "C++"],
#     "createdAt": datetime.datetime.now(timezone.utc),
# }


# students.insert_one(user)


# mockDatas = [
#     {
#         "firstName": "John",
#         "lastName": "Wick",
#         "email": "john@gmail.com",
#         "mobileNumber": 9876543210,
#         "countryCode": 91,
#         "age": 23,
#         "address": {
#             "doorNo": 10,
#             "street": "123 Main St",
#             "city": "Chennai",
#             "state": "Tamil Nadu",
#             "country": "India",
#             "pinCode": 600001,
#         },
#         "courses": ["Python", "Java", "C++"],
#         "createdAt": datetime.datetime.now(timezone.utc),
#     },
#     {
#         "firstName": "Alice",
#         "lastName": "Johnson",
#         "email": "alice@gmail.com",
#         "mobileNumber": 9876543222,
#         "countryCode": 1,
#         "age": 28,
#         "address": {
#             "doorNo": 15,
#             "street": "456 Oak St",
#             "city": "New York",
#             "state": "NY",
#             "country": "USA",
#             "pinCode": 10001,
#         },
#         "courses": ["JavaScript", "HTML", "CSS"],
#         "createdAt": datetime.datetime.now(timezone.utc),
#     },
#     {
#         "firstName": "David",
#         "lastName": "Smith",
#         "email": "david@gmail.com",
#         "mobileNumber": 9876543233,
#         "countryCode": 44,
#         "age": 25,
#         "address": {
#             "doorNo": 5,
#             "street": "789 Park Ave",
#             "city": "London",
#             "state": "England",
#             "country": "UK",
#             "pinCode": "SW1A 1AA",
#         },
#         "courses": ["Ruby", "PHP", "Swift"],
#         "createdAt": datetime.datetime.now(timezone.utc),
#     },
#     {
#         "firstName": "Mia",
#         "lastName": "Johnson",
#         "email": "mia@gmail.com",
#         "mobileNumber": 9876543244,
#         "countryCode": 33,
#         "age": 22,
#         "address": {
#             "doorNo": 8,
#             "street": "567 Pine St",
#             "city": "Paris",
#             "state": "Île-de-France",
#             "country": "France",
#             "pinCode": 75001,
#         },
#         "courses": ["React", "Angular", "Vue"],
#         "createdAt": datetime.datetime.now(timezone.utc),
#     },
#     {
#         "firstName": "Chris",
#         "lastName": "Johnson",
#         "email": "chris@gmail.com",
#         "mobileNumber": 9876543255,
#         "countryCode": 61,
#         "age": 26,
#         "address": {
#             "doorNo": 12,
#             "street": "890 Maple St",
#             "city": "Sydney",
#             "state": "New South Wales",
#             "country": "Australia",
#             "pinCode": 2000,
#         },
#         "courses": ["Node.js", "Express", "MongoDB"],
#         "createdAt": datetime.datetime.now(timezone.utc),
#     },
#     {
#         "firstName": "Eva",
#         "lastName": "Davis",
#         "email": "eva@gmail.com",
#         "mobileNumber": 9876543266,
#         "countryCode": 52,
#         "age": 24,
#         "address": {
#             "doorNo": 6,
#             "street": "234 Elm St",
#             "city": "Mexico City",
#             "state": "Mexico",
#             "country": "Mexico",
#             "pinCode": 1000,
#         },
#         "courses": ["Django", "Flask", "Laravel"],
#         "createdAt": datetime.datetime.now(timezone.utc),
#     },
#     {
#         "firstName": "Sophie",
#         "lastName": "Anderson",
#         "email": "sophie@gmail.com",
#         "mobileNumber": 9876543288,
#         "countryCode": 49,
#         "age": 30,
#         "address": {
#             "doorNo": 18,
#             "street": "678 Cedar St",
#             "city": "Berlin",
#             "state": "Berlin",
#             "country": "Germany",
#             "pinCode": 10115,
#         },
#         "courses": ["Vue.js", "Sass", "Webpack"],
#         "createdAt": datetime.datetime.now(timezone.utc),
#     },
#     {
#         "firstName": "Lily",
#         "lastName": "Brown",
#         "email": "lily@gmail.com",
#         "mobileNumber": 9876543300,
#         "countryCode": 61,
#         "age": 31,
#         "address": {
#             "doorNo": 22,
#             "street": "890 Oak St",
#             "city": "Melbourne",
#             "state": "Victoria",
#             "country": "Australia",
#             "pinCode": 3000,
#         },
#         "courses": ["GraphQL", "Apollo", "Prisma"],
#         "createdAt": datetime.datetime.now(timezone.utc),
#     },
# ]

# students.insert_many(mockDatas)


# read

# query = {"_id": ObjectId("65e95f51f039d0bbd87646a3")}

# s = students.find_one(query)

# query = {"age": {"$lt": 25}}
# fields = {"_id": 0, "age": 1, "firstName": 1, "lastName": 1}

# s = students.find(query, fields)

# print(s)

# candidates = list(s)

# print(candidates)

# for i in s:
#     print(i, "\n")


# delete one

# query = {"_id": ObjectId("65e95f51f039d0bbd87646a3")}

# students.delete_one(query)

# delete many

# query = {"age": {"$lt": 25}}

# students.delete_many(query)

# for i in students.find():
#     print(i, "\n")

# update one
# query = {"_id": ObjectId("65e95f51f039d0bbd876469f")}

# update = {"$set": {"age": 30}}

# students.update_one(query, update)


# update many
# query = {"age": 25}

# update = {"$set": {"age": 30}}

# students.update_many(query, update)
