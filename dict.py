# d = {"key": "value"}

# print(d)
# print(type(d))

student = {
    "firstName": "xyz",
    "lastName": "abc",
    "age": 20,
    "courses": ["python", "java", "c++"],
}

student["location"] = "pondy"
print(student)

student["firstName"] = "jose"
student["lastName"] = "marie"

print(student["firstName"])
print(student["lastName"])
print(student["age"])
print(student["courses"])
print(student["location"])
print(student["courses"][0])
print(student["courses"][1])
print(student["courses"][2])
