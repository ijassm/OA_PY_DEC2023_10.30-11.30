# def greeting():
#     print("Hello World!")


# greeting()
# greeting()
# print("Hello")
# greeting()

# l1 = [1, 2, 3, 4]
# l2 = [45, 6, 3]


# def sum(arr):
#     result = 0
#     for i in arr:
#         result += i
#     return result


# print(sum(l1))
# print(sum(l2))

l1 = [1, 2, 2, 3, 4]
l2 = [45, 6, 3]
l3 = [1]
l4 = [15, 2, 45, 12, 7]
l5 = [15, 3, 45, 12, 7]


# def valueEqualToIndex(list):
#     newList = []
#     l = len(list)
#     for i in range(l):
#         index1Based = i + 1
#         element = list[i]
#         if element == index1Based:
#             newList.append(list[i])
#     return newList


# print(valueEqualToIndex(l2))
# print(valueEqualToIndex(l3))
# print(valueEqualToIndex(l4))
# print(valueEqualToIndex(l5))


# def valueEqualToIndex(list, n):
#     return [list[i] for i in range(n) if list[i] == i + 1]


# print(valueEqualToIndex(l1, 5))

# Types of Arguments
# Arguments are specified after the function name, inside the parentheses


# def my_function(fname):
#     print(fname + " Refsnes")


# my_function("Emil")
# my_function("Tobias")
# my_function("Linus")


# Parameters or Arguments?

# From a function's perspective:

# A parameter is the variable listed inside the parentheses in the function definition.

# An argument is the value that are sent to the function when it is called.

# Arbitrary Arguments, *args


# def sum(*values):
#     print(values)
#     s = 0
#     for i in values:
#         s += i

#     return s


# print(sum(2, 5))
# print(sum(2, 5, 7))
# print(sum(2, 5, 7, 2))


# Keyword Arguments & Default Parameter Value


# def my_function(name, age, location="pondy"):
#     print("Name is", name)
#     print("Age is", age)
#     print("Location is", location)


# my_function(location="chennai", name="xyz", age=10)
# my_function(name="xyz", age=10)


# Arbitrary Keyword Arguments, **kwargs


# def my_function(**person):
#     print("Name is", person["name"])
#     print("Age is", person["age"])
#     print("Location is", person["location"])


# my_function(location="chennai", name="xyz", age=10)
