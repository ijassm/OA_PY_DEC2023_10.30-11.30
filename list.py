a = "xyz"
b = "abc"
c = "dbc"
d = "cba"

l = [3, 6, 8, 9, 4, 24]
even = []
odd = []

# print(l)
# print(l[0])
# print(l[1])
# print(l[2])
# print(l[3])
# print(l[4])
# print(l[-1])
# print(l[-2])
# print(l[-3])
# print(l[-4])
# print(l[-5])

# list are mutables

# print(l, "before")

# l[0] = 1

# print(l, "after")

# for i in l:
#     if i % 2 == 0:
#         even.append(i)
#     else:
#         odd.append(i)

count = len(l)

for i in range(count):
    if l[i] % 2 == 0:
        even.append(l[i])
    else:
        odd.append(l[i])


print("even - ", even)
print("odd - ", odd)
