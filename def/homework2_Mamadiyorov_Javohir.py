#11 def outer():
#     print("Outer start")
#
#     def inner():
#         print("Inner call")
#
#     inner()
#
# outer()

#12 def calculate(a, b):
#     def add():
#         return a + b
#
#     print("Sum:", add())
#
# calculate(5, 7)

#13 def greet(name):
#     def message():
#         return f"Hello, {name}!"
#
#     return message()
#
# print(greet("Javohir"))

#14 def outer():
#     def inner1():
#         print("Inner 1")
#
#     def inner2():
#         print("Inner 2")
#
#     inner1()
#     inner2()
#
# outer()

#15 def outer():
#     def inner():
#         return "Inner"
#
#     return inner
#
# res = outer()
# print(res())

#16 def math_ops(x, y):
#     def add():
#         print("Add:", x + y)
#
#     def sub():
#         print("Subtract:", x - y)
#
#     def mul():
#         print("Multiply:", x * y)
#
#     def div():
#         print("Divide:", x / y)
#
#     add()
#     sub()
#     mul()
#     div()
#
# math_ops(6, 3)

#17 def table(n):
#     def show_row(i):
#         print(f"{n} x {i} = {n * i}")
#
#     for i in range(1, 11):
#         show_row(i)
#
# table(5)

#18 def outer():
#     message = "Hello"
#
#     def inner():
#         nonlocal message
#         message = "Hi"
#         print(message)
#
#     inner()
#     print(message)
#
# outer()

#19 def process_list(nums):
#     def compute_sum():
#         return sum(nums)
#
#     return len(nums), compute_sum()
#
# length, total = process_list([1, 2, 3, 4, 5])
# print("Length:", length)
# print("Sum:", total)

#20 def outer():
#     def add_one(x):
#         return x + 1
#
#     def add_two(x):
#         return x + 2
#
#     return add_one, add_two
#
# f1, f2 = outer()
# print(f1(5))
# print(f2(5))
