def my_decorator(func):
    def wrapper():
        print("Before the function call")
        func()
        print("after the funtion call")
    
    return wrapper

@my_decorator
def hello():
    print("Hello vishwas")


hello()