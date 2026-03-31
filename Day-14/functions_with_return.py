# THE return STATEMENT

# The `len()` function returns the length of a string

name = 'RNS Technologies'
length_of_name = len(name)
print(length_of_name)

# RETURNING VALUES FROM FUNCTIONS

def add():
    """ Returns sum of numbers entered by the user """
    a = int(input("Enter a Value: "))
    b = int(input("Enter b Value: "))
    print(f'a Value {a} and b Value {b}')
    return a + b

print(add())

# A function with no return statement

def func():
    pass

def func2(x=100):
    """Returns multiple values: the input number, its square, and its cube."""
    return x, x ** 2, x ** 3, x ** 4

a, b, c, d = func2()

print(a, b, c, d)





