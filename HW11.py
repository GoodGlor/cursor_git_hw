# Task 1

def double_result(func):
    def inner(a, b):
        return func(a, b) * 2

    return inner


@double_result
def add(a, b):
    return a + b


# Task 2

def only_odd_parameters(func):
    def wrapper(a, b):
        if a % 2 == 1 and b % 2 == 1:
            return func(a, b)
        else:
            print('Please use only odd numbers!')

    return wrapper


@only_odd_parameters
def add(a, b):
    return a + b

# Task 3

from functools import wraps
import logging

log_template = '%(asctime)s - %(levelname)s - %(message)s'

logging.basicConfig(level=logging.DEBUG, format=log_template)


def logged(func):
    @wraps(func)
    def inner(*args, **kwargs):
        logging.info(f'Calling function {func.__name__}')
        result = func(*args, **kwargs)
        logging.info(f'You input {len(args) + len(kwargs)} arguments. ')
        logging.info(f'Result {func(*args, **kwargs)}')
        logging.info(f'Finish {func.__name__}')
        return result

    return inner


@logged
def func(*args):
    return 3 + len(args)


# Task 4

def type_check(correct_type):
    def type_func(func):
        def wrapper(num):
            if correct_type == type(num):
                return func(num)
            else:
                print(f'Wrong Type: {type(num)} should be printed, since non-int passed to decorated function')

        return wrapper

    return type_func


@type_check(int)
def times2(num):
    return num * 2


@type_check(str)
def first_letter(word):
    return word[0]

