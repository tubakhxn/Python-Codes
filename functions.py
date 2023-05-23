#Function can be called again & again if it is required
"""Function contains
1. Prototype
2. Defination
3. Cell
"""
def my_function():
    print("This is a function")

    print("Before function..")

    my_function()

def my_function(username):
    print("Hi"+ username)

    my_function("Tuba")
