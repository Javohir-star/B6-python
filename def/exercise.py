# def max_of_three(a, b, c):
#     if a > b and a > c:
#         return a
#     elif b > c and b > a:
#         return b
#     elif c > a and c > b:
#         return c
#
# res = max_of_three(1, 2, 3)
# print(res)
from idlelib.debugobj_r import remote_object_tree_item


#12 l = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# def contains(item):
#     if item in l:
#         return True
#     else:
#         return False
#
# res = contains(7)
# print(res)


#13 def count_vowels(word):
#     vowels = ['a', 'e', 'i', 'o', 'u']
#     c = 0
#     for letter in word:
#         if letter in vowels:
#             c += 1
#     return c
#
# res = count_vowels('eshmat toshmat gulchapchap xayt salom')
# print(f"{res} ta o'nli xarf bor")


#14 def reverse_word(word):
#     return str(word[::-1])
#
# res = reverse_word("gulchapchap")
# print(res)


#16 def power(base, exp=2):
#     return base ** exp
#
# res = power(9)
# print(res)


#17 def to_celsius(fahrenheit):
#     return fahrenheit - 273.15
#
# def to_fahrenheit(celsius):
#     return celsius + 273.15
#
# res1 = to_celsius(100)
# res2 = to_fahrenheit(100)
# print("To celsius:", res1)
# print("To fahrenheit:", res2)


#18 def unique_elements(lst):
#     s = set()
#
#     for unique in lst:
#         if lst.count(unique) == 1:
#             s.add(unique)
#     return s
#
# res = unique_elements([1, 2, 2, 3, 4, 4, 5, 6, 6])
# print(res)


#19 def factorial(n):
#     m = 1
#     for i in range(1, n+1):
#         m *= i
#     return m
#
# res = factorial(5)
# print(res)


#20 def filter_positive(nums: list[int]):
#     l = []
#     for num in nums:
#         if num > 0:
#             l.append(num)
#     return l
#
# res = filter_positive([1, 6, 4, 9, -10, 2, 3])
# print(res)


#21 def sum_args(*args: tuple[int]):
#     if not args:
#         return 0
#
#     for i in args:
#         if isinstance(i, str):
#             print("String can't be used.")
#             return -1
#
#     return sum(args)
#
# print(sum_args(1, 2, 3))