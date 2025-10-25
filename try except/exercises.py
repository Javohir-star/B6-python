#1 try:
#     a = int(input("a = "))
#     b = int(input("b = "))
#
#     print(a / b)
# except ZeroDivisionError:
#     print("Nolga bo'lish mumkin emas!")
#
# except ValueError:
#     print("Iltimos faqat raqam kiriting!")

#2 1def invert(l: list[int]):
#     try:
#         res = [n**(-1) for n in l]
#     except ZeroDivisionError:
#         print("Listingizda 0 bor ekan.")
#         return []
#
#     return res
#
# print(invert([0, 1, 2, 3, 4, 5]))
#
# 2def invert(l: list[int]):
#     res = []
#     for i in range(0, len(l)):
#         try:
#             res.append(l[i] ** (-1))
#         except ZeroDivisionError:
#             print(f"l[{i}] = 0 ekan, tashlab ketildi.")
#             continue
#
#     return res
#
# print(invert([0, 1, 2, 3, 4, 5]))

#3 try:
#     f = open("text.txt", "r")
#
#     print(f.read())
#
#     f.close()
# except FileNotFoundError:
#     print("Fayl topilmadi!")

#4 def str_to_int(l: list[str]):
#     try:
#         for i in l:
#             print(int(i), end=" ")
#     except ValueError:
#         print("Xato!")
#
# str_to_int(["8", "9", "Eshmat"])

#5 while True:
#     try:
#         a = int(input("a = "))
#
#         print("Rahmat!")
#         break
#     except ValueError:
#         print("Iltimos, son kiriting")
#         continue

#6 d = {
#     "name": "Eshmat",
#     "age": 19,
#     "city": "Tashkent"
# }
#
# try:
#     key = input("Enter key: ")
#     print(d[key])
# except KeyError:
#     print("Bunday kalit yo'q.")

#7 from typing import Callable
#
# def decorator(func: Callable):
#     def wrapper(*args, **kwargs):
#         try:
#             print("Function is being called...")
#             func(*args, **kwargs)
#             print("Function success!")
#         except Exception as e:
#             print("Calling function has exception:", e)
#
#     return wrapper
#
# @decorator
# def myfunc():
#     print(1 / 0)
#
# myfunc()

#9 l1 = [10, 15, 20, 25, 30]
# l2 = [1, 2, 3, 4, 5]
# res = []
#
# max_len = max(len(l1), len(l2))
#
# for i in range(0, max_len):
#     try:
#         res.append(l1[i] / l2[i])
#     except IndexError:
#         print(f"Ignored l[{i}]: Listlar uzunliklar turlicha ekan, uzun listdagi qolgan sonlarni ignore qilaman.")
#         break
#
# print(res)

from typing import Callable

def decorator(func: Callable):
    def wrapper(*args, **kwargs):
        try:
            for _ in range(3):
                func(*args, **kwargs)
        except Exception as e:
            print("Xatolik:", e)

    return wrapper

@decorator
def myfunc():
    print(1/1)

myfunc()
