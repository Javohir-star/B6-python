#1 def greet():
#     return "Hello"
#
# g = greet
# print(g())

#2 def add(a, b):
#     return a + b
# def subtract(a, b):
#     return a - b
#
# func = [add, subtract]
# for f in func:
#     print(f(10, 5))

#3 operations = {
#     "add": lambda a, b: a + b,
#     "sub": lambda a, b: a - b,
#     "mul": lambda a, b: a * b
# }
# choice = "mul"
# print(operations[choice](3, 4))

#4 m = [lambda x, n=n: x * n for n in range(1, 6)]
# for f in m:
#     print(f(10))

#5 from typing import Callable
# def apply(func: Callable, value: int):
#     return func(value)
#
# print(apply(lambda x: x ** 2, 5))

#6 from typing import Callable
# def operate_two(func: Callable, a: int, b: int):
#     return func(a, b)
#
# print(operate_two(lambda x, y: x * y, 4, 5))

#7 numbers = [1, 2, 3, 4, 5]
# square = lambda x: x ** 2
# for n in numbers:
#     print(square(n))

#8 string_funcs = [
#     lambda s: s.upper(),
#     lambda s: s.lower(),
#     lambda s: s.title()
# ]
#
# for f in string_funcs:
#     print(f("python"))


#9 funcs_tuple = (lambda x: x + 5,
#                lambda x: x + 10,
#                lambda x: x + 15)
# for f in funcs_tuple:
#     print(f(20))

#10 def choose(condition):
#     if condition:
#         return lambda x: x+10
#     else:
#         return lambda x: x-10
#
# func = choose(True)
# print(func(1))

#11 def operate(a, b, operation):
#     return operation(a, b)
#
# print(operate(5, 3, lambda x, y: x + y))

#12 def make_multiplier(n):
#     return lambda x: x * n
#
# double = make_multiplier(2)
# print(double(10))

#13 def select_function(operation):
#     if operation == 'square':
#         return lambda num: num * num
#     elif operation == 'cube':
#         return lambda num: num * num * num
#     elif operation == 'double':
#         return lambda num: num * 2
#
# res = select_function('cube')
# print(res(5))

#14 def filter_even(func, num):
#     return [n for n in num if func(n)]
#
# print(filter_even(lambda x: x % 2 == 0, [1, 2, 3, 4, 5, 6]))

#16 names = ["Ali", "Vali", "Soli"]
# def apply_to_names(func, lst):
#     return [func(n) for n in lst]
#
# print(apply_to_names(str.upper, names))

#17 def conditional_apply(num, func_true, func_false):
#     return [func_true(n) if n % 2 == 0 else func_false(n) for n in num]
#
# print(conditional_apply([1,2,3,4], lambda x: x*2, lambda x: x+1))

# from typing import Callable
#
# def repeater(func: Callable, n: int):
#     def inner():
#         for _ in range(n):
#             func()
#     return inner
#
# def say_hi():
#     return "Hi"
#
# print(repeater(say_hi, 3)())

#20 def choose_operator(symbol):
#     ops = {
#         '+': lambda a,b: a+b,
#         '-': lambda a,b: a-b,
#         '*': lambda a,b: a*b,
#         '/': lambda a,b: a/b
#     }
#     return ops[symbol]
#
# print(choose_operator('*')(3,4))

#21 words = ["cat", "elephant", "dog", "ant"]
# print(sorted(words, key=lambda w: len(w)))

#22 people = [("Alice", 25), ("Bob", 19), ("Carol", 30)]
# print(sorted(people, key=lambda p: p[1]))

#23 tuples = [(1,2), (3,4), (5,6)]
# print(list(map(lambda t: t[0], tuples)))

#24 print(list(map(lambda s: s[::-1], ["one", "two", "three"])))

#25 nums = [1,2,3,4,5,6,9,10,15]
# print(list(filter(lambda x: x % 3 == 0 or x % 5 == 0, nums)))

#26 products = {"apple": 5, "banana": 3, "cherry": 8}
# print({k:v for k,v in products.items() if (lambda x: x>4)(v)})

#27 strings = ["a", "b", "c"]
# print(list(map(lambda s: s.upper(), strings)))

#28 numbers = [-2, -1, 0, 1, 2]
# print(list(map(lambda x: 0 if x<0 else x, numbers)))

#29 cities = [("Tashkent", 3000000), ("Samarkand", 700000), ("Bukhara", 600000)]
# print(sorted(cities, key=lambda x: x[1], reverse=True))

#30 def apply_all(funcs, value):
#     return [f(value) for f in funcs]
#
# print(apply_all([lambda x: x+1, lambda x: x*2, lambda x: x**2], 3))

#31 even_odd = lambda x: "Even" if x % 2 == 0 else "Odd"
# print(even_odd(7))

#32 nums = [1,2,3,4,5,6]
# labels = [(lambda x: "Even" if x % 2 == 0 else "Odd")(n) for n in nums]
# print(labels)

#33 strings = ["apple", "banana", "orange", "pear"]
# print(list(filter(lambda s: s[0].lower() in 'aeiou', strings)))

#34 def print_condition(nums, cond):
#     for n in nums:
#         if cond(n):
#             return n
#
# res = print_condition([1,2,3,4,5], lambda x: x>3)
# print(res)

#35 def count_condition(lst, cond):
#     return sum(1 for x in lst if cond(x))
#
# print(count_condition([1,2,3,4,5], lambda x: x%2==0))

#36 def factorial(n):
#     natija = 1
#     for i in range(1, n + 1):
#         natija *= i
#     return natija
#
# factorials = [factorial(i) for i in range(1, 6)]
# print(factorials)

#37 is_palindrome = lambda s: s.lower() == s[::-1].lower()
# print(is_palindrome("Level"))

#40 is_prime = lambda n: n>1 and all(n%i!=0 for i in range(2, int(n**0.5)+1))
# print(is_prime(17))

#41 def make_power(n):
#     return lambda x: x**n
#
# square = make_power(2)
# print(square(5))

#42 def apply_chain(funcs, value):
#     for f in funcs:
#         value = f(value)
#     return value
#
# print(apply_chain([lambda x:x+2, lambda x:x*3], 5))

#43 def chain(func1, func2):
#     return lambda x: func2(func1(x))
#
# double_then_square = chain(lambda x:x*2, lambda x:x**2)
# print(double_then_square(3))

#44 def make_counter():
#     count = 0
#     def counter():
#         nonlocal count
#         count += 1
#         return count
#     return counter

#45 def string_repeater(s):
#     return lambda n: s * n
#
# repeat_hello = string_repeater("Hi")
#
# c = make_counter()
# print(c(), c(), c())
# print(repeat_hello(3))

#46 def choose_lambda(flag):
#     return (lambda a,b:a+b) if flag else (lambda a,b:a-b)
#
# print(choose_lambda(True)(5,3))

#47 lambdas = [lambda x, n=n: n**2 for n in range(5)]
# print([f(0) for f in lambdas])

#48 def add_one_wrapper(f):
#     return lambda x: f(x) + 1
#
# plus1 = add_one_wrapper(lambda x: x*2)
# print(plus1(5))

#49 apply_twice = lambda f, x: f(f(x))
# print(apply_twice(lambda y: y+3, 2))

#50 calc = {
#     '+': lambda a,b:a+b,
#     '-': lambda a,b:a-b,
#     '*': lambda a,b:a*b,
#     '/': lambda a,b:a/b if b!=0 else None
# }
# op = '+'
# print(calc[op](10, 5))

n = int(input())

for i in range(100, 1000):
    if i + (i % 100) == n:
        print(i, end=' ')

