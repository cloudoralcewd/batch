# LAMBDA EXPRESSIONS

# A lambda function is a small anonymous function that can take any number of arguments, but can only have one expression.

def add(a, b, c):
    """Returns the sum of three numbers."""
    return a + b + c

print(add(2,3,4))

# Syntax: lambda arguments: expression

print((lambda a, b, c, d: a + b + c + d)(2, 3, 4, 6))

square = lambda x = 10: x ** 2
print(square(1000))

friends = [('Diana Y', 30), ('Ana', 25), ('Tudor', 22)]
# print(type(friends))

friends.sort(key=lambda person: person[1])
print(friends)