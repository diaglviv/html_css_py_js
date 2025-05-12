def announce(f):
    """
    Decorator that announces the function name and its arguments.
    """
    def wrapper():
        print("About run the function...")
        f()
        print("Done with the function.")       
    return wrapper

@announce
def hello():
    print("Hello, world!")
    
hello()    