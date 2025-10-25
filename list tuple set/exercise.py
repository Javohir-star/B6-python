# l = [i for i in range(5, 501)]
# print(l)
#
# l = [i for i in range(0, -101, -1)]
# print(l)
#
# l = [i for i in range(100, -101, -2)]
# print(l)


# l = ["olma", "nok", "behi", "shaftoli", "banan"]
# n = input("Yoqtirgan mevani kiriting: ")
# if n in l:
#     print("Bor")
# else:
#     print("Yo'q")


# l = ["salom", "eshmat", "world", "hi", "telefon"]
#
# for i in l:
#     if 'a' in i:
#         print(i)


# l = [1, 2, 44, 12, 66, 22, 54, 98, 12, 43]
# s = 0
#
# for i in l:
#     s += i
#
# print(s)
#
#
# l = [1, 2, 44, 12, 66, 22, 54, 98, 12, 43]
#
# max_number = l[0]
# for i in l:
#     if i > max_number:
#         max_number = i
# print(max_number)
#
#
# l = ["banana", "apple", "pear", "banana"]
# s = 0
#
# for i in l:
#     if i == "banana":
#         s += 1
#
# print(s)


# l = [i**2 for i in range(1, 11)]
# print(l)


# l = ["eshmat", "toshmat", "hi", "hello", "waaa", "gulchapchap"]
# res = [word for word in l if len(word) > 5]
# print(res)


# l = ["eshmat", "toshmat", "hi", "hello", "waaa", "gulchapchap"]
# res = [word.upper() for word in l]
# print(res)


# l = [1, 2, 3, 4, 5, 6, 1, 2]
# for i in l:
#     if l.count(i) > 1:
#         l.remove(i)
#
# print(l)