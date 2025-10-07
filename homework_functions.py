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


#22 def multiply_args(*args: tuple[int]):
#     if not args:
#         return 0
#
#     for i in args:
#         if isinstance(i, str):
#             print("String can't be used.")
#             return -1
#
#     m = 1
#     for i in args:
#         m *= i
#     return m
#
# print(multiply_args(1, 2, 3))


#23 def student_info(name, age, **details):
#     print(f"Name: {name}")
#     print(f"Age: {age}")
#     for key, value in details.items():
#         print(f"{key}: {value}")
#
# student_info("Ali", 21, grade="A", country="Uzbekistan")


#24 def describe_pet(animal, name="Unknown"):
#     return f"{name}: {animal}"
#
#
# print(describe_pet(animal="dog", name="Rex"))


#25 def average(*numbers):
#     return sum(numbers) / len(numbers) if numbers else 0
#
# print(average(2, 4, 6))


#26 def print_dict(**kwargs):
#     for k, v in kwargs.items():
#         print(f"{k}: {v}")
#
# print_dict(name="Ali", age=21, country="Uzbekistan")


#27 def show_data(*args, **kwargs):
#     print("Args:", args)
#     print("Kwargs:", kwargs)
#
# show_data(1, 2, 3, name="Javohir", age=21)


#28 def calculate(*args, operation="sum"):
#     if operation == "sum":
#         return sum(args)
#     elif operation == "multiply":
#         m = 1
#         for i in args:
#             m *= i
#         return m
#
# print(calculate(2, 3, 4, operation="multiply"))


#29 def custom_greet(name, **options):
#     prefix = options.get("prefix", "Hello")
#     suffix = options.get("suffix", "")
#     return f"{prefix} {name}{suffix}"
#
#
# print(custom_greet("Ali", prefix="Dear", suffix="!"))


#31 def square_all(nums):
#     return [n ** 2 for n in nums]
#
# print(square_all([1, 2, 3]))


#32 def invert_dict(d):
#     return {v: k for k, v in d.items()}
#
# print(invert_dict({'a': 1, 'b': 2}))


#33 def common_elements(set1, set2):
#     return set1.intersection(set2)
#
# print(common_elements({1, 2, 3}, {2, 3, 4}))


#34 def list_to_tuple(lst):
#     return tuple(lst)
#
# print(list_to_tuple([1, 2, 3]))


#35 def find_key(d, value):
#     for k, v in d.items():
#         if v == value:
#             return k
#
# print(find_key({'a': 1, 'b': 2}, 2))


#36 def filter_even(numbers):
#     return [n for n in numbers if n % 2 == 0]
#
# print(filter_even([1, 2, 3, 4, 5, 6]))


#37 def longest_word(words):
#     return max(words, key=len)
#
# print(longest_word(["apple", "banana", "pear"]))


#38 def merge_dicts(d1, d2):
#     m = d1.copy()
#     m.update(d2)
#     return m
#
# print(merge_dicts({'a': 1, 'b': 2}, {'b': 3, 'c': 4}))


#39 def unique_count(lst):
#     return len(set(lst))
#
# print(unique_count([1, 2, 2, 3, 3, 3, 4]))


#40 def list_to_set(lst):
#     return set(lst)
#
# print(list_to_set([1, 2, 2, 3, 3, 3]))


#41 def is_prime(n):
#     if n < 2:
#         return False
#     for i in range(2, int(n ** 0.5) + 1):
#         if n % i == 0:
#             return False
#     return True
#
# print(is_prime(7))


#42 def is_palindrome(s):
#     s = s.lower()
#     return s == s[::-1]
#
# print(is_palindrome("Level"))


#45 def sort_by_length(words):
#     return sorted(words, key=len)
#
# print(sort_by_length(["apple", "kiwi", "banana"]))


#46 def max_value(d):
#     return max(d, key=d.get)
#
# print(max_value({'Ali': 90, 'Sami': 85, 'Laylo': 95}))


#47 def is_valid_email(email):
#     return '@' in email and  '.' in email
#
# print(is_valid_email("test@mail.com"))


#48 def outer_function(x):
#     def inner_function(y):
#         return x + y
#     return inner_function(5)
#
# print(outer_function(10))


#49 def custom_filter(numbers, condition):
#     return [n for n in numbers if condition(n)]
#
# def is_even(x):
#     return x % 2 == 0
#
# print(custom_filter([1, 2, 3, 4, 5, 6], is_even))


#50 def average_grades(grades_dict):
#     result = {}
#     for k, v in grades_dict.items():
#         result[k] = sum(v) / len(v)
#     return result
#
# grades = {"Ali": [90, 80, 85], "Sami": [70, 75, 72]}
# print(average_grades(grades))
