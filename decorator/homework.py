# 1
def start_end(func):
    def wrapper(*args, **kwargs):
        print("Starting...")
        result = func(*args, **kwargs)
        print("Done.")
        return result
    return wrapper


# 2
def call_counter(func):
    count = 0
    def wrapper(*args, **kwargs):
        nonlocal count
        count = count + 1
        print("Call:", count)
        return func(*args, **kwargs)
    return wrapper


# 3
def show_name(func):
    def wrapper(*args, **kwargs):
        print("Function:", func.__name__)
        return func(*args, **kwargs)
    return wrapper


# 4
def to_upper(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if isinstance(result, str):
            result = result.upper()
        return result
    return wrapper


# 5
def check_empty(func):
    def wrapper(*args, **kwargs):
        for a in args:
            if isinstance(a, str) and a == "":
                print("Empty string!")
                return
        return func(*args, **kwargs)
    return wrapper


# 6
def no_negative(func):
    def wrapper(*args, **kwargs):
        for a in args:
            if isinstance(a, (int, float)) and a < 0:
                print("Negative number not allowed")
                return
        return func(*args, **kwargs)
    return wrapper


# 7
def executing(func):
    def wrapper(*args, **kwargs):
        print("Executing", func.__name__, "with:", args, kwargs)
        return func(*args, **kwargs)
    return wrapper


# 8
def print_types(func):
    def wrapper(*args, **kwargs):
        for a in args:
            print("Type:", type(a))
        return func(*args, **kwargs)
    return wrapper


# 9
def repeat3(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(result)
        print(result)
        print(result)
        return result
    return wrapper


# 10
def none_to_text(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if result is None:
            result = "No result"
        return result
    return wrapper


# 11
def only_even(func):
    def wrapper(*args, **kwargs):
        for a in args:
            if isinstance(a, int) and a % 2 != 0:
                print("Only even numbers allowed")
                return
        return func(*args, **kwargs)
    return wrapper


# 12
def remove_duplicates(func):
    def wrapper(*args, **kwargs):
        new_args = []
        for a in args:
            if isinstance(a, list):
                clean = []
                for x in a:
                    if x not in clean:
                        clean.append(x)
                new_args.append(clean)
            else:
                new_args.append(a)
        return func(*tuple(new_args), **kwargs)
    return wrapper


# 13
def lower_args(func):
    def wrapper(*args, **kwargs):
        new_args = []
        for a in args:
            if isinstance(a, str):
                a = a.lower()
            new_args.append(a)
        return func(*tuple(new_args), **kwargs)
    return wrapper


# 14
def sort_args(func):
    def wrapper(*args, **kwargs):
        new_args = []
        for a in args:
            if isinstance(a, (list, tuple)):
                a = sorted(a)
            new_args.append(a)
        return func(*tuple(new_args), **kwargs)
    return wrapper


# 15
def positive_only(func):
    def wrapper(*args, **kwargs):
        for a in args:
            if isinstance(a, (int, float)) and a <= 0:
                print("Only positive numbers allowed")
                return
        return func(*args, **kwargs)
    return wrapper


# 16
def limit_calls(func):
    count = 0
    def wrapper(*args, **kwargs):
        nonlocal count
        if count >= 5:
            print("Limit reached")
            return
        count = count + 1
        return func(*args, **kwargs)
    return wrapper


# 17
def count_even(func):
    def wrapper(*args, **kwargs):
        for a in args:
            if isinstance(a, list):
                c = 0
                for x in a:
                    if isinstance(x, int) and x % 2 == 0:
                        c = c + 1
                print("Even count:", c)
        return func(*args, **kwargs)
    return wrapper


# 18
def skip_empty(func):
    def wrapper(*args, **kwargs):
        if len(args) > 0 and (args[0] == [] or args[0] == ""):
            print("Skipped")
            return
        return func(*args, **kwargs)
    return wrapper


# 19
def remove_none(func):
    def wrapper(*args, **kwargs):
        new_args = []
        for a in args:
            if isinstance(a, list):
                clean = []
                for x in a:
                    if x is not None:
                        clean.append(x)
                new_args.append(clean)
            else:
                new_args.append(a)
        return func(*tuple(new_args), **kwargs)
    return wrapper


# 20
def reverse_strings(func):
    def wrapper(*args, **kwargs):
        new_args = []
        for a in args:
            if isinstance(a, str):
                a = a[::-1]
            new_args.append(a)
        return func(*tuple(new_args), **kwargs)
    return wrapper


# 21
def mult10(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if isinstance(result, (int, float)):
            result = result * 10
        return result
    return wrapper


# 22
def wrap_parentheses(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if isinstance(result, str):
            result = "(" + result + ")"
        return result
    return wrapper


# 23
def convert_type(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if isinstance(result, list):
            result = tuple(result)
        elif isinstance(result, tuple):
            result = list(result)
        return result
    return wrapper


# 24
def dash_join(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if isinstance(result, str):
            result = "-".join(result)
        return result
    return wrapper


# 25
def sort_return(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if isinstance(result, (list, tuple)):
            result = sorted(result)
        return result
    return wrapper


# 26
def apply_lambda(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if isinstance(result, list):
            new_list = []
            for x in result:
                new_list.append(x * 2)
            return new_list
        return result
    return wrapper


# 27
def hello_wrap(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if isinstance(result, str):
            result = "Hello, " + result + "!"
        return result
    return wrapper


# 28
def double_list(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if isinstance(result, list):
            new_list = []
            for x in result:
                new_list.append(x * 2)
            return new_list
        return result
    return wrapper


# 29
def dict_upper(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if isinstance(result, dict):
            new_dict = {}
            for k, v in result.items():
                if isinstance(v, str):
                    v = v.upper()
                new_dict[k] = v
            return new_dict
        return result
    return wrapper


# 30
def filter_odds(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if isinstance(result, list):
            even_list = []
            for x in result:
                if isinstance(x, int) and x % 2 == 0:
                    even_list.append(x)
            return even_list
        return result
    return wrapper
