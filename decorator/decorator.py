# from typing import Callable
# import time
#
# count = 0
#
# def decorator(func: Callable):
#     def wrapper(*args, **kwargs):
#         print("Starting...")
#         time.sleep(0.5)
#         func(*args, **kwargs)
#         print("Done!")
#     return wrapper
#
# @decorator
# def myfunc():
#     global count
#     count += 1
#
# myfunc()
# myfunc()
# print(count)

# from typing import Callable
# import time
#
# count = 0
#
# def decorator(func: Callable):
#     def wrapper(*args, **kwargs):
#         print(func.__name__)
#         func(*args, **kwargs)
#     return wrapper
#
# @decorator
# def myfunc():
#     print("Hello")
#
# myfunc()

# from typing import Callable
#
# def decorator(func: Callable):
#     def wrapper(s):
#         if not s:
#             print("Empty!")
#             return
#         func(s)
#     return wrapper
#
# @decorator
# def myfunc(name):
#     print(f"Hello {name}")
#
# myfunc("A")

# from typing import Callable
#
# def decorator(func: Callable):
#     def wrapper(n: int):
#         if n < 0:
#             print("Negative")
#             return
#         func(n)
#     return wrapper
#
# @decorator
# def myfunc(name: int):
#     print(f"Positive, {name}")
#
# myfunc(-1)

# from typing import Callable
#
# def decorator(func: Callable):
#     def wrapper(*args, **kwargs):
#         l = args[0]
#         func(*args, **kwargs)
#     return wrapper
#
# @decorator
# def myfunc(lst: list[int]):
#     print(list(set(lst)))
#
# myfunc([1, 2, 2 ,3])

# from typing import Callable
#
# def decorator(func: Callable):
#     def wrapper(*args, **kwargs):
#         l = args[0]
#         for i in sorted(l):
#             print(i, end=' ')
#         func(*args, **kwargs)
#     return wrapper
#
# @decorator
# def myfunc(n):
#     print()
#
# myfunc([4, 2, 2 ,3])

# from typing import Callable
#
# def decorator(func: Callable):
#     def wrapper(*args, **kwargs):
#         l = args[0]
#         for i in l:
#             if i < 0:
#                 print("Negative")
#                 return
#         func(*args, **kwargs)
#     return wrapper
#
# @decorator
# def myfunc(n):
#     print()
#
# myfunc([4, 2, 2 ,-3])

#1_hard import time
#
# def our_cache(func):
#     last_calls = dict()
#     def wrapper(*args, **kwargs):
#         nonlocal last_calls
#         print(last_calls)
#         s = args[0]
#         if s in last_calls:
#             time.sleep(1)
#             return last_calls[s]
#         else:
#             res = func(s)
#             if len(last_calls) > 2:
#                 last_calls.pop(list(last_calls.keys())[0])
#             last_calls[s] = res
#
#         return wrapper
#
# @our_cache
# def my_func(s:str):
#     print("Working...")
#     time.sleep(4)
#     return f"Hi {s}!"
#
# print(my_func("Hello"))
# print(my_func("Hello"))