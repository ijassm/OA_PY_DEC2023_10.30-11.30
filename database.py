from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import time


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

print(type(time.time()))
print(time.time())

# create
user = {
    "firstName": "John",
    "lastName": "Wick",
    "email": "john@gmail.com",
    "mobileNumber": 9876543210,
    "countryCode": 9876543210,
    "age": 23,
    "address": {
        "doorNo": 10,
        "street": "123 Main St",
        "city": "Chennai",
        "state": "Tamil Nadu",
        "country": "India",
        "pinCode": 600001,
    },
    "courses": ["Python", "Java", "C++"],
    "createdAt": time.time(),
}


students.insert_one(user)
