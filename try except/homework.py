# # 1
# try:
#     a = float(input("Enter first number: "))
#     b = float(input("Enter second number: "))
#     print("Result:", a / b)
# except ZeroDivisionError:
#     print("Cannot divide by zero.")
# except ValueError:
#     print("Please enter valid numbers.")
#
# # 2
# def inverses(numbers):
#     result = []
#     for n in numbers:
#         try:
#             result.append(1 / n)
#         except ZeroDivisionError:
#             continue
#     return result
# print(inverses([2, 0, 5, 0, 10]))
#
# # 3
# try:
#     f = open("data.txt", "r")
#     print(f.read())
# except FileNotFoundError:
#     print("File not found.")
# finally:
#     try:
#         f.close()
#     except:
#         pass
#
# # 4
# strings = ["10", "5", "abc", "20"]
# nums = []
# for s in strings:
#     try:
#         nums.append(int(s))
#     except ValueError:
#         continue
# print(nums)
#
# # 5
# while True:
#     try:
#         num = int(input("Enter an integer: "))
#         break
#     except ValueError:
#         print("Invalid input, try again.")
# print("You entered:", num)
#
# # 6
# data = {"name": "Tom", "age": 22}
# try:
#     print(data["city"])
# except KeyError:
#     print("Key not found.")
#
# # 7
# lst = [1, 2, 3]
# try:
#     print(lst[5])
# except IndexError:
#     print("Index out of range.")
#
# # 8
# a = [10, 20, 30]
# b = [2, 0, 5, 8]
# result = []
# for i in range(min(len(a), len(b))):
#     try:
#         result.append(a[i] / b[i])
#     except ZeroDivisionError:
#         result.append(None)
# print(result)
#
# # 9
# def check_list(lst):
#     if not lst:
#         raise ValueError("List is empty.")
#     return sum(lst)
# try:
#     print(check_list([]))
# except ValueError as e:
#     print(e)
#
# # 10
# def only_digits(s):
#     if not s.isdigit():
#         raise ValueError("String contains non-digit characters.")
#     return True
# try:
#     only_digits("123a")
# except ValueError as e:
#     print(e)
#
# # 11
# def check_number(n):
#     if n < 0:
#         raise ValueError("Number is negative.")
#     return n
# try:
#     check_number(-5)
# except ValueError as e:
#     print(e)
#
# # 12
# values = ("10", "x", "30", "5a")
# nums = []
# for v in values:
#     try:
#         nums.append(int(v))
#     except ValueError:
#         continue
# print(nums)
#
# # 13
# while True:
#     try:
#         x = float(input("Enter a float: "))
#         break
#     except ValueError:
#         print("Invalid float, try again.")
# print("You entered:", x)
#
# # 14
# config = {"host": "localhost"}
# try:
#     port = config["port"]
# except KeyError:
#     print("Missing 'port' key.")
#
# # 15
# files = ["a.txt", "b.txt", "c.txt"]
# for name in files:
#     try:
#         with open(name) as f:
#             print(f.read())
#     except FileNotFoundError:
#         print(f"{name} not found.")
#
# # 16
# try:
#     f = open("nums.txt")
#     try:
#         numbers = [int(x) for x in f]
#         print(numbers)
#     except ValueError:
#         print("File has non-numeric data.")
# finally:
#     try:
#         f.close()
#     except:
#         pass
#
# # 17
# try:
#     n = int(input("Enter number: "))
# except ValueError:
#     print("Invalid.")
# else:
#     print("Number is:", n)
# finally:
#     print("Done.")
#
# # 18
# def double_it(s):
#     try:
#         return int(s) * 2
#     except ValueError:
#         print("Not a number.")
# print(double_it("12"))
# print(double_it("hi"))
#
# # 19
# lst = [10, 20, 30]
# try:
#     print(lst[5])
# except IndexError:
#     print("Using default:", lst[-1])
#
# # 20
# def check_email(email):
#     if "@" not in email:
#         raise ValueError("Invalid email.")
#     return True
# try:
#     check_email("userexample.com")
# except ValueError as e:
#     print(e)
#
# # 21
# def get_from_dict(d, key):
#     if not isinstance(d, dict):
#         raise TypeError("Argument must be a dictionary.")
#     try:
#         return d[key]
#     except KeyError:
#         print("Key not found.")
#         return None
# print(get_from_dict({"a": 1}, "b"))
#
# # 22
# def check_range(x, low, high):
#     if x < low or x > high:
#         raise ValueError("Number out of range.")
#     return x
# try:
#     check_range(15, 1, 10)
# except ValueError as e:
#     print(e)
#
# # 23
# def only_numbers(lst):
#     for i in lst:
#         if not isinstance(i, (int, float)):
#             raise TypeError("List contains non-number element.")
#     return True
# try:
#     only_numbers([1, 2, "a", 3])
# except TypeError as e:
#     print(e)
#
# # 24
# values = ["10", "a", "20", "x"]
# for v in values:
#     try:
#         print(int(v))
#     except ValueError:
#         print("Cannot convert:", v)
#
# # 25
# s = "10 20 abc 30"
# for w in s.split():
#     try:
#         print(int(w))
#     except ValueError:
#         print("Invalid:", w)
#
# # 26
# def safe_get(lst, index, default=None):
#     try:
#         return lst[index]
#     except IndexError:
#         return default
# print(safe_get([1, 2, 3], 5, "none"))
#
# # 27
# def check_email_simple(email):
#     if "@" not in email:
#         raise ValueError("Invalid email address.")
#     return True
# try:
#     check_email_simple("example.com")
# except ValueError as e:
#     print(e)
#
# # 28
# import random
# for i in range(3):
#     try:
#         if random.choice([True, False]):
#             raise ConnectionError("Download failed.")
#         print("Download succeeded.")
#         break
#     except ConnectionError as e:
#         print(e)
# else:
#     print("Failed after 3 tries.")
#
# # 29
# try:
#     divide = lambda a, b: a / b
#     print(divide(5, 0))
# except ZeroDivisionError:
#     print("Division by zero.")
#
# # 30
# def safe_run(func, *args):
#     try:
#         return func(*args)
#     except Exception as e:
#         print("Error:", e)
# def add(a, b): return a + b
# print(safe_run(add, 3, "x"))
#
# # 31
# def safe_call(func):
#     try:
#         func()
#     except Exception as e:
#         print(type(e).__name__, "-", e)
# def fail(): 1 / 0
# safe_call(fail)
#
# # 32
# try:
#     with open("numbers.txt") as f:
#         total = 0
#         for line in f:
#             try:
#                 total += int(line)
#             except ValueError:
#                 continue
#         print("Sum:", total)
# except FileNotFoundError:
#     print("numbers.txt not found")
#
# # 33
# def check_password(p):
#     if len(p) < 6:
#         raise ValueError("Too short.")
#     if not any(ch.isdigit() for ch in p):
#         raise ValueError("No digit.")
#     if not any(ch.isalpha() for ch in p):
#         raise ValueError("No letter.")
#     return True
# try:
#     check_password("123")
# except ValueError as e:
#     print(e)
#
# # 34
# pairs = [(10, 2), (5, 0), ("x", 3)]
# for a, b in pairs:
#     try:
#         print(a / b)
#     except Exception as e:
#         print("Error:", e)
#
# # 35
# items = [10, "x", 5, 0]
# for x in items:
#     try:
#         print(10 / int(x))
#     except Exception as e:
#         print("Skipped:", e)
#
# # 36
# def remove_dupes(data):
#     if not hasattr(data, "__iter__"):
#         raise TypeError("Not iterable.")
#     return list(set(data))
# try:
#     print(remove_dupes(123))
# except TypeError as e:
#     print(e)
#
# # 37
# def do_op(a, b, op):
#     if op == "add":
#         return a + b
#     elif op == "sub":
#         return a - b
#     else:
#         raise ValueError("Invalid operation.")
# try:
#     print(do_op(3, 2, "mul"))
# except ValueError as e:
#     print(e)
#
# # 38
# print("Opening file...")
# try:
#     print("Reading...")
#     raise IOError("Read failed.")
# except IOError as e:
#     print(e)
# finally:
#     print("File closed.")
#
# # 39
# import json
# data = '{"a":1, "b":2'
# try:
#     obj = json.loads(data)
# except json.JSONDecodeError:
#     print("Invalid JSON.")
#
# # 40
# import time
# def run_with_timer(func):
#     start = time.time()
#     try:
#         func()
#     except Exception as e:
#         print("Error:", e)
#     finally:
#         print("Time:", time.time() - start)
# def fail_fast(): 1 / 0
# run_with_timer(fail_fast)

# def safe_call(func):
#     def wrapper(*args, **kwargs):
#         try:
#             func(*args, **kwargs)
#         except ZeroDivisionError:
#             raise ZeroDivisionError("Division by zero.")
#         except Exception as e:
#             raise Exception("Error", e)
#     return wrapper
#
# @safe_call
# def myfunc():
#     import random
#     l = [ZeroDivisionError, FileNotFoundError, KeyError, TypeError]
#     i = random.randrange(0, 3)
#
#     return l[i]
#
# myfunc()

# def validate_args(func):
#     def wrapper(*args, **kwargs):
#         for i in args:
#             if not isinstance(i, int):
#                 raise TypeError("Given number isn't integer")
#
#         func(*args)
#     return wrapper
#
# @validate_args
# def myfunc(*args):
#     print(args)
#
# myfunc(1, 2, 3, 4)

# def convert_exceptions(func):
#     def wrapper(*args, **kwargs):
#         try:
#             func()
#         except KeyError as e:
#             raise ValueError(e)
#
#     return wrapper
#
# @convert_exceptions
# def myfunc():
#     d = dict()
#     print(d['key1'])
#
# myfunc()
