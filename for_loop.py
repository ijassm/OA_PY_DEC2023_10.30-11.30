# What is loop in basic programming?

# In computer Programming, a Loop is used to execute a group of instructions or a block of code multiple times, without writing it repeatedly. The block of code is executed based on a certain condition.
# Loops are the control structures of a program.

# range(start,stop, step)
# range(10) start - 0 | stop - 10 | step - 1
# range(2,10) start - 2 | stop - 10 | step - 1
# range(2,10,2) start - 2 | stop - 10 | step - 2

# for i in range(1,101):
#     print("hello",i)

# for i in range(1,101):
#     if(i % 2 == 0):
#         print("hello", i)
#     else:
#         print("bye", i)

# for i in range(1, 5):
#     print(i, end=" ")
#     if i % 2 == 0:
#         print()


# print("hello1", end="")
# print("welcome", end="")
# print("python")


# for i in range(1, 26):
#     print("{:2d}".format(i), end=" ")
#     if i % 5 == 0:
#         print()


# for i in range(1, 3):
#     for j in range(1, 3):
#         for k in range(1, 4):
#             print(i, j, k)

# i = 1
# j = 1 | j = 2

# i = 2
# j = 1 | j = 2

for i in range(5):
    for j in range(5):
        print("*", end=" ")
    print()
