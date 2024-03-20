# print(3 / 0)

try:
    # print(3 / 2)
    # print(name)
    print(5 + "3")
except ZeroDivisionError:
    print("can't divide by zero")
except NameError:
    print("variable must be declared")
except Exception as e:
    print("something error occurred", e)
else:
    print("else block finished")
finally:
    print("finally block finished")
