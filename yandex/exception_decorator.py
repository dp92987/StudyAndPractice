"""
Decorator to repeat function in case of error.
"""

import functools

def exception_decorator(func):
    @functools.wraps(func)
    def exception_decorator_wrapper(*args, **kwargs):
        while True:
            try:
                result = func(*args, **kwargs)
                return result
            except:
                pass
    return exception_decorator_wrapper


@exception_decorator
def foo(a, b):
    result = a / b
    return result


print(foo(1, 0))
