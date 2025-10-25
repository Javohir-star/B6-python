# from typing import Callable
#
# def safe_divide(a, b):
#     return a / b
#
# def error_handler():
#     return "Xatolik!"
#
# def run_if_safe(func: Callable, handler: Callable, a, b):
#     if b != 0:
#         return func(a, b)
#     else:
#         return handler()
#
# print(run_if_safe(safe_divide, error_handler, 5, 1))
