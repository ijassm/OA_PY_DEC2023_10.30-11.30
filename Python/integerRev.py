value = 123
rev = 0

# lastNum = value % 10
# rev = rev * 10 + lastNum
# value = value // 10

# lastNum = value % 10
# rev = rev * 10 + lastNum
# value = value // 10

# lastNum = value % 10
# rev = rev * 10 + lastNum
# value = value // 10

# lastNum = value % 10
# rev = rev * 10 + lastNum
# value = value // 10


while value != 0:
    lastNum = value % 10
    rev = rev * 10 + lastNum
    value = value // 10


print(value, "value")
print(rev, "rev")
