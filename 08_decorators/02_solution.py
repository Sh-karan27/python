def debug(function):
    def wrapper(*args,**kwargs):
        args_value = ", ".join(str(arg) for arg in args)
        kwargs_value = ", ".join(f"{k}={v}" for k,v in kwargs.items())
        print(f"calling: {function.__name__} with args {args_value} and kwargs {kwargs_value}")
        return function(*args,**kwargs)
    
    return wrapper




@debug
def hello():
    print("hello")

hello()

@debug
def greet(name,greeting="Namaste"):
    print(f"{greeting}, {name}")


greet("Karan",greeting="hello")