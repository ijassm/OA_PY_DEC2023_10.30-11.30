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


def valueEqualToIndex(list, n):
    return [list[i] for i in range(n) if list[i] == i + 1]


print(valueEqualToIndex(l1, 5))
