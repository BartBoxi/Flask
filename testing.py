
## Creation of logging decorator
def logging_decorator(a_function):
    def wrapper(*args):
        print(f"You called {a_function.__name__}")
        result = a_function(*args)
        print(f"It returned: {result}")
        return result
    return wrapper


# TODO: Use the decorator 👇
@logging_decorator
def a_function(*args):
    return sum(args)


a_function(1, 2, 3)