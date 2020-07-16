def announce(f):
    def wrapper():
        print("About to run the funtions....")
        f()
        print("Done running the fucntiona....")
    return wrapper

@announce

def hello():
    print("Hello world!")

hello()