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
    return a / b

test = foo(1, 1)
print(test)
