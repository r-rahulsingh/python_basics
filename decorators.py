def announce(f):
    def wrapper():
        print("About to run the function...")
        f()
        print("Done with the function.")
    return wrapper

@announce #Decorators
def hello():
    print("Hello, world!")

hello()

'''
output:

About to run the function...
Hello, world!
Done with the function.

'''

'''
Decorators runs after the calling functin is ran. 
'''