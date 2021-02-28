# # import collections
# #
# # s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
# d = {
# }
#
# for i in range(5):
#     d[i] = str(i+1)
#
# # print(d)
#
# dict = {}
# i = 0
# while d != {}:
#     print("before")
#     print(d)
#     print("aww")
#     print(i)
#     d.pop(i)
#     print("after")
#     print(d)
#     i += 1

arr = [['C1', 'C3'], ['C2', 'C1', 'C4'], ['C3'], ['C4', 'C1', 'C3'], ['C5', 'C2', 'C4']]
def delete_arr(arr,take):
    for content in arr:
        course = content[0]
        if course == take:
            arr.remove(content)
    return arr
i = 0
for content in arr:


    delete_arr(arr, ['C3'])
    print(arr)
    print(content[i])
    print("1")
temp = [[] for i in range(40)]
take = 'C3'
print(temp)

# while
#     i = -1
#     for content in arr:
#         i += 1
#         print("before")
#         # course = content[0]
#         # print(course)
#         course = content[0]
#         print(course)
#         temp[i].append(course)
#         # print(arr)
#         # delete_arr(arr,take)
#         # print("after")
#         # print(arr)
#
#
#
#     # index = arr.index([])
#     # print(index)
#     # # del arr[]
# #     # print(arr)
# # print("hoyy")
# # print(arr)
# print(temp)