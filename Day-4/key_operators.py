# Key Python Operators: Assignment, Comparison, and Identity Operators

# Assignment Operator
a = 5

a = a + 2
print(a)

# Augmented Assignment Operators
a += 2 # Equivalent to a = a + 2
print(a)

a -= 4 # Equivalent to a = a - 4
print(a)

a *= 10 # Equivalent to a = a * 10
print(a)

# Incrementing and decrementing
# a++ and a-- are not valid in Python, but we can achieve the same with augmented assignment operators
a += 1 # Equivalent to a = a + 1
a -= 1 # Equivalent to a = a - 1

# Comparison Operators
a, b = 10, 20
print(a == b)
print(a < b)

a = 2
print(id(a)) # Prints the memory address of a

a = 3 # Modifies the value of a
print(id(a)) # Prints a different memory address, showing that a now references a new object with the value 3

numbers = [1, 2, 3]
print(numbers)
print(len(numbers)) # Output: 3
print(id(numbers))

numbers.append(4)
print(numbers)
print(len(numbers)) # Output: 4
print(id(numbers))